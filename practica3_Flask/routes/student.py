import datetime
from flask import Blueprint, jsonify, request
from models.students import Student
from database.database import db

app_student = Blueprint('app_student', __name__)


@app_student.route('/api/students')
def get_students():
    try:
        students = Student.query.filter(Student.status == True).all()
        students_dict = [student.serialize() for student in students]
        return jsonify({'ok': True, 'results': students_dict})
    except Exception as e:
        return jsonify({'ok': False, 'message': str(e)})


@app_student.route('/api/students', methods=['POST'])
def post_student():
    try:
        json = request.get_json()
        student = Student()
        student.first_name = json['first_name']
        student.last_name = json['last_name']
        student.degree = json['degree']
        student.status = True
        student.created_at = datetime.datetime.now()
        db.session.add(student)
        db.session.commit()
        return jsonify({'ok': True, 'message': 'Student created successfully'})
    except Exception as e:
        return jsonify({'ok': False, 'message': str(e)})


@app_student.route('/api/students/<int:id>', methods=['POST'])
def put_student(id):
    try:
        json = request.get_json()
        student = Student.query.get_or_404(id)
        student.first_name = json['first_name']
        student.last_name = json['last_name']
        student.degree = json['degree']
        student.updated_at = datetime.datetime.now()
        db.session.commit()
        return jsonify({'ok': True, 'message': 'Student updated successfully'})
    except Exception as e:
        return jsonify({'ok': False, 'message': str(e)})


@app_student.route('/api/delete-student/<int:id>', methods=['POST'])
def delete_student(id):
    try:
        student = Student.query.get_or_404(id)
        student.status = False
        db.session.commit()
        return jsonify({'ok': True, 'message': 'Student deleted successfully'})
    except Exception as e:
        return jsonify({'ok': False, 'message': str(e)})
