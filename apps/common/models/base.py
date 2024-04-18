from django.db import models
import uuid
from datetime import datetime 

class Base(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)  
    created = models.DateTimeField(default=datetime.now, editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    # is_deleted = models.BooleanField(default=False)

    # def delete(self, *args, **kwargs):
    #     self.is_deleted = True
    #     self.save()

    # def hard_delete(self, *args, **kwargs):
    #     super().delete(*args, **kwargs)
    class Meta:
        abstract=True