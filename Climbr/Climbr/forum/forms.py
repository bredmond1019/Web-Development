from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, 
                      TextAreaField, 
                      IntegerField,
                      SubmitField, 
                      PasswordField, 
                      DateField, 
                      SelectField,
                      BooleanField,
                      ValidationError)

from wtforms.validators import (DataRequired,
                            Email, 
                            EqualTo, 
                            Length, 
                            URL)

from flask_wtf.file import FileField, FileRequired, FileAllowed

from ..models import User, Role


class PostForm(FlaskForm):
    body = TextAreaField("What's on your mind?", validators=[DataRequired()])
    submit = SubmitField("Submit")

class EditPostForm(FlaskForm):
    body = TextAreaField("",validators=[DataRequired()])
    submit = SubmitField("Confirm Changes")

