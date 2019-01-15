from django import forms
from django.forms import ModelForm
from .models import User,Cod,Feedback

class UserForm(forms.ModelForm):


    class Meta:
        model = User
        fields = [
            'name','roll_no','service','token_no','date'
        ]


class CodForm(forms.ModelForm):

    class Meta:
        model = Cod
        fields= [
            'roll_no','service','tracking_id','payment','Eta'
        ]

class Feedbackform(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'Rating', 'Comments', 'Details',
        ]