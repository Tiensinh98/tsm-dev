from django.db import models
import tsm_app.app_tools as pt
from .. import utils

__all__ = ['Team']


class Team(models.Model):
    """
    This model represents a team which is supervised by a leader (CustomUser) and consists of
    multiple team members
    """
    name = models.CharField(max_length=50, default='', null=False)
    department = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50, null=True)
    leader = models.OneToOneField(
        'CustomUser', on_delete=models.SET_NULL, null=True, related_name='leader')

    class Meta:
        ordering = ['-name']
        indexes = [
            models.Index(fields=['-name']),
        ]

    def get_issue_info(self):
        return f'Team(name={self.name}, leader= {self.leader})'

    def get_json_value(self):
        leader_json = None
        if self.leader is not None:
            leader_json = {
                "id": self.leader.id,
                "firstName": self.leader.first_name,
                "lastName": self.leader.last_name
            }
        return {
            "id": self.id,
            "name": self.name,
            "department": self.department,
            "description": self.description,
            "leader": leader_json,
        }

    @staticmethod
    def from_json_value(json_value: dict):
        task_arguments = {}
        field_to_converter = Team.get_non_primitive_field_to_converter()
        for key, value in json_value.items():
            if key in Team.__dict__.keys():
                if key in field_to_converter:
                    value = field_to_converter[key](value)
                task_arguments[key] = value
        return Team(**task_arguments)

    @staticmethod
    def get_non_primitive_field_to_converter() -> dict:
        return {
            'leader': lambda leader_id: (pt.CustomUser.objects.get(id=leader_id), 'leader')
        }