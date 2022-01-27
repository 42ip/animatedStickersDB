import sys,os
arr = []
files = os.listdir(sys.path[0] + '/stickersraw')
st = "{{$a :=  index .CmdArgs 0 }} \n"
st += "{{$b := cslice "
names = []
for fileName in files:
    names.append(fileName.split('.')[0])
names = sorted(names)
n = ""
for name in names:    
    n += "\"" + name + "\" "
st += n
st += """ }}
{{if or (eq $a "stickers") (eq $a "gifs") (eq $a "gif") }} 
	{{deleteTrigger 0 }}
	{{if eq (len .Args) 1}}
		{{$r := joinStr " " $b.StringSlice}}
		{{$r}}
	{{else if eq (len .Args) 2}}
	 	{{$c := index .CmdArgs 1}}
		{{$s := cslice " " }}
		{{range $index,$value := $b}}
			{{- if hasPrefix $value $c -}}
				{{$s = $s.Append $value}}
			{{- end -}}
		{{- end}}
		{{$r := joinStr " " $s.StringSlice}}
		{{$r := str $r}}
		{{$r}}
	{{end}}
{{end}}
{{range $b}} 
	 {{- if eq . $a -}}
	 {{- $link := joinStr "" "https://github.com/42ip/animatedStickersDB/blob/main/stickersraw/"  $a  ".gif?raw=true" -}} 
	 {{- $link -}} 
	 {{- end -}} 
{{- end}}"""

with open(sys.path[0] + "/output.yag", "w") as text_file:
    text_file.write(st)