# PYTHON EASY QR CODE

import qrcode

code = qrcode.make("https://www.linkedin.com/in/halilcavus/")
code.save("easyQR")