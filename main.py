# import uuid
import os

from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.exercise import blp as ExerciseBlueprint
from resources.plan import blp as PlanBlueprint


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
    db.init_app(app)

    with app.app_context():
        db.create_all()


    api = Api(app)
    api.register_blueprint(ExerciseBlueprint)
    api.register_blueprint(PlanBlueprint)


    return app

if __name__ == '__main__':
    create_app().run(debug=True)














































#
# @app.get('/plans')
# def get_all_plans():
#     return {'plans': list(plans.values())}
#
# @app.get('/plans/<plan_id>')
# def get_plan(plan_id):
#     try:
#         return plans[plan_id]
#     except KeyError:
#         abort(404, message='plan is not found')
#
#
# @app.post('/plans')
# def create_new_plans():
#     plan_data=request.get_json()
#     plan_id=uuid.uuid4().hex
#     plan={**plan_data, 'id': plan_id}
#     plans[plan_id]=plan
#
#     return plan
#
#
# @app.delete('/plans/<plan_id>')
# def delete_plan(plan_id):
#     try:
#         del plans[plan_id]
#         return {'message': 'plan is deleted'}
#     except KeyError:
#         abort(404, message='plan is not found')
#
# @app.put('/plans/<plan_id>')
# def update_plan(plan_id):
#     request_data=request.get_json()
#     try:
#         changed_plan=plans[plan_id]
#         changed_plan |= request_data
#         return changed_plan
#     except KeyError:
#         abort(404, message='plan is not found')
#
#
#
#
#
# @app.get('/exercises')
# def get_all_exercise():
#     return {'exercises': list(exercises.values())}
#
#
# @app.get('/exercise/<exercise_id>')
# def get_exercise(exercise_id):
#     try:
#         return exercises[exercise_id]
#     except KeyError:
#         abort(404, message="Exercise not found")
#
#
# @app.post('/exercise')
# def create_exercise():
#     exercise_data=request.get_json()
#
#     for exercise in exercises.values():
#         if (
#                 exercise_data['name'] == exercise['name']
#                 and exercise_data['plan_id'] == exercise['plan_id']
#         ):
#             abort(400, message=f'exercise already exists.')
#
#     exercise_id=uuid.uuid4().hex
#     new_exercise={**exercise_data, 'id': exercise_id}
#     exercises[exercise_id]=new_exercise
#
#     return new_exercise
#
#
# @app.delete('/exercise/<exercise_id>')
# def delete_exercise(exercise_id):
#     try:
#         del exercises[exercise_id]
#         return {'message': 'exercise is deleted'}
#     except KeyError:
#         abort(404, message="Exercise not found")
#
#
#
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
