from django.contrib import admin
from post.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','description')

admin.site.register(Post,PostAdmin)