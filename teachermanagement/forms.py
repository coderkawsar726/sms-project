from django import forms
from assignment.models import Assignment


class AddAssignForm(forms.ModelForm):

    class Meta():
        model = Assignment
        fields = "__all__"

class CompleteAssForm(forms.ModelForm):
    class Meta():
        model = Assignment
        fields = "__all__"