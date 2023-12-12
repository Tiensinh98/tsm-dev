from django.db import models
import django.utils.timezone as tz

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

    def get_json_value(self):
        return {
            'issue_name': self.issue_name,
            'start_date': self.start_date,
            'due_date': self.start_date,
            'priority': self.priority,
            'status': self.status,
            'description': self.description,
        }


class Project(BaseIssue):
    project_leader = models.ForeignKey(Leader, on_delete=models.SET_NULL, null=True)
    workers = models.ManyToManyField(Worker)

    def __str__(self):
        return f"{self.get_issue_info()} Leader: {self.project_leader}"

    def get_json_value(self):
        leader_info = self.project_leader.__dict__
        return {
            'project_leader': leader_info.get('first_name') + leader_info.get('last_name'),
            **super().get_json_value()
        }


class Task(BaseIssue):
    head_project: Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.get_issue_info()} Project: {self.head_project} Assignee: {self.worker}"

    def get_json_value(self):
        return {
            'head_project': self.head_project.get_json_value()['issue_name'],
            # 'worker': self.worker,
            **super().get_json_value()
        }

class Device(models.Model):
    device_name = models.CharField(max_length=50, default='', null=False)
    device_type = models.CharField(max_length=50, default=DEFAULT_DEVICE, choices=DEVICE_CHOICES)
    purchase_date = models.DateField(default=tz.now(), null=False)
    supplier = models.CharField(max_length=50, default='', null=False)
    invoice = models.ImageField(upload_to =f'devices/invoice/{device_type}/{device_name}')
    handover_date = models.DateField(default=tz.now(), null=False)
    basic_config = models.TextField(max_length=1000, default='', null=True)
    status = models.CharField(max_length=20, default=DEFAULT_DEVICE_STATUS, choices=DEVICE_STATUS_CHOICES)
    user = models.ForeignKey(Worker, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.device_type}({self.device_name} is used by {self.user})"


class DeviceUserHistory(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    user = models.ForeignKey(Worker, on_delete=models.CASCADE, null=True)
    handover_date = models.DateField(default='', null=False)
    expired_date = models.DateField(default='', null=False)

    def __str__(self):
        return f"{self.user} used {self.device} from {self.handover_date} to {self.expired_date}"
