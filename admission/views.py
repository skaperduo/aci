from django.shortcuts import render, redirect
from .models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs
from .forms import StudentPersonalInformationForm
from django.contrib import messages

# Create your views here.


# def admission(request):
#     all_programs = Programs.objects.all
#     all_shifts = PreferredShift.objects.all
#     all_year_level = YearLevel.objects.all
#     all_classification = StudentClassification.objects.all
#
#     return render(request, 'admission.html', {
#         'programs': all_programs,
#         'shifts': all_shifts,
#         'year_level': all_year_level,
#         'classification': all_classification
#     })


def admission(request):

    all_programs = Programs.objects.all
    all_shifts = PreferredShift.objects.all
    all_year_level = YearLevel.objects.all
    all_classification = StudentClassification.objects.all
    all_why = WhyDidYouChooseUs.objects.all
    all_where = WhereDidYouHearUs.objects.all

    if request.method == "POST":
        form = StudentPersonalInformationForm(request.POST or None)

        if form.is_valid():
            form.save()
        else:
            messages.success(request, 'There was an error!')
            print(form['stud_classification'].value())
            print(form['stud_program'].value())
            print(form['stud_year_level'].value())
            print(form['stud_shift'].value())
            print(form['first_name'].value())

        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why
        })

    else:
        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why
        })


