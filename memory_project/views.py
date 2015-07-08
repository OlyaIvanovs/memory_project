from datetime import datetime, timedelta
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from .forms import CardForm, CardChangeForm
from .models import Card, TranslateText


def index(request):
    context = None
    now = datetime.now()
    card_list = Card.objects.filter(show_date__lte=now)
    list_len = len(card_list)
    if list_len > 0:
        context = {'card': card_list[0], 'list_len': list_len}
    return render(request, 'memory_project/index.html', context)


def card_renew(request, card_id):
    p = get_object_or_404(Card, pk=card_id)
    val = request.POST['choice']
    if val == '1':
        num_days = 1
    elif val == '2':
        num_days = 2
    elif val == '3':
        num_days = 3
    elif val == '4':
        num_days = 7
    elif val == '5':
        num_days = 30
    else:
        num_days = 0
    p.show_date = datetime.now() + timedelta(days=num_days)
    p.value = val
    p.save()
    return HttpResponseRedirect(reverse('memory:index'))


def card_delete(request, card_id):
    p = get_object_or_404(Card, pk=card_id)
    p.delete()
    return HttpResponseRedirect(reverse('memory:index'))


def card_change(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    date = card.show_date
    value = card.value
    if request.method == 'POST':
        form = CardChangeForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.show_date = date
            card.value = value
            card.pk = card_id
            card.save()
            form.save
            return HttpResponseRedirect('/memory/')
    else:
        form = CardChangeForm(instance=card)
    return render(request, 'memory_project/card_form.html', {'form': form})


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.show_date = datetime.now()
            card.save()
            return HttpResponseRedirect('/memory/')
    else:
        form = CardForm()
    return render(request, 'memory_project/card_form.html', {'form': form})


def add_text(request):
    card_list = Card.objects.all()
    list_len = len(card_list)
    if list_len > 0:
        context = {'cards': card_list, 'list_len': list_len}
    return render(request, 'memory_project/all.html', context)


def all(request):
    card_list = Card.objects.all()
    list_len = len(card_list)
    if list_len > 0:
        context = {'cards': card_list, 'list_len': list_len}
    return render(request, 'memory_project/all.html', context)


def all_texts(request):
    text_list = TranslateText.objects.all()
    list_len = len(text_list)
    if list_len > 0:
        context = {'texts': text_list, 'list_len': list_len}
    return render(request, 'memory_project/all_texts.html', context)