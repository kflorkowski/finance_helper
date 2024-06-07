from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PersonForm, JobForm
from .models import Person, Job


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


def personal_details(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    # if person.user != request.user:
    #     return render(request, 'unauthorized.html')
    jobs = person.jobs.all()
    return render(request, 'personal_details.html', {'person': person, 'jobs': jobs})


def job_list(request, person_id):
    person = get_object_or_404(Person, id=person_id, user=request.user)
    jobs = person.jobs.all()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.person = person
            job.save()
            return redirect('job_list', person_id=person.id)
    else:
        form = JobForm()

    return render(request, 'job_list.html', {'form': form, 'jobs': jobs, 'person': person})
