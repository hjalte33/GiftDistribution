# GiftDistribution
Every year at Christmas time, my family has a system where we write down a list on who gives a gift to who.
That way everyone only get one big gift instead of a lot of small ones, and it's all fair and even.
Being a big family, the makeing of the list was often tedious and dificult, because some should not give a gift some other eg. married couples should not find a gift for each other since it wouldn't be as fun. 
Also a cycle of only 2 people should be avoided since it again is not that much fun.

Therefore I decided to make this small python script that creates a random list takeing care of all the family realtions and cycle lengths. 
There is by 100% chance a better and nicer way of solveing this problem using linear algebra or something like that, but i dont care since trying by random seems to work just fine, so I im not fixing it when it's not broken. 

The scripts needs an input file that contains a list of participants.
Each line should contain name of a participant
If a participant should not give gifts to particular other participants, write the "noGiftsNames" after the name seperated with commas.
Names can contain spaces, so you can add a surname if needed. Spaces in front of and after a name gets striped away. 
Names are case sensitive.
example:

./input.csv
name, noGiftName, noGiftName...
alice, carl S.
bob, carl J.
carl J.
carl S.
henrik, alice ,bob

./output.csv
Number of tries 4 
The seed used for this solution is 0 
Smallest cycle length for this solution is 5 

alice gives a gift to henrik
bob gives a gift to alice
carl J. gives a gift to carl S.
carl S. gives a gift to bob
henrik gives a gift to carl J.
