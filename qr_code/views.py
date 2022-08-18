from django.shortcuts import render
from django.views import View

from django.http import FileResponse, HttpResponse

import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw
from io import BytesIO


# Create your views here.
class GenerateQRCode(View):
    def post(self, request):
        url = request.POST.get('url')
       
        if url == '':
            return render(request, 'partials/failure.html')

        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(url, image_factory = factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        
        context = { 'qrcode': stream.getvalue().decode(),
            'url': url
         }
        return render(request, 'qr_code/partials/view_qrcode.html', context)

class DownloadQRCode(View):
    def get(self, request):
        url = request.GET.get('url')
        print(url)
        if url == '':
            return render(request, 'partials/failure.html')

        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(url, image_factory = factory, box_size=20)
        stream = BytesIO()
        img.save(stream)
        headers = {
            'Content-Type': 'image/svg+xml',
            'Content-Disposition': 'inline; filename="qrcode.svg"'
        }
        
        #response = FileResponse(stream.getvalue().decode(), as_attachment=True,filename='qrcode.svg')

        
        return HttpResponse(stream.getvalue().decode(), headers=headers)
        #return response