from django.db import models

class Notify_Me(models.Model):
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)  
    
    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-created_date']
