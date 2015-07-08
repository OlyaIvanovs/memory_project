from django.forms import ModelForm, Textarea
from .models import Card


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['first_side_text', 'second_side_text', 'extra_text', 'value']
        widgets = {
            'extra_text': Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        labels = {
            'first_side_text': ('Question'),
            'second_side_text': ('Answer'),
            'extra_text': ('Example'),
        }



class CardChangeForm(ModelForm):
    class Meta:
        model = Card
        fields = ['first_side_text', 'second_side_text', 'extra_text']
        labels = {
            'first_side_text': ('Question'),
            'second_side_text': ('Answer'),
            'extra_text': ('Example'),
        }
        widgets = {
            'extra_text': Textarea(attrs={'cols': 40, 'rows': 5}),
        }