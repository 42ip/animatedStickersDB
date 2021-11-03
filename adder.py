# loop to add emojis to the .json file.
from mdMaker import mdMaker
import json,sys
d = dict()

with open(sys.path[0] + '/stickers.json', 'r+') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    d = json_object

cont = True
# One by one space seperated the stickers should be added;
# Eg : 
###   usewhenprashspeaks  {url link for the sticker}
###   yellowman {url link for the sticker}
## you can add aliases if you like. just put it after the first name. minimum one name must be there and a url must be there
# eg vibe dancedood  https://cdn.discordapp.com/emojis/795467294604132363.gif?v=1 
# this will save to the json file both the names to the link.
###  just press enter (to end the loop and save the json file.)
c = len(d)
print(c)
while cont:
    c += 1
    a = input().split(" ")
    if len(a) <  2:
            cont = False
    else:
        d[c] = a
test = dict()
count = 1
for key in d:
    test[count] = d[key]
    count += 1
obj = json.dumps(test,indent= 1)
with open(sys.path[0] + "/stickers.json", "w") as outfile:
    outfile.write(obj)
mdMaker(d)