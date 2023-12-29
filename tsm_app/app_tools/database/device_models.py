from django.db import models
from django.utils import timezone

from . import issue_models

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
        project_id = None
        if self.project is not None:
            project_id = self.project.id
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
            'project_id': project_id
        }
