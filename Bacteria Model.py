# -*- coding: utf-8 -*-
"""
Created on Mon May 08 14:46:11 2017

@author: Peter
"""

import random

class bacteria:
  'a single Bacteria'  #super realistic
  bacteria_count=0
  
  def __init__(self, name,age,number_of_offspring):
    self.name=name #name of bacteria
    self.age=age
    self.number_of_offspring=number_of_offspring
    bacteria.bacteria_count += 1
    
  def displayCount(self):
    print("population=%d" % bacteria.bacteria_count)
    
  def displayBacteria(self):
    print "Name=",self.name,", age in hours=",self.age,"multiplication count=",self.number_of_offspring

initial_number_of_bacteria=100
growth_rate=0.0002
death_rate=0.0001

# create an initial population. 

population=[]
for indx in range(initial_number_of_bacteria):
  this_bacteria=bacteria("Bacteria",random.randint(1,240),random.randint(0,4))
  population.append(this_bacteria)

population[0].displayBacteria()
population[0].displayCount()
print len(population)
print "age=",population[0].age

for hour in range(240):
  if ((hour % 24)==0):
    print("day="+str(hour/24))
    print("population="+str(len(population)))	
  remove_this_bacteria=[]
  add_this_bacteria=[]
  for this_bacteria_indx in range(len(population)): # increment each bacteria's age
    population[this_bacteria_indx].age = population[this_bacteria_indx].age+1

    this_bacteria_divides=False
    division_coin=random.random() #dif bacteria --> dif rates "old" bacteria can lose pathways etc.
    # re-shape this distribution newer cultures grow faster while nutrients are not depleted
    if (division_coin < growth_rate):
      this_bacteria_divides=True
    if (this_bacteria_divides): 
      population[this_bacteria_indx].number_of_offspring += 1
      add_this_bacteria.append(1)

    this_bacteria_dies=False
    death_coin=random.random()# coin flip for death
    # re-shape this distribution to reflect depleted nutrients with time
    if (death_coin < death_rate): 
      this_bacteria_dies=True
    if (this_bacteria_dies):
      remove_this_bacteria.append(this_bacteria_indx)
      
  for indx in range(len(remove_this_bacteria)):
    print("     remove bacteria "+str(remove_this_bacteria[indx]))
    population.pop(remove_this_bacteria[indx])
  for indx in range(len(add_this_bacteria)):
    print("     add bacteria ")
    new_bacteria_age=0 
    new_bacteria_number_of_clones=0
    new_bacteria=bacteria("Bacteria",new_bacteria_age,new_bacteria_number_of_clones)
    population.append(this_bacteria)    
  
population[0].displayBacteria()
print population[0].age
