def main():
	VAR: int = None
	VAR = input()
	if VAR == 1:
		VAR -= 1
	elif VAR == 4:
		VAR += 7
		VAR /= 2
	else:
		VAR *= 10
	print(VAR)
