from importlib import import_module
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
from django.core.exceptions import SuspiciousOperation
from django.conf import settings

class CustomMiddleware(MiddlewareMixin):  

    def __init__(self, get_response=None):
        self.get_response = get_response
        engine = import_module(settings.SESSION_ENGINE)
        self.SessionStore = engine.SessionStore


    def process_request(self, request):
        session_key = request.COOKIES.get(settings.SESSION_COOKIE_NAME)
        request.session = self.SessionStore(session_key)
        # print(request.path)  
        # print(request.session.get('email'))
        if not request.path == "/login/" and request.session.get('email') == None :
            return redirect('login')

