
from django.db import models
from datetime import datetime
from django.utils import timezone
from django.utils.timezone import now
from django.db.models import F , Q
from django.db.models.functions import Now
class Task(models.Model):
    title = models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    created=models.DateTimeField(default=datetime.now(),editable=False)
    due_date=models.DateTimeField(default=datetime.now())
    OPEN='OPEN'
    WORKING='WORKING'
    DONE='DONE'
    OVERDUE='OVERDUE'
    state= [
    (OPEN,'open'),
    (WORKING,'working'),
    (DONE,'done'),
    (OVERDUE,'overdue'),]
    status=models.CharField(max_length=15,choices=state,default=OPEN,)

    objects = models.Manager()
    
    def __str__(self):
        return self.title