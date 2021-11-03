# loop to add emojis to the .json file.
import json,sys,os
d = dict()
# The custom code will appear on the output.txt file. just copy and paste into the place
with open(sys.path[0] + '/stickers.json', 'r+') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
    d = json_object
startfile = "{{$a :=  index .CmdArgs 0 }} \n"
endfile = "{{end}}"
fileno = 1
def updatePath(i):
    PATH = sys.path[0] + "/outputs/output{}.txt".format(i)
    return PATH
PATH = sys.path[0] + "/outputs/output{}.txt".format(fileno)
f = open(PATH, "w")
f.write(startfile)
f.write("{{if or (eq $a \"stickers\") (eq $a \"gifs\") (eq $a \"gif\") }}");f.write("\n")
f.write("{{deleteTrigger 0 }}");f.write("\n")
# todo: need to create a failsafe where the search gifs , if it ever exceeds 8000 characters, must overflow into the next command properly.
# This section will allow you to see the gifs with the first letter as index.
f.write("{{if eq (len .Args) 1}}")
arr = sorted([d[key][0] for key in d])
print(arr)
f.write(" ".join(arr) + "\n")
f.write("{{else if eq (len .Args) 2}}\n")
f.write("{{$b := index .CmdArgs 1}}\n")
for letter in "abcdefghijklmnopqrstuvwxyz":
    listed = " ".join(list(filter(lambda string: string[0].lower() == letter,arr)))
    f.write("{" + "{{{next} if eq (lower $b) \"{l}\"}}".format(next="else" if letter != 'a' else "" ,l=letter) + "}\n" + (listed if len(listed) > 0 else "none found :(") + "\n")
f.write("{{end}}{{end}}\n")
f.write(r"{{ deleteResponse 30 }}");f.write("\n")
# this section ends here

start = False

def giveString(arr,start):
    s = ""
    if len(arr) == 2:
        s =  "{"+("{{if eq $a \"{}\" }}".format(arr[0]) if start else "{{else if eq $a \"{}\" }}".format(arr[0])) + "}\n" if arr[0] != 'waa' else "{" + "{{ else if reFind  \"^wa*a$\" $a }}".format(arr[0]) + "}\n"
        s += "\t"
    else:
        s = "{" + ("{if or " if start else "{ else if or ")
        for name in arr[:-1]:
            s += "(" + "eq $a \"{}\" ) ".format(name)
        s += "}" + "}\n\t"
    s += arr[-1]
    s += "\n"
    return s

for key in d:
    f.write(giveString(d[key],start))
    start = False
    currsize = os.path.getsize(PATH)
    if currsize > 7500:
        print("new file created")
        start = True
        f.write(endfile)
        fileno += 1
        PATH = updatePath(fileno)
        f = open(PATH,"w")
        f.write(startfile)
f.write(endfile)
f.close()
     




