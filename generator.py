
import numpy as np
#creating LCG class
class LCG:
    def __init__(self,seed, a,c,m):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m
    def getSeed(self):
        return self.seed
        
    def setSeed(self,inputseed): 
        self.seed= inputseed
        return(self.seed)
       
        
    def getRandomNumber(self):
        self.seed=(self.a*self.seed+self.c)%self.m
        number = self.seed/self.m
        return number
        
    def numberSequence(self, length):
        sequence1 = []
        seeda = self.seed
        self.seed = np.zeros([length+1])
        self.seed[0] = seeda
        for x in range(length):
            self.seed[x+1]=(self.seed[x]*(self.seed[x]+1))%self.m
            sequence1.append(self.seed[x+1]/self.m)     
        return (sequence1)

    
    def __next__(self):
        self.seed=(self.a*self.seed+self.c)%self.m
        nextnumber = self.seed/self.m
        return nextnumber
         

# Testing the output random number sequence and getting and setting seed 
#Code to test LCG() functions
'''
a=LCG(1,1103515245,12345,2**32)
print(a.getSeed())
print(a.getRandomNumber())
print(a.getRandomNumber())
print(a.numberSequence(5))
a.setSeed(100000)
print(a.getSeed())
print(a.getRandomNumber())
print(a.__next__())
'''
# Creating the SCG class
class SCG(LCG):
    def __init__(self, seed, m):
        self.seed=seed
        self.m=m
        if (self.seed%4)!=2:
           raise ValueError('Seed value should have 2 as remainder value') 
    
    def getRandomNumber(self):
        rand = (self.seed*(self.seed+1))%self.m
        return rand/self.m
        
    def getSequence(self,length):
        sequence1=[]
        seeda= self.seed
        self.seed=np.zeros([length+1])
        self.seed[0] = seeda
        for x in range(length):
            self.seed[x+1]=(self.seed[x]*(self.seed[x]+1))%self.m
            sequence1.append(self.seed[x+1]/self.m)     
        return (sequence1)  

#Code to test SCG() functions
'''
s=SCG(2,2**32)
print('SCG random number',s.getRandomNumber())
print(s.getSequence(10))
'''