from django.db import models
from django.utils import timezone

from . import issue_models
from .. import utils

__all__ = ['Device']

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


class Device(models.Model):
    """
    This model represents a device used by a specified Project. It has several attributes
    e.g. device_name, device_type, etc.
    """
    device_name = models.CharField(max_length=50, default='', null=False)
    device_type = models.CharField(max_length=50, default=DEFAULT_DEVICE, choices=DEVICE_CHOICES)
    purchase_date = models.DateField(default=timezone.now, null=False)
    supplier = models.CharField(max_length=50, default='', null=False)
    invoice = models.ImageField(upload_to ='devices/invoices/')
    handover_date = models.DateField(default=timezone.now, null=False)
    basic_config = models.TextField(max_length=1000, default='', null=True)
    status = models.CharField(max_length=20, default=DEFAULT_DEVICE_STATUS, choices=DEVICE_STATUS_CHOICES)
    project: issue_models.Project = models.ForeignKey(issue_models.Project, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.device_type}({self.device_name} is used by {self.project})"

    def get_json_value(self):
        project_json = None
        if self.project is not None:
            json = self.project.get_json_value()
            project_json = {
                "name": json["name"],
                "id": json["id"],
                "leader": json["leader"]
            }
        return {
            'id': self.id,
            'deviceName': self.device_name,
            'deviceType': self.device_type,
            'purchaseDate': self.purchase_date,
            'supplier': self.supplier,
            'invoice': self.invoice,
            'handoverDate': self.handover_date,
            'basicConfig': self.basic_config,
            'status': self.status,
            'project': project_json
        }

    @staticmethod
    def from_json_value(json_value):
        return Device(**json_value)

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {
            "purchaseDate": lambda date: (utils.get_datetime_from_str(date), "purchase_date"),
            "handover_date": lambda date: (utils.get_datetime_from_str(date), "handover_date"),
            "project": lambda project_id: (issue_models.Project.objects.get(id=project_id), 'project')
        }
