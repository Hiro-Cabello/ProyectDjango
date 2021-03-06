
#Django
from django.urls import path
#from django.views.generic import TemplateView


# View
from users import views

urlpatterns = [




#Management
    path(
        route='login/',
        #view=views.login_view,
         view=views.LoginView.as_view(),
        name='login'),
    path(
        route='logout/',
        view=views.LogoutView.as_view() ,
        name='logout'),
    path(
        route='signup/',
        view=views.signup,
        name='signup'),
    #este va editar el profile
    path(
        route='me/profile',
        view=views.update_profile,
        name='update_profile'),

# Posts
path(
    route='<str:username>/',
    view=views.UserDetailView.as_view(),
    # view=TemplateView.as_view(template_name='users/detail.html'),
    name='detail'
)

]
