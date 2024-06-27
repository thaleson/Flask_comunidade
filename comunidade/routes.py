from flask import render_template, redirect, flash, url_for, request,abort
from comunidade import app, database, bcrypt
from comunidade.forms import FormLogin, FormCreateAcount, FormEdit_Profile,FormCreatePost
from comunidade.models import User, Post
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os
from PIL import Image




@app.route('/')
def home():
    posts=Post.query.all()
    

    return render_template('home.html',posts=posts)


@app.route('/contato')
def contact():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def users():
    user_list = User.query.all()
    return render_template('usuarios.html', user_list=user_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_createacount = FormCreateAcount()

    if form_login.validate_on_submit() and 'button_submit_login' in request.form:
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form_login.password.data):
            login_user(user, remember=form_login.remember_data)
            flash(
                f"Login feito com sucesso no e-mail: {form_login.email.data}", 'alert-success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("E-mail ou senha incorretos", 'alert-danger')

    if form_createacount.validate_on_submit() and 'button_submit_createaccount' in request.form:
        encrypted_password = bcrypt.generate_password_hash(
            form_createacount.password.data).decode('utf-8')
        user = User(
            username=form_createacount.username.data,
            email=form_createacount.email.data,
            password=encrypted_password
        )
        database.session.add(user)
        database.session.commit()
        flash(f"Cadastro feito com sucesso: {
              form_createacount.email.data}", 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_createacount=form_createacount)


@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash("Você saiu com sucesso !!", 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def profile():
    photo_profile = url_for(
        'static', filename='photos_profile/{}'.format(current_user.profile_picture))
    return render_template('perfil.html', photo_profile=photo_profile)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def create_post():
    form=FormCreatePost()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            body=form.body.data,
            autor=current_user
        )
        database.session.add(post)
        database.session.commit()
        flash("Post criado com sucesso !!!", 'alert-success')
        return redirect(url_for('home'))
    return render_template('criar_post.html' ,form=form)




def savephoto(imagem):
    code = secrets.token_hex(8)
    name, extension = os.path.splitext(imagem.filename)
    full_name = code + name + extension
    full_path = os.path.join(app.root_path, 'static/photos_profile', full_name)

    # Abrir a imagem e redimensioná-la
    img = Image.open(imagem)
    size = (200, 200)
    img.thumbnail(size)

    img.save(full_path)

    return full_name


def update_courses(form_edit_profile):
    course_list = []
    
    try:
        for field in form_edit_profile:
            # Verifica se o campo possui os atributos 'name' e 'label'
            if hasattr(field, 'name') and hasattr(field, 'label'):
                # Verifica se o nome do campo contém 'course_'
                if 'course_' in field.name:
                    if field.data:
                        course_list.append(field.label.text)
        
        # Verifica se a lista de cursos está vazia
        if not course_list:
            return "Nenhum curso encontrado."
        
        # Junta os rótulos dos cursos em uma única string, separada por ponto e vírgula
        return ';'.join(course_list)
    
    except Exception as e:
        # Retorna uma mensagem de erro em caso de exceção
        return f"Erro ao atualizar cursos: {e}"


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form_edit_profile = FormEdit_Profile()
    if form_edit_profile.validate_on_submit():
        current_user.email = form_edit_profile.email.data
        current_user.username = form_edit_profile.username.data
        if form_edit_profile.profile_photo.data:
            name_image = savephoto(form_edit_profile.profile_photo.data)
            current_user.profile_picture = name_image

        current_user.courses=update_courses(form_edit_profile)    
        database.session.commit()
        flash("Perfil atualizado com sucesso", 'alert-success')
        return redirect(url_for('profile'))
    elif request.method == "GET":
        form_edit_profile.email.data = current_user.email
        form_edit_profile.username.data = current_user.username

    photo_profile = url_for(
        'static', filename='photos_profile/{}'.format(current_user.profile_picture))
    return render_template('editarperfil.html', photo_profile=photo_profile, form_edit_profile=form_edit_profile)




@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def display_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return render_template('404.html'  ), 404
    
    form = None
    if current_user == post.autor:
        form = FormCreatePost()
        if request.method == 'GET':
            form.title.data = post.title
            form.body.data = post.body
        elif form.validate_on_submit():
            post.title = form.title.data
            post.body = form.body.data
            database.session.commit()
            flash("Post atualizado com sucesso", 'alert-success')
            return redirect(url_for('home'))
    
    return render_template('post.html', form=form, post=post)


@app.route('/post/<int:post_id>/excluir', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor:
        database.session.delete(post)
        database.session.commit()
        flash("Post deletado com sucesso", 'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)
        
