from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Card, News
from .forms import ContactForm


# Create your views here.
def main(request):
    yangiliklar = News.objects.all()

    context = {
        'news': yangiliklar
    }


    return render(request, 'main/index.html', context)

def about(request):
    cards = Card.objects.all()

    context = {
        'malumotlar': cards
    }


    return render(request, 'main/about.html', context)


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print('Xatolik')


    return render(request, 'main/contact.html')