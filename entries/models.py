from django.db import models

class Entries(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, default="default name")
    notes = models.TextField()
    signout_date = models.DateTimeField(auto_now=True)
    is_signout = models.BooleanField(default=False)
        
    def __str__(self):
        return f'{self.name}'