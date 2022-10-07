import random

b=4/6 #chance of B surviving (default 4/6)
a=3/6 #chance of A surviving (default 3/6)

def dual():
    al,bl=True,True #make both A and B alive

    """
    test
    #getting simulation probabilities
    for x in range (-1,-100,-1):
        if(isnumeric(a[x])):
            aden=a[x] #A denominator
        else:
            break
    for x in range (1,100):
        if(isnumeric(a[x])):
            anem=a[x] #A nemorator
        else:
            break
    #calculating precentage for A surviving
    apre=
    #waste of time and code becuase forgot basic maths
    #Then learn some basic maths
    """

    #calculating probabilities as a precentages
    apre=a*100
    bpre=b*100

    #simulating the dual
    while(al==True & bl==True):
        #A shooting
        i=random.randrange(1,101)
        if(i>bpre):
            bl=False #B got shot
        else:
            j=random.randrange(1,101)
            if(j>apre):
                al=False #A got shot

        #Annoucing results
        if(al==True & bl==True):
            print("Match draw, Both Alive")
        elif(al==True):
            print("A won")
            return 1
        else:
            print("B won")
            return 2

def multirun():
    bw,aw=0,0
    rt=int(input("Times to run the simulation: ")) #run times
    for ic in range (0,rt):
        rn = dual()
        if (rn==1):
            aw=aw+1
        elif(rn==2):
            bw=bw+1
    print("Out of "+str(rt)+" Rounds A won "+str(aw)+" Times and B won "+str(bw)+" Times")
    awp=(aw/rt)*100
    bwp=(bw/rt)*100
    print("A's win rate is "+str(awp)+"% and B's win rate is "+str(bwp)+"%")

def main():
    multirun()

if __name__== "__main__":
    main()
