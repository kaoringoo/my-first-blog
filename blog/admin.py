from django.contrib import admin
from .models import Post #Postモデルをimport

admin.site.register(Post) #モデルをAdminページ（管理画面）上で見えるようにするため

# Register your models here.
