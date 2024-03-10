from  marshmallow import  Schema, fields



class PlainExerciseSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    descriptions = fields.Str(required=True)
    instructions = fields.Str(required=True)
    target_muscles =fields.Str(required=True)



class PlainPlanSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    goals = fields.Str(required=True)
    workout_frequency = fields.Str(required=True)
    daily_session_duration = fields.Str(required=True)

class UpdatePlan(Schema):
    name = fields.Str()
    goals = fields.Str()
    workout_frequency = fields.Str()
    daily_session_duration = fields.Str()


class ExerciseSchema(PlainExerciseSchema):
    plan_id= fields.Int(required=True, load_only=True)
    plan = fields.Nested(PlainPlanSchema(), dump_only=True)


class PlanSchema(PlainPlanSchema):
    exercises=fields.List(fields.Nested(PlainExerciseSchema()), dump_only=True)



