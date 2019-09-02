from django.db import models
from multiselectfield import MultiSelectField


# Create your models here.
class ServicesData(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=100, unique=True)
    course_duration = models.CharField(max_length=100)
    course_state_date = models.DateField(max_length=100)
    course_start_time = models.TimeField(max_length=100)
    course_trainer_name = models.CharField(max_length=100)
    course_trainer_exp = models.CharField(max_length=100)


class FeedbackData(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateTimeField(max_length=100)
    feedback = models.CharField(max_length=100)


class EnquiryData(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)

    COURSES_CHOICES = (
        ('py', "python"),
        ('dj', "django"),
        ('py', "Rest Api"),
        ('fl', "Flask"),
        ('UI', "Ui"),
    )

    courses = MultiSelectField(COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('Moring', 'Moring Shift'),
        ('Afternoon', 'Afternoon shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift'),
    )

    shifts = MultiSelectField(SHIFTS_CHOICES)

    start_date = models.DateTimeField(max_length=100)
