from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, 
                      TextAreaField, 
                      IntegerField,
                      SubmitField, 
                      PasswordField, 
                      DateField, 
                      SelectField,
                      BooleanField)

from wtforms.validators import (DataRequired,
                            Email, 
                            EqualTo, 
                            Length, 
                            URL)

class SignUpForm(FlaskForm):
    first_name = StringField('First Name', [
        DataRequired(),
        ])
    last_name = StringField('Last Name', [
        DataRequired(),
    ])
    # Need to make sure they are 18+ years old -- include privacy clause -- ?
    age = SelectField('Age', validators=[
        DataRequired(),
        ], choices = [
            (x, x) for x in range(16, 100)
        ])

    address = StringField("Address", validators=[
        DataRequired(),
        ])
    city = StringField("City", validators=[
        DataRequired(),
        ])
    state = SelectField('State', validators=[
        DataRequired(),
        ], choices = [ 
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY'),
        ]
    )
    zip_code = IntegerField(validators=[DataRequired()])
    
    email = StringField('Email', [
        Email(message = 'Not a valid email address.'), 
        DataRequired()
    ])
    password = PasswordField('Password', [
        DataRequired(message = "Please enter a password")])
    confirm_password = PasswordField('Confirm Password', [
        DataRequired(message = 'Passwords need to match.')])
    
    climbing_gym = SelectField('Preferred Climbing Gym', [
        DataRequired(),
        ], choices = [
            ('The Cliffs @ LIC', 'Cliffs LIC'),
            ('Brooklyn Boulders Gowanus', 'BKB GW'),
            ('Brooklyn Boulders Queensborough', 'BKB QB'),
            ('Central Rock Gym', 'Centra Rock'),
            ('Steep Rock West', 'Steep Rock West'),
            ('The Gravity Vault', 'Gravity Vault'),
            ('Chelsea Piers', 'Chelsea Piers'),
            ]
    )
    # toprope, lead, trad
    climbing_preference = SelectField("Preferred Climbing Style", [
        DataRequired()
        ], choices= [
            ("Top Rope", 'Top Rope'),
            ("Sport", "Sport"),
            ("Trad", "Trad"),
        ])
    

    # recaptcha = RecaptchaField()
    sumbit = SubmitField("Submit")







class LoginForm(FlaskForm):
    email = StringField('Email', [
        Email(message = 'Not a valid email address.'), 
        DataRequired()
    ])
    password = PasswordField('Password', [
        DataRequired(message = "Please enter a password")])
    remember_me = BooleanField("Keep me logged in")
    submit = SubmitField('Log In')
