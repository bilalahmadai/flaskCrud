from flask import Flask, render_template, request, redirect, url_for, flash
from mySQL import *
app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route("/")
def Index():
    mycursor.execute("SELECT * FROM stdrecord")
    data = mycursor.fetchall()
    # mycursor.close()
    return render_template("index.html", students=data)


@app.route("/insert", methods=["POST"])
def insert():
    if request.method == "POST":
        flash("added successfully")
        name = request.form['name']
        rollno = request.form['rollnumber']

        query = "INSERT INTO stdrecord(\
                 name,\
                 rollno)\
                 VALUES(%s,%s)"
        insertValue = (name, rollno)

        mycursor.execute(query, insertValue)
        dbconn.commit()
        return redirect(url_for('Index'))


@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == "POST":

        id = request.form['id']
        name = request.form['name']
        rollno = request.form['rollnumber']

        query = "UPDATE stdrecord SET name=%s,rollno=%s  WHERE id=%s "
        insertValue = (name, rollno, id)
        mycursor.execute(query, insertValue)
        dbconn.commit()
        flash("updated successfully")
    return redirect(url_for("Index"))


# @app.route("/delete/<string:id_data>", methods=['POST', 'GET'])
# def delete(id_data):
#     # print(id_data)
#     # flash("deleted successfully")
#     mycursor.execute("DELETE FROM stdrecord WHERE id=%s", (id_data))
#     dbconn.commit()
#     return redirect(url_for("Index"))
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    # cur = mysql.connection.cursor()
    mycursor.execute("DELETE FROM stdrecord WHERE id=%s", (id_data,))
    # mysql.connection.commit()
    dbconn.commit()
    return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
