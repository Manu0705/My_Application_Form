from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# MySQL config
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sapth@4747",
    database="applications_db"
)
cursor = db.cursor()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    fullname = request.form['fullname']
    fathername = request.form['fathername']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    sql = "INSERT INTO applications (fullname, fathername, email, phone, message) VALUES (%s, %s, %s, %s, %s)"
    values = (fullname, fathername, email, phone, message)
    cursor.execute(sql, values)
    db.commit()

    return "Application submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
