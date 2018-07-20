#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Michael (Wen) Jiang"

# matplotlib 	2.1.1
# pandas 		0.22.0
# scipy		    1.0.0

import matplotlib.pylab as plt
import pandas as pd
import scipy.stats as st

def readDP(dPath):

    data = pd.read_csv(dPath)

    # obtain the date and closing
    data1 = data.ix[:, ['date', 'close']]
    data2 = data1['date'].values.tolist()
    data3 = data1['close'].values.tolist()

    return data2, data3


def reverseDP(dList, pList):
    print(dList)
    print(pList)

    # initialize initial variables
    n = 0
    tempList = dList[0][:2]
    ascendingDList = []
    ascendingPList = []

    # check for the first occurrence and store
    while (n < len(dList)):
        if dList[n][:2] != tempList[:2]:
            tempList = dList[n][:2]
            ascendingDList.append(dList[n - 1])
            ascendingPList.append(pList[n - 1])
        n = n + 1

    ascendingDList = ascendingDList[:9][::-1]
    ascendingPList = ascendingPList[:9][::-1]

    return ascendingDList, ascendingPList

def exsmooth(val, alp):
    result = [val[0]]
    for n in range(1, len(val)):
        result.append(alp * val[n] + (1 - alp) * result[n - 1])
    return result


def satisfaction(ascendingDList, ascendingPList):

    while True:
        try:
            # Python 2.x should use raw_input. Python 3.x should use input
            like = int(input("\nAgain? 1 for Yes, 0 or non-one digit for No. \t"))

        # exception handling
        except:
            print("Please try again. Please enter using 0-9 keys only")
            continue
        if (like != 1):
            exsmoothMatplotlibGraph(ascendingDList, ascendingPList)
        break


def generateExpGraph(ourPList, value):
    # Friendly reminder on closing the graphical windows apart from the command-line interface if needed
    print("Close the plot windows if needed to continue")

    # for 1-starting x-axis index for a period of 9
    correct9 = (range(1, 10, 1))

    # matplotlib plotting
    plt.plot(correct9, ourPList, color='red', label="value")
    plt.plot(correct9, value, color='green', label="forecast")
    plt.xlabel('time period')
    plt.ylabel('value')
    plt.legend(loc='lower center')
    plt.title('ES')
    plt.show()

def exsmoothMatplotlibGraph(ourDList, ourPList):
    while True:
        try:
            # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
            alpha = float(input("0 to 1：\t"))
        except:
            print("Please try again. 0 to 1 only")
            # ask for input again
            continue
        if ((alpha <= 1 and alpha >= 0)):
            # stop if it's correct
            break

    values = exsmooth(ourPList, alpha)

    # for 1-starting x-axis index for a period of 9
    n = 1

    # data printing in command-line interface
    for items in values:
        print(ourDList[n - 1], ": No.", n, " predicted:", items)
        n = n + 1;

    #generate matplotlib graph
    generateExpGraph(ourPList, values)

def generateLGraph(correct9, ascendingPList, intercept, slope):
    # Reminder on closing the graphical windows apart if needed
    print("Close the plot windows if needed to continue")
    # matplotlib plotting
    plt.scatter(correct9, ascendingPList, correct9, c="r", alpha=0.5, marker='o',
                label="Predicted")
    plt.plot(correct9, intercept + slope * correct9, 'g', label='fitted line')
    plt.title('Scatter and LR Plot')
    plt.xlabel("Time Period")
    plt.ylabel("Time Value")
    plt.legend(loc=2)
    plt.show()


def lRMatplotlibGraph(ascendingPList):
    # for 1-starting x-axis index for a period of 9
    correct9 = (range(1, 10, 1))

    slope, intercept, r_value, p_value, std_err = st.linregress(correct9, ascendingPList)
    print("Slope:\t\t\t", slope, "\nIntercept:\t\t\t", intercept, "\nR_value:\t\t\t", r_value, "\nP_value:\t\t\t",
          p_value,
          "\nStd_err:\t\t\t",
          std_err)
    print("Correlation coefficient:\t", r_value)

    generateLGraph(correct9, ascendingPList, intercept, slope)

def fileInput():

    #tested file should contains at least date and close formats as once downloaded and specified in NASDAG

    while True:
        prompt = input("Please type in the path as specified in the submitted file and press 'Enter': ")
        try:
            path = open(prompt, 'r')
        except :
            print("Wrong file or no such file exist in the specified path")
        else:
            break
    return path

def main():

    path=fileInput()

    dList, pList = readDP(path)

    ascendingDList, ascendingPList = reverseDP(dList, pList)

    exsmoothMatplotlibGraph(ascendingDList, ascendingPList)

    satisfaction(ascendingDList, ascendingPList)

    lRMatplotlibGraph(ascendingPList)

if __name__ == "__main__":
    main()
