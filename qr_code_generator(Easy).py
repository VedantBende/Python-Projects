import qrcode             #Is used for making QR Code
from PIL import Image     #Is used for customizing QR Code
import qrcode.constants   #Is used for removing high level errors

#Below given code simply makes Black and White QR Code
img1 = qrcode.make(input("Enter the url: "))
img1.save(input("Enter the file name: ") + ".png")


#Below given code is used for making customized QR Code (Like = Color of QR , Size of QR, etc.)
#There are total of 40 versions, with each increasing version the more complex QR Code gets.
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10, border = 4)

qr.add_data(input("Enter the url: "))
qr.make(fit = True)
img2 = qr.make_image(fill_color = "red", back_color = "blue")
img2.save(input("Enter the file name: ") + ".png")
print("QR Image Saved")