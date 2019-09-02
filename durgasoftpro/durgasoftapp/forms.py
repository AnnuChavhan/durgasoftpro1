from django import forms
from multiselectfield import MultiSelectFormField


class FeedbackForm(forms.Form):
    name = forms.CharField(
        label='Enter your Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter your Rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter your Feedback',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Feedback'
            }
        )
    )


class EnquiryForm(forms.Form):
    name = forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your mobile number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your Mobile number'
            }
        )
    )
    GENDER_CHOICES = (
        ('F', 'Female'),
        ('M', 'Male')
    )
    gender = forms.ChoiceField(
        widget=forms.RadioSelect, choices=GENDER_CHOICES
    )
    COURSES_CHOICES = (
        ('py', "python"),
        ('dj', "django"),
        ('py', "Rest Api"),
        ('fl', "Flask"),
        ('UI', "Ui")
    )
    courses = MultiSelectFormField(choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('Moring', 'Moring Shift'),
        ('Afternoon', 'Afternoon shift'),
        ('Evening', 'Evening Shift'),
        ('Night', 'Night Shift')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOICES)

    start_date = forms.DateTimeField(
        widget=forms.SelectDateWidget
    )
