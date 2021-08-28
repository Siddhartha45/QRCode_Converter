import pyqrcode
import png
from pyqrcode import QRCode

website = input("Enter the website: ")

url = pyqrcode.create(website)

url.png("qrcode.png", scale = 4)

print("The QRCode for the given link has been created and saved as qrcode.png.")
#QRCode is saved as "qrcode.png" in the same path where python file exists.