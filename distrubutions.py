import numpy as np
import matplotlib.pyplot as plt

a = 1.4
c = 2 * (a + np.exp(-a))
experimentNum = 5000
steps = 250
signChoice = [-1, 1]

def floatRange(a, b, steps):
    step = (b - a) / steps
    return [i * step + a for i in range(steps)]

def makePlot(ds, name):
    plt.plot(floatRange(min(ds), max(ds), steps), np.histogram(ds, steps)[0], label=name)
    plt.savefig(name + ".png")
    plt.close()

def coinFlip():
    return 1 - 2 * np.random.choice(2)

def genA():
    if np.random.uniform(0, 1) < 2 * a / c:                 # probability of getting an uniform part
        return np.random.uniform(-a, a)
    else:                                                   # else we have exponential distribution
        return coinFlip() * (np.random.exponential(1) + a)  # positive or negative?

def genB():
    t = np.random.uniform(0, 1)
    if t > 1 - np.exp(-a) / c:
        return -np.log((1 - t) * c)
    if t > np.exp(-a) / c:
        return t * c - a - np.exp(-a) 
    return np.log(t * c)

if __name__ == "__main__":
    resA = []
    resB = []
    for _ in range(experimentNum):
        resA.append(genA())
        resB.append(genB())
    makePlot(resA, "Method A")
    makePlot(resB, "Method B")
