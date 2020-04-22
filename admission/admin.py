from django.contrib import admin
from .models import Programs, PreferredShift, YearLevel, StudentClassification, StudentPersonalInformation, WhereDidYouHearUs, WhyDidYouChooseUs


admin.site.register(Programs)
admin.site.register(PreferredShift)
admin.site.register(YearLevel)
admin.site.register(StudentClassification)
admin.site.register(StudentPersonalInformation)
admin.site.register(WhereDidYouHearUs)
admin.site.register(WhyDidYouChooseUs)

# Register your models here.
