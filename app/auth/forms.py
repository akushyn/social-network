from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField,
    EmailField,
    validators
)


class LoginForm(FlaskForm):
    """
    Login form
    """
    username = StringField("Username", validators=[validators.DataRequired()])
    password = PasswordField("Password", validators=[validators.DataRequired()])
    remember = BooleanField("Remember")
    submit = SubmitField("Log In")


class RegisterForm(FlaskForm):
    """
    Register form
    """
    username = StringField("Username", validators=[validators.DataRequired()])
    email = EmailField("Email")
    password = PasswordField("Password", validators=[validators.DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            validators.DataRequired(),
            validators.EqualTo("password")
        ]
    )
    submit = SubmitField("Register")
