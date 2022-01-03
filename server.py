from flask import Flask , render_template , url_for , request ,redirect, flash, session
import DB

app = Flask(__name__)
app.secret_key = 'Formula'

@app.route("/")
def home():
    if len(session)>0:
        email = session['email']
        name = DB.getName(email)
        return render_template('home.html',page_title="Home Page",name = name)
    else:
        return render_template('ohome.html',page_title="Home Page")

@app.route("/Signup/",methods = ['POST', 'GET'])
def Signup():
    if request.method == 'POST':
        name = request.form['fs'] + ' ' + request.form['ls']
        email = request.form['em']
        password = request.form['ps']
        if DB.verify(email) == False:
            values = (DB.length()+1,name,email,password)
            DB.insert(values)
            session['email'] = email
            return redirect(url_for('home'))
        else:
            msg = "This Email is Exist, Do You Want to Login ? "
            return render_template('Signup.html',page_title="Sign Up",msg=msg)
    else:
        return render_template('Signup.html',page_title="Sign Up")

@app.route("/Login/",methods = ['POST', 'GET'])
def Login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if DB.verify(email,password) == True:
            session['email'] = email
            return redirect(url_for('home'))

        else:
            flash('Invalid email or password. Please try again!')
            return redirect(url_for('Login'))

    return render_template('Login.html',page_title="Login")

@app.route("/Logout/")
def Logout():
    session.pop('email')
    return redirect(url_for("home"))

@app.route("/JavaScript/")
def js():
    return render_template('js.html',page_title="JavaScript Tutorial")

@app.route("/Java/",methods = ['POST', 'GET'])
def java():
    if request.method == 'POST':
        email = session['email']
        code = request.form['code']
        uid = DB.getIDUser(email)
        if DB.verifyCode(code):
            DB.enroll(uid,2)
            DB.deleteCode(code)
            return render_template('java.html',page_title="Java Tutorial")
        else:
            flash('Invalid Code. Please try again!')
            price = DB.getPrice("Java")
            return render_template('code.html',page_title="Verify",lang = "java",price=price)

    else:
        email = session['email']
        uid = DB.getIDUser(email)
        if DB.isenroll(uid,2):
            return render_template('java.html',page_title="Java Tutorial")
        else:
            price = DB.getPrice("Java")
            return render_template('code.html',page_title="Verify",lang = "java",price=price)

@app.route("/C++/",methods = ['POST', 'GET'])
def Cpp():
    if request.method == 'POST':
        email = session['email']
        code = request.form['code']
        uid = DB.getIDUser(email)
        if DB.verifyCode(code):
            DB.enroll(uid,3)
            DB.deleteCode(code)
            return render_template('cpp.html',page_title="C++ Tutorial")
        else:
            flash('Invalid Code. Please try again!')
            price = DB.getPrice("C++")
            return render_template('code.html',page_title="Verify",lang = "Cpp",price=price)
    else:
        email = session['email']
        uid = DB.getIDUser(email)
        if DB.isenroll(uid,3):
            return render_template('cpp.html',page_title="C++ Tutorial")
        else:
            price = DB.getPrice("C++")
            return render_template('code.html',page_title="Verify",lang = "Cpp",price=price)

@app.route("/Python/",methods = ['POST', 'GET'])
def Python():
    if request.method == 'POST':
        email = session['email']
        code = request.form['code']
        uid = DB.getIDUser(email)
        if DB.verifyCode(code):
            DB.enroll(uid,5)
            DB.deleteCode(code)
            return render_template('python.html',page_title="Python Tutorial")
        else:
            flash('Invalid Code. Please try again!')
            price = DB.getPrice("Python")
            return render_template('code.html',page_title="Verify",lang = "Python",price=price)
    else:
        email = session['email']
        uid = DB.getIDUser(email)
        if DB.isenroll(uid,5):
            return render_template('python.html',page_title="Python Tutorial")
        else:
            price = DB.getPrice("Python")
            return render_template('code.html',page_title="Verify",lang = "Python",price=price)


if __name__ == "__main__":
    app.run(debug=True , port=3024)

# DB.insertCode('N12345')
