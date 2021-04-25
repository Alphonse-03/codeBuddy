from django.contrib import admin
from .models import CustomUser
# Register your models here.


from .models import *
from tinymce.widgets import TinyMCE

class questionAdmin(admin.ModelAdmin):


    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


# 
admin.site.register(CustomUser)
admin.site.register(Applicants)
admin.site.register(JobProfile)
admin.site.register(waste)
admin.site.register(JobPortal)
admin.site.register(Profile)
# admin.site.register(questions,questionAdmin)
admin.site.register(questions)
admin.site.register(ConnectRequest)
admin.site.register(Message)
admin.site.register(Intrest)
admin.site.register(TestOptions)