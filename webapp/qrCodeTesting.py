import pyqrcode


def qrStringEncoder(string):

    qrcode = pyqrcode.create(string)
    qrcode.svg('qrcodeExample.svg', scale=8)
    print(qrcode.terminal(quiet_zone=1))


qrStringEncoder('hello')





#
# def qrStringEncoder(string):
#     # takes a string to encode
#     # returns QR code image (version 1)
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(string)
#     qr.make(fit=True)
#
#     img = qr.make_image()
#     img.show()
#     return img
# #qrStringEncoder('jamesdean@gmail.com/student/The Martian/18:00')
