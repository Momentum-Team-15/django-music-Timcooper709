from django.contrib import admin
from .models import User, Album, Artist, Favorite
# Register your models here.
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Favorite)
