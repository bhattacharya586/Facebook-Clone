from flask import Flask, render_template,session,request,redirect,url_for,jsonify
import sqlite3
import math
import uuid 
import random
import datetime
import pyrebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
firebaseConfig = {
    'apiKey': "AIzaSyB37ilXIVcj7mCmPn4OxqrN-dZOOtp0gHw",
    'authDomain': "facebook-b0b12.firebaseapp.com",
    'projectId': "facebook-b0b12",
    "databaseURL": "https://facebook-b0b12-default-rtdb.firebaseio.com",
    'storageBucket': "facebook-b0b12.appspot.com",
    'messagingSenderId': "325685957298",
    'appId': "1:325685957298:web:92132792b48b3d943d2fab",
    'measurementId': "G-X8HELK95C9",
    "type": "service_account",
    "project_id": "facebook-b0b12",
    "private_key_id": "c012602e5f63389061dc71af9d867f6c65e2412c",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCacJSeH4YN2qgD\ndIyc8Hca3y2sDdzI/X4X8kpVpaZSTsb/a/HYazXktSYKHBiW2mJ8+HOpuQhgcnYq\n99gxGgEyzCPKiKqmN7F4ybMiX/qJRkdSVFQlajoZ/YdG2660v3ZcecUuI4i2Xhyj\n5pSmG7HOp5ucX1rm0u7gp0puR/ZRsmUNimFVMtv6QL5OoXLOuxROCen6AkrCOD8+\n3AM+p4rtT2npanOFVVJ2xHiE4fuAl4BV1woYa9BHB0JfIKCxeRoPeTgcgvp2B4FQ\nc+O23/qh772fzeKgwzfNw3NiH0Bw+dvUYV/gtOv+5FAe/U4K9ftbo6c7Vf6ClpG3\nzbmO0XmBAgMBAAECggEANDeVYEM7UYrZHNX2xwdc1faYnCBRwplG3XTb4kpwSkr9\naJYIPsq8/ZesBWYLgFHVU/izLrLznJyGzK9g5vUqa5DvFwcPX8Tb2gGkch5ueKSM\n7864ZrAcdfYtG22ii9VigRDg9OEp07NNTrNjFiit/TfZWs040GuIPegCN/hX1bYL\nh+opZyJF8aFJFR2r2TVEsTsNqEKniv6QyYBfuMPj+BT8rWL5DIEWUx9x/PanFYzq\nei8uQN3/lkU2oeLUxx6eLlj2Otx3jE4lYvRMzKGJtfE9RGu898KES2wKFbf1w2lv\nyW+0aDfY5mw7Kp+vCPTsDvQd8a3dVt55uYgJwp5SwwKBgQDMOzTFyNXdD+tg9B72\nn7NzhixO3iVKwjya/gXLzHj62mm2opVsrbMuz2I+fOChptcWobkACJ1ksUJGDD4X\nOfrM9dRbvcqnTGPtPDARO/UKSvAbIE/h+Ctq9jwyCoc1+lo53sSWuPGFTZOZZuV0\nUwvE9ORpEopY4s2xlQqE1+nJwwKBgQDBllksgfyMoggFENCtVQVabY7Kr9CYHkYm\nd8Is07w2hp0pNmVlNt09xGtbr8RB6nsEyqfZ/RZcs5WqRzAS67Io4arcnVpgOGbR\nfRiKjpPHMBUalFKKfkG3mK5lrHxcGuOwmUS03nG2oChJzzfugbPMDmXzKiHQ1f/3\nLa1cgeX3awKBgQCuOLedHeWrDmCKNdaQJs5r94KmyQThEG+o/JgvMb/mpxnVTj7Q\nFiGsBgfWLKtn2y7TRKTP7YlvE3Po05rIL5LO88rzdCWDsDvybgzHNvGjlSfczCS5\nLP7E4UeanLaZincbtPjZZu3J/NKz4z5MjGeW3h5XsBRLHTfBjNYLWzE6BwKBgQCv\nsVs3SLXDkN7EcjFhzpLwMhRxIcWn+XnjObdx5aygs+V43NSDWprKjzR8XvY4eK2z\neJWEAu1Drvz7MGaSFXV5Iu5mES1PvICcSfN29NVr5tiQaeLLrLDKBvjob/Xhxcm1\nojS4DlaXz50g978kaHScksi2Oxu7pC0N0VfQaFglBwKBgB1Z+88Dd4fY9BbXvNZK\nTBPWyA7xDNJJt77wPTwmmacTufEKD/+GcNDGn36tU+kgPmOxzj05XWp8g1MekDkT\njG1n33EpqrTKlSMdXniqYquSTyC5jfsKp3pEHjCo/5lPySW2f8RZljhKSXx6ENIn\nuZwmJEBLN0bYTanUQrovLYYY\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-8m7t4@facebook-b0b12.iam.gserviceaccount.com",
    "client_id": "114333179885938058762",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8m7t4%40facebook-b0b12.iam.gserviceaccount.com"
}

# Firebase initialization
firebase = pyrebase.initialize_app(firebaseConfig)
# Firebase realtime database
database = firebase.storage()
# Connection establish with credentials
cred = credentials.Certificate(firebaseConfig)
firebase_admin.initialize_app(cred)
# Firestore connections
firedb = firestore.client()


app = Flask(__name__)
app.secret_key = 'randowmjfnwejfnwkjdnwnfewkjnfkjwefnwjenfjwnefjwef'

@app.route("/api/<info>", methods=['GET', 'POST'])
def searchAPI(info):
    conn = sqlite3.connect("database.db")
    sql = ''' SELECT id,name,email,profilepic FROM users where name LIKE "%'''  +str(info)+ '''%" and id != ? '''
    
    cur = conn.cursor()
    cur.execute(sql,[getUser(session["user__session"])[0]])
        
    rows = cur.fetchall()
    
    
    
    for i in range(0,len(rows)):
        row = rows[i]

        conn = sqlite3.connect("database.db")
        sql__se = ''' SELECT id,senderid,towhomid,status FROM friendrequest where (senderid = ? and towhomid = ?) OR (senderid = ? and towhomid = ?)'''
        cur = conn.cursor()
        cur.execute(sql__se,[getUser(session["user__session"])[0],row[0],row[0],getUser(session["user__session"])[0]])
        old__request = cur.fetchone()
        
        row = list(row)
        
        if old__request is None:
            row.append("New")
        else:
            row.append(old__request[3])
        rows[i] = tuple(row)

    info = {
        "friends": rows
    }

    return jsonify(info)

@app.route("/friendsapi/<towhom>", methods=['GET', 'POST'])
def friendsAPI(towhom):
    sender = getUser(session["user__session"])[0]
    type = "friend"
    
    retval = notification(sender,towhom,type)

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    today = datetime.datetime.now()
    status = 0
    checkSum = ''' SELECT * FROM friendrequest where senderid = ? and towhomid = ? '''
    cur.execute(checkSum,[towhom,getUser(session["user__session"])[0]])
    check = cur.fetchone()
    
    if check is None: 
        try:
            sql = "INSERT INTO friendrequest VALUES (?,?,?,?,?,?)"
            cur.execute(sql,[None,sender,towhom,str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S")),"sent"])
            conn.commit()   
            status = 1
        except IntegrityError: 
            status = 0
    else:
        status = 2
    conn.close()
    
    info = {
        "status" : status 
    }

    return jsonify(info)



@app.route("/utilities", methods=['GET', 'POST'])
def utilities():
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT count(*) FROM notification where for = ? and status = ? '''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0],"not seen"])
    notification_ = cur.fetchone()
    
    info = {
        "message" : 40,
        "notification": notification_[0]  
    }

    return jsonify(info)

@app.route("/commentUtilities/<info>", methods=['GET', 'POST'])
def commentUtilities(info):
    # conn = sqlite3.connect("database.db")
    # sql__se = ''' SELECT count(*) FROM notification where for = ? and status = ? '''
    # cur = conn.cursor()
    # cur.execute(sql__se,[getUser(session["user__session"])[0],"not seen"])
    # notification_ = cur.fetchone()
    

    doc_ref = firedb.collection(u'725003950ba2c03d959dcc25d92248b9').document(info).collection("all__comments")
    
    doc = doc_ref.get()
    

    comms = []

    for i in doc:
        comms.append((i.id,i.to_dict()))


    info = {
        "message" : 40,
        "comments": comms  
    }

    return jsonify(info)

@app.route("/uploadComment", methods=['GET', 'POST'])
def uploadComment():
    if "user__session" in session:
        if request.method == 'POST':
            conn = sqlite3.connect("acebook.db")
            cur = conn.cursor()
            today = datetime.datetime.now()
            info = request.form["from"]
            try:
                sql = "INSERT INTO comment VALUES (?,?,?,?,?,?,?,?,?)"
                cur.execute(sql,[info,request.form["message"],str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S")),getUser(session["user__session"])[0],getUser(session["user__session"])[7],getUser(session["user__session"])[1],"N/A","N/A"])
                conn.commit()
                
                doc_ref = firedb.collection(u'725003950ba2c03d959dcc25d92248b9').document(info).collection("all__comments").document(str(uuid.uuid1()))
                doc_ref.set({
                    "CommentID": info,
                    "Message": request.form["message"],
                    "DateOfUpload": str(today.day)+"/"+str(today.month)+"/"+str(today.year),
                    "TimeOfUpload": firestore.SERVER_TIMESTAMP,
                    "CommentAuthorID": getUser(session["user__session"])[0],
                    "CommentAuthorProfilePic": getUser(session["user__session"])[7],
                    "CommentAuthorName": getUser(session["user__session"])[1],
                    "Image": "N/A",
                    "Video": "N/A",
                })

            except IntegrityError:
                pass

            info = {    
                "status" : "success"
            }
            conn.close()
            return jsonify(info)

@app.route("/getComment/<info>", methods=['GET', 'POST'])
def getComment(info):
    
    conn = sqlite3.connect("acebook.db")
    sql__se = ''' SELECT * FROM comment where CommentID = ? '''
    cur = conn.cursor()
    cur.execute(sql__se,[info])
    timeline_ = cur.fetchall()
    conn.close()
    return jsonify({"message": timeline_})


@app.route("/timeline", methods=['GET', 'POST'])
def timeline():
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT * FROM posts where uploaderid = ? ORDER BY sr DESC '''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0]])
    timeline_ = cur.fetchall()
    comms = []
    for i in timeline_:
        soltu = []
        
    sql__se = ''' SELECT * FROM friends where friendid1 = ? '''
    cur.execute(sql__se,[getUser(session["user__session"])[0]])
    friends = cur.fetchall()
    friend__list = []
    for friend in friends:
        sql__se = ''' SELECT * FROM posts where uploaderid = ? ORDER BY sr DESC '''
        cur = conn.cursor()
        cur.execute(sql__se,[friend[2]])
        timeline_2 = cur.fetchall()
        timeline_ += timeline_2

    conn.close()
    timeline_ = sorted(timeline_, key=lambda x: x[22], reverse=True)
    
    info = {
        "timeline":  timeline_     
    }

    return jsonify(info)


@app.route("/getnotification", methods=['GET', 'POST'])
def getnotification():
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT * FROM notification where for = ? ORDER BY id DESC'''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0]])
    notification_ = cur.fetchall()
    
    info = {
        "allnotifications" : notification_
    }

    return jsonify(info)

@app.route("/getfriendrequests", methods=['GET', 'POST'])
def getfriendrequests():
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT * FROM friendrequest where towhomid = ? AND status = "sent" '''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0]])
    friends = cur.fetchall()
    friend__list = []
    for friend in friends:
        friend__list.append(getUser(friend[1]))


    info = {
        "allfriendrequests" : friend__list
    }

    return jsonify(info)

@app.route("/getfriends", methods=['GET', 'POST'])
def getfriends():
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT * FROM friends where friendid1 = ? '''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0]])
    friends = cur.fetchall()
    friend__list = []
    for friend in friends:
        friend__list.append(getUser(friend[2]))


    info = {
        "allfriendrequests" : friend__list
    }

    return jsonify(info)


@app.route("/updateSeen/<info>", methods=['GET', 'POST'])
def updateSeen(info):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    try:  
        sql = "UPDATE notification SET status = 'seen' where for = ? and status = 'not seen'"  
        cur.execute(sql,[getUser(session["user__session"])[0]])
        conn.commit()
    except IntegrityError:
        pass
    
    conn = sqlite3.connect("database.db")
    sql__se = ''' SELECT count(*) FROM notification where for = ? and status = ? '''
    cur = conn.cursor()
    cur.execute(sql__se,[getUser(session["user__session"])[0],"not seen"])
    notification_ = cur.fetchone()
    
    info = {
        "message" : 40,
        "notification": notification_[0],
        "status" : "Done"
    }
    conn.close()
    return jsonify(info)

# Utilities

def makeid(length):
    result = ''
    characters  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    charactersLength = len(characters)
    for i in range(0,length+1):
        result += characters[math.floor(random.randint(0,61))]
    return result

def notification(sender,reciever,type):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    today = datetime.datetime.now()
    if(type=="friend"):
        text = "Hey "+getUser(reciever)[1]+" you have a friend request from "+getUser(sender)[1] 
    try:
        sql = "INSERT INTO notification VALUES (?,?,?,?,?,?,?,?,?)"
        cur.execute(sql,[None,sender,reciever,str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S")),type,text,"not seen",""])
        conn.commit()    
    except IntegrityError: 
        return 0
    conn.close()
    return 1


def getUser(userId):
    conn = sqlite3.connect("database.db")
    sql = ''' SELECT * FROM users where email="'''+userId+'''" OR id="'''+userId+'''" '''
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchone()
    conn.close()
    
    return rows



@app.route("/request/<type>/<info>", methods=['GET', 'POST'])
def acceptReq(type,info):
    
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    try:  
        sql = "UPDATE friendrequest SET status = ? where senderid = ? and towhomid = ? and status = 'sent'"  
        cur.execute(sql,[type,info,getUser(session["user__session"])[0]])
        conn.commit()
    except IntegrityError:
        pass
    
    if type=="accept":
        today = datetime.datetime.now()
        try:
            sql = "INSERT INTO friends VALUES (?,?,?,?,?)"
            cur.execute(sql,[None,info,getUser(session["user__session"])[0],str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S"))])
            conn.commit()

            sql = "INSERT INTO friends VALUES (?,?,?,?,?)"
            cur.execute(sql,[None,getUser(session["user__session"])[0],info,str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S"))])
            conn.commit()

        except IntegrityError: 
            return 0

    info = {    
        "status" : "success"
    }
    conn.close()
    return jsonify(info)
















































# Page Server

@app.route('/')
@app.route('/index')
def login__001():

    return render_template("login-register/001__login.html")

@app.route('/otpVerification/<id>')
def login__002(id):
    return render_template("login-register/002__otpverification.html")

@app.route('/profile')
def login__003():
    return render_template("login-register/003__profile.html")

@app.route('/description/<id>')
def login__004(id):
    return render_template("login-register/004__description.html")

@app.route('/policy/<id>')
def login__005(id):
    return render_template("login-register/005__policy.html")














# Page Handlers





@app.route('/profileSave',methods=['GET','POST'])
def profileSave():
    if "user__session" in session:
        if request.method == 'POST':
            if 'file' not in request.files:
                return "No File"
            
            file = request.files['file']
            email = session["user__session"]

            

            if file.filename == '':
                return "No File"

            if file:
                filename = (file.filename)
                k = database.child("users/"+email.split('@')[0]+"/profilePic/profile.jpg").put(file)
                file__ref = database.child("users/"+email.split('@')[0]+"/profilePic/profile.jpg").get_url(k["downloadTokens"])
                
                conn = sqlite3.connect("database.db")
                cur = conn.cursor()
                try:
                    sql = "UPDATE users SET profilepic= ? where email = ?"
                    cur.execute(sql,[file__ref,email])
                    doc_ref = firedb.collection(u'2a2c26d251a5547cfefac36e8bae4ba6').document(getUser(email)[0])
                    doc_ref.update({
                        "ProfilePic":  file__ref,
                    })

                    conn.commit()
                except IntegrityError:
                    return render_template("/")    
                return redirect(url_for("home"))

@app.route('/home')
def home():
    if "user__session" in session:
        conn = sqlite3.connect("database.db")
        sql = ''' SELECT * FROM users where email="'''+session["user__session"]+'''" '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchone()
        conn.close()
        
    return render_template("homewhite.html",user=rows)

@app.route('/logout')
def logout():
    session.pop('user__session', None)
    return redirect(url_for('login__001'))

    
@app.route('/createUser',methods=['GET','POST'])
def createUser():
    if request.method == "POST":
        email = request.form['email']
        passw = request.form['password']
        name = request.form['name']
        desc = request.form['desc']
        gendr = request.form['gender']
        date = request.form['date']

        conn = sqlite3.connect("database.db")
        sql = ''' SELECT * FROM users where email="'''+email+'''" '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchone()
        id = str(uuid.uuid1())
        if rows is None:
            try:

                sql = "INSERT INTO users VALUES (?,?,?,?,?,?,?,?)"
                cur.execute(sql,[id,name,email,passw,date,gendr,desc,''])

                doc_ref = firedb.collection(u'2a2c26d251a5547cfefac36e8bae4ba6').document(id)
                doc_ref.set({
                    "UserID":  id,
                    "Name": name,
                    "Firstname":  name.split(" ")[0],
                    "Lastname": name.split(" ")[1],
                    "Email":   email,
                    "Password": passw,
                    "Birthday": date,
                    "Gender":   gendr,
                    "AboutMe":  desc,
                    "ProfilePic":  'N/A',
                    "Blocked":  'N/A',
                    "Reported": 'N/A',
                    "Banned":   'N/A',
                    "FavouriteBooks":   'N/A',
                    "FavouriteMovies":  'N/A',
                    "FavouriteMusic":   'N/A',
                    "FavouriteQuote":   'N/A',
                    "FavouriteTVShows": 'N/A',
                    "Interests":    'N/A',
                    "PoliticalViews":   'N/A',
                    "Religion": 'N/A',
                    "EducationID":  'N/A',
                    "LastUpdated":  str(datetime.datetime.now()),
                    "WorkPlace":    'N/A',
                })

                session["user__session"] = email
                conn.commit()
            except IntegrityError:
                return render_template("/")    
            return redirect(url_for("login__003"))
        else:
            print("Chi")

        conn.close()
        return render_template("login-register/005__policy.html")

@app.route('/loginhandle',methods=['GET','POST'])
def loginhandle():
    if request.method == "POST":
        email = request.form['email__l']
        passw = request.form['password__l']
        conn = sqlite3.connect("database.db")
        sql = ''' SELECT * FROM users where email="'''+email+'''" and password="'''+passw+'''" '''
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchone()
        if rows is not None:
            session["user__session"] = email    
            return redirect(url_for("home"))
        else:
            print("Chi")

        conn.close()
        return render_template("login-register/005__policy.html")
      

@app.route('/posts',methods=['GET','POST'])
def posts():
    if "user__session" in session:
        if request.method == 'POST':
            
            # Flags
            video__flag = False
            image__flag = False
            text__flag = False
            content = request.form['content']
            
            if(len(content)!=0):
                text__flag = True

            post__id = str(uuid.uuid1())
            
            image__urls = ""
            video__urls = ""
            # Video Flags Set
            if request.files['image[]'].filename != '':
                image__flag = True
                images = request.files.getlist('image[]')
                count = 0
                
                for image in images:
                    count+=1
                    i__file = (image.filename)
                    
                    file__url = database.child("posts/"+post__id+"/Post-"+str(count)+".jpg").put(image)
                    file__ref = database.child("posts/"+post__id+"/Post-"+str(count)+".jpg").get_url(file__url["downloadTokens"])

                    image__urls += file__ref + ","
            else:
                image__urls = ""

            if request.files['video[]'].filename != '':
                video__flag = True
                videos = request.files.getlist('video[]')
                
                count = 0
                for video in videos:
                    count+=1
                    v__file = (video.filename)
                    
                    file__url = database.child("posts/"+post__id+"/Post-"+str(count)+".mp4").put(video)
                    file__ref = database.child("posts/"+post__id+"/Post-"+str(count)+".mp4").get_url(file__url["downloadTokens"])

                    video__urls += file__ref + ","
            else:
                video__urls = ""
            
            conn = sqlite3.connect("database.db")
            sql__se_ = ''' SELECT count(*) FROM posts'''
            cur = conn.cursor()
            cur.execute(sql__se_)
            count_ = cur.fetchone()
            today = datetime.datetime.now()
            try:
                sql = "INSERT INTO posts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                cur.execute(sql,[post__id,getUser(session["user__session"])[0],str(image__flag),str(video__flag),"False","False","False","False",str(text__flag),image__urls,video__urls,"",post__id,"","",content,str(today.day)+"/"+str(today.month)+"/"+str(today.year),str(today.strftime("%H:%M:%S")),"","0",post__id,"0",int(int(count_[0])+1),getUser(session["user__session"])[1],getUser(session["user__session"])[7]])
                conn.commit()

                doc_ref = firedb.collection(u'f3e856d6b4652e3c92eee4aea520101d').document(post__id)
                doc_ref.set({
                    "PostId":  post__id,
                    "AuthorId": getUser(session["user__session"])[0],
                    "HasImage": str(image__flag),
                    "HasVideo": str(video__flag),
                    "HasFeeling": "False",
                    "HasPoll": "False",
                    "HasLocation": "False",
                    "HasUser": "False",
                    "HasText": str(text__flag),
                    "ImageURL": image__urls,
                    "VideoURL": video__urls,
                    "FeelingURL": "N/A",
                    "PollID":  post__id,
                    "LocationName": "N/A",
                    "UsersMentions": "N/A",
                    "Message": content,
                    "DateOfUpload": str(today.day)+"/"+str(today.month)+"/"+str(today.year),
                    "TimeOfUpload": str(today.strftime("%H:%M:%S")),
                    "Priority": "0",
                    "Likes": "0",
                    "CommentID": post__id,
                    "Shares": "0",
                    "SerialNumber": int(int(count_[0])+1),
                    "AuthorName": getUser(session["user__session"])[1],
                    "AuthorProfilePic": getUser(session["user__session"])[7],
                })

            except IntegrityError:
                pass

            conn.close()
            return redirect(url_for('home'))
            



if  __name__ == "__main__":
    
    app.run(threaded=True, port=5000)