from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def index(request):
    user = request.session.get('email')
    if request.method == 'POST' and not user == None:
        try:
            del request.session['email']
            return redirect('login')
        except:
            print('error')

    context = {'user' : user}
    return render(request, 'home.html', context)
   

def login(request):
    User = get_user_model()
    
    if request.method == 'POST':
        user_form = User(email=request.POST.get('username'), password=request.POST.get('password'))
        user = User(email="normal@user.com", password="foo")
        
        if  user.password == user_form.password and user.email == user_form.email:

            request.session['email'] = 'normal@user.com'
            return redirect("index")
        
        else: 
            print('Please enter valid Username or Password.')

    return render(request, 'login.html')