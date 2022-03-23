import pyqrcode
import png

print("Welcome to QR code Genertaor")

msg=input("Type your secret message")
code=pyqrcode.create(msg)
code.png("QRCODE.png",scale=5)
print("QR Code Generator Succesfully!")