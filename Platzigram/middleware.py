"""Platzigram middleware catalog."""
#Es un sistema de "complementos" ligero y de bajo nivel para alterar globalmente la entrada o salida de Django.

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """ 

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:   #Esto es para asegurarse que hay un usuario
            if not request.user.is_staff:#si entro como admin me permita el acceso y no lo bloquee el
                profile = request.user.profile  #Esto es una manera de traer los onetoone 
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'), reverse('logout')]:
                        return redirect('update_profile')
#reverse -> apartir de un nombre trae la url 
        response = self.get_response(request)
        return response

#https://docs.djangoproject.com/en/3.0/topics/http/middleware/