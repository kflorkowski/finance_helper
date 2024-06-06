from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PersonForm
from .models import Person


@login_required
def home(request):
    return render(request, 'home.html')


def people(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('people')
    else:
        form = PersonForm()
    persons = Person.objects.filter(user=request.user)
    return render(request, 'people.html', {'form': form, 'persons': persons})
