import pandas as pd
from scipy.spatial import KDTree
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb,
)

df = pd.read_csv('HI_6.csv')
print(df)

# NOTE: Need to -1 from the divisor when averaging IF light blue background or black is found

# split into 90 sections
i = 0
while i <= 49:
    j = 0
    while j <= 49:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r1_total = r1_total + int(str[0])
            g1_total = g1_total + int(str[1])
            b1_total = b1_total + int(str[2])
            j = j + 1
        
    while 50 <= j <= 99:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r4_total = r4_total + int(str[0])
            g4_total = g4_total + int(str[1])
            b4_total = b4_total + int(str[2])
            j = j + 1

    while 100 <= j <= 149:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r7_total = r7_total + int(str[0])
            g7_total = g7_total + int(str[1])
            b7_total = b7_total + int(str[2])
            j = j + 1
    i = i + 1

while 50 <= i <= 150:
    j = 0
    while j <= 49:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r2_total = r2_total + int(str[0])
            g2_total = g2_total + int(str[1])
            b2_total = b2_total + int(str[2])
            j = j + 1
        
    while 50 <= j <= 99:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r5_total = r5_total + int(str[0])
            g5_total = g5_total + int(str[1])
            b5_total = b5_total + int(str[2])
            j = j + 1

    while 100 <= j <= 149:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r8_total = r8_total + int(str[0])
            g8_total = g8_total + int(str[1])
            b8_total = b8_total + int(str[2])
            j = j + 1
    i = i + 1

while 100 <= i <= 149:
    j = 0
    while j <= 49:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r3_total = r3_total + int(str[0])
            g3_total = g3_total + int(str[1])
            b3_total = b3_total + int(str[2])
            j = j + 1
        
    while 50 <= j <= 99:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r6_total = r6_total + int(str[0])
            g6_total = g6_total + int(str[1])
            b6_total = b6_total + int(str[2])
            j = j + 1

    while 100 <= j <= 149:
        if df[i][j] != '(255,255,0)': # whatever number that light blue background is
            # parse
            str = df[i][j]
            str.replace("(", "")
            str.replace(")", "")
            str.split(',')
            r9_total = r9_total + int(str[0])
            g9_total = g9_total + int(str[1])
            b9_total = b9_total + int(str[2])
            j = j + 1
    i = i + 1    


r1_avg = r1_total/2500 
g1_avg = g1_total/2500 
b1_avg = b1_total/2500 

r2_avg = r2_total/2500 
g2_avg = g2_total/2500 
b2_avg = b2_total/2500 

r3_avg = r3_total/2500 
g3_avg = g3_total/2500 
b3_avg = b3_total/2500

r4_avg = r4_total/2500 
g4_avg = g4_total/2500 
b4_avg = b4_total/2500 

r5_avg = r5_total/2500 
g5_avg = g5_total/2500 
b5_avg = b5_total/2500 

r6_avg = r6_total/2500 
g6_avg = g6_total/2500 
b6_avg = b6_total/2500 

r7_avg = r7_total/2500 
g7_avg = g7_total/2500 
b7_avg = b7_total/2500 

r8_avg = r8_total/2500 
g8_avg = g8_total/2500 
b8_avg = b8_total/2500 

r9_avg = r9_total/2500 
g9_avg = g9_total/2500 
b9_avg = b9_total/2500 


s1_color = convert_rgb_to_name((r1_avg,g1_avg,b1_avg))
s2_color = convert_rgb_to_name((r2_avg,g2_avg,b2_avg))
s3_color = convert_rgb_to_name((r3_avg,g3_avg,b3_avg))
s4_color = convert_rgb_to_name((r4_avg,g4_avg,b4_avg))
s5_color = convert_rgb_to_name((r5_avg,g5_avg,b5_avg))
s6_color = convert_rgb_to_name((r6_avg,g6_avg,b6_avg))
s7_color = convert_rgb_to_name((r7_avg,g7_avg,b7_avg))
s8_color = convert_rgb_to_name((r8_avg,g8_avg,b8_avg))
s9_color = convert_rgb_to_name((r9_avg,g9_avg,b9_avg))

print(s1_color)
print(s2_color)
print(s3_color)
print(s4_color)
print(s5_color)
print(s6_color)
print(s7_color)
print(s8_color)
print(s9_color)


def convert_rgb_to_names(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return f'closest match: {names[index]}'