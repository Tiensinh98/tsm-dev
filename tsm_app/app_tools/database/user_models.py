from django.db import models
from django.contrib.auth import models as auth_models


__all__ = [
    'CustomUser', 'Profile', 'Telephone'
]

ROLE_CHOICES = [
    ('software_developer', 'Software Developer'),
    ('software_engineer', 'Software Engineer'),
    ('junior_software_developer', 'Junior Software Developer'),
    ('junior_software_engineer', 'Junior Software Engineer'),
    ('senior_software_developer', 'Senior Software Developer'),
    ('senior_software_engineer', 'Senior Software Engineer')
]


class CustomUser(auth_models.AbstractUser):
    """
    Model that stores all user information i.e. username, password,
    email, first_name, last_name and a profile
    """
    class Meta:
        app_label = 'tsm_app'
        swappable = 'AUTH_USER_MODEL'

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


class Profile(models.Model):
    user: CustomUser = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='user')
    supervisor: CustomUser = models.OneToOneField(
        CustomUser, on_delete=models.SET_NULL, null=True, related_name='supervisor')
    role = models.CharField(
        null=False,
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0]
    )
    dob = models.DateField(null=True)
    profile_image = models.ImageField(upload_to='users/profile/')
    description = models.TextField(max_length=1000, null=True)

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


class Telephone(models.Model):
    """
    Model that stores all telephone numbers of users
    """
    tel = models.CharField(max_length=20, null=True)
    profile: Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.profile} - {self.tel}'

    def get_json_value(self):
        return {
            'tel': self.tel,
            'profile_id': self.profile.id,
            'user_id': self.profile.user.id
        }
