from db import db


class PlanModel(db.Model):
    __tablename__ = "plans"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    goals = db.Column(db.String, unique=False, nullable=False)
    workout_frequency = db.Column(db.String, unique=False, nullable=False)
    daily_session_duration = db.Column(db.String, unique=False, nullable=False)
    exercises = db.relationship("ExerciseModel", back_populates="plan", lazy="dynamic", cascade="all, delete" )
