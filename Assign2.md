# Statistical Mechanics Assignment 2

#### Question 1
The theoretical odds for betting on colours in the American version of roulette are $\frac{9}{19}$ which is roughly speaking $47.37$% of the time. This can be seen from the image below where we have the numbers $[1,36]$ inclusive with an equal amount of red and black numbers. On top of this we also a $0$ and $00$ giving us a total of 38 tiles with 18 of them being red and 18 being black. Hopefully it's trivial to infer that the theoretical odds of winning are $\frac{9}{19}$.

![Second Image](/home/cameron/Stat_Mech/Assign2/AmericanWheel.gif)

#### Question 2

The Following pdf was constructed by considering the amount of money that Andrew had at any given time over the space of 1000 nights. To do this we started every night off with $$1000$ and let the system evolve over time with only a $47.37\%$ of winning and at evey time step we recorded the total of money Andrew had to be placed into the histogram giving the overall pdf.

![First Image](/home/cameron/Stat_Mech/Assign2/anytime.png)

#### Question 3

At any give time we have a probability distribution of how much money Andrew will have. This distribution will have encoded into it the likelihood of each value including the beyond the values which Andrew will still be at the table. For the values which are greater than $x_m$ and greater than $x_w$ we hve information about the likelihood that Andrew as left the table. So it makes perfect sense to say that the integral of the probability distribution between $x_m$ and $x_w$ would tell us how likely it is that he is still at the table.
