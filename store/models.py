from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    book_category = models.CharField(max_length=200, default="")
    publication_date = models.DateField()
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    price = models.FloatField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Cart(models.Model):
    posts = models.ManyToManyField(Post, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)
