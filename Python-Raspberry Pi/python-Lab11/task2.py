import base64
import sqlite3
import webbrowser
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'topsecret!'
ids_list = []
link_list = []
city_list = []
country_list = []
student_list = []

class Form(FlaskForm):
    student = SelectField('Student',choices=[])


def DB_connection(db_file):
    """ Create connection to any db """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        connection.row_factory = sqlite3.Row
    except Exception as e:
        print(e)

    return connection

def fetch_data():
    global ids_list, link_list, city_list, country_list, student_list
    ids_list = []
    link_list = []
    city_list = []
    country_list = []
    student_list = []
    connection = DB_connection("week10.db")
    cursor = connection.cursor()
    res = cursor.execute("SELECT * FROM Lab10")
    for row in res:
        ids_list.append(row[0])
        link_list.append(base64.b64decode(row[1]).decode())
        city_list.append(row[2])
        country_list.append(row[3])
        student_list.append(row[4])
    connection.close()


@app.route('/')
def index():
    return render_template('index.html', the_title="Task 2 - Saba")

@app.route('/findstudent', methods=['GET', 'POST'])
def findstudent():
    fetch_data()
    choi = zip(ids_list, student_list)
    form = Form()
    form.student.choices = [(x[0], x[1]) for x in choi ]
    if request.method == 'POST':
        connection = DB_connection("week10.db")
        cursor = connection.cursor()
        res = cursor.execute("SELECT * FROM Lab10")
        row = cursor.execute("SELECT * FROM Lab10 WHERE id = ?", (form.student.data,)).fetchone()
        connection.close()
        url = base64.b64decode(row['Link']).decode()
        webbrowser.open(url, new=2)
    return render_template('findstudent.html', form=form, the_title="Task 2: FindStudent - Saba")

@app.route('/displayall')
def displayall():
    fetch_data()
    lab10res = zip(ids_list, link_list, city_list, country_list, student_list)
    return render_template('displayall.html', results=lab10res, the_title="Task 2: DisplayAll - Saba")


if __name__ == '__main__':
    app.run(debug=True)

