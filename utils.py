import numpy as np

def probabilities(numbers):
    probs = [0.,0.,0.,0.]
    players = [0,1,2,3]
    
    order_of_players = [x for _,x in sorted(zip(numbers,players))]
    numbers.sort()
    probs[order_of_players[0]] += numbers[0]
    for i in range(3):
        probs[order_of_players[i]] += (numbers[i+1]-numbers[i])/2
        probs[order_of_players[i+1]] += (numbers[i+1]-numbers[i])/2
    probs[order_of_players[3]] += 1-numbers[3]

    probs /= sum(probs)
    probs *= 100
    for i in range(len(probs)):
        probs[i] = np.round(probs[i],3)
    return probs

def recursive(num_players):
    # Buggy right now, but the idea can be as follows.
    selected = False
    if num_players==1:
        skipped = False

    best = np.full((turns,9),-1.)
    for idx,p_value in enumerate(lins.copy()):
        if num_players==4:
            print(p_value)

        player_list.change_value(num_players-1, p_value)
        
        if num_players-1:
            best_old, skipped = recursive(num_players-1)
            selection = np.max(best_old,axis=0)[0]
            # all max probabilities
            best_configs = best_old[np.where(best_old[:,0]==selection)]
            mean_probs = np.mean(best_configs,axis=0)[1:]

            if selection == -1:
                continue

            if not skipped:
                best[idx][0] = mean_probs[NUM_PLAYERS-num_players]
                best[idx][1:5] = mean_probs[:4]
                best[idx][5:] = mean_probs[-4:]
                
        else:
            if player_list.same_values_exist() and num_players-1==0:
                continue
            else:
                skipped = False

            selected = True
            
            probs = probabilities(player_list.p_values)
            best[idx][0] = probs[NUM_PLAYERS-num_players]
            best[idx][1:5] = probs
            best[idx][5:] = player_list.p_values
        
        if num_players == NUM_PLAYERS:

            if np.max(best,axis=0)[0] > selection:
                print("Max: ", np.max(best,axis=0)[0])
                selection = np.max(best,axis=0)[0]
        
    return best, skipped