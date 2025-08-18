import qrcode

# The text you want inside the QR
name = "nischal"

# Generate the QR
qr_img = qrcode.make(name)

# Save the QR code as an image file
qr_img.save("nischal.png")

print("QR code saved as nischal.png")
