from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)
conn = pymysql.connect('localhost', 'root', 'P@ssw0rd', 'pdeesawatSQL')


@app.route("/")
def showData():
    version = 'version 1.0.0'
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM `student`;")
        rows = cur.fetchall()
        return render_template('index.html', data=version, datas=rows)


@app.route("/student")
def showForm():
    return render_template('addstudent.html')


@app.route("/insert", methods=['POST'])
def insertForm():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql = "INSERT into `student` (`fname`, `lname`, `phone`) values ('{}','{}','{}')".format(fname, lname,
                                                                                                     phone)
            cursor.execute(sql)
            conn.commit()
        return redirect(url_for('showData'))


@app.route("/delete/<string:id_data>", methods=['GET'])
def delete(id_data):
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM `student` WHERE `id`={};".format(id_data))
        conn.commit()
    return redirect(url_for('showData'))


@app.route("/update", methods=['POST'])
def updateForm():
    if request.method == 'POST':
        id = request.form['id']
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        with conn.cursor() as cursor:
            sql = "UPDATE `student` SET `fname`='{}', `lname`='{}', `phone`='{}' WHERE `id`={};".format(fname, lname,
                                                                                                        phone, id)
            cursor.execute(sql)
            conn.commit()
        return redirect(url_for('showData'))


if __name__ == '__main__':
    app.run(debug=True)
