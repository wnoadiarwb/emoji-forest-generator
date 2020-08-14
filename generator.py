
import random 
import json

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

def convertCharacter(emoji):
	return chr(int(emoji[2:], 16))

forestString = ""

def generateForest():
	global forestString
	for z in range(1500):
		r = random.randint(0,15)
		if r == 0:
			forestString += convertCharacter(random.choice(items))
		if r > 0 and r < 13:
			# forestString += random.choice((" ", "🌲"))
			forestString += " "
		if r >= 13:
			forestString += convertCharacter(random.choice(forest))

generateForest()

# with open('output.json', 'w') as out_f:
# 	json.dump(forestString, out_f)

OutputFile = open("output.txt","w",encoding="utf8") 
OutputFile.write(forestString)
OutputFile.close()
