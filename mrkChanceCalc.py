import random

def main():
    markInput()

def markInput():
    mrk = int(input("Enter your mark: "))
    markChanceCalc(mrk)

def markChanceCalc(mark):
    rounds=100
    errorValue=3
    for i in range(rounds+1):
        tempHolder=random.randrange(0,101)
        if(tempHolder-errorValue>mark && tempHolder+errorValue<mark):
            




main()
