import logging
from flask import Flask
from config import BasicConfig
from database.database import db
from routes.students_view import students_view
from routes.student import app_student
from routes.teachers_view import teachers_view

app = Flask(__name__)
app.config.from_object(BasicConfig)
db.init_app(app)
app.register_blueprint(students_view)
app.register_blueprint(teachers_view)
app.register_blueprint(app_student)
logging.basicConfig(level=logging.DEBUG, filename='data_layer.log')
