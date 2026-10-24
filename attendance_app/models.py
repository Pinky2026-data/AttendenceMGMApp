from flask_login import UserMixin
from attendance_app import db

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    dob = db.Column(db.String(10),nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    attendance = db.relationship('Attendance', backref='student', lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    __table_args__ = (
        db.UniqueConstraint('student_id', 'date', name='unique_attendance'),
    )

    def __repr__(self):
        return f"<Attendance {self.student_id} on {self.date}>"