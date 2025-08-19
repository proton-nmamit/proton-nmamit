import os
from django.core.management.base import BaseCommand
from magazine.models import Magazine
from django.core.files import File

class Command(BaseCommand):
    help = 'Re-upload magazine cover images to Cloudinary'

    def handle(self, *args, **kwargs):
        magazines = Magazine.objects.all()
        for magazine in magazines:
            if magazine.cover_image and os.path.isfile(magazine.cover_image.path):
                self.stdout.write(f"Re-uploading cover for: {magazine.title}")
                with open(magazine.cover_image.path, 'rb') as f:
                    django_file = File(f)
                    magazine.cover_image.save(os.path.basename(magazine.cover_image.name), django_file, save=True)
            else:
                self.stdout.write(f"No local cover image for: {magazine.title}")
        self.stdout.write("Re-upload complete.")
