import qrcode
from PIL import Image


img = qrcode.make('https://github.com/ChunL-Su')
img.show()











def create_qrcode(url):
    qr = qrcode.QRCode(
        version=1,  # 设置容错率为最高
        error_correction=qrcode.ERROR_CORRECT_H,  # 用于控制二维码的错误纠正程度
        box_size=8,  # 控制二维码中每个格子的像素数，默认为10
        border=4,  # 二维码四周留白，包含的格子数，默认为4
    )

    qr.add_data(url)  # QRCode.add_data(data)函数添加数据
    qr.make(fit=True)  # QRCode.make(fit=True)函数生成图片

    img = qr.make_image()
    img = img.convert("RGBA")  # 二维码设为彩色
    # logo = Image.open(r"d:\logo.jpg")  # 传gif生成的二维码也是没有动态效果的
    logo = Image.open(r"d:\wyh.png")

    w,h = img.size
    logo_w,logo_h = logo.size
    l_w = int((w - logo_w) / 2)
    l_h = int((h - logo_h) / 2)
    logo = logo.convert("RGBA")
    img.paste(logo, (l_w, l_h), logo)
    img.show()
    img.save(r"d:\www.png", quality=100)

# create_qrcode('快来关注我^O^/')
