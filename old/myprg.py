import qrcode
img = qrcode.make(
    'https://youtu.be/_nQzneu9sVw?si=EdKoU-r3htGHwdTf'
)
img.save('myQRcode.png')
img.show()
