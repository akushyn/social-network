from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class EditProfileForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    bio = TextAreaField('About me', validators=[Length(min=0, max=200)])
    submit = SubmitField('Submit')
