from django.forms import ModelForm, Textarea
from django.utils.text import slugify
from .models import Card, TranslateText


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


class TextForm(ModelForm):
    class Meta:
        model = TranslateText
        fields = ['title', 'content']
        labels = {
            'title': ('Title'),
            'content': ('Your Text'),
        }

    def save(self):
        instance = super(TextForm, self).save(commit=False)
        max_length = TranslateText._meta.get_field('slug').max_length
        instance.slug = slugify(instance.title)[:max_length]
        instance.save()
        return instance