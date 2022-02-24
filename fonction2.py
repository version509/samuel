from math import sqrt

def customTotal(ls):
    if type(ls) == list:
        s = 0
        for el in ls:
            s += el
    return s
        
def mean(ls):
    if type(ls) == list:
        moy = customTotal(ls) / len(ls)
    return moy

def variance(ls):
    if type(ls) == list:
        moy = mean(ls)
        var = 0
        for el in ls:
            var += (el - moy)**2
    return var
            
def standardDerivation(ls):
    sD = sqrt(variance(ls))
    return sD
  


# Test
liste = [2,3,5,6,7,8]

print("Somme : ", customTotal(liste))
print("Moyenne : ", mean(liste))
print("Variance : ", variance(liste))
print("Ecart-ype : ", standardDerivation(liste))