text= "HELLO"

text_bit = bytearray(text, encoding="utf-8")
for c in text_bit:
    print(c, end=" ")
