from django.db import models

# Create your models here.
class Item(models.Model):
    # Blank in this instance just means that field will not be nullable when set to false and if we've said true then we would be allowed to have a blank field or a nullable field
    name = models.CharField(max_length=30, blank=False)
    done = models.BooleanField(blank=False, default=False)

    #dunder method to return the name of the object
    def __str__(self):
        return self.name