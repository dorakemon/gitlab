from django_registration.forms import RegistrationForm
from users.models import User


class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = User
        fields = [
            User.USERNAME_FIELD,
            User.get_email_field_name(),
            "password1",
            "password2",
            "course",   
            "place",
            "university_faculty",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None
