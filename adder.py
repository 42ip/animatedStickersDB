# loop to add emojis to the .json file.
from mdMaker import mdMaker
import json,sys
d = dict()

with open(sys.path[0] + '/stickers.json', 'r+') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    d = json_object
cont = ""
# One by one space seperated the stickers should be added;
# Eg : 
###   usewhenprashspeaks  {url link for the sticker}
###   yellowman {url link for the sticker}
###  just press enter (to end the loop and save the json file.)
while cont != "100":
      a = input().split(" ")
      if len(a) !=  2:
            cont = '100'
      else:
        d[a[0]] = a[1]
obj = json.dumps(d,indent= 1)
with open(sys.path[0] + "/stickers.json", "w") as outfile:
    outfile.write(obj)
mdMaker(d)