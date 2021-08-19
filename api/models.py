from django.db import models
from django.contrib.auth.models import User
class Link(models.Model):
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    random_string = models.CharField(max_length=9)
    visit_count = models.IntegerField(default=0)

    def __str__(self):
        return self.link
    
    def short_link(self):
        return f"http://127.0.0.1:8000/r/{self.random_string}"


