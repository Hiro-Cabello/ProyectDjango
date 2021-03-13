from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.contrib.auth import views as auth_views
from django.urls import reverse
#models
from django.contrib.auth.models import User
from users.models import Profile

from users.forms import ProfileForm 

from posts.models import Post


# Create your views here.

class UserDetailView( LoginRequiredMixin , DetailView):
    template_name='users/detail.html'
    slug_field='username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data( self , **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts']=Post.objects.filter(user=user).order_by('-created')
        return context



@login_required
def update_profile(request):
    profile=request.user.profile
    #return render(request,'users/update_profile.html')

    if request.method == 'POST':
        #Ojo los archivos no vienen dentro de request.POST sino viene dentro de request.Files 

        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            profile.website= data['website']
            profile.phone_number= data['phone_number']
            profile.biography= data['biography']
            if data['picture']:
                profile.picture= data['picture']
            print(form.cleaned_data)

            profile.save()

            url = reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url) 

    else:
        form = ProfileForm()
    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


class LoginView(auth_views.LoginView ):
    template_name='users/login.html'

"""
def login_view(request):
    #   import pdb;pdb.set_trace()   ---Deboger
      
    #(Pdb) request.POST
    #<QueryDict: {}>

    #TIPO DE PETICION

    #(Pdb) request.method
    #'GET'

    
    #Esto es el deboger
    #import pdb;pdb.set_trace()
    if request.method == 'POST':
        print('entro al post')
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
            #return redirect('/posts/')
        else: 
            return render(request,'users/login.html',{'error':'Invalid username and password'})
        

    return render(request,'users/login.html')
"""

def signup(request):
    #import pdb;pdb.set_trace(),
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        password_confirmation=request.POST['password_confirmation']

        if password != password_confirmation:  
            return render(request,'users/signup.html',{'error':'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except:
           return render(request,'users/signup.html',{'error':'No se puede ingresar usuarios duplicados'})

       
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('users:login')

    return render(request,'users/signup.html')

class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    template_name='users/logged_out.html'


#@login_required
"""
def logout_view(request):
     logout(request)
     return redirect('users:login')
"""


""" 
Middlewares
Un middleware en Django es una serie de hooks y una API de bajo nivel que nos permiten modificar el objeto request antes de que llegue a la
vista y response antes de que salga de la vista.

Django dispone de los siguientes middlewares por defecto:

SecurityMiddleware
SessionMiddleware
CommonMiddleware
CsrfViewMiddleware
AuthenticationMiddleware
MessageMiddleware
XFrameOptionsMiddleware
Crearemos un middleware para redireccionar al usuario al perfil para que actualice su información cuando no haya definido aún biografía o avatar.
https://docs.djangoproject.com/en/3.0/topics/http/middleware/
"""