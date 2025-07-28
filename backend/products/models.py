from django.db import models


# Create your models here.
       
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField()
    price = models.IntegerField()
    image = models.ImageField(default="")



    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = Product.objects.get(id=self.id)
        except Product.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.image and self.image and obj.image != self.image:
            # delete the old image file from the storage in favor of the new file
            obj.image.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.image.delete()
        return super(Product, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        return super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name