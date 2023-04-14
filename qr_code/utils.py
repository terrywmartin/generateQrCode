import qrcode
import qrcode.image.svg

from io import BytesIO


def generate_qr_code(type, **kwargs):
    factory = qrcode.image.svg.SvgImage
    qr = qrcode.QRCode(
             version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
            image_factory=factory
        )
    
    if type == 'url':
        url = kwargs['url']
        data = url
        
    elif type == 'vcard':
        first_name = kwargs['first_name']
        last_name = kwargs['last_name']
        email_address = kwargs['email_address']
        phone = kwargs['phone']
        data = f'BEGIN:VCARDVERSION:3.0\r\nN:{last_name};{first_name}\r\nFN:{first_name} {last_name}\r\nEMAIL:{email_address}\r\nTEL:{phone}\r\nEND:VCARD'

    elif type == 'wifi':
        ssid = kwargs['ssid']
        password = kwargs['password']
        security_method = kwargs['security_method']
        data = f'WIFI:S:{ssid};T:{security_method};P:{password};;'

    qr.add_data(data)
    img = qr.make_image()
    stream = BytesIO()
    img.save(stream) 
    return stream