import pymysql
from flask_restful import Resource
from flask import *
from functions import *
# import JWT packages#
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required



# Add a member class
# member_signup and member_signin
class MemberSignup(Resource):
    def post(self):
        # get data from client
        data = request.json
        surname= data["surname"]
        others= data["others"]
        gender= data["gender"]
        phone= data["phone"]
        dob= data["dob"]
        status= data["status"]
        password= data["password"]


        # Check phone number format
        if not check_phone(phone):
            return jsonify({"message": "Invalid phone number format"})
        
        # Normalize phone number
        phone = normalize_phone(phone)
        

        # check if password is valid
        response = passwordValidity(password)
        if response == True:
            # connect to DB
            # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
            connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
            cursor = connection.cursor()
            # instert into database
            sql = "insert into members (surname, others, gender, phone, dob, status, password ) values( %s, %s, %s, %s, %s, %s,%s)"
            data = (surname, others, gender, phone, dob, status, hash_password(password))
            try:
                cursor.execute(sql, data)
                connection.commit( )
                send_sms(phone, "Registration successful.Thanks joining PEFA")
                return jsonify({ "message": "REGISTER SUCCESSFUL. Thanks joining PEFA" })

            except:
                connection.rollback()
                return jsonify({ "message": "FAILED. Please Try Again" })

        else:
            return jsonify({ "message": response })


class MemberSignin(Resource):
    def get(self):
        # get request from client
        data = request.json
        phone = data ["phone"]
        password = data ["password"]

        # Check phone number format
        if not check_phone(phone):
            return jsonify({"message": "Invalid phone number format"})
        
         # Normalize phone number
        phone = normalize_phone(phone)

        # connect to db
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        # check if phone exist
        sql = "select* from members where phone =%s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, phone)
        if cursor.rowcount == 0:
            return jsonify({"message":"Phone does not exist"})
        
        else:
            # check password////
            member = cursor.fetchone()
            hashed_password =member['password']
            is_matchpassword = hash_verify(password,hashed_password)
            if is_matchpassword == True:
                #including jwt
                access_token = create_access_token(identity= member, fresh= True)
                return jsonify({'access_token': access_token,'member':member})
            
                # is_matchpassword == False:
            elif is_matchpassword == False:
                return jsonify({ "message":"LOGIN FAILED,wrong password" })

            else:

                return jsonify({ "message": "Something went wrong" })


class MemberProfile(Resource):
    @jwt_required(fresh=True)
    def post(self):
        data = request.json
        member_id = data["member_id"]
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        # connect to DB
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        
        sql = "SELECT * FROM members WHERE member_id = %s"
        cursor  = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, member_id)
        count = cursor.rowcount
        if  count == 0:
            return jsonify({  "message":"Member does not exist!"  })
        else:
            member = cursor.fetchone()
            return jsonify({  "message": member })
        


class ChangePassword(Resource):
    @jwt_required(fresh= True)
    def put(self):
        data = request.json 
        member_id = data["member_id"]
        current_password = data["current_password"] 
        new_password = data['new_password']
        confirm_password = data["confirm_password"]    
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')  
        sql = "select* from members where member_id = %s"
        cursor =connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql, member_id)
        if cursor.rowcount ==0:
            return jsonify({"message":"Member not found"})
        else:
            member =cursor.fetchone()
            hashed_password= member["password"]
            is_matchpassword = hash_verify(current_password,hashed_password)
            if is_matchpassword:
                rensponse = passwordValidity(new_password)
                if rensponse ==True:
                    if new_password == confirm_password:
                        # password match
                        sql = "update members set password =%s where member_id=%s"
                        cursor1= connection.cursor()
                        data = ( hash_password(new_password), member_id)
                        try:
                            cursor1.execute(sql,data)
                            connection.commit()
                            return jsonify({"message":"Password changed"})
                        except:
                            connection.rollback()
                            return jsonify({"message":"Password not changed"})
                    else:
                        # Password not match entry
                        return jsonify({"message":"New password does not match with confirm password"})
                else:
                    return jsonify({"message":rensponse})
                
            
            else:
                return jsonify({"message":"old password is wrong"})        
            

class About(Resource):
    def get(self):
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        sql = "select* from aboutchurch "  
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        count = cursor.rowcount
        if count == 0:
            return jsonify({'message': 'No  church details'})
        else:
            about = cursor.fetchall()
            return jsonify(about) 



class DeskPost(Resource):
    def get(self):
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        sql = "select* from desk_post "  
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        count = cursor.rowcount
        if count == 0:
            return jsonify({'message': 'No  updates posted'})
        else:
            deskpost = cursor.fetchall()
            return jsonify(deskpost)                  
        


class Elders(Resource):
    def get(self):
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        sql = "select* from elders "  
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        count = cursor.rowcount
        if count == 0:
            return jsonify({'message': 'No elder found'})
        else:
            elder = cursor.fetchall()
            return jsonify(elder)                  


class Pastors(Resource):
    def get(self):
        connection = pymysql.connect('Pefa.mysql.pythonanywhere-services.com', user='Pefa',password='peter1234',database='Pefa$default')
        # connection = pymysql.connect(host ='localhost',user = 'root', password ='', database = 'pefa_db')
        sql = "select* from pastor "  
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        count = cursor.rowcount
        if count == 0:
            return jsonify({'message': 'No pastor found'})
        else:
            pastor = cursor.fetchall()
            return jsonify(pastor)                  





          