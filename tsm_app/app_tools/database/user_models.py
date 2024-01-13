import uuid
import numpy as np

from django.db import models
from django.contrib.auth import models as auth_models


__all__ = [
    'CustomUser', 'Profile',
    'Telephone'
]

ROLE_CHOICES = [
    ('software_developer', 'Software Developer'),
    ('software_engineer', 'Software Engineer'),
    ('junior_software_developer', 'Junior Software Developer'),
    ('junior_software_engineer', 'Junior Software Engineer'),
    ('senior_software_developer', 'Senior Software Developer'),
    ('senior_software_engineer', 'Senior Software Engineer')
]
DEFAULT_ROLE_CHOICE = ROLE_CHOICES[0][0]


class CustomUser(auth_models.AbstractUser):
    """
    Model that stores all user information i.e. username, password,
    email, first_name, last_name and a profile
    """
    class Meta:
        app_label = 'tsm_app'
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return f'User(email={self.email}, first_name={self.first_name})'

    def get_json_value(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'firstName': self.first_name,
            'lastName': self.last_name
        }

    @staticmethod
    def from_json_value(json_value: dict):
        return CustomUser(**json_value)

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {}


class Profile(models.Model):
    user: CustomUser = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='user')
    supervisor: CustomUser = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='supervisor')
    role = models.CharField(
        null=False,
        max_length=50,
        choices=ROLE_CHOICES,
        default=DEFAULT_ROLE_CHOICE
    )
    dob = models.DateField(null=True)
    avatar = models.ImageField(upload_to='users/profile/')
    description = models.TextField(max_length=1000, null=True)
    avatar_color = models.CharField(default="rgb(0, 0, 0)")

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user', None)
        if user is None and len(args) == 0:
            print('Try to instantiate Profile without user PrimaryKey!!! '
                  'Dummy user will be created!!!')
            unique_id = uuid.uuid4().hex
            user = CustomUser(
                username=f"dummy_user{unique_id}",
                password="dummy_password",
                email=f"dummy_email_{unique_id}@gmail.com")
            user.save()
            kwargs['user'] = user
            kwargs["avatar_color"] = self.get_random_rgb()
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'Profile(user={self.user})'

    def get_json_value(self):
        return {
            "id": self.id,
            "supervisor": {
                "id": self.supervisor.id,
                "firstName": self.supervisor.first_name,
                "lastName": self.supervisor.last_name
            },
            "userId": self.user.id,
            "role": self.role,
            "dob": self.dob,
            # "avatar": self.avatar,
            "avatarColor": self.avatar_color,
            "description": self.description
        }

    @staticmethod
    def from_json_value(json_value: dict):
        return Profile(**json_value)

    @staticmethod
    def get_random_rgb():
        low = 0
        high = 255
        r = np.random.randint(low, high)
        g = np.random.randint(low, high)
        b = np.random.randint(low, high)
        return f"rgb({r},{g},{b})"


class Telephone(models.Model):
    """
    Model that stores all telephone numbers of users
    """
    tel = models.CharField(max_length=20, null=True)
    profile: Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        profile = kwargs.get('profile', None)
        if profile is None and len(args) == 0:
            print('Try to instantiate Telephone without profile PrimaryKey!!! '
                  'Dummy Profile will be created!!!')
            profile = Profile(
                role=DEFAULT_ROLE_CHOICE)
            kwargs['profile'] = profile
        super().__init__(*args, **kwargs)
    def __str__(self):
        return f'{self.profile} - {self.tel}'

    def get_json_value(self):
        return {
            'tel': self.tel,
            'profileId': self.profile.id,
            'userId': self.profile.user.id
        }
