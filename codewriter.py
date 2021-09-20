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
f.write("{{if eq $a \"stickers\" }}");f.write("\n")
arr = sorted([d[key][0] for key in d])
f.write(" ".join(arr))
f.write("\n")
start = False

def giveString(arr,start):
    s = ""
    if len(arr) == 2:
        s =  "{"+("{{if eq $a \"{}\" }}".format(arr[0]) if start else "{{else if eq $a \"{}\" }}".format(arr[0])) + "}\n"
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
     




