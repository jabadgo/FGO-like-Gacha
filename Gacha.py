import numpy as np
import random as rd
import os
import csv

mypath = os.getcwd()+'\data'
os.chdir(mypath)

files = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
Named_Pool = {}
if len(files) == 6:
    for z in files:
        x = os.path.splitext(z)[0]
        with open(z,'rt') as csvfile:
            preR = list(csv.reader(csvfile,dialect='excel'))
            exit_variable= [i[0] for i in preR]
            Named_Pool[x] = exit_variable
else:
    print('Some necessary files are missing.')


#Summoning pools and odds
SQ_Pool = {'R_CE':'3 Star Craft Essence','SR_CE':'4 Star Craft Essence','SSR_CE':'5 Star Craft Essence','R_S':'3 Star Servant','SR_S':'4 Star Servant','SSR_S':'5 Star Servant'}
SQ_P = [0.4,0.12,0.04,0.4,0.03,0.01]
classes = ['Archer','Lancer','Berserker','Ruler','Saber','Rider','Caster','Assassin','Avenger']

def summoning(pool,p):
    #This function takes care of the actual summoning by randomly selecting an item from a list
    #The selection is based on each item's probability
    pool_obj = list(pool.keys())
    summon = np.random.choice(pool_obj,1,p)
    return summon


def saintquartz_summon(SQ_amount,summon_size,summoning_pool,probability):
    #This function simulates a SaintQuartz summon
    error = str('Not enough Saint Quartz, brother.\n')
    summoning_pool = SQ_Pool
    probability = SQ_P
    a = (1,10)
    result = []
    if summon_size in a:
        if summon_size == 10:
            if SQ_amount >= 30:
                i = 1
                while True:
                    if i <= summon_size:
                        pre_smn = summoning(summoning_pool,probability)
                        i += 1
                        for a in pre_smn:
                            result.append(a)
                    else:
                        break
            else:
                return error
        else:
            if SQ_amount >= 3:
                i = 1
                while True:
                    if i <= summon_size:
                        pre_smn = summoning(summoning_pool,probability)
                        i += 1
                        for a in pre_smn:
                            result.append(a)
                    else:
                        break
            else:
                return error
    return result


def user_inputsq():
#Taking and checking user input
    while True:
        try:
            Usr_SQ = int(input('How many Saint Quartz do you have? \nAnswer: '))
            break
        except ValueError:
            print('ERROR: Please write a number.\n')
    return Usr_SQ


def user_inputsize():
    while True:
        Usr_choice = input('\n\nDo you want to do a 10x or 1x summon?\n A. 10x summon\n B. 1x summon\nAnswer (A/B):')
        if Usr_choice.lower() in ('a','b'):
            break
        else:
            print('ERROR: Please write either A or B.\n')
    return Usr_choice


def usr_summon(Usr_SQ,Usr_choice):
    if Usr_choice == 'a':
        size = 10
    elif Usr_choice == 'b':
        size = 1
    Summoned = saintquartz_summon(Usr_SQ,size,SQ_Pool,SQ_P)
    return Summoned


Usr_SQ = user_inputsq()
Usr_choice = user_inputsize()
while True:
    Summoned = usr_summon(Usr_SQ,Usr_choice)
    if isinstance(Summoned,str):
        print(Summoned)
        print('\nYou have %s Saint Quartz left' % Usr_SQ)
    else:
        print('You got:\n')
        for b in Summoned:
            result = print(SQ_Pool[b],': ',rd.choice(Named_Pool[b]))
        if len(Summoned) == 10:
            newSQ =  Usr_SQ - 30
            info = print('\n - - \n\nYou have %s Saint Quartz left' % newSQ)
        else:
            newSQ =  Usr_SQ - 3
            info = print('\n - -\n\nYou have %s Saint Quartz left' % newSQ)
    exit_choice = input('Do you want to summon again (Y/N)\nAnswer:')
    if exit_choice.lower() in ('y','n'):
        if exit_choice.lower() == 'n':
            print('\nThanks for using this program.\n')
            input('Press ENTER to close this window.')
            break
        else:
            Usr_SQ = newSQ
            Usr_choice = user_inputsize()
    else:
        print('Write Y or N to either summor again or leave the program\n')
