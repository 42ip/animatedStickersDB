# loop to add emojis to the .json file.
import json,sys
d = dict()
# The custom code will appear on the output.txt file. just copy and paste into the place
f = open(sys.path[0] + "/output.txt", "w")
f.write("{{$a :=  index .CmdArgs 0 }} \n")
with open(sys.path[0] + '/stickers.json', 'r+') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    d = json_object
h = True
for key in d:
      if h:
        f.write("{");f.write("{{if eq $a \"{}\" }}".format(key));f.write("}");f.write("\n")
        h = False
      else:
          f.write("{");f.write("{{else if eq $a \"{}\" }}".format(key));f.write("}");f.write("\n")
      f.write("\t");f.write(d[key]);f.write("\n")
f.write("{{end}}")

