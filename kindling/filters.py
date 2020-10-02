import django_filters
from .models import *

class EntrySignupFilter(django_filters.FilterSet):
    class meta:
        model = EntrySignup
        fields = '__all__'
