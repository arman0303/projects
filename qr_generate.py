import qrcode

# ENTER YOUR APPLICATION URL HERE
url = "https://arman0303.github.io/projects/"   # ← Replace with your Flask/website URL

# Generate QR Code
img = qrcode.make(url)

# Save QR Code image
img.save("application_qr.png")

print("QR Code generated successfully: application_qr.png")
