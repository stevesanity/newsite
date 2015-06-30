__author__ = 'xls'
from django import forms
from showdata.models import *

class Accounteditform(forms.Form):
    First_name = forms.CharField
    Last_name = forms.CharField
    Email_address = forms.EmailField
    Pass_word = forms.CharField
    Pass_word_reaffirm = forms.CharField

class Loginverifyingform(forms.Form):
    Email_address = forms.EmailField
    Pass_word = forms.CharField


