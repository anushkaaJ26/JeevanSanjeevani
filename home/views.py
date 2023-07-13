#pip install pyrebase flask firebase-admin
#pip3 install pyrebase4
from django.shortcuts import render,HttpResponse,redirect
import pyrebase
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from flask import Flask, render_template

firebaseConfig = {
  "apiKey": "AIzaSyCOnU6dHyoMqyLHSL2iv0Y_AxfK_UFqzI0",
  "authDomain": "accident-detection-syste-867ba.firebaseapp.com",
  "databaseURL": "https://accident-detection-syste-867ba-default-rtdb.firebaseio.com",
  "projectId": "accident-detection-syste-867ba",
  "storageBucket": "accident-detection-syste-867ba.appspot.com",
  "messagingSenderId": "1063367313314",
  "appId": "1:1063367313314:web:c9562d29e2bfbcdddf54fb",
  "measurementId": "G-E3KXRW6VRK"
};

firebase=pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
database=firebase.database()



# Create your views here.
def homepage(request):
    return render(request,'index.html')

def signin(request):
        if request.method=='POST':
            uniqueID=request.POST.get('uID')
            if uniqueID!=None:
                uname=request.POST.get('uname')
                email=request.POST.get('email')
                contact=request.POST.get('contact')
                mode=request.POST.get("user-mode")
                address=request.POST.get("address")
                pass1=request.POST.get('p1')
                pass2=request.POST.get('p2')
                print(uniqueID)
                if pass1!=pass2:
                    return HttpResponse("Pass1 and Pass2 are Not Same please enter correct password")
                else:
                        data = {    
                        'Name': uname,
                        'Email': email,
                        'Contact No': contact,
                        'Unique ID': uniqueID,
                        'User Mode': mode,
                        'Address' : address,
                        'Password' : pass1,
                        }
                        if mode=="Police":
                            user=auth.create_user_with_email_and_password(email,pass1)
                            new_node_ref = database.child('Accident Handler').child('Police')
                            new_node_ref.push(data)
                        else:
                            user=auth.create_user_with_email_and_password(email,pass1)
                            new_node_ref = database.child('Accident Handler').child('Hospital')
                            new_node_ref.push(data)
                return redirect('signin')
            else:
                # if uniqueID==null:
                user=request.POST.get('uname_L')
                pas=request.POST.get('p1_L')
                print("hey")
                if(user!=None):
                    login=auth.sign_in_with_email_and_password(user,pas)
                #print(login)
                    return render(request,'dashboard.html')            
                else:
                    return HttpResponse("Invalid")
        else:
            return render(request,'signin.html')

def dashboard(request):
    return render(request,'dashboard.html')

def profile(request):
    return render(request,'profile.html')

def profile1(request):
    return render(request,'profile1.html')

def profile2(request):
    return render(request,'profile2.html')

def profile3(request):
    return render(request,'profile3.html')

# def profileNext(request):
#     return render(request,'profile.html')

def aadhaar(request):
    # Create Flask app
    app = Flask(__name__)
    # Retrieve PDF URL from Firebase Storage
    storage = firebase.storage()
    pdf_url = storage.child('victim/parth/Aadhaar1.pdf').get_url(None)
    data={
        "url":pdf_url
    }
    # Render template with PDF URL
    with app.app_context():
        return render(request,'docview.html',data)
    
def license(request):
    # Create Flask app
    app = Flask(__name__)
    # Retrieve PDF URL from Firebase Storage
    storage = firebase.storage()
    pdf_url = storage.child('victim/parth/license.pdf').get_url(None)
    data={
        "url":pdf_url
    }
    # Render template with PDF URL
    with app.app_context():
        return render(request,'docview.html',data)
    
def report(request):
    # Create Flask app
    app = Flask(__name__)
    # Retrieve PDF URL from Firebase Storage
    storage = firebase.storage()
    pdf_url = storage.child('victim/parth/Insurance.pdf').get_url(None)
    data={
        "url":pdf_url
    }
    # Render template with PDF URL
    with app.app_context():
        return render(request,'docview.html',data)

# def aadhar1(request):
#     return render(request,'docview1.html')

# def license1(request):
#     return render(request,'docview1.html')

# def report1(request):
#     return render(request,'docview1.html')
