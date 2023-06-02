#HackerRank: https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math
def find_angle_MBC(BA, BC):
    AC = math.sqrt(BA **2 + BC **2)

    MC = AC / 2
    cos_B = (BC / 2) / (math.sqrt(BA **2 + BC ** 2) / 2)
    angle = int(round(math.acos(cos_B) * (180 / math.pi), 0))
    return angle       

a = int(input())  
b = int(input())                  
print('{}\N{DEGREE SIGN}'.format(find_angle_MBC(a, b))) 



