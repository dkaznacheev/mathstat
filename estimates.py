import numpy as np
import matplotlib.pyplot as plt
import random

maxK = 20
sampleSize = 500
experimentNum = 500
theta = 1.0

def makePlot(ds, distName):
    l = len(ds)
    name = distName + " distribution"
    plt.plot(list(range(1, l + 1)), ds, label = distName)
    plt.savefig(name + ".png")
    plt.close()

def main():
    dsUni = []
    dsExp = []
    for k in range(1, maxK):
        dUni = 0.0
        dExp = 0.0
        for i in range(experimentNum):
            sampleUni = np.random.uniform(0, theta, sampleSize)
            estimateUni = ( sum(map(lambda x: x**k, sampleUni)) / sampleSize * (k + 1) ) ** (1 / k)
            dUni += (theta - estimateUni) ** 2
            
            sampleExp = np.random.exponential(1.0 / theta, sampleSize)
            estimateExp = ( sum(map(lambda x: x**k, sampleExp)) / sampleSize / np.math.factorial(k) ) ** (1 / k)
            dExp += (theta - estimateExp) ** 2

        dsUni.append(dUni / experimentNum)
        dsExp.append(dExp / experimentNum)
        print("Calculated k = ", k)
    
    print(dsUni)
    print(dsExp)
    makePlot(dsUni, "Uniform")
    makePlot(dsExp, "Exponential")


if __name__ == "__main__":
    main()
