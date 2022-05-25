from tempfile import TemporaryFile
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def create_img(text_on_img: dict):
    tmp = TemporaryFile()
    # bin_img = BytesIO()
    img = Image.open('terra.png')
    I1 = ImageDraw.Draw(img)
    my_font = ImageFont.truetype('UbuntuMono-B.ttf', 24)
    red = (180, 75, 109)
    green = (75, 180, 146)
    sign = '-'
    color = red
    if text_on_img['positive']:
        sign = '+'
        color = green
    I1.text((8, 95),
            f"{sign}{text_on_img['percents']}% {text_on_img['cur_price']}",
            font=my_font, fill=color)
    img.save(tmp, format="PNG")
    # tmp.write(img.tobytes)
    tmp.seek(0)
    return(tmp.read())
