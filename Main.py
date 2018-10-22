import time
import random


#VARIABLES
  #user input

RangeMinUserInput = int(input("enter the minimum value as a integer: "))
RangeMaxUserInput = int(input("enter the maximum value as a integer: "))
MaximumInputAllowed = RangeMaxUserInput

MaximumInputAllowedRound = int(round(MaximumInputAllowed))

min = MaximumInputAllowedRound/2
max = MaximumInputAllowedRound/2

DataSetSize = RangeMaxUserInput 
CorrectRange = [RangeMinUserInput, RangeMaxUserInput]

l_min = MaximumInputAllowedRound/2
l_max = MaximumInputAllowedRound/2

  
#Creates an empty list that the "Create data" outputs its number to
DataList = []

#generate numbers inside user determined range which are then put in 'DataList'
for x in range(DataSetSize + 1):
   DataList.append(random.randint(RangeMinUserInput, RangeMaxUserInput))
   
   #lern
#for y in DataSetSize:
for x in range(DataSetSize):
    if DataList[x] > max:
        max = DataList[x]
    elif DataList[x] < min:
        min = DataList[x]
#training
for x in range(DataSetSize*10):
    if min < l_min:
        l_min -= 1
    if max > l_max:
        l_max += 1

#Output

print("numbers inside range: ", DataList  )
print("user Defined range:  ")  
print('')
print("____  ____  ____  ____  ____  ____  ____  ____  _____  ____  ____")
print('')
print("Learned min: ", l_min) 
print("learned Max: ", l_max)



