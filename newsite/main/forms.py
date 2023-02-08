from .models import Contact

from django.forms import ModelForm

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname', 'lastname', 'country', 'subject']