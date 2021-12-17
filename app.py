from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

# from blacklist import BLACKLIST
from blacklist import BLACKLIST
from db import db
from ma import ma
from resources.user import UserRegister, UserLogin, UserLogout, User, TokenRefresh, UploadImage

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config['JWT_BLACKLIST_ENABLED'] = True  # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens

app.secret_key = "somadome"  # could do app.config['JWT_SECRET_KEY'] if we prefer
api = Api(app)

jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


@jwt.token_in_blocklist_loader
def check_if_token_in_blacklist(jwt_headers, jwt_payload):
    return jwt_payload['jti'] in BLACKLIST


@jwt.revoked_token_loader
def revoked_token_callback(jwt_headers, jwt_payload):
    return jsonify({
        'description': 'the token has been revoked.',
        'error': 'token revoked'
    }), 401


api.add_resource(UserRegister, "/register")
# api.add_resource(User, "/user/<string:user_name>")
# api.add_resource(User, "/user/<int:userId>")
api.add_resource(User, "/user/profile")
api.add_resource(UserLogin, "/login")
api.add_resource(TokenRefresh, "/refresh")
api.add_resource(UserLogout, "/logout")
api.add_resource(UploadImage, "/upload")


if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    app.run(port=5000, debug=True)
