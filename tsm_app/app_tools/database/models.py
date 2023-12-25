from datetime import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth import models as auth_models

__all__ = [
    'Leader', 'Worker', 'Project', 'Task',
    'WorkerTelephone', 'Device', 'DeviceUserHistory', 'CustomUser'
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
DEFAULT_DEVICE = 'laptop'
DEVICE_CHOICES = [
    (DEFAULT_DEVICE, 'Laptop'),
    ('monitor', 'Monitor'),
    ('keyboard', 'Keyboard'),
    ('mouse', 'Mouse'),
    ('cpu', 'CPU'),
]
DEFAULT_DEVICE_STATUS = 'in_use'
DEVICE_STATUS_CHOICES = [
    (DEFAULT_DEVICE_STATUS, 'In Use'),
    ('in_fix', 'In Fix'),
    ('idle', 'Idle'),
]

class DatabaseException(Exception):
    def __str__(self):
        return 'Database Exception'


class BaseWorker(models.Model):
    """
    docstring
    """
    first_name = models.CharField(null=False, max_length=30, default='John')
    last_name = models.CharField(null=False, max_length=30, default='Bell')
    dob = models.DateField(null=True)

    def __str__(self):
        return f'{self.__class__.__name__}({self.first_name} {self.last_name})'

    def get_json_value(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'dob': self.dob
        }

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        """
        docstring
        """
        return {
            'dob': lambda ts, format='%Y-%m-%d': datetime.strptime(ts, format) if ts is not None else None,
        }


class Leader(BaseWorker):
    """
    docstring
    """
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

    def get_json_value(self):
        return {
            **super().get_json_value(),
            'role': self.role
        }

    @staticmethod
    def from_json_value(json_value: dict):
        leader_arguments = {}
        field_to_converter = Leader.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in BaseWorker.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                leader_arguments[key] = value
        try:
            leader = Leader(**leader_arguments)
            return leader
        except DatabaseException as e:
            print('Leader may exist already')
            return


class Worker(BaseWorker):
    """
    docstring
    """
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

    def get_json_value(self):
        return {
            **super().get_json_value(),
            'role': self.role,
            'supervisor': self.supervisor.get_json_value()
        }



class WorkerTelephone(models.Model):
    """
    docstring
    """
    telephone_number = models.CharField(max_length=20, null=True)
    worker: BaseWorker = models.ForeignKey(BaseWorker, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.worker} - {self.telephone_number}'


class BaseIssue(models.Model):
    """
    docstring
    """
    issue_name = models.CharField(max_length=50, default='', null=False)
    start_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default=DEFAULT_PRIORITY, null=True)
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=DEFAULT_STATUS, null=True)
    description = models.TextField(max_length=1000, null=True)

    class Meta:
        ordering = ['-issue_name']
        indexes = [
            models.Index(fields=['-issue_name']),
        ]

    def get_issue_info(self):
        return f'{self.__class__.__name__}: {self.issue_name} Status: {self.status}'

    def get_json_value(self):
        return {
            'id': self.id,
            'issue_name': self.issue_name,
            'start_date': self.start_date,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status,
            'description': self.description,
        }

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        """
        docstring
        """
        return {
            'start_date': lambda ts, format='%Y-%m-%d': datetime.strptime(ts, format) if ts is not None else None,
            'due_date': lambda ts, format='%Y-%m-%d': datetime.strptime(ts, format) if ts is not None else None
        }


class Project(BaseIssue):
    """
    docstring
    """
    project_leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.get_issue_info()} Leader: {self.project_leader}"

    def get_json_value(self):
        project_leader_json = None
        if self.project_leader is not None:
            project_leader_json = self.project_leader.get_json_value()
        return {
            **self.baseissue_ptr.get_json_value(),
            'project_leader': project_leader_json,
            'workers': [worker.get_json_value() for worker in self.workers.all()]
        }

    @staticmethod
    def from_json_value(json_value: dict):
        project_arguments = {}
        field_to_converter = Project.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in BaseIssue.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                project_arguments[key] = value
        project_leader_json = json_value.get('project_leader')
        if project_leader_json is not None:
            try:
                leader = Leader(**project_leader_json)
                leader.save()
                project_arguments['project_leader'] = leader
            except DatabaseException as e:
                print(e)
                leader = Leader.objects.get(baseworker_ptr_id=project_leader_json['id'])
            project_arguments['project_leader'] = leader
        return Project(**project_arguments)


    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {
            **BaseIssue.get_non_primitive_field_to_converter(),
            'project_leader': lambda leader_id: Leader.objects.get(baseworker_ptr_id=leader_id)
        }


class Task(BaseIssue):
    """
    docstring
    """
    head_project: Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_issue_info()} Project: {self.head_project} Assignee: {self.worker}"

    def get_json_value(self):
        worker_json = None
        if self.worker is not None:
            worker_json = self.worker.get_json_value()
        return {
            **self.baseissue_ptr.get_json_value(),
            'head_project': self.head_project.get_json_value(),
            'worker': worker_json
        }


class Device(models.Model):
    """
    docstring
    """
    device_name = models.CharField(max_length=50, default='', null=False)
    device_type = models.CharField(max_length=50, default=DEFAULT_DEVICE, choices=DEVICE_CHOICES)
    purchase_date = models.DateField(default=timezone.now, null=False)
    supplier = models.CharField(max_length=50, default='', null=False)
    invoice = models.ImageField(upload_to =f'devices/invoice/{device_type}/{device_name}')
    handover_date = models.DateField(default=timezone.now, null=False)
    basic_config = models.TextField(max_length=1000, default='', null=True)
    status = models.CharField(max_length=20, default=DEFAULT_DEVICE_STATUS, choices=DEVICE_STATUS_CHOICES)
    user = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.device_type}({self.device_name} is used by {self.user})"

    def get_json_value(self):
        user_json = None
        if self.user is not None:
            user_json = self.user.get_json_value()
        return {
            'id': self.id,
            'device_name': self.device_name,
            'device_type': self.device_type,
            'purchase_date': self.purchase_date,
            'supplier': self.supplier,
            'invoice': self.invoice,
            'handover_date': self.handover_date,
            'basic_config': self.basic_config,
            'status': self.status,
            'user': user_json
        }


class DeviceUserHistory(models.Model):
    """
    docstring
    """
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    handover_date = models.DateField(default=timezone.now, null=False)
    expired_date = models.DateField(default=timezone.now, null=False)

    def __str__(self):
        return f"{self.user} used {self.device} from {self.handover_date} to {self.expired_date}"


class CustomUser(auth_models.AbstractUser):
    """
    Model for user authentication
    """
    class Meta:
        app_label = 'tsm_app'
        swappable = 'AUTH_USER_MODEL'

    dob = models.DateField(null=True)
    profile_image = models.ImageField(upload_to ='users/profile/')
