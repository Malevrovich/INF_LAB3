import re

inp = input()

id = 335146

smile = ""

if id % 5 == 0:
	smile += ":"
elif id % 5 == 1:
	smile += ";"
elif id % 5 == 2:
	smile += "X"
elif id % 5 == 3:
	smile += "8"
else:
	smile += "="

if id % 4 == 0:
	smile += "-"
elif id % 4 == 1:
	smile += "<"
elif id % 4 == 2:
	smile += "-{"
else:
	smile += "<{"

if id % 7 == 0:
	smile += "("
elif id % 7 == 1:
	smile += ")"
elif id % 7 == 2:
	smile += "O"
elif id % 7 == 3:
	smile += "|"
elif id % 7 == 4:
	smile += "\\"
elif id % 7 == 5:
	smile += "/"
else:
	smile += "P"

print(smile)

print(len(re.findall(r';-{\(', inp)))

#TESTS
#;-{( abs;-{(  ;-}( :+;{ ;--{(;;-{(;-{(  ::;-{()( => 5
#;-{( => 1
#;;--{{(( => 0
#"" => 0
#;:;-{()  ;-{) => 1
#i'm sad... ;-{( i'm happy ;-{) => 1
