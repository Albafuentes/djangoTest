from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    title = "title de prueba"
    return HttpResponse(title)

def login(request):
    User = get_user_model()
    user = User(email="normal@user.com", password="foo")
    user_form = User(email=request.POST.get('username'), password=request.POST.get('password'))

    if user.password == user_form.password:
        request.session['username'] = user_form.username
        session = "has logged"
    else:
        session = "has not logged"

    context = {"session": session}
    return render(request, 'login.html', context=context)