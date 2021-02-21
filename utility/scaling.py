import math

#normalizing function for scaling between range 0-1

def sigmoid_normalization(x):

    result=1/(1+math.exp(-x))
    return result

def sigmoid_normalization_v2(x):

    result=1/(1+math.exp(-(x*2**(abs(x)))))
    return result



