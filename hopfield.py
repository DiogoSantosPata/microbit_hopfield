from microbit import *
import random

## Display patterns on the microbit led screen
def display_pattern(this_pat): 
    ss = ""
    for ii in range(25):
        tmp = 0
        if this_pat[ii] == 1: tmp=5
        ss += str(tmp)
        if ii%5==4: ss+= ':'
    ss = ss[:-1]
    display.show(Image(ss))
   
   
## Create random patterns with size 25 (the amount of leds available in the microbit)
def set_random_pattern():
    rpat = []
    for ii in range(25):
        a = random.randint(0,1)
        if a==0: rpat.append(1)
        else: rpat.append(-1)
    return rpat

## Get the original pattern and alter its state up to 76% (19 out of 25 leds)
def alter_pattern(pat):
    new_pat = []
    for ii in range(25): new_pat.append( pat[ii] )
    
    for ii in range(19):
        a = random.randint(0,24)
        new_pat[a] = new_pat[a] * -1
    display_pattern(new_pat)
    return new_pat

## Given the altered pattern, try to reconstruct the original pattern by the dot product of the learnt weights
def recall(this_pat,weights):
    
    for rr in range(6):
        new_pat = []
        for ii in range(25):
            tmp = 0
            for jj in range(25):
                tmp += this_pat[jj] * weights[jj][ii]                
            if tmp>=0: tmp= 1
            if tmp<0: tmp= -1
            new_pat.append(tmp)
        for ii in range(25): this_pat[ii] = new_pat[ii]
        display_pattern(this_pat)
    
## Learn the connectivity between all the leds 
def train_weights(weights, this_pat):
    for ii in range(25):
        for jj in range(25):
            if ii!=jj: weights[ii][jj] += this_pat[ii]*this_pat[jj]
            if ii==jj: weights[ii][jj] = 0
    return weights



##################
###### MAIN ######
##################

## Create 2 random patterns
pat = set_random_pattern()
pat2 = set_random_pattern()

## Display the pattern that we want to reconstruct (this is still the original)
display_pattern(pat)

## Set and learn the weights matrix
weights = [ [ 0 for j in range(25) ]  for i in range(25) ] 
weights = train_weights(weights, pat)
weights = train_weights(weights, pat2)

## Main application loop        
while True:
 
    if button_a.is_pressed():   ## Display the original pattern on the microbit screen
        display_pattern(pat)

    if button_b.is_pressed():   ## Randomize the pattern and try to reconstruct 
        recall(alter_pattern(pat),weights)
        
