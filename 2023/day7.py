import os
import sys
from math import floor, ceil




def bubblesort(elements):
    swapped = False
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            j = 0
            while True:
                element0 = 0
                element1 = 0
                if elements[i]['Hand'][j] == 'T':
                    element0 = 10
                elif elements[i]['Hand'][j] == 'J':
                    element0 = 1
                elif elements[i]['Hand'][j] == 'Q':
                    element0 = 12
                elif elements[i]['Hand'][j] == 'K':
                    element0 = 13
                elif elements[i]['Hand'][j] == 'A':
                    element0 = 14
                else:
                    element0 = int(elements[i]['Hand'][j])
                    
                if elements[i + 1]['Hand'][j] == 'T':
                    element1 = 10
                elif elements[i + 1]['Hand'][j] == 'J':
                    element1 = 1
                elif elements[i + 1]['Hand'][j] == 'Q':
                    element1 = 12
                elif elements[i + 1]['Hand'][j] == 'K':
                    element1 = 13
                elif elements[i + 1]['Hand'][j] == 'A':
                    element1 = 14
                else:
                    element1 = int(elements[i+1]['Hand'][j])    
                
                if element0 == element1:
                    j += 1
                else:
                    break
                
            if element0 > element1:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]        
        if not swapped:
            return elements
    return elements
    
def part1(filename):
    file1 = open(os.path.join(sys.path[0], "data", filename), 'r')
    output = 0
    hands = []
    sortedhands = []
    while True:
        line = file1.readline()
        if not line:
            break
        if line != '' and line != '\n':
            line = line.strip()
            hand,bid = line.split()
            hands.append({'Hand': hand, 'Bid': int(bid), 'Sortindex': 0})              
            
           
    for hand in hands:
        dedup = "".join(set(hand['Hand']))
        #print(dedup)
        if len(dedup) == 1:
            # Five of a kind
            hand['Sortindex'] = 7
        elif len(dedup) == 2:
            if hand['Hand'].count(str([hand['Hand'][0]][0])) == 1 or hand['Hand'].count(str([hand['Hand'][0]][0])) == 4:
                if hand['Hand'].count('J') > 0:
                    # Five of a kind
                    hand['Sortindex'] = 7
                else:
                    # Four of a kind
                    hand['Sortindex'] = 6
            else:
                if hand['Hand'].count('J') == 1:
                    # Four of a kind
                    hand['Sortindex'] = 6
                elif hand['Hand'].count('J') > 1:
                    # Five of a kind
                    hand['Sortindex'] = 7
                else:
                    # Full House
                    hand['Sortindex'] = 5
        elif len(dedup) == 3:
            if hand['Hand'].count(str([hand['Hand'][0]][0])) == 1:
                if hand['Hand'].count(str([hand['Hand'][1]][0])) == 2:
                    if hand['Hand'].count('J') == 1:
                        # Full House
                        hand['Sortindex'] = 5
                    elif hand['Hand'].count('J') == 2:
                        # Four of a kind
                        hand['Sortindex'] = 6
                    else:
                        # Two Pair
                        hand['Sortindex'] = 3   
                else:
                    if hand['Hand'].count('J') > 0:
                        # Four of a kind
                        hand['Sortindex'] = 6
                    else:
                        # Three of a kind    
                        hand['Sortindex'] = 4
            elif hand['Hand'].count(str([hand['Hand'][0]][0])) == 2:
                if hand['Hand'].count('J') == 1:
                    # Full House
                    hand['Sortindex'] = 5
                elif hand['Hand'].count('J') == 2:
                    # Four of a kind
                    hand['Sortindex'] = 6
                else:
                    # Two Pair
                    hand['Sortindex'] = 3   
            else:
                if hand['Hand'].count('J') > 0:
                    # Four of a kind
                    hand['Sortindex'] = 6
                else:
                    # Three of a kind    
                    hand['Sortindex'] = 4                 
        elif len(dedup) == 4: 
            if hand['Hand'].count('J') > 0:
                # Three of a kind    
                hand['Sortindex'] = 4
            else:
                # One Pair
                hand['Sortindex'] = 2
        elif len(dedup) == 5: 
            if hand['Hand'].count('J') > 0:
                # One Pair
                hand['Sortindex'] = 2 
            else:
                # High Card
                hand['Sortindex'] = 1
        else:
            print('UNCATEGORIZED')
               

    
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 1])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 2])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 3])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 4])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 5])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 6])
    sortedhands = sortedhands + bubblesort([p for p in hands if p['Sortindex'] == 7])
    
    for idx, hand in enumerate(sortedhands):
        output += hand['Bid']*(idx+1)
        
    print(output)
    
    file1.close()    
  


if __name__ == '__main__':
    part1('day7.prod.txt')