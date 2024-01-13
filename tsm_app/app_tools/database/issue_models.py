import django.utils.timezone
from django.db import models

from . import user_models
from .. import utils

__all__ = [
    'Project', 'Task'
]

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


class DatabaseException(Exception):
    def __str__(self):
        return 'Database Exception'


class Issue(models.Model):
    """
    Base Models for Project and Task models.
    This defines some common attributes of an Issue e.g. name, start_date, end_date, etc.
    """
    name = models.CharField(max_length=50, default='', null=False)
    # TODO: created_date = models.DateField(auto_now_add=True)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=DEFAULT_PRIORITY, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=DEFAULT_STATUS, null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['-name']),
        ]

    def get_issue_info(self):
        return f'{self.__class__.__name__}: {self.name} Status: {self.status}'

    def get_json_value(self):
        return {
            "id": self.id,
            "name": self.name,
            "startDate": self.start_date,
            "dueDate": self.due_date,
            "createdDate": self.created_date,
            "priority": self.priority,
            "status": self.status,
            "description": self.description,
        }

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        """
        docstring
        """
        return {
            'startDate': lambda date: (utils.get_datetime_from_str(date), 'start_date'),
            'dueDate': lambda date: (utils.get_datetime_from_str(date), 'due_date'),
        }


class Project(Issue):
    """
    This model inherits all attributes from Issue and adds in a ForeignKey to CustomUser for a project leader
    """
    leader: user_models.CustomUser = models.ForeignKey(
        user_models.CustomUser, on_delete=models.SET_NULL, null=True)
    shortcut: models.CharField(null=True)
    image = models.ImageField(null=True, upload_to ='devices/projects/')

    def __str__(self):
        return f"{self.get_issue_info()} Leader: {self.leader}"

    def get_json_value(self):
        leader_json = None
        if self.leader is not None:
            leader_json = {
                "id": self.leader.id,
                "firstName": self.leader.first_name,
                "lastName": self.leader.last_name
            }
        return {
            **self.issue_ptr.get_json_value(),
            "shortcut": self.shortcut,
            "image": self.image,
            "leader": leader_json
        }

    @staticmethod
    def from_json_value(json_value: dict):
        project_arguments = {}
        field_to_converter = Issue.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in Issue.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                project_arguments[key] = value
        return Project(**project_arguments)


    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {
            **Issue.get_non_primitive_field_to_converter(),
            'leader': lambda leader_id: (user_models.CustomUser.objects.get(id=leader_id), 'leader')
        }


class Task(Issue):
    """
    This model inherits Issue and represents the lowest level of issue which is Task.
    It keeps a ForeignKey to CustomUser to indicate who is responsible for this task,
    and a ForeignKey to Project to imply which project this task belongs to.
    """
    line_project: Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assignee: user_models.CustomUser = models.ForeignKey(
        user_models.CustomUser, on_delete=models.SET_NULL, null=True)

    def __init__(self, *args, **kwargs):
        kwargs.pop("headers", None)
        line_project = kwargs.get('line_project', None)
        if line_project is None and len(args) == 0:
            print('Try to instantiate Telephone without profile PrimaryKey!!! '
                  'Dummy Profile will be created!!!')
            line_project = Project(
                name=f'dummy_project_name')
            line_project.save()
            kwargs['line_project'] = line_project
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f"{self.get_issue_info()} Project: {self.line_project} Assignee: {self.assignee}"

    def get_json_value(self):
        assignee_json = None
        if self.assignee is not None:
            assignee_json = {
                "id": self.assignee.id,
                "firstName": self.assignee.first_name,
                "lastName": self.assignee.last_name
            }
        line_project_json = self.line_project.get_json_value()
        return {
            **self.issue_ptr.get_json_value(),
            'lineProject': {
                "name": line_project_json["name"],
                "id": line_project_json["id"],
                "leader": line_project_json["leader"],
            }, # project foreign key cannot be null
            'assignee': assignee_json
        }

    @staticmethod
    def from_json_value(json_value: dict):
        task_arguments = {}
        field_to_converter = Task.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in Issue.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                task_arguments[key] = value
        return Task(**task_arguments)

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {
            **Issue.get_non_primitive_field_to_converter(),
            'lineProject': lambda project_id: (Project.objects.get(id=project_id), 'line_project'),
            'assignee': lambda assignee_id: (user_models.CustomUser.objects.get(id=assignee_id), 'assignee')
        }
