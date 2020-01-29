import re

regex = r"https?://.*\.(jpg|png|gif|)"

test_str = ("http://site.com/folder/1.png\n"
            "https://jksfdlksj/sdf/132.jpg\n"
            "https://jksfdlksj/678.gif\n"
            "https://jksfdlksj/hjhk.jpeg\n"
            "https://jksfdlksj/hjkjljh.tif")
m = ['png', 'jpg', 'gif']
matches = re.finditer(regex, test_str, re.MULTILINE)
for i in matches:
    if i.group(1) in m:
        print(f'Да ссылка {i.group()} ведет к картинке {i.group(1)} формата')
