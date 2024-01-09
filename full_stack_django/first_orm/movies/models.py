from django.db import models

# Create your models here.

class Movie(models.Model):
    # id
    title = models.CharField(max_length = 45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def __repr__(self):
    #     return "Title {}".format(self.title)

    def __str__(self):
        return f"<Movie Object: {self.title}, {self.description}, {self.release_date}, {self.duration}, ({self.id})>"
        