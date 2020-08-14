
import random 

with open('emojis-items.txt') as f:
	items = f.readlines()
items = [x.strip() for x in items]

with open('emoji-forest.txt') as g:
	forest = g.readlines()
forest = [x.strip() for x in forest]



def unicode2String(emoji):
	emoji = emoji[:1] + "000" + emoji[2:]
	uniPyString = "\\" + emoji

	return uniPyString

forestString = ""

def generateForest():
	global forestString
	for z in range(1500):
		r = random.randint(0,5)
		if r == 0:
			forestString += unicode2String(random.choice(items))
		if r > 0 and r < 3:
			forestString += " "
		if r >= 3:
			forestString += unicode2String(random.choice(forest))

generateForest()

OutputFile = open("output.txt","w") 
OutputFile.write(forestString) 
OutputFile.close()
