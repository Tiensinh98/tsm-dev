from django.db import models

from . import user_models
from .. import utils

__all__ = ['Team']


class Team(models.Model):
    """
    This model represents a team which is supervised by a leader (CustomUser) and consists of
    multiple team members
    """
    name = models.CharField(max_length=50, default='', null=False)
    department = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    leader: user_models.CustomUser = models.OneToOneField(
        user_models.CustomUser, on_delete=models.SET_NULL, null=True, related_name='leader')
    member: user_models.CustomUser = models.ForeignKey(
        user_models.CustomUser, on_delete=models.SET_NULL, null=True, related_name="member")

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
    def get_non_primitive_field_to_converter() -> dict:
        return {
            'leader': lambda leader_id: (user_models.CustomUser.objects.get(id=leader_id), 'leader')
        }