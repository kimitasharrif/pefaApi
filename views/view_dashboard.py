# Import Required modules
import pymysql
from flask_restful import *
from flask import *
from functions import *
import pymysql.cursors

# import JWT Packages
from flask_jwt_extended import create_access_token, jwt_required, create_refresh_token
class DeskPost(Resource):
    def post(self):
        json = request.json
        desk_title = json['desk_title']
        message = json['message']
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        cursor = connection.cursor()
        sql = '''insert into desk_post (desk_title, message) values(%s, %s)'''
                
                # Data
        data = (desk_title, message )
        try:
            cursor.execute(sql, data)
            connection.commit() 
            return jsonify({'message': 'Desk Post Successiful'})
        except:
                    connection.rollback()
                    return jsonify({'message': 'Desk Post Failed'})
    
# class DeskUpdate(Resource):
#     @jwt_required(fresh= True)
#     def put(self):
#         data = request.json 
#         desk_id = data["desk_id"]
#         desk_title = data["desk_title"] 
#         message = data['message']
#         # confirm_password = data["confirm_password"]    
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
#         # connection = pymysql.connect(host='advance.mysql.pythonanywhere-services.com', user='advance',password='peter1234',database='advance$default')  
#         sql = "select* from members where desk_id = %s"
#         cursor =connection.cursor(pymysql.cursors.DictCursor)
#         cursor.execute(sql, desk_id)
#         if cursor.rowcount ==0:
#             return jsonify({"message":"Member not found"})
#         else:
#             member =cursor.fetchone()
#             hashed_password= member["password"]
#             is_matchpassword = hash_verify(current_password,hashed_password)
#             if is_matchpassword:
#                 rensponse = passwordValidity(new_password)
#                 if rensponse ==True:
#                     if new_password == confirm_password:
#                         # password match
#                         sql = "update members set password =%s where member_id=%s"
#                         cursor1= connection.cursor()
#                         data = ( hash_password(new_password), member_id)
#                         try:
#                             cursor1.execute(sql,data)
#                             connection.commit()
#                             return jsonify({"message":"Password changed"})
#                         except:
#                             connection.rollback()
#                             return jsonify({"message":"Password not changed"})
#                     else:
#                         # Password not match entry
#                         return jsonify({"message":"New password does not match with confirm password"})
#                 else:
#                     return jsonify({"message":rensponse})
                
            
#             else:
#                 return jsonify({"message":"old password is wrong"})        
        
class AdminSignup(Resource):
    def post(self):
        json = request.json
        username = json['username']
        email = json['email']
        phone = json['phone']
        password = json['password']

        # Check Password
        response = passwordValidity(password)
        if response:
            if check_phone(phone):
                # connection = pymysql.connect(host='localhost',
                #                                 user='root',
                #                                 password='',
                #                                 database='pefa_db')
                connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
                cursor = connection.cursor()
                sql = '''insert into admin(username, email,
                phone, password) values(%s, %s, %s, %s)'''
                
                # Data 
                data = (username, email, encrypt(phone), 
                        hash_password(password))
                try:
                    cursor.execute(sql, data)
                    connection.commit()
                    code = gen_random(4)
                    send_sms(phone, '''Thank you for Joining Shoeapp. 
                    Your Secret No: {}. Do not share.'''.format(code))
                    return jsonify({'message': 'Thank you for Joining Shoeapp'})
                except:
                    connection.rollback()
                    return jsonify({'message': 'Not OK'})

            else:
                return jsonify({'message': 'Invalid Phone ENter +254'})
        else :
            return jsonify({'message': response})
        

class AdminSignin(Resource):
    def post(self):
        json = request.json
        username = json['username']
        password = json['password']

        sql = "select * from admin where username = %s"
        # connection = pymysql.connect(host='localhost',
        #                                         user='root',
        #                                         password='',
        #                                         database='pefa_db')
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
          
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, username)
        count = cursor.rowcount
        if count == 0:
            return jsonify({'message': 'Username does Not exist'})
        else:
            admin = cursor.fetchone()
            hashed_password = admin['password']
            # Verify
            if hash_verify(password, hashed_password):
                # TODO JSON WEB Tokens
                       access_token = create_access_token(identity=username,
                                                          fresh=True)  

                       return jsonify({'message': admin, 
                                       'access_token': access_token})            
            else:
                       return jsonify({'message': 'Login Failed'})
            


class AdminProfile(Resource):
     @jwt_required(fresh=True)
     def post(self):
          json = request.json
          admin_id = json['admin_id']
          sql = "select * from admin where admin_id = %s"
        #   connection = pymysql.connect(host='localhost',
        #                                         user='root',
        #                                         password='',
        #                                         database='pefa_db')
          connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
          
          cursor = connection.cursor(pymysql.cursors.DictCursor)
          cursor.execute(sql, admin_id)
          count = cursor.rowcount
          if count == 0:
               return jsonify({'message': 'No Such Admin'})
          else:
               admin = cursor.fetchone()
               return jsonify({'message': admin})          