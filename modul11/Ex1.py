import requests
import pandas as pd
from PIL import Image, ImageFilter


url = 'https://api.github.com/events'
response = requests.get(url)
if response.status_code == 200:
    data_1 = response.url
    print(f'код 200 - Все ОК')
else:
    print('Ошибка при выполнении запроса')

print('______________________________________')
# выполнение запроса на сайт


data_2 = pd.read_fwf(r'C:\Users\efanov_av\PycharmProjects\pythonProject\modul11\Text.txt')
print(data_2.head())
print('______________________________________')
# считывание данных с файла, вывод данных в консоль


image = Image.open(r'C:\Users\efanov_av\PycharmProjects\pythonProject\modul11\Enduro.jpg')
resized_image = image.resize((400, 200))
resized_image.save('resized_Enduro.jpg')
# изменить разрешение изображения

image = Image.open(r'C:\Users\efanov_av\PycharmProjects\pythonProject\modul11\Enduro.jpg')
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blur_Enduro.jpg')
# применить эффекты к изображению

image = Image.open(r'C:\Users\efanov_av\PycharmProjects\pythonProject\modul11\Enduro.jpg')
image.save('converted_Enduro.gif')
# сохранение изображения в другой формат