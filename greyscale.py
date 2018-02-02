from PIL import Image,ImageColor
class Greyconvert:
    temp=0
    def convert(self,rawcaptcha):  
        try:
            #rawcaptcha='CAPTCHA - 0.jpeg'
            im=Image.open(rawcaptcha)
            im1=im.load()
            breadth,length=im.size
            rgb=im.convert('RGB')
            for i in range(0,breadth):
                for j in range(0,length):
                    r,g,b=rgb.getpixel((i,j))
                    new_r=r*0.299
                    new_g=g*0.587
                    new_b=b*0.114
                    temp=(new_r+new_g+new_b)
                    if(int(temp)>=200):
                        temp=255
                    elif(int(temp)<=50):
                        temp=0
                    im.putpixel((i,j), int(temp))          
            newimage=im.copy()
            newimage.show()
            return newimage
        except IOError:
            print(IOError)
arg=input()
obj=Greyconvert()
obj.convert(arg)