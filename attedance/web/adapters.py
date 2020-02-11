
from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.forms import ValidationError

class FooAppAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        print("called____________________")
        return super(FooAppAccountAdapter, self).save_user(
            request, user, form, commit
        )

    def clean_email(self, email):
        RestrictedList = ['Your restricted list goes here.']
        if email in RestrictedList:
            raise ValidationError('You are restricted from registering. Please contact admin.')
        return email


class FooAppSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        print("called+++++++++++++++++++++++")
        return super(FooAppSocialAccountAdapter, self).pre_social_login(
            request, sociallogin
        )

    def save_user(self, request, sociallogin, form=None):
        print("called)))))))))))))))))))))")
        return super(FooAppSocialAccountAdapter, self).save_user(
            request, sociallogin, form)