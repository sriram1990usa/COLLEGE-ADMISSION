from django.forms import ModelForm
from .models import *

class CourseForm(ModelForm):
    class Meta:
        model=Courses
        fields="__all__"