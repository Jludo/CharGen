#imports

import random, math, os
from genlists import charbg, charquirk

# stat generation

def die(x):
  return random.randint(1,x)

def statgen():
  statroll = [die(6),die(6),die(6),die(6)]
  return sum(statroll)-min(statroll)

class char_class:
  def __init__(self,name,rSTR,rDEX,rCON,rINT,rWIS,rCHA):
    self.name = name
    statlist = [statgen(),statgen(),statgen(),statgen(), statgen(),statgen()]
    statlist.sort()

    self.STR = statlist[rSTR]
    self.DEX = statlist[rDEX]
    self.CON = statlist[rCON]
    self.INT = statlist[rINT]
    self.WIS = statlist[rWIS]
    self.CHA = statlist[rCHA]
  
  def statprint(self):
    return print(f'Class: {self.name}\nBackground: {random.choice(charbg)}\nQuirk: {random.choice(charquirk)}\n\nSTR: {self.STR}\nDEX: {self.DEX}\nCON: {self.CON}\nINT: {self.INT}\nWIS: {self.WIS}\nCHA: {self.CHA}')

wizard = char_class('Wizard',5,1,3,0,2,4)

#class_choice = input()

wizard.statprint()

# Race, Class, Background, Quirk, HP, AC, SP, Stats