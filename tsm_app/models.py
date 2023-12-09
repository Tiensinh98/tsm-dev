from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

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


# class UserInfo(models.Model):
#     ROLE_CHOICES = [
#         ('software_developer', 'Software Developer'),
#         ('software_engineer', 'Software Engineer'),
#         ('junior_software_developer', 'Junior Software Developer'),
#         ('junior_software_engineer', 'Junior Software Engineer'),
#     ]
#
#     user: User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     role = models.CharField(
#         null=False,
#         max_length=50,
#         choices=ROLE_CHOICES,
#         default=ROLE_CHOICES[0][0]
#     )
#
#     def __str__(self):
#         return f'{self.__class__.__name__}({self.user.username} - {self.role.name})'


class BaseWorker(models.Model):
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Bell')
    dob = models.DateField(null=True)

    def __str__(self):
        return f'{self.__class__.__name__}({self.first_name} {self.last_name})'


class Leader(BaseWorker):
    LEADER_ROLES_CHOICES = [
        ('senior_software_developer', 'Senior Software Developer'),
        ('senior_software_engineer', 'Senior Software Engineer')
    ]

    role = models.CharField(
        null=False,
        max_length=50,
        choices=LEADER_ROLES_CHOICES,
        default=LEADER_ROLES_CHOICES[0][0]
    )


class Worker(BaseWorker):
    ROLE_CHOICES = [
        ('software_developer', 'Software Developer'),
        ('software_engineer', 'Software Engineer'),
        ('junior_software_developer', 'Junior Software Developer'),
        ('junior_software_engineer', 'Junior Software Engineer'),
    ]
    role = models.CharField(
        null=False,
        max_length=50,
        choices=ROLE_CHOICES,
        default=ROLE_CHOICES[0][0]
    )
    supervisor: Leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True)


class WorkerTelephone(models.Model):
    telephone_number = models.CharField(max_length=20, null=True)
    worker: BaseWorker = models.ForeignKey(BaseWorker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.worker} - {self.telephone_number}'


class BaseIssue(models.Model):
    issue_name = models.CharField(max_length=50, default='', null=False)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=DEFAULT_PRIORITY, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=DEFAULT_STATUS, null=True)
    description = models.TextField(max_length=1000, null=True)

    def get_issue_info(self):
        return f'{self.__class__.__name__}: {self.issue_name} Status: {self.status}'


class Project(BaseIssue):
    project_leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.get_issue_info()} Leader: {self.project_leader}"


class Task(BaseIssue):
    head_project: Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_issue_info()} Project: {self.head_project} Assignee: {self.worker}"
