from PIL import Image,ImageColor
im=Image.open('sample.jpeg')
iml=im.load()
breadth,length=im.size
iml[3,4]=(1,2,3)
print(iml[3,4])