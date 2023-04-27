import pandas as pd
import math

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



def getPercentages(csv):
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
                    color = closestColor(int(str2[0]), int(str2[1]), int(str2[2]))
                    if color == 'Red':
                        b1Red = b1Red + 1
                        # print("BD1: red" )
                    if color == 'Blue':
                        b1Blue = b1Blue + 1
                        # print("BD1: blue" )
                    if color == 'Green':
                        b1Green = b1Green + 1
                        # print("BD1: green" )
            for x in boundaryTwo:
                # print(str(x))
                if cell == x:
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    color = closestColor(int(str2[0]), int(str2[1]), int(str2[2]))
                    if color == 'Red':
                        b2Red = b2Red + 1
                        # print("BD2: red" )
                    if color == 'Blue':
                        b2Blue = b2Blue + 1
                        # print("BD2: blue" )
                    if color == 'Green':
                        b2Green = b2Green + 1
                        # print("BD2: green" )
            for x in boundaryThree:
                # print(str(x))
                if cell == x:
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    color = closestColor(int(str2[0]), int(str2[1]), int(str2[2]))
                    if color == 'Red':
                        b3Red = b3Red + 1
                        # print("BD3: red" )
                    if color == 'Blue':
                        b3Blue = b3Blue + 1
                        # print("BD3: blue" )
                    if color == 'Green':
                        b3Green = b3Green + 1
                        # print("BD3: gree" )
            for x in boundaryFour:
                # print(str(x))
                if cell == x:
                    str1 = csv.iloc[i,j].replace('[', '')
                    str1 = str1.replace(']', '')
                    str1 = str1.strip()
                    # print(str1)
                    str2 = str1.split()
                    color = closestColor(int(str2[0]), int(str2[1]), int(str2[2]))
                    if color == 'Red':
                        b4Red = b4Red + 1
                        # print("BD4: red" )
                    if color == 'Blue':
                        b4Blue = b4Blue + 1
                        # print("BD4: blue" )
                    if color == 'Green':
                        b4Green = b4Green + 1
                        # print("BD4: green" )
            j = j + 1
        i = i + 1
    # print("B1: " + str(b1Red) + " " + str(b1Green) + " " + str(b1Blue) )
    # print("B2: " + str(b2Red) + " " + str(b2Green) + " " + str(b2Blue) )
    # print("B3: " + str(b3Red) + " " + str(b3Green) + " " + str(b3Blue) )
    # print("B4: " + str(b4Red) + " " + str(b4Green) + " " + str(b4Blue) )

    b1Red = b1Red / len(boundaryOne)
    b1Green = b1Green / len(boundaryOne)
    b1Blue = b1Blue / len(boundaryOne)
    b2Red = b2Red / len(boundaryTwo)
    b2Green = b2Green / len(boundaryTwo)
    b2Blue = b2Blue / len(boundaryTwo)
    b3Red = b3Red / len(boundaryThree)
    b3Green = b3Green / len(boundaryThree)
    b3Blue = b3Blue / len(boundaryThree)
    b4Red = b4Red / len(boundaryFour)
    b4Green = b4Green / len(boundaryFour)
    b4Blue = b4Blue / len(boundaryFour)
    return b1Red, b1Green, b1Blue, b2Red, b2Green, b2Blue, b3Red, b3Green, b3Blue, b4Red, b4Green, b4Blue


def printToCsv(lst):
    with open("dataset2To25.csv", 'w') as f:
        for row in lst:
            f.write(','.join(row) + '\n')











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
# PercegetPercentages those cells, and estimate the color
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
        if int(str2[0]) > 30: 
            if df.iloc[i][j] == '[ 78 172  91 255]':
                cell = '[' + str(i) + ',' + str(j) + ']'
                boundaryOne.append(cell)
            if df.iloc[i][j] == '[ 45 112 186 255]':
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
    # print(str(len(boundaryFour)))
files = ["S1_2", "S1_4", "S1_6","S1_8", "S1_10", "S1_12","S1_14", "S1_16", "S1_18", "S1_20", "S1_22",
         "S1_3", "S1_5", "S1_7","S1_9", "S1_11", "S1_13","S1_15", "S1_17", "S1_19", "S1_21", "S1_23", "S1_24", "S1_25",
         "S2_2", "S2_4", "S2_6","S2_8", "S2_10", "S2_12","S2_14", "S2_16", "S2_18", "S2_20", "S2_22",
         "S2_3", "S2_5", "S2_7","S2_9", "S2_11", "S2_13","S2_15", "S2_17", "S2_19", "S2_21", "S2_23", "S2_24", "S2_25",
         "S3_2", "S3_4", "S3_6","S3_8", "S3_10", "S3_12","S3_14", "S3_16", "S3_18", "S3_20", "S3_22",
         "S3_3", "S3_5", "S3_7","S3_9", "S3_11", "S3_13","S3_15", "S3_17", "S3_19", "S3_21", "S3_23", "S3_24", "S3_25",
         "S4_2", "S4_4", "S4_6","S4_8", "S4_10", "S4_12","S4_14", "S4_16", "S4_18", "S4_20", "S4_22",
         "S4_3", "S4_5", "S4_7","S4_9", "S4_11", "S4_13","S4_15", "S4_17", "S4_19", "S4_21", "S4_23", "S4_24", "S4_25",
         "S5_2", "S5_4", "S5_6","S5_8", "S5_10", "S5_12","S5_14", "S5_16", "S5_18", "S5_20", "S5_22",
         "S5_3", "S5_5", "S5_7","S5_9", "S5_11", "S5_13","S5_15", "S5_17", "S5_19", "S5_21", "S5_23", "S5_24", "S5_25",
         "S7_2", "S7_4", "S7_6","S7_8", "S7_10", "S7_12","S7_14", "S7_16", "S7_18", "S7_20", "S7_22",
         "S7_3", "S7_5", "S7_7","S7_9", "S7_11", "S7_13","S7_15", "S7_17", "S7_19", "S7_21", "S7_23", "S7_24", "S7_25",
         "S9_2", "S9_4", "S9_6","S9_8", "S9_10", "S9_12","S9_14", "S9_16", "S9_18", "S9_20", "S9_22",
         "S9_3", "S9_5", "S9_7","S9_9", "S9_11", "S9_13","S9_15", "S9_17", "S9_19", "S9_21", "S9_23", "S9_24", "S9_25",
         "S10_2", "S10_4", "S10_6","S10_8", "S10_10", "S10_12","S10_14", "S10_16", "S10_18", "S10_20", "S10_22",
         "S10_3", "S10_5", "S10_7","S10_9", "S10_11", "S10_13","S10_15", "S10_17", "S10_19", "S10_21", "S10_23", "S10_24", "S10_25",
         "S11_2", "S11_4", "S11_6","S11_8", "S11_10", "S11_12","S11_14", "S11_16", "S11_18", "S11_20", "S11_22",
         "S11_3", "S11_5", "S11_7","S11_9", "S11_11", "S11_13","S11_15", "S11_17", "S11_19", "S11_21", "S11_23", "S11_24", "S11_25",
        #  "S15_2", "S15_4", "S15_6","S15_8", "S15_10", "S15_12","S15_14", "S15_16", "S15_18", "S15_20", "S15_22",
        #  "S15_3", "S15_5", "S15_7","S15_9", "S15_11", "S15_13","S15_15", "S15_17", "S15_19", "S15_21", "S15_23", "S15_24", "S15_25",
         "S17_2", "S17_4", "S17_6","S17_8", "S17_10", "S17_12","S17_14", "S17_16", "S17_18", "S17_20", "S17_22",
         "S17_3", "S17_5", "S17_7","S17_9", "S17_11", "S17_13","S17_15", "S17_17", "S17_19", "S17_21", "S17_23", "S17_24", "S17_25",
         "S18_2", "S18_4", "S18_6","S18_8", "S18_10", "S18_12","S18_14", "S18_16", "S18_18", "S18_20", "S18_22",
         "S18_3", "S18_5", "S18_7","S18_9", "S18_11", "S18_13","S18_15", "S18_17", "S18_19", "S18_21", "S18_23", "S18_24", "S18_25",
         "S21_2", "S21_4", "S21_6","S21_8", "S21_10", "S21_12","S21_14", "S21_16", "S21_18", "S21_20", "S21_22",
         "S21_3", "S21_5", "S21_7","S21_9", "S21_11", "S21_13","S21_15", "S21_17", "S21_19", "S21_21", "S21_23", "S21_24", "S21_25",
         "S23_2", "S23_4", "S23_6","S23_8", "S23_10", "S23_12","S23_14", "S23_16", "S23_18", "S23_20", "S23_22",
         "S23_3", "S23_5", "S23_7","S23_9", "S23_11", "S23_13","S23_15", "S23_17", "S23_19", "S23_21", "S23_23", "S23_24", "S23_25",
         "S25_2", "S25_4", "S25_6","S25_8", "S25_10", "S25_12","S25_14", "S25_16", "S25_18", "S25_20", "S25_22",
         "S25_3", "S25_5", "S25_7","S25_9", "S25_11", "S25_13","S25_15", "S25_17", "S25_19", "S25_21", "S25_23", "S25_24", "S25_25",
         "S26_2", "S26_4", "S26_6","S26_8", "S26_10", "S26_12","S26_14", "S26_16", "S26_18", "S26_20", "S26_22",
         "S26_3", "S26_5", "S26_7","S26_9", "S26_11", "S26_13","S26_15", "S26_17", "S26_19", "S26_21", "S26_23", "S26_24", "S26_25",
         "S28_2", "S28_4", "S28_6","S28_8", "S28_10", "S28_12","S28_14", "S28_16", "S28_18", "S28_20", "S28_22",
         "S28_3", "S28_5", "S28_7","S28_9", "S28_11", "S28_13","S28_15", "S28_17", "S28_19", "S28_21", "S28_23", "S28_24", "S28_25",
         "S30_2", "S30_4", "S30_6","S30_8", "S30_10", "S30_12","S30_14", "S30_16", "S30_18", "S30_20", "S30_22",
         "S30_3", "S30_5", "S30_7","S30_9", "S30_11", "S30_13","S30_15", "S30_17", "S30_19", "S30_21", "S30_23", "S30_24", "S30_25",
         "S31_2", "S31_4", "S31_6","S31_8", "S31_10", "S31_12","S31_14", "S31_16", "S31_18", "S31_20", "S31_22",
         "S31_3", "S31_5", "S31_7","S31_9", "S31_11", "S31_13","S31_15", "S31_17", "S31_19", "S31_21", "S31_23", "S31_24", "S31_25",
         "S34_2", "S34_4", "S34_6","S34_8", "S34_10", "S34_12","S34_14", "S34_16", "S34_18", "S34_20", "S34_22",
         "S34_3", "S34_5", "S34_7","S34_9", "S34_11", "S34_13","S34_15", "S34_17", "S34_19", "S34_21", "S34_23", "S34_24", "S34_25",
        #  "S35_2", "S35_4", "S35_6","S35_8", "S35_10", "S35_12","S35_14", "S35_16", "S35_18", "S35_20", "S35_22",
        #  "S35_3", "S35_5", "S35_7","S35_9", "S35_11", "S35_13","S35_15", "S35_17", "S35_19", "S35_21", "S35_23", "S35_24", "S35_25",
         "S36_2", "S36_4", "S36_6","S36_8", "S36_10", "S36_12","S36_14", "S36_16", "S36_18", "S36_20", "S36_22",
         "S36_3", "S36_5", "S36_7","S36_9", "S36_11", "S36_13","S36_15", "S36_17", "S36_19", "S36_21", "S36_23", "S36_24", "S36_25",
         "S40_2", "S40_4", "S40_6","S40_8", "S40_10", "S40_12","S40_14", "S40_16", "S40_18", "S40_20", "S40_22",
         "S40_3", "S40_5", "S40_7","S40_9", "S40_11", "S40_13","S40_15", "S40_17", "S40_19", "S40_21", "S40_23", "S40_24", "S40_25",
         "S41_2", "S41_4", "S41_6","S41_8", "S41_10", "S41_12","S41_14", "S41_16", "S41_18", "S41_20", "S41_22",
         "S41_3", "S41_5", "S41_7","S41_9", "S41_11", "S41_13","S41_15", "S41_17", "S41_19", "S41_21", "S41_23", "S41_24", "S41_25",
         "S43_2", "S43_4", "S43_6","S43_8", "S43_10", "S43_12","S43_14", "S43_16", "S43_18", "S43_20", "S43_22",
         "S43_3", "S43_5", "S43_7","S43_9", "S43_11", "S43_13","S43_15", "S43_17", "S43_19", "S43_21", "S43_23", "S43_24", "S43_25"]
lst = [["Sub_Hz", "B1_red","B1_green","B1_blue","B2_red","B2_green", "B2_blue", "B3_red", "B3_green", "B3_blue", "B4_red", "B4_green", "B4_blue"]]
for x in files:
    tmp = []
    cfile = "new1/" + x + '.csv'
    csvRead = pd.read_csv(cfile)
    print("\n" + x)
    b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(csvRead)
    tmp.append(str(x))
    tmp.append(str(b1r))
    tmp.append(str(b1g))
    tmp.append(str(b1b))
    tmp.append(str(b2r))
    tmp.append(str(b2g))
    tmp.append(str(b2b))
    tmp.append(str(b3r))
    tmp.append(str(b3g))
    tmp.append(str(b3b))
    tmp.append(str(b4r))
    tmp.append(str(b4g))
    tmp.append(str(b4b))
    lst.append(tmp)
    print ('B1 : Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
    print ('B2 : Middle: ' + str(b2r), str(b2g), str(b2b))
    print ('B3 : Inner: ' + str(b3r), str(b3g), str(b3b))
    print ('B4 : Top Outer: ' + str(b4r), str(b4g), str(b4b))

printToCsv(lst)

# NI6 = pd.read_csv('NI_6.csv')
# NI10 = pd.read_csv('NI_10.csv')
# NI22 = pd.read_csv('NI_22.csv')
# HI6 = pd.read_csv('HI_6.csv')
# HI10 = pd.read_csv('HI_10.csv')
# HI22 = pd.read_csv('HI_22.csv')

   

# # print('\nNI_6')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(NI6)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
# print('\nNI_10')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(NI10)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
# print('\nNI_22')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(NI22)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
# print('\nHI_6')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(HI6)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
# print('\nHI_10')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(HI10)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
# print('\nHI_22')
# b1r, b1g, b1b, b2r, b2g, b2b, b3r, b3g, b3b, b4r, b4g, b4b = getPercentages(HI22)
# print ('Bottom Outer: ' + str(b1r), str(b1g), str(b1b))
# # print ('\tClosest color: '+ closestColor(b1r, b1g, b1b))
# print ('Middle: ' + str(b2r), str(b2g), str(b2b))
# # print ('\tClosest color: '+ closestColor(b2r, b2g, b2b))
# print ('Inner: ' + str(b3r), str(b3g), str(b3b))
# # print ('\tClosest color: '+ closestColor(b3r, b3g, b3b))
# print ('Top Outer: ' + str(b4r), str(b4g), str(b4b))
# # print ('\tClosest color: '+ closestColor(b4r, b4g, b4b))
