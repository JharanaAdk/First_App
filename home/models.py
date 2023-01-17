from django.db import models

class demomodel(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    DOB = models.DateField()
    created_at = models.DateTimeField(auto_created=True)
    description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name
        
    
