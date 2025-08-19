from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Magazine
import qrcode
from io import BytesIO
import base64

def magazine_detail(request, pk=None):
    # If no pk is provided, get the latest active magazine
    if pk is None:
        magazine = Magazine.objects.filter(is_active=True).first() # Get the latest active magazine
        if not magazine:
            return render(request, 'magazine/no_magazine.html')
    else:
        magazine = get_object_or_404(Magazine, pk=pk, is_active=True)
    
    # Determine the link to use for the QR code
    if magazine.pdf_file:
        link_to_share = request.build_absolute_uri(magazine.drive_link)
    else:
        link_to_share = magazine.drive_link

    # Generate QR code for the magazine link
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link_to_share)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    qr_code_data = base64.b64encode(buffer.getvalue()).decode()
    
    context = {
        'magazine': magazine,
        'qr_code': qr_code_data,
    }
    
    return render(request, 'magazine/magazine_detail.html', context)

def track_download(request, pk):
    magazine = get_object_or_404(Magazine, pk=pk)
    magazine.download_count += 1
    magazine.save()
    return JsonResponse({'status': 'success', 'count': magazine.download_count})

def magazine_list(request):
    magazines = Magazine.objects.filter(is_active=True)
    return render(request, 'magazine/magazine_list.html', {'magazines': magazines})
