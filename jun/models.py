from django.db import models

# Create your models here.
class Blog_jun(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    files =models.FileField(null=True,upload_to='files/')
    isFile=models.BooleanField(default=False)
    def summary(self):
        return self.body[:30]