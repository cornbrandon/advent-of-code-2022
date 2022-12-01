import argparse

parser = argparse.ArgumentParser(description='Process elves file')
parser.add_argument('inputFile')

args = parser.parse_args()

with open(args.inputFile) as file:
    elfSum = 0
    sumList = []
    for line in file:
        try:
            elfSum += int(line)
        except:
            sumList.append(elfSum)
            elfSum = 0
            
    #if we aren't at 0 we have a leftover value
    if elfSum != 0:
        sumList.append(elfSum)
        
    sumList.sort(reverse=True)
    print(f"Top 3: {sum(sumList[:3])}")
    print(f"Max:{max(sumList)}")
