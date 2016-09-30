def diceroll():
	from random import randint
	diceroll = randint(0,6)
	
import time

def help1():
	print(("List of Commands: ")+("\nGo\nTalk\nExamine\nTake\nFight\nStat"))
	
def stats():
	print(("Health: "+str(Health)),("\nSanity: "+str(Sanity)),("\nGorilla Power: "+str(GorillaPower)))

Health = 10
Sanity = 5
GorillaPower = 1

loop = 1
while loop == 1:
	print("-----------------------------------")
	print("     Harambe: The Adventure        ")
	print("-----------------------------------")
	while True:
		try:
			Name = input("What is your name?: ")
			if Name.lower() == "harambe":
				raise TypeError
			break
		except TypeError:
			print("Do not use the lords name in vain!")
	loop = loop+1
	
while loop == 2:
	print("Mom: Happy Birthday " + Name + "! Guess where I'm taking you today!")
	time.sleep(1)
	print("You: Where!")
	time.sleep(1)
	print("Mom: Cincinnati zoo!")
	time.sleep(1)
	print("You: Yay!")
	time.sleep(1)
	print("---2 Hours Later you arrive at Cincinnati zoo---")
	time.sleep(1)
	print("Mom: Do you want to see the gorillas?")
	time.sleep(1)
	print("You: Yeah!")
	time.sleep(1)
	loop = loop+1

while loop == 3:
	print("-----------------------------------")
	time.sleep(1)
	print(("You arrive at the gorrila enclosure ")+("\nThere is a big glass pane to see the gorrilas ")+("\nThere is also an infomation panel about the gorrilas ")+("\nPaths lead to the east and west"))
	loop = 4

while loop = 4:
	first = input("What do you do?")
	if first.lower() == "help":
		help1()
		loop = 4
	if first.lower() == "stats":
		stats()
		loop = 4
	if "go" and "east" in first.lower():
		print("-----------------------------------")
		print("You head east")
		loop = 5
	if "go" and "west" in first.lower():
		print("-----------------------------------")
		print("You head west")
		loop = 6
	if "take" in first.lower():
		print("-----------------------------------")
		print("Nothing to take!")
		loop = 4
	if "examine" and "panel" in first.lower():
		print("-----------------------------------")
		print("The panel is boring. You want to see the gorrilas!")
		loop = 4
	if "examine" not "panel" or "glass" in first.lower():
		print("-----------------------------------")
		print("Examine what?")
		loop = 4
	if "examine" and "glass" in first.lower():
		print("-----------------------------------")
		print("You see Harambe in all his glory!"),("\nGain a Gorilla Power")
		if GorillaPower < 1:
			GorillaPower = GorillaPower+1
		else:
			print("You fail to absorb the power")
		loop = 4
	else:
		print("-----------------------------------")
		loop = 4
