from django.db import models

# Create your models here.

class Users(models.Model):
    # id
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)



    def __str__(self):
        return f"<User Object: {self.first_name}, {self.last_name}, {self.email}, {self.age}, ({self.id})>"
        