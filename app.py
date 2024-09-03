from flask import*
from flask_restful import Api
app = Flask(__name__)
# import os

api = Api(app)
from datetime import timedelta
from flask_jwt_extended import JWTManager
# from flask_cors import CORS
# CORS(app)
# SET UP JWT
app.secret_key="dfgjvnosihfgilfjshfeudfljawe_.sdcbwww.???,undcyedvDDC"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=28)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


# endpoints/ routes

from views.views import MemberSignup,MemberSignin,MemberProfile, ChangePassword, About, Elders,DeskPost,Pastors
api.add_resource(MemberSignup, '/api/membersignup')
api.add_resource(MemberSignin, '/api/membersignin')
api.add_resource(MemberProfile, '/api/memberprofile')
api.add_resource(About, '/api/about')
api.add_resource(Elders, '/api/elders')
api.add_resource(Pastors, '/api/pastors')
api.add_resource(DeskPost, '/api/deskpost')




from views.view_dashboard import AddDeskPost, AdminSignup, AdminSignin, AdminProfile,DeskDelete
api.add_resource(AddDeskPost, '/api/add_deskpost')
api.add_resource(DeskDelete, '/api/deskdelete')
api.add_resource(AdminSignup, '/api/adminsignup')
api.add_resource(AdminSignin, '/api/adminsignin')
api.add_resource(AdminProfile, '/api/adminprofile')
api.add_resource(ChangePassword, '/api/changepass')


if __name__ =='__main__':
    app.run(debug=True)