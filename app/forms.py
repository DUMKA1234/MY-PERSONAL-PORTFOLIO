# from django import forms
# from . import models
# class StudentForm(forms.ModelForm):
#     class Meta:
#         model = models.students
#         fields = "__all__"

from django import forms
from . import models

class StudentForm(forms.ModelForm):
 class postForm(forms.ModelForm):
    class Meta:
        model = models.students  # Make sure the model name matches
        model = models.post
        fields = "__all__"
