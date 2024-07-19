# obituaries/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Obituary
from django.urls import reverse


def admin_redirect(request):
    return redirect('/homepage/')


def homepage(request):
    return render(request, 'homepage.html')


def view_obituaries(request):
    obituaries = Obituary.objects.all()
    return render(request, 'view_obituaries.html', {'obituaries': obituaries})


def obituary_detail(request, slug):
    obituary = get_object_or_404(Obituary, slug=slug)
    return render(request, 'obituary_detail.html', {'obituary': obituary})


def submit_obituary(request):
    if request.method == 'POST':
        name = request.POST['name']
        date_of_birth = request.POST['date_of_birth']
        date_of_death = request.POST['date_of_death']
        content = request.POST['content']
        author = request.POST['author']

        obituary = Obituary(
            name=name,
            date_of_birth=date_of_birth,
            date_of_death=date_of_death,
            content=content,
            author=author
        )
        obituary.save()

        return redirect(reverse('view_obituaries'))

    return render(request, 'obituary_form.html')
