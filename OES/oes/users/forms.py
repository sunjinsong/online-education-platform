from django import forms
from captcha.fields import CaptchaField
class RegisterForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()
    captcha=CaptchaField()

class ForgetPwdForm(forms.Form):
    email = forms.EmailField()
    captcha = CaptchaField()


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
