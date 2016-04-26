#!/usr/bin/env python
import random
import numpy as np
import matplotlib.pyplot as plt
from array import array

win_rate = 4637
turn = 0
win = 0
money = []
Q6 = np.zeros(5000)
tock = list(range(0,5000))
time = []
long_run = 1000.

while turn < long_run:
    print turn / long_run
    total = 1000
    tick = 0
    while total < 2000 and total > 10:
        bet = total * 0.05
        win = random.randrange(0,10000)
        if win < win_rate:
            total = total + bet
        else:
            total = total - bet
        Q6[tick] = Q6[tick] + total
        money.append(total)
        time.append(tick)
        tick = tick + 1

    turn = turn + 1

i = 0
while i < 5000:
    Q6[i] = Q6[i] / long_run
    i = i +1

bin_values = range(0,2000)

plt.hist(money,label = "Money at Any Given Time", bins = bin_values)
plt.title("Money at any Time")
plt.xlabel("Dollars")
plt.ylabel("Frequency")
plt.show()

plt.plot(tock, Q6 , "o")
plt.title("Average Money at Given Time")
plt.ylabel("Dollars")
plt.xlabel("Time")
plt.axis([0,1500,0,1200])
plt.show()
