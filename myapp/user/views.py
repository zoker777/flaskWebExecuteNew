from flask import render_template, session, url_for, request
from werkzeug.utils import redirect
from myapp import app_user


@app_user.route('/login')
def loginpage():
    return render_template("login.html")

@app_user.route('/loginProcess',methods=['POST','GET'])
def loginProcesspage():
    if request.method=='POST':
        nm=request.form['nm']
        pwd=request.form['pwd']
        if nm=='zj' and pwd=='123':
            session['username'] = nm
            # return render_template("index.html",data=nm)
            return redirect(url_for('index'))
        else:
            return 'the username or userpwd does not match!'