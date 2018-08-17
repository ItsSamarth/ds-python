import math
ab,bc = float(input()) , float(input())

#calculate hypotenus
hype = math.hypot(ab,bc)

#calculate required angle
angle = round(math.degrees(math.acos(bc/hype)))

#degree symbol
degree = chr(176)

print(angle,degree, sep='')
