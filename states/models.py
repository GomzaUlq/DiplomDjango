from django.db import models


class State(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
