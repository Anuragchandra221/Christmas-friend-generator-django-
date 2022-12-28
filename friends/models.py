from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=15)

class Friends(models.Model):
    name = models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank=True, null=True )
    selected = models.BooleanField(default=False)
    hasAFriend = models.BooleanField(default=False)

    def __str__(self): 
        return self.name

class Pair(models.Model):
    name1 = models.CharField(max_length=20)
    name2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name1 + " and " + self.name2