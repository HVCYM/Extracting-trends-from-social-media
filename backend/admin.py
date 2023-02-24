from django.contrib import admin
from .models import Card,HashtagList,Uploadfile

admin.site.register([Card,HashtagList,Uploadfile])