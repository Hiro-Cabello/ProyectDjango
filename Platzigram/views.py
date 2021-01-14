#Django
from django.http import HttpResponse
#Utilities
from datetime import datetime
import json 

#Todas mis vistas reciben un request y lo que regresan es una respuesta
#a estas funciones django le llama vistas 
def hello_world(request):
    return HttpResponse('Hello, World Hiro {now}'.format(
        now=datetime.now().strftime('%b %dth , %Y - %H:%M hrs')
        ))



#http://127.0.0.1:8000/hi/?numbers=10,5,6,4,7,8,1
def sorted_integers(request):
    #Sirve para interacturar con la consola antes de retornar el httpresponse
        #import pdb;pdb.set_trace()
        #request.Get  {}
    numbers= [int(x) for x in request.GET['numbers'].split(",")]
    sorted_ints= sorted(numbers)
    data={
        'status':'ok',
        'numbers':sorted_ints,
        'message':'Integers sorted successfully.'
    }
    #dumps convierte un diccionario a json
    return HttpResponse(json.dumps(data), content_type='application/json')
    #return 

#http://127.0.0.1:8000/hi/JAIRO/21/
def say_hi(request,name,age):
    if age<12:
        message='Sorry {} , yo no pueden ingresar menores de edad'.format(name)
    else:
        message='Hi , Bienvenid@ {} ! platzi expert'.format(name)
    return HttpResponse(message)



def lista_posts(request):
    #posts=[1,2,3,4]
    posts = [
    {
        'name': 'My Dog.',
        'user': 'Yésica Cortes',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Khe.',
        'user': 'Pink Woman',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Nautural web.',
        'user': 'Pancho Villa',
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/200/200/?image=1076'
    },
    
]

    content=[]
    for post in posts:
        content.append("""
        <p><strong>{name}</strong></p>
        <p><small>{user}-<i>{timestamp}</p>
        <figure><img src="{picture}"/></figure>
        """.format(**post))#.format(**post)) esto para desempaquetar el diccionario
   
    return  HttpResponse('<br>'.join(content))#HttpResponse(str(posts)) con esto regresaria solo la lista
