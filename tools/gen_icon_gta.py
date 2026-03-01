from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, os, random
size=1024
img=Image.new('RGBA',(size,size),(20,16,28,255))
d=ImageDraw.Draw(img)
for y in range(size):
    t=y/size
    r=int(28*(1-t)+255*t*0.55)
    g=int(20*(1-t)+80*t*0.45)
    b=int(45*(1-t)+130*t*0.55)
    d.line([(0,y),(size,y)], fill=(r,g,b,255))
cx,cy=size//2,int(size*0.42)
for rad in range(340,40,-8):
    a=max(0,190-(340-rad))
    d.ellipse((cx-rad,cy-rad,cx+rad,cy+rad), fill=(255,120+rad%80,140,a))
for i in range(9):
    y=int(cy+30+i*24)
    d.rectangle((int(size*0.2),y,int(size*0.8),y+10), fill=(255,120,170,150))
poly=[(0,int(size*0.72)),(60,int(size*0.66)),(120,int(size*0.69)),(170,int(size*0.62)),(240,int(size*0.68)),(310,int(size*0.6)),(380,int(size*0.67)),(460,int(size*0.58)),(540,int(size*0.66)),(620,int(size*0.59)),(700,int(size*0.67)),(790,int(size*0.61)),(860,int(size*0.7)),(930,int(size*0.64)),(1024,int(size*0.69)),(1024,1024),(0,1024)]
d.polygon(poly, fill=(18,16,24,235))
for x in (170,820):
    d.line((x,int(size*0.5),x-8,920), fill=(26,22,30,255), width=16)
    for ang in (-70,-45,-20,15,40,65):
        ex=x+int(math.cos(math.radians(ang))*180)
        ey=int(size*0.5)+int(math.sin(math.radians(ang))*110)
        d.line((x,int(size*0.5),ex,ey), fill=(26,22,30,240), width=10)
pad=90
badge=(pad,int(size*0.64),size-pad,size-pad)
shadow=Image.new('RGBA',(size,size),(0,0,0,0))
sd=ImageDraw.Draw(shadow)
sd.rounded_rectangle((badge[0]+8,badge[1]+14,badge[2]+8,badge[3]+14), radius=70, fill=(0,0,0,170))
shadow=shadow.filter(ImageFilter.GaussianBlur(8))
img.alpha_composite(shadow)
d.rounded_rectangle(badge, radius=70, fill=(28,22,34,240), outline=(255,140,200,220), width=10)
font_paths=[r'C:\Windows\Fonts\arialbd.ttf', r'C:\Windows\Fonts\segoeuib.ttf']
font=None
for p in font_paths:
    if os.path.exists(p):
        font=ImageFont.truetype(p,240)
        break
if font is None:
    font=ImageFont.load_default()
text='NL'
bb=d.textbbox((0,0),text,font=font)
tw,th=bb[2]-bb[0],bb[3]-bb[1]
tx=(size-tw)//2
ty=int(size*0.69)-th//2
for off,col in [((-8,8),(20,10,25,230)),((0,0),(255,180,230,255)),((0,6),(255,90,170,255))]:
    d.text((tx+off[0],ty+off[1]),text,font=font,fill=col)
bar=(int(size*0.26),int(size*0.86),int(size*0.74),int(size*0.92))
d.rounded_rectangle(bar,radius=20,fill=(255,95,160,220))
subf=ImageFont.truetype(font_paths[0],56) if os.path.exists(font_paths[0]) else ImageFont.load_default()
sub='NocLauncher'
sb=d.textbbox((0,0),sub,font=subf)
d.text(((size-(sb[2]-sb[0]))//2,int(size*0.867)),sub,font=subf,fill=(35,20,40,255))
pix=img.load()
for _ in range(18000):
    x=random.randrange(size);y=random.randrange(size)
    r,g,b,a=pix[x,y]
    n=random.randint(-12,12)
    pix[x,y]=(max(0,min(255,r+n)),max(0,min(255,g+n)),max(0,min(255,b+n)),a)
out_png=r'C:\Users\kiril\Desktop\noc1\assets\icon.png'
out_ico=r'C:\Users\kiril\Desktop\noc1\assets\icon.ico'
img.save(out_png,'PNG')
img.save(out_ico,format='ICO',sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(24,24),(16,16)])
print('saved')
