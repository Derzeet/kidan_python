from datetime import date
from django.db import models

class FollowingList(models.Model):
    follower = models.ForeignKey('Account', on_delete=models.PROTECT, related_name="follower")
    following = models.ForeignKey('Account', on_delete=models.PROTECT, related_name="following")


class Account(models.Model):
    name = models.CharField(max_length=50, null=False)
    tag = models.CharField(max_length=30, null=False)
    bio = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    date_of_birth = models.DateField(null=False)
    joined_at = models.DateField(default=date.today)

class Kids(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)

