from django.db import models


class FizzBuzz(models.Model):
    fizzbuzz_id = models.AutoField(primary_key=True)
    useragent = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()
    