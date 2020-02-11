from django import forms
from allauth.socialaccount.forms import SignupForm
from allauth.account.forms import SetPasswordField, PasswordField

class SocialPasswordedSignupForm(SignupForm):

    password1 = SetPasswordField(max_length=10,label=("Password"))
    password2 = PasswordField(max_length=10, label=("Password (again)"))

    #taken from https://github.com/pennersr/django-allauth/blob/master/allauth/account/forms.py

    def clean_password2(self):
        if ("password1" in self.cleaned_data and "password2" in self.cleaned_data):
            if (self.cleaned_data["password1"] != self.cleaned_data["password2"]):
                raise forms.ValidationError(("You must type the same password each time."))
        return self.cleaned_data["password2"]

    def signup(self, request, user):
        user.set_password(self.user, self.cleaned_data["password1"])
        user.save()