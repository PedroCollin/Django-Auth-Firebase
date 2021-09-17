from django.shortcuts import render
from firebase import Firebase
from django.contrib import auth

Config = {
    'apiKey': "AIzaSyAgKDdMpUT51t9oh_BSEF9W-uOlarmWpXM",
    'authDomain': "teste-f21d3.firebaseapp.com",
    'databaseURL': "https://teste-f21d3-default-rtdb.firebaseio.com",
    'projectId': "teste-f21d3",
    'storageBucket': "teste-f21d3.appspot.com",
    'messagingSenderId': "500502342443",
    'appId': "1:500502342443:web:30468e31bae469a0e3736e",
    'measurementId': "G-PW0C19DNM6"
}

default_app = Firebase(Config)

global authi
authi= default_app.auth()
databse = default_app.database()


def signin(request):
    return render(request, template_name="signIn.html")


def postsign(request):
    global authi
    email = request.POST.get('email')
    passw = request.POST.get('password')

    try:
        user = authi.sign_in_with_email_and_password(email, passw)
        return render(request, 'welcome.html')

    except:
        return render(request, 'signIn.html')


def logout(request):
    try:
        del request.session['uid']
    except KeyError:
        pass
    return render(request, 'signIn.html')


def signUp(request):

    return render(request, 'signup.html')


def postsignup(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    passw = request.POST.get('password')

    global authi

    print(authi.create_user_with_email_and_password(email, passw))
    try:
        user = authi.create_user_with_email_and_password(email, passw)
    except:
        message = "unable to create account try again"
        return render(request, 'signup.html', {"messg": message})
    uid = user['localId']

    data = {"name": name, "status": "1"}
    databse.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")