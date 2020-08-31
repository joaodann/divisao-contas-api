import uuid
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Group(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)
    members = ArrayField(models.CharField(max_length=30), blank=True)

    def save(self, *args, **kwargs):
        try:
            members = Group.objects.get(pk=self.id).members
            self.members.extend(members)
            self.members = list(set(self.members))
        finally:
            return super(Group, self).save(*args, **kwargs)