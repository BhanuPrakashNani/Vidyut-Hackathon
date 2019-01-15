from PIL import Image
from pytesseract import image_to_string
import sys
import csv


s = image_to_string(Image.open("sample.jpeg"))
print (s)

l = s.strip().split("\n")
l = list(filter(None, l))


print(l)
i = l.index("Shipping Address:")
print(l[i+1])
a = l[i+1]
for i in l:
    if "Invoice Number:" in i:
        print(i[15:])
b = i[15:]
print(l[0])
c = l[0]
s =[a,b,c]
print(s)

