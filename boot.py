from flask import Flask
from flask_restful import Api
import ChoiceCourseController
import CourseController
import LoginController
import  PorfossorController
import TimeCourseController

app = Flask(__name__)
api = Api(app)



api.add_resource(TimeCourseController.list,'/timecourse', endpoint='TimeCourse')
api.add_resource(CourseController.list , '/courses', endpoint='courses')
api.add_resource(CourseController.Delete , '/delete/<int:course_id>', endpoint='delete')
api.add_resource(ChoiceCourseController.Delete , '/choisedelete/<int:course_id>', endpoint='deletechoise')
api.add_resource(ChoiceCourseController.list, '/ChoiceCurse', endpoint="ChoiceCurse")
api.add_resource(CourseController.updateCurse , '/updateCurse', endpoint=' updateCurse')
api.add_resource(CourseController.insertCurse , '/insert', endpoint='insert')
api.add_resource(PorfossorController.list , '/profossors' , endpoint='profossors')
api.add_resource(LoginController.Login, '/login' , endpoint='Login')


if __name__ == '__main__':
    app.run('127.0.0.1',5000,True)



