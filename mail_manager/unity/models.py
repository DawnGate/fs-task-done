from django.db import models

# Create your models here.

class SignUpEmail(models.Model):
    # i don't want add unique or primary key for email field
    # just a simple demo so little restrict is better 
    email = models.EmailField()
    add_date = models.DateTimeField(auto_now_add=True)