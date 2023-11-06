import datetime
from flask import Blueprint, jsonify, redirect, request, render_template, url_for
from models.students import Student
from database.database import db
from forms.students_form import StudentForm

students_view = Blueprint('students', __name__, template_folder='templates')


@students_view.route('/')
def get_all_students():
    students = Student.query.filter(Student.status == True).all()
    return render_template('index_students.html', students=students)


@students_view.route('/students', methods=['GET', 'POST'])
def post_students():
    student = Student()
    student_form = StudentForm(obj=student)

    if request.method == 'POST':
        if student_form.validate_on_submit():
            student.created_at = datetime.datetime.now()
            student.status = True
            student_form.populate_obj(student)
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('students.get_all_students'))

    return render_template('add_student.html', form=student_form)


@students_view.route('/students/<int:id>', methods=['GET', 'POST'])
def put_students(id):
    student = Student.query.get_or_404(id)
    student_form = StudentForm(obj=student)

    if request.method == 'POST':
        if student_form.validate_on_submit():
            student.updated_at = datetime.datetime.now()
            student_form.populate_obj(student)
            db.session.commit()
            return redirect(url_for('students.get_all_students'))

    return render_template('edit_student.html', form=student_form)


@students_view.route('/delete-student/<int:id>', methods=['GET', 'POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.status = False
        db.session.commit()
        return redirect(url_for('students.get_all_students'))

    return render_template('delete_student.html', student=student)
