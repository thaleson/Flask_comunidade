# Assuming database is defined in main.py
from comunidade import database, login_manager
from datetime import datetime, timezone
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))

class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(80), unique=True, nullable=False)
    email = database.Column(database.String(120), unique=True, nullable=False)
    password = database.Column(database.String(60), nullable=False)
    profile_picture = database.Column(database.String(20), default='default.jpg')
    posts = database.relationship('Post', backref='autor', lazy=True)  # 'autor' is the backref
    courses = database.Column(database.String, nullable=False, default='Não informado')

    def count_pots(self):
        return len(self.posts)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(100), nullable=False)
    body = database.Column(database.Text, nullable=False)
    creation_date = database.Column(database.DateTime, default=datetime.now(timezone.utc))
    id_user = database.Column(database.Integer, database.ForeignKey("user.id"), nullable=False)
