from flask import Flask,jsonify,request,render_template
from DB import mongo_db
from DB import enc_dec
import pandas as pd

app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    return ''' This is a vault application.  
                <form method="POST" action="/login">
                <input type="submit" value="login">
            </form>

            <form method="POST" action="/validate_signup">
                <input type="text" name="uname" placeholder="username"><br>
                <input type="email" name="email" placeholder="email address"><br>
                <input type="text" name="password" placeholder="*********"><br>
                <input type="submit" value="submit">
            </form>
           '''
@app.route('/login',methods=["POST","GET"])
def login():
    return '''<form method="POST" action="/validate_login">
                <input type="email" name="email" placeholder="email address"><br>
                <input type="text" name="password" placeholder="*********"><br>
                <input type="submit" value="login">
            </form>'''

@app.route('/validate_login',methods=["POST","GET"])
def validate_login():
    data = {}
    data["email"] = email = request.form["email"]
    data["password"] = passowrd = request.form["password"]
    result = mongo_db.validate(email,passowrd)
    tenantid = result
    
    content = mongo_db.get_table(tenantid)
    #print(type(content))
    #print("content",content)
    #print(len(content))
    for value in content:
        
        finalresult = []
        for items in value:
            result_list = []
            #print("value",value)
            my_data = value["_id"]
            #print("mydata",my_data)
            result_list.append(my_data["appname"])
            result_list.append(my_data["username"])
            result_list.append(my_data["password"])
            #print(result_list)
        finalresult.append(result_list)
        print(finalresult)
    dataframe = pd.DataFrame(finalresult,columns=["appnamme","username","password"])
    print(dataframe)
    return content


@app.route("/validate_signup",methods=["POST","GET"])
def validate_signup():
    data = {}
    data["name"] = name = request.form["uname"]
    data["email"] = email = request.form["email"]
    data["password"] = password =  request.form["password"]
    result = enc_dec.encrypt(name,email,password)
    return result







if __name__ == "__main__":
    app.run(debug=True)