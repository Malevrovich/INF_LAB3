import re

def repl(m):
	num = int(m[0])
	return str(3 * num ** 2 + 5)

print(re.sub(r'-?\d+', repl, input()))
