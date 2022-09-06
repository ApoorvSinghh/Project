from flask import Flask
from flask_cors import CORS
from flask_mysqldb import MySQL
from settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from blueprint_auth import authentication



app = Flask(__name__)

app.config["root"] = MYSQL_USER
app.config["apoorv123"] = MYSQL_PASSWORD
app.config["appdb"] = MYSQL_DB
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.register_blueprint(authentication, url_prefix="/api/auth")
db = MySQL(app)

if __name__ == "__main__":
    app.run()