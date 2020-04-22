from django import forms
from .models import StudentPersonalInformation, Programs, PreferredShift, YearLevel, StudentClassification


class StudentPersonalInformationForm(forms.ModelForm):
    class Meta:
        model = StudentPersonalInformation

        fields = ['last_name',
                  'first_name',
                  'middle_name',
                  'birthdate',
                  'birth_place',
                  'religion',
                  'nationality',
                  'gender',
                  'civil_status',
                  'email_address',
                  'social_media_accounts',
                  'mobile_number',
                  'landline_number',
                  'home_address',
                  'stud_classification',
                  'stud_program',
                  'stud_shift',
                  'stud_year_level',
                  'where_hear_us',
                  'why_choose_us'
                  ]


