import qrcode

# Data for QR code
data = "hello world"

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data to QR
qr.add_data(data)
qr.make(fit=True)

# Customize colors
img = qr.make_image(fill_color='red', back_color='white')

# Save QR code image
img.save('C:\\Users\\amsal\\Downloads\\myqrcode1.png')

