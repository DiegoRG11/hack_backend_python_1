from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#Hack1

@app.route("/users", methods=["GET"])
def fn_get_users():

    return jsonify({
        "payload":"success"
    })

if __name__ == "__main__":
    app.run(debug=True)

#Hack2

@app.route("/user", methods=["POST"])
def fn_add_user():
    email = 'foo@foo.com'
    name = 'Fooziman'
    id = 1

    return jsonify({
        "payload":"success"
    })

#Hack3

@app.route("/user", methods=["DELETE"])
def fn_delete_user():
    email = 'diisaac.36@gmail.com'
    
    return jsonify({
        "payload":"success"
    })

#Hack4

@app.route("/user", methods=["PUT"])
def fn_update_user():
    email = 'barziman@hotmail.com'
    name = 'Barziman'
    id = 1

    return jsonify({
        "payload":"success",
        "error": False
    })

#Hack5

@app.route("/api/v1/users", methods=["GET"])
def fn_consulta_users():
    email = 'foo@foo.com'
       
    return jsonify({
        "payload":[]
    })

#hack6

@app.route("/api/v1/user", methods=["POST"])
def fn_api_user():
    email = request.args["email"]
    name = request.args["name"]


    return jsonify({
        "payload":{
            "email":email,
            "name":name
        }
    })

#hack7

@app.route("/api/v1/user/add", methods=["POST"])
def fn_api_add():

    email = request.form.get("email")   
    name = request.form.get("name")
    id = request.form.get("id")
   

    return jsonify({
        "payload":  {
            'email':email,
            'name':name,
            'id':id,
        }
    }) 

#hack8

@app.route("/api/v1/user/create", methods=["POST"])
def fn_api_create():

    if(request.method == "POST"):

        data = {
            'email': 'foo@foo.foo',
            'name': 'fooziman',
            'id': '123'
        }

    return jsonify({
        "payload": data
     })





if __name__ == "__main__":
    app.run(debug=True)