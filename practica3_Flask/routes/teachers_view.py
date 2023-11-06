import datetime
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from models.teachers import Teacher
from database.database import db
from forms.teachers_form import TeacherForm

teachers_view = Blueprint('teachers', __name__)


@teachers_view.route('/view-teachers')
def get_all_teachers():
    teachers = Teacher.query.filter(Teacher.status == True).all()
    return render_template('index_teachers.html', teachers=teachers)


@teachers_view.route('/teachers', methods=['GET', 'POST'])
def post_teacher():
    teacher = Teacher()  # Create a new Student object
    teacher_form = TeacherForm(obj=teacher)  # Create a new StudentForm object
    if request.method == 'POST':
        if teacher_form.validate_on_submit():
            teacher.created_at = datetime.datetime.now()
            teacher.status = True
            # Populate the Student object with the data from the form
            teacher_form.populate_obj(teacher)
            db.session.add(teacher)
            db.session.commit()
            return redirect(url_for('teachers.get_all_teachers'))
    return render_template('add_teacher.html', form=teacher_form)


@teachers_view.route('/teachers/<int:id>', methods=['GET', 'POST'])
def put_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    teacher_form = TeacherForm(obj=teacher)
    if request.method == 'POST':
        if teacher_form.validate_on_submit():
            teacher.updated_at = datetime.datetime.now()
            teacher_form.populate_obj(teacher)
            db.session.commit()
            return redirect(url_for('teachers.get_all_teachers'))
    return render_template('edit_teacher.html', form=teacher_form)


@teachers_view.route('/delete-teacher/<int:id>', methods=['GET', 'POST'])
def delete_teacher(id):
    teacher = Teacher.query.get_or_404(id)
    if request.method == 'POST':
        teacher.status = False
        db.session.commit()
        return redirect(url_for('teachers.get_all_teachers'))
    return render_template('delete_teacher.html', teacher=teacher)
