from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pub_date = models.DateField()

    def __str__(self):
        return self.title
