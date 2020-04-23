from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs
from .forms import StudentPersonalInformationForm


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
            subject = "ACI Online Pre-registration Confirmation"
            message = "Thank you for Pre-registering to ACI \n " \
                      "Looking forward to seeing you in ACI Campus! \n God bless.."
            from_email = 'aciunofficial@gmail.com'
            email = form['email_address'].value()
            to_list = [email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('confirm')
        # return render(request, 'admission.html', {
        #     'programs': all_programs,
        #     'shifts': all_shifts,
        #     'year_level': all_year_level,
        #     'classification': all_classification,
        #     'where': all_where,
        #     'why': all_why
        # })

    else:
        return render(request, 'admission.html', {
            'programs': all_programs,
            'shifts': all_shifts,
            'year_level': all_year_level,
            'classification': all_classification,
            'where': all_where,
            'why': all_why
        })


def confirmation(request):
    return render(request, 'confirmation.html', {})
