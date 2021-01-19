from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('pk','user','title','photo')
    list_display_links=('pk','user')
    list_editable=('title','photo')
    search_fields=('user__username','title')
    readonly_fields=('created','modified')
