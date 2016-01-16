import os
import sys
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import random
import linecache


lengthOfArg = len(sys.argv) #Number of arguments entered

#Create a legend holding up to 10 keys
blue_patch = mpatches.Patch(color='b', label='Graph 1')
green_patch = mpatches.Patch(color='g', label='Graph 2')
red_patch = mpatches.Patch(color='r', label='Graph 3')
cyan_patch = mpatches.Patch(color='c', label='Graph 4')
magenta_patch = mpatches.Patch(color='m', label='Graph 5')
yellow_patch = mpatches.Patch(color='y', label='Graph 6')
black_patch = mpatches.Patch(color='k', label='Graph 7')
darkRed_patch = mpatches.Patch(color = '#b30000', label = 'Graph 8')
darkBlue_patch = mpatches.Patch(color = '#262673', label='Graph 9')
darkGreen_patch = mpatches.Patch(color='#006622', label='Graph 10')



#Counters to loop through each graph entered in command line
fileCounter = 0
listIndex = 0
textFilesList = []
x=0
lineByLineIndex =0

while fileCounter< lengthOfArg - 1:  #Graph each graph to .plt for each iteration
    xVector = [] #Store x values (first column)
    yVector = [] #Store Y values (second column)
    fileCounter +=1
    with open(sys.argv[fileCounter]) as f:
        next(f)
        if sys.argv[fileCounter] == "POTbc20-Cl7BsubPc60-Aug232015-R.Sample.csv": #Uncomment this code with the name of a file that needs to ignore the first two rows
            next(f)
        for line in f:
            yMax = 0
            maxYVal = 0
            currentLine = line.split(",")
            xVector.append(currentLine[0])
            yVector.append(currentLine[1])
           
             
            if fileCounter == 1:
                plt.plot( xVector, yVector, 'b')
                plt.legend(handles=[blue_patch])
            if fileCounter == 2:
                plt.plot( xVector, yVector, 'g')
                plt.legend(handles=[blue_patch, green_patch])
            if fileCounter == 3:
                plt.plot( xVector, yVector, 'r')
                plt.legend(handles=[blue_patch, green_patch,red_patch])
            if fileCounter == 4:
                plt.plot( xVector, yVector, 'c')
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch])
            if fileCounter == 5:
                plt.plot( xVector, yVector, 'm')
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch])
            if fileCounter == 6:
                plt.plot( xVector, yVector, 'y')
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch,yellow_patch])
            if fileCounter == 7:
                plt.plot( xVector, yVector, 'k')
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch,yellow_patch,black_patch])
            if fileCounter == 8:
                plt.plot( xVector, yVector, '#b30000') #dark red
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch,yellow_patch,black_patch,darkRed_patch])
            if fileCounter == 9:
                plt.plot( xVector, yVector, '#262673') #dark blue
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch,yellow_patch,black_patch,darkRed_patch,darkBlue_patch])
            if fileCounter == 10:
                plt.plot( xVector, yVector, '#006622') #dark green
                plt.legend(handles=[blue_patch, green_patch,red_patch,cyan_patch,magenta_patch,yellow_patch,black_patch,darkRed_patch,darkBlue_patch,darkGreen_patch])
            


plt.ylabel('A')
plt.xlabel('nm')
plt.show()

      
           
        
    


