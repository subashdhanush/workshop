import qrcode
from PIL import Image
data = "https://christsquare.com/"
qr = qrcode.make(data)
qr.show()
