from django.db import models

class ModuleRegistry(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=20)
    installed = models.BooleanField(default=False)
    enabled = models.BooleanField(default=False)
    install_date = models.DateTimeField(null=True, blank=True)
    update_date = models.DateTimeField(null=True, blank=True)
    metadata = models.JSONField(default=dict)
    
    def __str__(self):
        return f"{self.name} v{self.version}"