from time import gmtime
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

import datetime



# Create your views here.
def index(request):
    user = request.session.get('email')

    if request.method == 'POST' and not user == None:
        try:
            del request.session['email']
            return redirect('login')
        except:
            print('error')
            
    for key, value in request.session.items():
        print('{} => {}'.format(key, value))

    context = {'user' : request.session}
    return render(request, 'home.html', context)
   

def login(request):
    User = get_user_model()
    error = False
    
    if request.method == 'POST':
        user_form = User(email=request.POST.get('username'), password=request.POST.get('password'))
        user = User(email="normal@user.com", password="foo")
        created_session = datetime.datetime.now()
        
        if  user.password == user_form.password and user.email == user_form.email:

            request.session['created_session'] = str(created_session)
            request.session['email'] = user_form.email
            return redirect("index")
        
        else: 
            error = True

    context= {'error': error}
    return render(request, 'login.html', context)