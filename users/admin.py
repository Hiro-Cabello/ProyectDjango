from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


from django.contrib.auth.models import User
# Register your models here.
from users.models import Profile
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('pk','user','phone_number','website','picture')
    list_display_links=('pk','user')
    list_editable=('phone_number','website','picture')
    search_fields=(
        'user__email',
        'user__username',
        'user_first_name',
        'user__last_name',
        'phone_number'
    )
    #Para ingresar los filtros
    list_filter=(
        'created',
        'modified',
        'user__is_active',
        'user__is_staff',
    )
# Primer elemento es el titulo luego el contenido que se va agregando por tuplas 

    fieldsets = (
        ('Profile', {
            "fields": (
                ('user','picture'),
            ),
        }),
         ('Extra info',{
            'fields':(
                ('website','phone_number'),
                ('biography')
                ),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        })
    )
    #readonly_fields=('created','modified','user')
    #todo lo que este en estos campos no es editable
    readonly_fields=('created','modified')



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural='profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline ,)
    list_display=(
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


#Primero registro el modelo de usuario
admin.site.unregister(User)
admin.site.register(User,UserAdmin)