import qrcode

code = qrcode.QRCode(
    version = 1,
    box_size=60,
    border=2
)

code.add_data("https://www.linkedin.com/in/halilcavus/")
code.make(fit=True)

image = code.make_image(fill_color="black",back_color="white")
image.save("twice.png")



print("QR Code oluşturuldu!.")
