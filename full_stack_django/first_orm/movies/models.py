from django.db import models
# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Movie(models.Model):
    # id
    title = models.CharField(max_length = 45)
    director = models.ForeignKey(Director, related_name="movies", on_delete = models.CASCADE, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # def __repr__(self):
    #     return "Title {}".format(self.title)

    def __str__(self):
        return f"<Movie Object: {self.title}, {self.director.name}, ({self.id})>"