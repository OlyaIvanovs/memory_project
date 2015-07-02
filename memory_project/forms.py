from django.forms import ModelForm
from .models import Card


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['first_side_text', 'second_side_text', 'value']


class CardChangeForm(ModelForm):
    class Meta:
        model = Card
        fields = ['first_side_text', 'second_side_text']