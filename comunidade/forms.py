from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user

from comunidade.models import User


class FormCreateAcount(FlaskForm):

    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[
                             DataRequired(), Length(6, 20)])
    password_confirm = PasswordField('Confirmação da senha', validators=[
                                     DataRequired(), EqualTo('password')])
    button_submit_createaccount = SubmitField('Criar Conta', validators=[])

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('E-mail já cadastrado')


class FormLogin(FlaskForm):

    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[
                             DataRequired(), Length(6, 20)])
    remember_data = BooleanField('Lembrar Dados de Acesso')
    button_submit_login = SubmitField('Fazer login', validators=[])


class FormEdit_Profile(FlaskForm):

    username = StringField('Nome de usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    profile_photo=FileField('Atualizar foto de Perfil',validators=[FileAllowed(['jpg','png'])])
    course_excel = BooleanField('Excel curso')
    course_vba = BooleanField('VBA curso')
    course_python = BooleanField('Python curso')
    course_java = BooleanField('Java curso')
    course_powerbi = BooleanField('Power BI curso')
    course_sql = BooleanField('SQL curso')
    button_submit_editprofile = SubmitField('Confirmar Edição')
    

    def validate_email(self, email):

        if current_user.email != email.data:

            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Já existi um usuario, com esse e-mail. Cadastre outro email')


class FormCreatePost(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(2,200)])
    body = TextAreaField('Escreva seu post aqui', validators=[DataRequired()])
    button_submit_createpost = SubmitField('Criar Post', validators=[])