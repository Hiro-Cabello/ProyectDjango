from django.shortcuts import render,redirect


#Ayuda a que no se pueda abrir este post sin antes haberse logeado
from django.contrib.auth.decorators import login_required

from datetime import datetime

from posts.forms import PostForm 
  



#render es una funcion que toma un request
#Las views manejan la lógica de los que traen los datos
#from django.http import HttpResponse
from datetime import datetime

posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/500/700/?image=1076',
    }
]
# Create your views here.
#Esto es cuando se usaba   ---->>>>>>from django.http import HttpResponse
#def list_posts(request):
    #posts=[1,2,3,4]
    #content=[]
    #for post in posts:
    #    content.append("""
    #    <p><strong>{name}</strong></p>
    #    <p><small>{user}-<i>{timestamp}</p>
    #    <figure><img src="{picture}"/></figure>
    #    """.format(**post))#.format(**post)) esto para desempaquetar el diccionario
   
    #return  HttpResponse('<br>'.join(content))#HttpResponse(str(posts)) con esto regresaria solo la lista



@login_required
def list_posts(request):
    #va a buscar en la directorios de la aplicacion donde hace match 
    return render(request,'posts/feed.html',{'posts':posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()#con esto automaticamente se va crear un posts
            return redirect('feed')
        
    else : 
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile':request.user.profile
        }
    )
    


