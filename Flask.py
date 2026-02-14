from flask import Flask, render_template,request,flash,redirect,url_for
import mysql.connector

app = Flask(__name__)
app.secret_key = "mysecretkey"

#connection with mysql
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nihal@123",
        database="coffeehouse"
    )
@app.route("/view") #For Flash Screen
def view():
  return render_template("Test.html")

@app.route("/", methods=["GET", "POST"]) #use to connect url with python function
def Home(): #python function
  if request.method == "POST":
    fname = request.form["fname"]
    lname = request.form["lname"]
    gen = request.form["gen"]
    mail = request.form["mail"]
    mob = request.form["mob"]

    con = get_db_connection()
    mycursor = con.cursor()

    mycursor.execute("""
    INSERT INTO registration
    (First_Name, Last_Name, Gender, Email, Mobile_Number)
    VALUES (%s, %s, %s, %s, %s)
    """, (fname, lname, gen, mail, mob))

    con.commit()
    mycursor.close()
    con.close()
    flash("Data inserted successfully!", "success")
    return redirect(url_for("view"))


  return render_template("Home.html")



@app.route("/beans")
def Beans():
  return render_template("beans.html")


@app.route("/abt")
def abt():
  return render_template("About.html")
if __name__ == "__main__":
  app.run(debug=True, use_reloader=False)