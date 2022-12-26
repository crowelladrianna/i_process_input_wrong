# Explanation of Code

i_process_input_wrong.py is a code poem with a provided translation for how I would go about reading it out loud.

The code itself breaks down the task of ordering lunch into two parts that appear simple at first glance, processing the environment and saying an order.

Processing the input is an overly complicated recursive process that completes in one step if the amount of input is below a certain random number and adds additional input to process before trying again if it is not. The comment “should’ve solved iteratively” points to the fact that the same problem could be solved much more simply by going through every element in the list one at a time, and that such an approach would not crash the program the same way recursion does (since Python limits depth of recursion to 1000).

Saying words is a slightly more understandable bit of code. If conditions are favorable, the words come out as inputted. Otherwise, they are broken apart and shuffled to come out in a random order.

The code then includes various lists of input to be processed.

The final stanzas show the results of running the order_lunch function on different sets of input five times each.

All this is shows the difficulty of moving through the world as an autistic person, sensory overload like the crashing of a poorly written program, in a way that traditional poetry is not able to.

# i process input wrong (translated)

a simple function:  
order lunch from blue wall.  
I process blue wall  
I say my order  

should’ve solved iteratively,  

I process input wrong.  
If input’s less than Monday’s limit,  
I return.  

Or else,  
input append  
a shaking hand,  
input extend  
a new sore wrist, a turning stomach,  
or perhaps the growling.  
Either way, now, sick.  

return,  
I process input  

I say words  
if well rehearsed  
and thought not lost  
and luck not greater than Monday’s limit,  
print words  

Or else,  
lost thought words split.  
shuffle, lost thought  
print join, lost thought.  

Monday’s limit is non deterministic  

My order is  
“spicy salmon roll”  

I didn’t understand until  
pandemic quiet.  

I cry standing in the  
campus center bathroom: puddle leaking from the middle stall,  
hand dryer rush,  
accidental toilet flush,  
and the accompanying spray.  
Victoria’s Secret Pure Seduction  
from the Alpha Chi Omega girls gossiping  
about their shitty boyfriends  
while the far sink drips  
its water waste against the porcelain.  

One thirty: salt still curing the roof of my mouth  
or tempering it to taste  
the spicy salmon maki after Shakespeare  

I don’t want to be  
here where  
the scratch  
chatter  
ginger pho steam  
frier oil  
scratch  
of life  
where life itself  
beats my heart too hard  
on the balls of my feet,  
where the bodies  
the life  
press too close in line behind me,  
the coughs,  
the coffee aftertaste,  
the disagreement of the milk that lightened it,  
the footsteps,  
bodies  
life against my sweating side,  
life hot against the veins  
that converge in tapping fingers  
on the thighs.  
Life in the frat boys,  
too excited, bubbling Coke  
into unpaid glass,  
class  
in another hour across campus  

order lunch in a pandemic (quiet)

spicy salmon roll  
spicy salmon roll  
roll spicy salmon  
salmon roll spicy  
spicy salmon roll  

order lunch, one thirty, order  

spicy salmon roll  
spicy salmon roll  
spicy salmon roll  
salmon roll spicy  
Traceback (most recent call last):  
&nbsp;&nbsp;&nbsp;RecursionError: maximum recursion depth  

order lunch, here  
ORDER  

Traceback  
Traceback  
Traceback  
Traceback  
maximum recursion depth  