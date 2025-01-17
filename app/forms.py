from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length
 
class RegisterForm(FlaskForm):

    username = StringField ('Username', validators= [DataRequired(), Length(8, 15)])
    email = StringField ('Email', validators= [DataRequired(), Length(8, 15)])
    password = PasswordField ('Password', validators= [DataRequired()])
    confirm_password = PasswordField ('Confirm Password', validators= [DataRequired()])
    submit = SubmitField ('Register')

class AddProductForm(FlaskForm):
    
    product_name= StringField ('Product Name', validators= [DataRequired(), Length(8, 15)])
    product_decription= StringField ('Product Decriptiom', validators= [DataRequired(), Length(8, 15)])
    stock_available = SelectField ('Products', choices = [('1','1'), ('2','2'), ('3','3'),],  validators= [DataRequired(), Length(8, 15)])
    submit = SubmitField ('Add Product')
