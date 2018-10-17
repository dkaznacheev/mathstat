import numpy as np
import matplotlib.pyplot as plt
import random
import math
from scipy.stats import norm, chi2

minK = 10
maxK = 500
dK = 5
experimentNum = 500
theta = 0
delta = 2
gamma = 0.1

def makePlot(ds, distName):
    name = distName
    plt.plot(list(range(minK, maxK, dK)), ds, label = distName)
    plt.savefig(name + ".png")
    plt.close()

def avg(a):
    return sum(a) / len(a)

def main():
    resA = []
    resB = []
    for k in range(minK, maxK, dK):
        testA = []
        testB = []
        for _ in range(experimentNum):
            dsNorm = [random.normalvariate(0, 2) for _ in range (k)]
            leftA = sum(map(lambda x: x * x, dsNorm)) / chi2.ppf((1 + gamma) / 2, k)
            rightA = sum(map(lambda x: x * x, dsNorm)) / chi2.ppf((1 - gamma) / 2, k)
            leftB = k * (avg(dsNorm) ** 2) / (norm.ppf((3 + gamma) / 4) ** 2)
            rightB = k * (avg(dsNorm) ** 2) / (norm.ppf((3 - gamma) / 4) ** 2)
            testA.append(rightA - leftA)
            testB.append(rightB - leftB)
        la = avg(testA)
        lb = avg(testB)
        print("{}: {}, {}".format(k, la, lb))
        resA.append(la)
        resB.append(lb)

    makePlot(resA, "Stat_A")
    makePlot(resB, "Stat_B")


if __name__ == "__main__":
    main()
