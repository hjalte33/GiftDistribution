""" This is a small program that distributes gifts for cristmas"""
import csv
import random
import sys
import getopt

def main(argv):
    """the main"""
    inputfile = 'names.csv'
    outputfile = 'solution.csv'
    seed = 0
    minCycleLength = 3
    try:
        opts, args = getopt.getopt(argv,"hi:o:s:c:",["ifile=","ofile=","seed=","minCycleLength"])
    except getopt.GetoptError:
        print ('GiftDistribution.py -i <inputfile> -o <outputfile> -s <seed value> -c <minCycleLength')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('GiftDistribution.py -i <inputfile> -o <outputfile> -s <seed value> -c <minCycleLength')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-s", "--seed"):
            seed = arg
        elif opt in ("-c", "--minCycleLength"):
            minCycleLength = int(arg)


    print ('Input file is "', inputfile)
    print ('Output file is "', outputfile)
    print ('seed is "', seed)  
    ran = random.Random(seed)


    with open('./%s' % inputfile , newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        giftGivers = []
        for _row in spamreader:

            # clean whitespace at the ends.
            row = [s.strip() for s in _row]

            if row:  #check if theres actually any content
                # look at for seed in the list.
                if row[0] == "seed":
                    try:
                        ran = random.Random(row[1])
                        seed = row[1]
                    except:
                        pass
                else:
                    giftGivers.append(row)

    participants = [row[0] for row in giftGivers]
    solution = []
    counter = 0
    cycleLength = 0
    while cycleLength < minCycleLength: # keep trying till we have long enough cycles
        solution = [] # reset the solution
        while len(solution) != len(participants): # keep trying till we get a valid solution
            counter += 1
            hasGift = []
            solution = []
            for giftGiver in giftGivers:
                posible = [person for person in participants if person not in giftGiver + hasGift]
                if posible:
                    chosen = ran.choice(posible)
                    hasGift.append(chosen)
                    solution.append([giftGiver[0],chosen])
                else:
                    pass 
        cycleLength = findCycleLength(solution,participants)

    print('Number of tries ',counter,'\n')
    print('smallest cycle length for this solution is ',cycleLength,'\n\n')
    print(solution)
    
    with open('./%s' % outputfile, 'w') as solutionFile:
        formatted=[]
        formatted.append('Number of tries %s \n' % counter)
        formatted.append('The seed used for this solution is %s \n' % seed)
        formatted.append('Smallest cycle length for this solution is %s \n\n' %cycleLength)
        for row in solution:
            formatted.append(row[0] + ' gives a gift to ' + row[1] +'\n')
        for row in formatted:
            solutionFile.write(row)


def findCycleLength(solution,participants):
    checkedIndex = []
    smallestCycle = len(solution) 
    cycleLength = 0
    index = 0
    while len(checkedIndex) != len(solution): #are we done?:     
        checkedIndex.append(index) # Note that we already checked this index.
        cycleLength += 1
        theNext = solution[index][1] # Who is the next person
        index = participants.index(theNext) #find the index of the next giftGiver # do it all again.   
        if index in checkedIndex: #see if the we already checkd this person
            if cycleLength < smallestCycle:
                smallestCycle = cycleLength # remember this cycle length
            alist = list(range(len(solution)))
            nextIndexes =  [item for item in alist if item not in checkedIndex] # get list of unchecked people
            if nextIndexes : # if there is more, check them. 
                cycleLength = 0 # reset the cycle counter
                index = nextIndexes[0] #select the next unchecked person on the list
                continue
            else: # we checked all
                break           
    return smallestCycle






if __name__ == "__main__":
   main(sys.argv[1:])

