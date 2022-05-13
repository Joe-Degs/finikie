from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    description = models.TextField()
    date_created = models.DateTimeField(auto_created=True, editable=False)
    date_completed = models.DateTimeField(auto_created=False, default=None)
    completed = models.BooleanField(default=False, auto_created=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check = models.Q(date_completed__gt=models.F(('date_created'))),
                name= 'check_date_completed',
            )
        ]