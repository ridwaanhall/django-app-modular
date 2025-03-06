from django.db import models

class InstalledModule(models.Model):
    name = models.CharField(max_length=255, unique=True)
    installed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
