from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import math, os, random
size=1024
img=Image.new('RGBA',(size,size),(8,26,18,255))
d=ImageDraw.Draw(img)
# neon green dusk gradient
for y in range(size):
    t=y/size
    r=int(8*(1-t)+20*t)
    g=int(32*(1-t)+180*t)
    b=int(22*(1-t)+70*t)
    d.line([(0,y),(size,y)], fill=(r,g,b,255))
# radial glow center
cx,cy=size//2,int(size*0.42)
for rad in range(360,30,-7):
    a=max(0,190-(360-rad))
    d.ellipse((cx-rad,cy-rad,cx+rad,cy+rad), fill=(80,255,170,a))
# synthwave horizontal scan lines
for i in range(11):
    y=int(cy+22+i*22)
    d.rectangle((int(size*0.18),y,int(size*0.82),y+8), fill=(110,255,190,140))
# skyline silhouette
poly=[(0,int(size*0.72)),(70,int(size*0.64)),(130,int(size*0.69)),(200,int(size*0.59)),(270,int(size*0.67)),(340,int(size*0.57)),(410,int(size*0.66)),(500,int(size*0.56)),(585,int(size*0.64)),(670,int(size*0.58)),(760,int(size*0.68)),(835,int(size*0.61)),(910,int(size*0.7)),(1024,int(size*0.66)),(1024,1024),(0,1024)]
d.polygon(poly, fill=(10,18,14,240))
# palm silhouettes
for x in (170,840):
    d.line((x,int(size*0.5),x-6,930), fill=(12,22,16,255), width=16)
    for ang in (-70,-45,-20,15,40,65):
        ex=x+int(math.cos(math.radians(ang))*180)
        ey=int(size*0.5)+int(math.sin(math.radians(ang))*110)
        d.line((x,int(size*0.5),ex,ey), fill=(14,26,18,245), width=10)
# emblem card
pad=84
badge=(pad,int(size*0.64),size-pad,size-pad)
shadow=Image.new('RGBA',(size,size),(0,0,0,0))
sd=ImageDraw.Draw(shadow)
sd.rounded_rectangle((badge[0]+10,badge[1]+14,badge[2]+10,badge[3]+14), radius=74, fill=(0,0,0,170))
shadow=shadow.filter(ImageFilter.GaussianBlur(10))
img.alpha_composite(shadow)
d.rounded_rectangle(badge, radius=74, fill=(10,34,22,238), outline=(130,255,200,240), width=10)
# typography
font_paths=[r'C:\Windows\Fonts\arialbd.ttf', r'C:\Windows\Fonts\segoeuib.ttf']
font=None
for p in font_paths:
    if os.path.exists(p):
        font=ImageFont.truetype(p,246)
        break
if font is None:
    font=ImageFont.load_default()
text='NL'
bb=d.textbbox((0,0),text,font=font)
tw,th=bb[2]-bb[0],bb[3]-bb[1]
tx=(size-tw)//2
ty=int(size*0.69)-th//2
for off,col in [((-9,9),(6,22,14,230)),((0,0),(180,255,220,255)),((0,7),(30,220,140,255))]:
    d.text((tx+off[0],ty+off[1]),text,font=font,fill=col)
# accent bar
bar=(int(size*0.23),int(size*0.86),int(size*0.77),int(size*0.92))
d.rounded_rectangle(bar,radius=22,fill=(70,255,170,225))
subf=ImageFont.truetype(font_paths[0],54) if os.path.exists(font_paths[0]) else ImageFont.load_default()
sub='NocLauncher'
sb=d.textbbox((0,0),sub,font=subf)
d.text(((size-(sb[2]-sb[0]))//2,int(size*0.867)),sub,font=subf,fill=(8,30,18,255))
# grain + vignette
pix=img.load()
for _ in range(22000):
    x=random.randrange(size); y=random.randrange(size)
    r,g,b,a=pix[x,y]
    n=random.randint(-14,14)
    pix[x,y]=(max(0,min(255,r+n)),max(0,min(255,g+n)),max(0,min(255,b+n)),a)
# vignette
vig=Image.new('L',(size,size),0)
vd=ImageDraw.Draw(vig)
for r in range(size//2,0,-6):
    a=int(max(0, 180*(1-r/(size/2))))
    vd.ellipse((size//2-r,size//2-r,size//2+r,size//2+r), outline=a, width=8)
img.putalpha(ImageChops.subtract(img.split()[-1], vig.point(lambda p: p//5)))
out_png=r'C:\Users\kiril\Desktop\noc1\assets\icon.png'
out_ico=r'C:\Users\kiril\Desktop\noc1\assets\icon.ico'
img.save(out_png,'PNG')
img.save(out_ico,format='ICO',sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(24,24),(16,16)])
print('saved')

