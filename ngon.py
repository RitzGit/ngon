#!/usr/bin/env python3

from PIL import Image, ImageDraw
import math

res = int(input("Resolution?\n"))

w = int(input("Width?\n"))

width = res
height = res
radius = int(res/2)

points = []

n = int(input("How many corners would you like?\n"))

g = input("\"gon\" or \"gram\"?\n")

im = Image.new('RGB', (width,height), (255,255,255))
draw = ImageDraw.Draw(im)

center = (width/2,height/2)

for i in range(n+1):
    x = center[0] + (radius * math.cos(2*math.pi * i/n))
    y = center[1] + (radius * math.sin(2*math.pi * i/n))
    points.append((x,y))

if g == "gon":  
    print("Calculating...")
    for i in range(len(points)-1):
        draw.line((points[i][0],points[i][1],points[i+1][0],points[i+1][1]), fill=(0,0,0), width =w)
    im.save(str(n) + "-gon.png", quality = 100)
if g == "gram":
    s = int(input("Stepsize?\n"))
    print("Calculating...")
    if s > 0 and n > 0 and s+1 < n:
        for p in points:
            if points.index(p) + s < n:
                draw.line((p[0],p[1],points[points.index(p)+s][0],points[points.index(p)+s][1]), fill=(0,0,0), width=w)
            else:
                draw.line((p[0],p[1],points[points.index(p)+s-n][0],points[points.index(p)+s-n][1]), fill=(0,0,0), width=w)
        im.save(str(n) + "-gram-" + str(s) + ".png", quality = 100)
    else:
        print("You did something wrong. Please try again.")
    

print("Finished!\nFile saved as "+ str(n) + "-gram-" + str(s) + ".png" )

input()