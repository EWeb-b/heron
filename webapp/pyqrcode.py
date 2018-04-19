import qrcode

def qrStringEncoder(string):
    # takes a string to encode
    # returns QR code image (version 1)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(string)
    qr.make(fit=True)

    img = qr.make_image()
    img.show()
    return img
