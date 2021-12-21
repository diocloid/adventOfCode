import argparse
import numpy as np
from collections import defaultdict


def play(universecounter, dicerolls):
    newuniversecounter = defaultdict(int)
    player1winstemp = 0
    player2winstemp = 0
    for key, value in universecounter.items():
        player1score = key[0]
        player2score = key[1]
        player1space = key[2]
        player2space = key[3]
        ticktock = key[4]
        universecountercounter = value
        #print(value)


        for roll in dicerolls:
        
            if (ticktock == 0):
                player1spaceNEW = player1space + roll%10
                if(player1spaceNEW%10 == 0):
                    player1finalspace = 10
                else:
                    player1finalspace = player1spaceNEW%10
                player1scoreNEW = player1score + player1finalspace

                if(player1scoreNEW > 20):
                    player1winstemp += universecountercounter
                else:
                    newuniversecounter[player1scoreNEW, player2score, player1finalspace, player2space, 1] += universecountercounter 
                # else:
                #     if([player1finalspace, player2space, player1scoreNEW, player2score, 1] in newuniversecounter):
                #       newuniversecounter[player1finalspace, player2space, player1scoreNEW, player2score, 1] += universecountercounter 
                #     else: 
                #         newuniversecounter[player1finalspace, player2space, player1scoreNEW, player2score, 1] = 1 
            elif (ticktock == 1):
                player2spaceNEW = player2space + roll%10
                if(player2spaceNEW%10 == 0):
                    player2finalspace = 10
                else:
                    player2finalspace = player2spaceNEW%10
                player2scoreNEW = player2score + player2finalspace

                if(player2scoreNEW > 20):
                    player2winstemp += universecountercounter
                else:
                    newuniversecounter[player1score, player2scoreNEW, player1space, player2finalspace, 0] += universecountercounter
                    # if((player1space, player2finalspace, player1score, player2scoreNEW, 1) in newuniversecounter):
                    #     newuniversecounter[player1space, player2finalspace, player1score, player2scoreNEW, 0] += universecountercounter 
                    # else: 
                    #     newuniversecounter[player1space, player2finalspace, player1score, player2scoreNEW, 0] = 1 

    return newuniversecounter, player1winstemp, player2winstemp
        

def main(args):
    dicerolls = []
    for x in range(1,4):
        for y in range(1,4):
            for z in range(1,4):
                dicerolls.append(x+y+z)

    ticktock = 0
    player1score = 0
    player2score = 0
    player1space = args.player1
    player2space = args.player2
    player1winsacrossuniverses = 0
    player2winsacrossuniverses = 0
    universecounter = {}
    universecounter[player1score, player2score, player1space, player2space, ticktock] = 1
    
    while universecounter:
        universecounter, player1winstemp, player2winstemp = play(universecounter, dicerolls)
        player1winsacrossuniverses += player1winstemp
        player2winsacrossuniverses += player2winstemp

    print(max(player1winsacrossuniverses,player2winsacrossuniverses))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='AdventOfCode2021Day21')
    parser.add_argument('--player1', type=int, required=True,
                    )
    parser.add_argument('--player2', type=int, required=True,
                    )
    args = parser.parse_args()

    main(args)