from .models import Video
from django.forms import ModelForm

class RasmForm(ModelForm):
    class Meta:
        model = Video
        fields = ['file', 'username']


