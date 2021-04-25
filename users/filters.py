import django_filters

from .models import Intrest

class ApplicantFilter(django_filters.FilterSet):
    class Meta:
        model=Intrest
        fields=fields=['Intrest','marks','category']

    
