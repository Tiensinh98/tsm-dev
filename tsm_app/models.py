from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

__all__ = ['Worker', 'Telephone', 'Project', 'Task']

DEFAULT_PRIORITY = 'medium'
PRIORITY_CHOICES = [
    ('highest', 'Highest'),
    ('high', 'High'),
    (DEFAULT_PRIORITY, 'Medium'),
    ('low', 'Low'),
    ('lowest', 'Lowest')
]
DEFAULT_STATUS = 'to_do'
STATUS_CHOICES = [
    (DEFAULT_STATUS, 'To Do'),
    ('in_development', 'In Development'),
    ('on_hold', 'On Hold'),
    ('done', 'Done'),
    ('reject', 'Reject')
]


class Worker(models.Model):
    ROLE_CHOICES = [
        ('software_developer', 'Software Developer'),
        ('software_engineer', 'Software Engineer'),
        ('junior_software_developer', 'Junior Software Developer'),
        ('junior_software_engineer', 'Junior Software Engineer'),
    ]

    user: User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
        null=False,
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0]
    )

    def __str__(self):
        return f'{self.__class__.__name__}({self.user.username} - {self.role.name})'


class Leader(models.Model):
    ROLE_CHOICES = [
        ('software_developer', 'Software Developer'),
        ('software_engineer', 'Software Engineer'),
        ('junior_software_developer', 'Junior Software Developer'),
        ('junior_software_engineer', 'Junior Software Engineer'),
    ]

    user: User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(
        null=False,
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0]
    )

    def __str__(self):
        return f'{self.__class__.__name__}({self.user.username} - {self.role.name})'


class Telephone(models.Model):
    telephone_number = models.CharField(max_length=20, default='')
    staff: Worker = models.ForeignKey(Worker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff.user.username} - {self.telephone_number.name}'


class Project(models.Model):
    project_name = models.CharField(max_length=50, blank=False)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=DEFAULT_PRIORITY)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=DEFAULT_STATUS)
    description = models.TextField(max_length=1000, blank=True)
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, null=True)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return (f'{self.project_name.name} - {self.status.name}\n'
                f'Description: {self.description.name}')


class Task(models.Model):
    task_name = models.CharField(max_length=50, blank=False)
    start_date = models.DateField()
    due_date = models.DateField()
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=DEFAULT_PRIORITY)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=DEFAULT_STATUS)
    description = models.TextField(max_length=1000, blank=True)
    project: Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (f'{self.task_name.name} - {self.status.name} '
                f'belongs to project {self.project.project_name}\n'
                f'Description: {self.description.name}')
