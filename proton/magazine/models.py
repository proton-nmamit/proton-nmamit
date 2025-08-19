from django.db import models
from django.utils import timezone
from cloudinary_storage.storage import MediaCloudinaryStorage
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

class Magazine(models.Model):
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=10, help_text="e.g., 2024-25")
    description = models.TextField(blank=True)
    drive_link = models.URLField(help_text="Google Drive link to the magazine", blank=True, null=True)
    pdf_file = models.FileField(upload_to='magazine_pdfs/', storage=MediaCloudinaryStorage(), blank=True, null=True, help_text="Upload the magazine PDF")
    cover_image = models.ImageField(upload_to='magazine_covers/', storage=MediaCloudinaryStorage(), blank=True, null=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    download_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-published_date']
    
    def save(self, *args, **kwargs):
        # Process image if a new one is provided  
        if self.cover_image:
            process_image = False
            if not self.pk:
                # New object: process if image is provided and not already webp.
                process_image = not self.cover_image.name.lower().endswith('.webp')
            else:
                # Existing object: check if image was changed.
                previous = Magazine.objects.filter(pk=self.pk).first()
                if previous and previous.cover_image != self.cover_image:
                    process_image = not self.cover_image.name.lower().endswith('.webp')
            if process_image:
                try:
                    # Open and convert the image to webp format with compression
                    im = Image.open(self.cover_image)
                    output = io.BytesIO()
                    im.save(output, format="WEBP", quality=60)
                    output.seek(0)
                    # Create a new InMemoryUploadedFile instance for the converted image
                    self.cover_image = InMemoryUploadedFile(
                        output,
                        "ImageField",
                        self.cover_image.name.rsplit(".", 1)[0] + ".webp",
                        "image/webp",
                        output.getbuffer().nbytes,
                        None
                    )
                except Exception as e:
                    # log the exception if needed; otherwise pass
                    pass

        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.title} ({self.year})"
