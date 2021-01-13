from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           if request.method == 'GET':
              return user
           elif request.method == 'DELETE':
              users['users_list'].remove(user)
              resp = jsonify(), 204
              return resp
      resp = jsonify({"Msg": "User not found with provided id."}), 404
      return resp
   return users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name')
      if search_username :
         subdict = {'users_list' : []}
         search_job = request.args.get('job')
         if  search_job :
            for user in users['users_list']:
               if user['name'] == search_username:
                  if user['job'] == search_job:
                     subdict['users_list'].append(user)
            return subdict
         else :
            for user in users['users_list']:
               if user['name'] == search_username:
                  subdict['users_list'].append(user)
            return subdict

      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      #resp.status_code = 200 #optionally, you can always set a response code. 
      # 200 is the default code for a normal response
      return resp
    