
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from attendance_app.models import User, Attendance

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        return render_template('unauthorized.html')
    students = User.query.filter_by(role='student').all()
    data = [(s, Attendance.query.filter_by(student_id=s.id).count()) for s in students]
    return render_template('admin_dashboard.html', students=data)

@admin_bp.route('/attendance')
@login_required
def attendance_log():
    if current_user.role != 'admin':
        return render_template('unauthorized.html')
    records = Attendance.query.order_by(Attendance.date.desc()).all()
    return render_template('admin_attendance.html', records=records)

@admin_bp.route('/admin/home')
def admin_home():
    if current_user.role != 'admin':
        return redirect(url_for('auth.login'))
    return render_template('admin_home.html')



from collections import defaultdict

@admin_bp.route('/attendance-summary')
@login_required
def attendance_summary():
    if current_user.role != 'admin':
        return render_template('unauthorized.html')

    records = Attendance.query.order_by(Attendance.date.desc()).all()

    student_attendance = defaultdict(list)
    for record in records:
        student_attendance[record.student.username].append(record.date.strftime('%Y-%m-%d'))

    summary = [(name, len(dates), dates) for name, dates in student_attendance.items()]

    return render_template('attendance_summary.html', summary=summary)
