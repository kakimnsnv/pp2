import re
def test1():
    text = "cat cot car c._oat cut"
    pattern = "[c]\S*[t]"
    x = re.findall(pattern, text)
    print(x)

def test2():
    text = "http://glkjdfg.gldkfj https://gdfgkjfd.gfgdfsg"
    pattern = r"^http://\w+|https://\w+"
    x = re.findall(pattern, text)
    print(x)

def test3():
    text = "(777) 255-84-44  (775) 265-85-43 (ffd) 254-34-23 (777)534-32-21"
    pattern = "[(]\d{3}[)] \d{3}[-]\d{2}[-]\d{2}"
    x = re.findall(pattern, text)
    print(x)

test3()