from pyzbar.pyzbar import decode
from PIL import Image

# Open the QR code image
img = Image.open('C:\\Users\\amsal\\Downloads\\myqrcode1.png')

# Decode the QR code
result = decode(img)

# Print the result
print(result)
