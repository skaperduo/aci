from django.db import models

# Create your models here.


class Programs(models.Model):
    program_title = models.CharField(max_length=255)
    program_description = models.TextField

    def __str__(self):
        return str(self.pk) + ' ' + self.program_title


class PreferredShift(models.Model):
    shift_title = models.CharField(max_length=3)
    shift_time = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.shift_title + ' - ' + self.shift_time


class YearLevel(models.Model):
    year_level = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.year_level


class StudentClassification(models.Model):
    classification = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pk) + ' ' + self.classification


class WhereDidYouHearUs(models.Model):
    where = models.CharField(max_length=255)

    def __str__(self):
        return self.where


class WhyDidYouChooseUs(models.Model):
    why = models.CharField(max_length=255)

    def __str__(self):
        return self.why


class StudentPersonalInformation(models.Model):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    birthdate = models.CharField(max_length=255)
    birth_place = models.CharField(max_length=255)
    religion = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    civil_status = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    social_media_accounts = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    landline_number = models.CharField(max_length=255)
    home_address = models.CharField(max_length=255)
    stud_classification = models.ForeignKey(StudentClassification, default=1, on_delete=models.SET_DEFAULT)
    stud_program = models.ForeignKey(Programs, default=1, on_delete=models.SET_DEFAULT)
    stud_shift = models.ForeignKey(PreferredShift, default=1, on_delete=models.SET_DEFAULT)
    stud_year_level = models.ForeignKey(YearLevel, default=1, on_delete=models.SET_DEFAULT)
    where_hear_us = models.ForeignKey(WhereDidYouHearUs, default=1, on_delete=models.SET_DEFAULT)
    why_choose_us = models.ForeignKey(WhyDidYouChooseUs, default=1, on_delete=models.SET_DEFAULT)

    def __str__(self):
        return str(self.pk) + ' ' + self.last_name + ', ' + self.first_name + ' ' + self.middle_name





