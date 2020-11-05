from django.contrib import admin
from .models import Profile,Java,Python,C,Cpp
# Register your models here.
admin.site.register(Profile)
admin.site.register(C)
admin.site.register(Cpp)
admin.site.register(Java)
admin.site.register(Python)
