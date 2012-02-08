
from django import forms
from django.contrib.localflavor.us.forms import USPhoneNumberField

from contact_form.forms import ContactForm

class ContactForm(ContactForm):
    name = forms.CharField()
    email = forms.EmailField()
    phone = USPhoneNumberField(required=False, help_text="Enter phone number in xxx-xxx-xxxx format.")
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'span6'}))
