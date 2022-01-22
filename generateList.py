import sys,os
arr = []
files = os.listdir(sys.path[0] + '/stickersraw')
st = "{{$a :=  index .CmdArgs 0 }} \n"
st += "{{$b := cslice "
names = []
for fileName in files:
    st += '"' + fileName.split('.')[0] + '"'
    st += " "
    names.append(fileName.split('.')[0] + " ")
st += "}} \n"
st += '{{if or (eq $a "stickers") (eq $a "gifs") (eq $a "gif") }} \n'
st += '{{' + 'deleteTrigger 0 }}\n'
st += '{{if eq (len .Args) 1' + '}}'
st += ' '.join(names) + '\n'
st += "{{" + "end}}" + "{{" + "end}}"
st += "{{range $b}} \n"
st += '\t {{- if eq . $a -}}\n'
st += '\t {{- $link := joinStr "" "https://github.com/42ip/animatedStickersDB/blob/main/stickersraw/"  $a  ".gif?raw=true" -}} \n'
st += '\t {{- $link -}} \n'
st += '\t {{- end -}} \n'
st += '{{- end}}'	
	

with open("output.txt", "w") as text_file:
    text_file.write(st)