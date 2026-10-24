
### New Code



from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import date
from attendance_app import db
from attendance_app.models import Attendance

attendance_bp = Blueprint('attendance', __name__, url_prefix='/attendance')

@attendance_bp.route('/', methods=['GET','POST'])
@login_required
def attendance_view():
    if current_user.role != 'student':
        return render_template('unauthorized.html')
    today = date.today()
    exists = Attendance.query.filter_by(student_id=current_user.id, date=today).first()
    if request.method == 'POST':
        if exists:
            flash('Already marked today')
        else:
            attendance = Attendance(student_id=current_user.id, date=today)
            db.session.add(attendance)
            db.session.commit()
            flash('Attendance marked')
        return redirect(url_for('attendance.attendance_view'))
    records = Attendance.query.filter_by(student_id=current_user.id).order_by(Attendance.date.desc()).all()
    return render_template('attendance.html', records=records, marked_today=bool(exists))


