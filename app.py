from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import mysql.connector as conn

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Adm!n@123"
app.config["MYSQL_DB"] = "demodb"

mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def index():
    userDetails = ""
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        cur = mysql.connection.cursor()
        cur.execute("insert into users(name,email) values(%s,%s)",
                    (username, email))
        mysql.connection.commit()

        users = cur.execute("select * from users")
        if users > 0:
            userDetails = cur.fetchall()
    return render_template("index.html", userDetails=userDetails)


if __name__ == "__main__":
    app.run(debug=True)
