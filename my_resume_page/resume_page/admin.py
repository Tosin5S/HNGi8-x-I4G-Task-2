from django.contrib import admin
from resume_page.models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
