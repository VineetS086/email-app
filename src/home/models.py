from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
import random
import string


def get_random_string(length):
    chars = string.ascii_letters + string.digits
    random_str = ''.join((random.choice(chars) for i in range(length)))
    return random_str
    

class History(models.Model):
    user        = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    page        = models.CharField(max_length=50)
    action      = models.CharField(max_length=50)

    email_from  = models.EmailField(blank = True, null=True)
    email_to    = models.TextField(blank=True, null=True)
    ip          = models.CharField(max_length=50, default='127.0.0.1')
    time        = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'{self.action} - {self.page} - {self.user}'


class User_Key(models.Model):
    user    = models.OneToOneField(User, on_delete=models.CASCADE)
    key     = models.CharField(max_length=15, default=get_random_string(15))

    def activate(self, bool=True):
        self.user.is_active = bool