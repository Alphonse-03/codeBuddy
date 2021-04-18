# from django.contrib import admin
# from .models import Profile,Java,Python,C,Cpp,ConnectRequest,Message
# # Register your models here.

# from tinymce.widgets import TinyMCE

# class CAdmin(admin.ModelAdmin):
#     formfield_overides={
#         models.TextField:{'widget':TinyMCE()},
#     }
from django.contrib import admin

# Register your models here.
from .models import *
from tinymce.widgets import TinyMCE

class questionAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(waste)
admin.site.register(Profile)
# admin.site.register(questions,questionAdmin)
admin.site.register(questions)
admin.site.register(ConnectRequest)
admin.site.register(Message)
admin.site.register(Intrest)
admin.site.register(TestOptions)