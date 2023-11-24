from flask import Flask
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
##########
from form import form
##########


app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
##########
app.register_blueprint(form)
##########
