import pandas as pd
import math
# from numpy import genfromtxt
# df = genfromtxt('overlapped.csv', delimiter=',')

def distance(br, bg, bb, colorr, colorg, colorb):
    return math.sqrt((colorr-br)**2 + (colorg-bg)**2 + (colorb-bb)**2)

def closestColor(br, bg, bb):
    # Blue, red, green, orange, yellow
    blueDist = distance(br,bg, bb, 0, 0, 255)
    redDist = distance(br,bg, bb, 255, 0, 0)
    greenDist = distance(br,bg, bb, 0, 255, 0)
    # orangeDist = distance(br,bg, bb, 255, 165, 0)
    # yellowDist = distance(br,bg, bb, 255, 255, 0)
    # listDist = [blueDist, redDist, greenDist, orangeDist, yellowDist]
    listDist = [blueDist, redDist, greenDist]

    minValue = min(listDist)
    minIndex = listDist.index(minValue)
    match(minIndex):
        case 0:
            return 'Blue'
        case 1:
            return 'Red'
        case 2:
            return 'Green'
        # case 3:
        #     return 'Orange'
        # case 4:
        #     return 'Yellow'

df = pd.read_csv('boundaries.csv')
# print(df)
boundaryOne = []
boundaryTwo = []
boundaryThree = []
boundaryFour = []

# list all boundaries

# boundary 1 is outer bottom
# boundary 2 is mid
# boundary 3 is inner
# boundary 1 is outer top

#once we get those boundaries, get the cells in between the boundaries, 
# avg those cells, and estimate the color
i = 0
df = df.applymap(str)
while i < 199:
    j = 0
    while j < 199:
        # print(df.iloc[i][j])
        str3 = df.iloc[i][j].replace('[', '')
        str3 = str3.replace(']', '')
        str3 = str3.strip()
        str2 = str3.split()
        if df.iloc[i][j] != '[255 255 255 255]': 
            if df.iloc[i][j] == '[126 170  85 255]':
                cell = '[' + str(i) + ',' + str(j) + ']'
                boundaryOne.append(cell)
            if df.iloc[i][j] == '[ 77 114 190 255]':
                cell = '[' + str(i) + ',' + str(j) + ']'
                boundaryTwo.append(cell)
                # np.append(boundaryOne, np.array([[i, j]]), axis=0)
                # print(boundaryOne)
                # print('['+str(i)+','+str(j)+']')
            if df.iloc[i][j] == '[104  55 154 255]':
                cell = '[' + str(i) + ',' + str(j) + ']'
                boundaryThree.append(cell)
                # np.append(boundaryTwo, np.array([[i, j]]), axis=0)
                # print('['+str(i)+','+str(j)+']')
            if df.iloc[i][j] == '[235  51  35 255]':
                cell = '[' + str(i) + ',' + str(j) + ']'
                boundaryFour.append(cell)
        j = j + 1
    i = i + 1



NI6 = pd.read_csv('NI_6.csv')
NI10 = pd.read_csv('NI_10.csv')
NI22 = pd.read_csv('NI_22.csv')
HI6 = pd.read_csv('HI_6.csv')
HI10 = pd.read_csv('HI_10.csv')
HI22 = pd.read_csv('HI_22.csv')

# for x in boundaryOne:
#     print(x)

# print(boundaryOne.size)
def getAvg(csv):
    csv = csv.applymap(str)
    # print(len(boundaryOne))
    b1Red = 0
    b1Green = 0
    b1Blue = 0
    b2Red = 0
    b2Green = 0
    b2Blue = 0
    b3Red = 0
    b3Green = 0
    b3Blue = 0
    b4Red = 0
    b4Green = 0
    b4Blue = 0
    i = 0
    while i < 199:
        j = 0
        while j < 199:
            cell = '[' + str(i) + ',' + str(j) + ']'
            for x in boundaryOne:
                # print(str(x))
                if cell == x:
                    
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    # print(str2[0] +"here" + str2[1]+"here"+ str2[2]+"here")
                    b1Red = b1Red + int(str2[0])
                    b1Green = b1Green + int(str2[1])
                    b1Blue = b1Blue + int(str2[2])
            for x in boundaryTwo:
                # print(str(x))
                if cell == x:
                    
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    # print(str2[0] +"here" + str2[1]+"here"+ str2[2]+"here")
                    b2Red = b2Red + int(str2[0])
                    b2Green = b2Green + int(str2[1])
                    b2Blue = b2Blue + int(str2[2])
            for x in boundaryThree:
                # print(str(x))
                if cell == x:
                    
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    # print(str2[0] +"here" + str2[1]+"here"+ str2[2]+"here")
                    b3Red = b3Red + int(str2[0])
                    b3Green = b3Green + int(str2[1])
                    b3Blue = b3Blue + int(str2[2])
            for x in boundaryFour:
                # print(str(x))
                if cell == x:
                    
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    # print(str2[0] +"here" + str2[1]+"here"+ str2[2]+"here")
                    b4Red = b4Red + int(str2[0])
                    b4Green = b4Green + int(str2[1])
                    b4Blue = b4Blue + int(str2[2])
            j = j + 1
        i = i + 1
    # b1Red = b1Red / len(boundaryOne)
    # b1Green = b1Green / len(boundaryOne)
    # b1Blue = b1Blue / len(boundaryOne)
    # b2Red = b2Red / len(boundaryTwo)
    # b2Green = b2Green / len(boundaryTwo)
    # b2Blue = b2Blue / len(boundaryTwo)
    # b3Red = b3Red / len(boundaryThree)
    # b3Green = b3Green / len(boundaryThree)
    # b3Blue = b3Blue / len(boundaryThree)
    # b4Red = b4Red / len(boundaryFour)
    # b4Green = b4Green / len(boundaryFour)
    # b4Blue = b4Blue / len(boundaryFour)
    return int(b1Red), int(b1Green), int(b1Blue), int(b2Red), int(b2Green), int(b2Blue), int(b3Red), int(b3Green), int(b3Blue), int(b4Red), int(b4Green), int(b4Blue)



print('\nNI_6')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(NI6)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
print('\nNI_10')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(NI10)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
print('\nNI_22')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(NI22)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
print('\nHI_6')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(HI6)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
print('\nHI_10')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(HI10)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
print('\nHI_22')
b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getAvg(HI22)
print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
print ('Middle: ' + str(b2r), str(b2g), str(b2b))
print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
print ('Inner: ' + str(b3r), str(b3g), str(b3b))
print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))


