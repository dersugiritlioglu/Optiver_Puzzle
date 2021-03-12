import numpy as np
from players_list import PlayersList
from utils import *

NUM_PLAYERS=4 # how many players are playing the game
turns = 25 # the steps would be 1/(turns-1); (multiples of 6)+1 is preferred.
selection0 = 0
np.set_printoptions(suppress=True)
lins = np.linspace(0,1,turns)
for_loops = True # True for using for loops, false for recursive function.


########################################################################
    
player_list = PlayersList()

best0 = np.full((turns,9),-1.)

print(lins)
if for_loops:
    for idx0,p0 in enumerate(lins.copy()):
            print(p0)
            best1 = np.full((turns,9),-1.)
            for idx1,p1 in enumerate(lins.copy()):
                    best2 = np.full((turns,9),-1.)
                    for idx2,p2 in enumerate(lins.copy()):
                            best3 = np.full((turns,9),-1.)
                            skipped = True
                            for idx3,p3 in enumerate(lins.copy()):           
                                    player_list.change_value(0,p0)
                                    player_list.change_value(1,p1)
                                    player_list.change_value(2,p2)
                                    player_list.change_value(3,p3)
                                    if player_list.same_values_exist():
                                        continue
                                    else:
                                        skipped = False
                                    probs = probabilities([p0,p1,p2,p3])               
                                    best3[idx3] = (probs[3],probs[0],probs[1],probs[2],probs[3], p0,p1,p2,p3)

                            selection3 = np.max(best3,axis=0)[0]
                            # all max probabilities
                            best_configs3 = best3[np.where(best3[:,0]==selection3)]
                            mean_probs3 = np.mean(best_configs3,axis=0)[1:]
                            if selection3 == -1:
                                continue

                            if not skipped:
                                best2[idx2] = mean_probs3[2], mean_probs3[0], mean_probs3[1], mean_probs3[2], mean_probs3[3], mean_probs3[-4], mean_probs3[-3], mean_probs3[-2], mean_probs3[-1]

                    selection2= np.max(best2,axis=0)[0]
                    best_configs2 = best2[np.where(best2[:,0]==selection2)]
                    mean_probs2 = np.mean(best_configs2,axis=0)[1:]

                    if selection2 == -1:
                        continue

                    try:
                        best1[idx1] = mean_probs2[1], mean_probs2[0],mean_probs2[1],mean_probs2[2],mean_probs2[3],mean_probs2[-4],mean_probs2[-3],mean_probs2[-2],mean_probs2[-1]
                    except:                  
                        continue       
            selection1= np.max(best1,axis=0)[0]
            best_configs1 = best1[np.where(best1[:,0]==selection1)]
            mean_probs1 = np.mean(best_configs1,axis=0)[1:]
            if selection1 == -1:
                continue
            try:
                best0[idx0] = mean_probs1[0], mean_probs1[0],mean_probs1[1],mean_probs1[2],mean_probs1[3],mean_probs1[-4],mean_probs1[-3],mean_probs1[-2],mean_probs1[-1]
            except:
                print(0)
                continue

            if np.max(best0,axis=0)[0] > selection0:
                print("Max: ", np.max(best0,axis=0)[0])
                selection0 = np.max(best0,axis=0)[0]

    selection0 = np.max(best0,axis=0)[0]
    print(selection0)
    result = best0[np.where(best0[:,0]==selection0)][0] # one can see other optimum scenarios by deleting the 0 at the end.
else:
    best0 = recursive(NUM_PLAYERS)[0]
    selection0 = np.max(best0,axis=0)[0]
    print(selection0)
    print(best0[np.where(best0[:,0]==selection0)])


print("\n\nProbabilities:\n","-"*50)
print("Player A:", result[1])
print("Player B:", result[2])
print("Player C:", result[3])
print("Player D:", result[4])

print("Selections:\n","-"*50)
print("Player A selects:", result[-4])
print("Player B selects:", result[-3])
print("Player C selects:", result[-2])
print("Player D selects:", result[-1])
print('(These are mean selections, D can select anything in between 1/6 and 5/6, with a mean of 3/6. A can select 1/6 or 5/6, B would select the one A left.)')
