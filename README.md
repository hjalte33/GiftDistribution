# GiftDistribution
Every year at Christmas time, my family writes down a list on who gives a gift to who.
That way everyone only get one big gift instead of a lot of small ones. 

The scripts needs an input file that contains a list of participants.
Each line should contain name of a participant
If the participant should not give gifts to a particular other participant, write the "noGiftsNames" after the name seperated with commas.
Names can contain spaces, so you can add a surname. 
Names are case sensitive.
example:

./input.csv
name, noGiftName, noGiftName
alice, carl
bob, carl J
carl J.
carl S.
henrik, alice ,bob

./output.csv
Number of tries 1 
The seed used for this solution is 0 
Smallest cycle length for this solution is 5 

alice gives a gift to henrik
bob gives a gift to carl J.
carl J. gives a gift to alice
carl S. gives a gift to bob
henrik gives a gift to carl S.
