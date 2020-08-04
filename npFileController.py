import numpy as np

def savalist(filename:str,List:list):
    a = np.array(List)
    np.save(filename+".npy",a)

def readlist(filename:str):
    a = np.load(filename+".npy")
    a = a.tolist()
    return a