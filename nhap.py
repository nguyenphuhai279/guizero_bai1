from guizero import *
from random import *
app = App(title="Hello word")
title = Text(app, text="Nhấn vào Button để tìm ra gián điệp ngẫu nhiên", size=14, color="blue")
button = PushButton(app, text="Click", command=app.destroy)
def change_text():
    random_text = random.choice()
    text_widget.value = random_text
    text_widget.color = random.choice()
text_widget = Text(app)
app.display()