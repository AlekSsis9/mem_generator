from PIL import Image,ImageDraw,ImageFont

print("Генератор мемов запущен!")
top_text = input("Введи верхний текст ")
bottom_text = input("Введи нижний текст ")
# print(top_text, bottom_text)


print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")

image_number = int(input())

if image_number == 1:
    image_file = "cat_in_cafe.png"
elif image_number == 2:
    image_file = "cat_with_glass.png"
image = Image.open(image_file)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype('arial.ttf', size=70)

text = draw.textbbox((0, 0), top_text, font)
draw.text(((width - text[2]) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
draw.text(((width - text[2]) / 2, height - text[3] - 10), bottom_text, font=font, fill="black")
image.save("mem.jpg")
