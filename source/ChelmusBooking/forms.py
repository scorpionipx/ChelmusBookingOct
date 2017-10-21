from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.core.mail import send_mail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

# SMPT mail content
SMPT_MAIL = 'chelmus.booking@gmail.com'
MAIL_SUBJECT = 'Inregistrare Chelmus Booking reusita!'
MAIL_CONTENT = 'Salutari! Bun venit in comunitatea Chelmus Booking!'


class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'email',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Inregistrare', css_class='btn-primary')
            )
        )

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        try:
            pass_ = self.cleaned_data.get('password1', None)
            custom_mail_content = MAIL_CONTENT + '\n\nDate autentificare:\nnume utilizator: ' + str(user.username) + \
                                  '\nparola: ' + str(pass_)

            send_mail(
                MAIL_SUBJECT,
                custom_mail_content,
                SMPT_MAIL,
                [user.email],
                fail_silently=False,
            )
        except Exception as err:
            print("Error occurred while trying to send mail.\n" + str(err))

        return user


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Autentificare', css_class='btn-primary')
            )
        )





