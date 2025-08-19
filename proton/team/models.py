from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import MediaCloudinaryStorage
from django.core.validators import MinValueValidator, MaxValueValidator
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

# Create your models here.

class member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    position = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=10, null=True, default='2024')
    email = models.EmailField()
    phone = models.BigIntegerField(null=True, validators=[
            MinValueValidator(1000000000),  # At least 10 digits
            MaxValueValidator
        ])
    role = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='team/members_images',
        storage=MediaCloudinaryStorage(),
        null=True,
        blank=True
    )
    linkedin = models.URLField()
    github = models.URLField()
    instagram = models.URLField()

    def save(self, *args, **kwargs):
        # Process image if a new one is provided  
        if self.image:
            process_image = False
            if not self.pk:
                # New object: process if image is provided and not already webp.
                process_image = not self.image.name.lower().endswith('.webp')
            else:
                # Existing object: check if image was changed.
                previous = member.objects.filter(pk=self.pk).first()
                if previous and previous.image != self.image:
                    process_image = not self.image.name.lower().endswith('.webp')
            if process_image:
                try:
                    # Open and convert the image to webp format with compression
                    im = Image.open(self.image)
                    output = io.BytesIO()
                    im.save(output, format="WEBP", quality=60)
                    output.seek(0)
                    # Create a new InMemoryUploadedFile instance for the converted image
                    self.image = InMemoryUploadedFile(
                        output,
                        "ImageField",
                        self.image.name.rsplit(".", 1)[0] + ".webp",
                        "image/webp",
                        output.getbuffer().nbytes,
                        None
                    )
                except Exception as e:
                    # log the exception if needed; otherwise pass
                    pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name