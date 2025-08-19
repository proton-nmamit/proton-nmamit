from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

def photos(request):
    try:
        photos = Photo.objects.all().order_by('-created_at')
        photo_count = photos.count()
        
        # Debug information
        logger.info(f"Number of photos found: {photo_count}")
        logger.info(f"MEDIA_URL: {settings.MEDIA_URL}")
        logger.info(f"MEDIA_ROOT: {settings.MEDIA_ROOT}")
        
        for photo in photos:
            logger.info(f"Photo {photo.id}: {photo.caption}")
            logger.info(f"Image URL: {photo.image.url}")
        
        context = {
            'photos': photos,
            'photo_count': photo_count,
            'debug': settings.DEBUG
        }
        return render(request, 'gallery.html', context)  # Remove 'gallery/' prefix
    except Exception as e:
        logger.error(f"Error in photos view: {str(e)}")
        return HttpResponse(f"Error loading gallery: {str(e)}", status=500)