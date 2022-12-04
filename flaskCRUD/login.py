from mySQL import *

# mycursor.execute("CREATE DATABASE IF NOT EXISTS appbook")

# mycursor.execute("SHOW DATABASES;")
# for i in mycursor:
#     print(i)
# create table
# tblbook = """
# book_id INT(6) not null primary key auto_increament,
# book_name VARCHAR(50) not null,
# BookImg VARCHAR(100)  not null,
# Book_pages INT(6) not null,
# Book_pub_date YEAR not null"""

# mycursor.execute(" CREATE TABLE IF NOT EXISTS book ( " + tblbook + ")")

#    PRIMARY KEY(book_id)

# tbltest = "INSERT INTO test(name,\
#         url) VALUES(%s,%s)"
# tbltest_value = ("python","abc")

# mycursor.execute(tbltest, tbltest_value)

# mycursor.execute("SELECT id,name, url FROM test")
# result=mycursor.fetchall()
# for i in result:
#         print(i)

mycursor.execute("SELECT * FROM stdrecord")
result = mycursor.fetchall()
# mycursor.execute("SELECT * FROM test WHERE  id=1")
# result=mycursor.fetchall()
for i in result:
        print(i)
# mycursor.execute("SELECT `name` FROM test;")
# mycursor.execute("DESCRIBE test;")
# for i in mycursor:
#     print(i)

# dbconn.commit()




@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == "POST":

        id = request.form['id']
        name = request.form['name']
        rollno = request.form['rollnumber']

        query = "UPDATE stdrecord SET(\
                 name=%s,\
                 rollno=%s)\
                 WHERE id=%s "
        insertValue = (name, rollno, id)
        mycursor.execute(query, insertValue)
        dbconn.commit()
        flash("updated successfully")
    return redirect(url_for("Index"))