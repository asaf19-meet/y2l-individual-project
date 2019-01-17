from flask import Flask, render_template, url_for, redirect, request, session, flash
from databases import *

UPLOAD_FOLDER = '/path/to/the/uploads'
app = Flask(__name__)


# App routing code here
@app.route('/', methods=["POST", "GET"])
def home():
    if session.get('logged_in_student') == True:
        user_stu = get_student_by_username(session["username"])
        students = student.other_stu
        return render_template("student_page.html", student = user_stu, students = students)
    else:
        return render_template("home.html")



@app.route('/student/stuednt_option_page', methods=['GET', 'POST'])
def stuednt_option_page():
    user_stu = get_student_by_username(session["username"])
    if request.method == 'GET':
        return render_template('student_option_page.html',students = get_students())
    else: 
        other_stu_username = request.form['requested_student']
        other_stu = get_student_by_username(other_stu_username)
        connect_student_student(other_stu,user_stu)
        return redirect(url_for('stuednt_option_page',username = tutor_username))
    


@app.route('/student/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        POST_USERNAME = str(request.form['username'])
        POST_PASSWORD = str(request.form['password'])
        student = auth_student(POST_USERNAME, POST_PASSWORD)
        print(student)
        if student is not None:
            session['logged_in_student'] = True
            session["username"] = student.username
            print("logged_in_student")
            return redirect(url_for('home'))
        else:
            print("wrong")
            return render_template("student_login.html", error="Bad login")
    else:
        return render_template("student_login.html")
 
@app.route("/student/logout")
def student_logout():
    session['logged_in_student'] = False
    return home()


@app.route("/student/signup", methods=['GET', 'POST'])
def student_signup():
    if request.method == 'GET':
        return redirect(url_for('student_signup'))
    else:
        username = request.form['username']
        password = request.form['password']
        name = request.form['name']
        location = request.form['location']
        phone_number = request.form['phone_number']
        nationality = request.form['nationality']
        add_student(username,password,name,location,phone_number,nationality)
        session['logged_in_student'] = True
        session["username"] = username

        return redirect(url_for('home'))
           
# Running the Flask app
if __name__ == "__main__":
    app.run(debug=True)
