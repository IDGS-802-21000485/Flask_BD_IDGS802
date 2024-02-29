from wtforms import Form
from wtforms import StringField, TextAreaField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    id = IntegerField("id",[validators.number_range(min=1, max=28, message="Valor no valido")])
    nombre = StringField("Nombre",[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=10, message="Ingresa nombre valido")
    ])
    email = EmailField("Correo", [
        validators.Email(message="Ingresa el correo valido")
    ])
    
    apaterno = StringField("apaterno")
    