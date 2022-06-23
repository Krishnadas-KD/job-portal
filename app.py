from email import message
from typing import Counter
from flask import *
import flask
from pymysql import NULL
from dbconnect import *
from werkzeug.utils import secure_filename
import os
from emailsend import mailsender

app=Flask(__name__)
app.secret_key="bnm"

global msg
msg=NULL
@app.route('/logout')
def logout():

    session['email']=None
    session['account']=None
    return flask.redirect('/')


@app.route('/')
def Mainpage():
    

    if session.get("account")==None or session.get("email")==None:
        return flask.redirect('/signin')
    if session['email']!=None:

        if session['account']=="js":
            result2=selectonecond("select * from jsdetaile where email=%s",(session['email']))
            if result2==None:
                print("hi")
                result2=selectonecond("select * from logindata where email=%s",(session['email']))
                return render_template("jsenter.html" ,result=result2)
            else:
                joblist=select("select * from jops")
                img=select("select * from jpdetaile")
                return render_template("homepagejs.html",joplist=img,msg=msg)
        elif session['account']=="jp":
            result2=selectonecond("select * from jpdetaile where email=%s",(session['email']))
            if result2==None:
                result2=selectonecond("select * from logindata where email=%s",(session['email']))
                return render_template("jpenter.html" ,result=result2)
            else:
                jopslist=selectcond("select * from jops where email=%s",session['email'])
                print(jopslist)
                return render_template("homepagejp.html",jopslist=jopslist)
    return render_template("homeemp.html")



@app.route('/jphome')
def jphome():
    jopslist=selectcond("select * from jops where email=%s",session['email'])
    print(jopslist)
    return render_template("jphome.html",jopslist=jopslist)

@app.route('/jshome')
def jshome():
    joblist=select("select * from jops")
    img=select("select * from jpdetaile")
    return render_template("jshome.html",joplist=img,msg=msg)

@app.route('/signin')
def signin():
    return render_template("Login.html")
@app.route('/Signup')
def Signup():
    return render_template("Signin.html")

@app.route('/register',methods=['POST','GET'])
def register():
    try:
        fname=request.form['fname']
        email=request.form['email']
        phoneno=request.form['phoneno']
        password=request.form['password']
        vmode=request.form['vmode']
        print(fname,email,phoneno,password,vmode)
        result=iud("insert into logindata(fname,email,phoneno,password,vmode) values(%s,%s,%s,%s,%s)",(fname,email,phoneno,password,vmode))
        print()
        return flask.redirect("/")
    except:
        return flask.redirect("/")


@app.route('/login',methods=['POST','GET'])
def login():
    
    email=request.form['email']
    password=request.form['password']
    result=selectonecond("select * from logindata where email=%s and password=%s",(email,password))

    if result==None:
        return render_template("Login.html",msg="Invalid Email or Password")
    if result[4]=="js":
            print(email)
            session['email']=email
            session['account']="js"
            return flask.redirect('/')
    
    elif result[4]=="jp":
            session['email']=email
            session['account']="jp"
            return flask.redirect('/')

    else:
        session.clear()
        return flask.redirect('/')



@app.route('/adddetailsjs',methods=['POST','GET'])

def add_Detailsjs():
    email=request.form['emailv']
    fname=request.form['fullname']
    Bio=request.form['bio']
    age=request.form['age']
    dob=request.form['dob']
    qualification=request.form['qualification']
    gender=request.form['gender']
    city=request.form['city']
    phoneno=request.form['phoneno']
    photo=request.files['photo']
    cv=request.files['cv']
    phtotname=secure_filename(photo.filename)
    cvname=secure_filename(cv.filename)
    photourl='../static/profileimage/'+phtotname
    cvurl='../static/cv/'+cvname
    cv.save(os.path.join(app.root_path, 'static/cv/'+cvname))
    photo.save(os.path.join(app.root_path, 'static/profileimage/'+phtotname))

    result=iud("insert into jsdetaile(email,name,bio,age,dob,qualification,gender,city,phone,photo,cv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        ,(email,fname,Bio,age,dob,qualification,gender,city,phoneno,photourl,cvurl))

    return flask.redirect("/")

@app.route('/cjoblist/<id>',methods=['POST','GET'])

def cjoblist(id):
    val=selectcond("select * from jops where email=%s",(id))
    return render_template("cjopview.html",joplist=val)



@app.route('/adddetailsjp',methods=['POST','GET'])
def add_Detailsjp():
    
    fname=request.form['fullname']
    year=request.form['cyear']
    ceo=request.form['ceo']
    founder=request.form['founder']
    phoneno=request.form['phoneno']
    email=request.form['emailv']
    capital=request.form['capital']
    city=request.form['city']
    photo=request.files['photo']
    disc=request.form['disc']
    phtotname=secure_filename(photo.filename)
    photourl='../static/profileimage/'+phtotname
    photo.save(os.path.join(app.root_path, 'static/profileimage/'+phtotname))

    result=iud("insert into jpdetaile values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        ,(fname,year,ceo,founder,phoneno,email,capital,city,photourl,disc))

    return flask.redirect("/")

@app.route('/updatepage',methods=['POST','GET'])
def updatepage():
    if session['account']=="js":
        result=selectonecond("select * from jsdetaile where email=%s",(session['email']))
        return render_template("jsupdate.html",result=result)
    if session['account']=="jp":
        result=selectonecond("select * from jpdetaile where email=%s",(session['email']))
        return render_template("jpupdate.html",result=result)


@app.route('/updatedetailsjp',methods=['POST','GET'])
def UpdateDetailsjp():
    
    fname=request.form['fullname']
    year=request.form['cyear']
    ceo=request.form['ceo']
    founder=request.form['founder']
    phoneno=request.form['phoneno']
    email=request.form['emailv']
    capital=request.form['capital']
    city=request.form['city']
    disc=request.form['disc']
    photo=request.files['photo']
    print(photo.filename)
    if photo.filename != "":
        phtotname=secure_filename(photo.filename)
        photourl='../static/profileimage/'+phtotname
        photo.save(os.path.join(app.root_path, 'static/profileimage/'+phtotname))
        result=iud("update jpdetaile set profile=%s where Email=%s"
        ,(photourl,session['email']))
        if session['email']!=email:
            result=iud("update logindata set email=%s,phoneno=%s,fname=%s where email=%s"
        ,(email,phoneno,fname,session['email']))
        session['email']=email
        return flask.redirect("/")
    if session['email']!=email:
        result=iud("update logindata set email=%s,phoneno=%s,fname=%s where email=%s"
        ,(email,phoneno,fname,session['email']))
    result=iud("update jpdetaile set  Cname=%s,Cyear=%s,ceo=%s,founder=%s,MobileNo=%s,Email=%s,capital=%s,city=%s,disc=%s where Email=%s"
        ,(fname,year,ceo,founder,phoneno,email,capital,city,disc,session['email']))
    session['email']=email
    return flask.redirect("/")


@app.route('/updatedetailsjs',methods=['POST','GET'])
def UpdateDetailsjs():
    email=request.form['emailv']
    fname=request.form['fullname']
    Bio=request.form['bio']
    age=request.form['age']
    dob=request.form['dob']
    qualification=request.form['qualification']
    gender=request.form['gender']
    city=request.form['city']
    phoneno=request.form['phoneno']
    photo=request.files['photo']
   
    cv=request.files['cv']
    phtotname=secure_filename(photo.filename)
    cvname=secure_filename(cv.filename)
    photourl='../static/profileimage/'+phtotname
    cvurl='../static/cv/'+cvname


    if photo.filename != "":
        photo.save(os.path.join(app.root_path, 'static/profileimage/'+phtotname))
        result=iud("update jsdetaile set photo=%s where email=%s"
        ,(photourl,session['email']))
    if cv.filename != "":
        cv.save(os.path.join(app.root_path, 'static/cv/'+cvname))
        result=iud("update jsdetaile set cv=%s where email=%s"
        ,(cvurl,session['email']))

    if session['email']!=email:
        result=iud("update logindata set email=%s,phoneno=%s,fname=%s where email=%s"
        ,(email,phoneno,fname,session['email']))
        
    #insert into jsdetaile(email,name,bio,age,dob,qualification,gender,city,phone,photo,cv) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    result=iud("update jsdetaile set email=%s,name=%s,bio=%s,age=%s,dob=%s,qualification=%s,gender=%s,city=%s,phone=%s where email=%s"
        ,(email,fname,Bio,age,dob,qualification,gender,city,phoneno,session['email']))
    session['email']=email
    return flask.redirect("/")

@app.route('/profileview',methods=['POST','GET'])

def profileiew():
    
    if session['account']=='js':
        email=session['email']
        result=selectonecond("select * from jsdetaile where email=%s",(email))
        return render_template("jsprofile.html" ,result=result)
    if session['account']=='jp':
        email=session['email']
        result=selectonecond("select * from jpdetaile where email=%s",(email))
        return render_template("jpprofile.html" ,result=result)
        

@app.route('/addjops',methods=['POST','GET'])

def addjops():
    
    jopc=request.form['jopc']
    jopdic=request.form['jopdic']
    jopvac=request.form['jopvac'] 
    result=iud("insert into jops(email,jobcatogory,discription,vacancy,applyed) values(%s,%s,%s,%s,%s)",(session['email'],jopc,jopdic,jopvac,0))
    joplist=select("select * from jops")
    for i in joplist:
        id=i[0]
    l="table"+str(id)
    result=iud("update jops set tname=%s where id=%s",(l,id))
    result=createtable(l)
    result=select("select email from jsdetaile")

    mailsender(result) 
    print(result)
    return flask.redirect("/")

@app.route('/apply/<id>',methods=['POST','GET'])

def applyjop(id):

    result=selectonecond("select * from jsdetaile where email=%s",(session['email']))
    result2=selectonecond("select * from jops where id=%s",(id))
    result3=selectonecond("select * from "+result2[6]+" where email=%s",(session['email']))
    if result3 is not None:
            global masg
            msg="Already applyed"
            joblist=select("select * from jops")
            img=select("select * from jpdetaile")
            return render_template("jshome.html",joplist=img,msg=msg)
    result3=iud("insert into "+result2[6]+"(email,name,phone) values(%s,%s,%s)",(session['email'],result[1],result[8]))
    result4=iud("update jops SET applyed=applyed+1 where id=%s",(id))
    return flask.redirect("/")


@app.route('/view/<id>',methods=['POST','GET'])

def viewinfo(id):
    result=selectcond("select * from jops where id=%s",(id))
    for i in result:
        email=i[1]
    result=selectonecond("select * from jpdetaile where email=%s",(email))
    return render_template("jpprofile.html" ,result=result)

@app.route('/more/<id>',methods=['POST','GET'])

def moreinfo(id):
    result=selectonecond("select * from jops where id=%s",(id))
    print(result[6])
    result2=select("select * from "+result[6])
    return render_template("moredetails.html" ,result=result2,l=result[2],l2=result[3],l3=result[4],id=result[0])





@app.route('/viewjs/<id>/<idjs>',methods=['POST','GET'])

def viewjs(id,idjs):
    result=selectonecond("select * from jops where id=%s",(id))
    result2=selectonecond("select * from "+result[6]+" where id=%s",(idjs))
    result=selectonecond("select * from jsdetaile where email=%s",(result2[1]))
    return render_template("jsprofile.html" ,result=result)

if __name__ == "__main__":
  app.run(debug=True)