import numpy as np
import pandas as pd
columns=[0,1,2,0,1,2,0,1,2]
def calculate(list):
  try:
    data=np.array(list).reshape(3,3)
    df=pd.DataFrame(data)
    calculations={
      'mean':[[df.mean(axis=0)[0],df.mean(axis=0)[1],df.mean(axis=0)[2]],[df.mean(axis=1)[0],df.mean(axis=1)[1],df.mean(axis=1)[2]],df.mean().mean()],
      'variance':[[data.var(axis=0)[0],data.var(axis=0)[1],data.var(axis=0)[2]],[data.var(axis=1)[0],data.var(axis=1)[1],data.var(axis=1)[2]],data.var()],
      'standard deviation':[[data.std(axis=0,dtype=np.float64)[0],data.std(axis=0)[1],data.std(axis=0)[2]],[data.std(axis=1)[0],data.std(axis=1)[1],data.std(axis=1)[2]],data.std()],
     'max':[[df.max(axis=0)[0],df.max(axis=0)[1],df.max(axis=0)[2]],[df.max(axis=1)[0],df.max(axis=1)[1],df.max(axis=1)[2]],df.max().max()],
     'min':[[df.min(axis=0)[0],df.min(axis=0)[1],df.min(axis=0)[2]],[df.min(axis=1)[0],df.min(axis=1)[1],df.min(axis=1)[2]],df.min().min()],
      'sum':[[df.sum(axis=0)[0],df.sum(axis=0)[1],df.sum(axis=0)[2]],[df.sum(axis=1)[0],df.sum(axis=1)[1],df.sum(axis=1)[2]],df.sum().sum()],
    }
    return calculations
  except ValueError:
    raise ValueError("List must contain nine numbers.")
  
