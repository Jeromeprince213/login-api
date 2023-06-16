#login_app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from bcrypt import checkpw

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Initialize CORS
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flaskmicroadmin:apolloatr@localhost/microservicesdb'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()
    if user and checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login failed!'})
if __name__ == '__main__':
    app.run(debug=True,port=5002)