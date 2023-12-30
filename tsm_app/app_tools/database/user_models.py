import logging
import uuid

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
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_id': self.profile.id,
            'team_id': self.team.id
        }

    @staticmethod
    def from_json_value(json_value: dict):
        return CustomUser(**json_value)


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
    profile_image = models.ImageField(upload_to='users/profile/')
    description = models.TextField(max_length=1000, null=True)

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
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'Profile(user={self.user})'

    def get_json_value(self):
        return {
            'id': self.id,
            'supervisor_id': self.supervisor.id,
            'user_id': self.user.id,
            'role': self.role,
            'dob': self.dob,
            'profile_image': self.profile_image,
            'description': self.description
        }

    @staticmethod
    def from_json_value(json_value: dict):
        return Profile(**json_value)


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
            'profile_id': self.profile.id,
            'user_id': self.profile.user.id
        }
