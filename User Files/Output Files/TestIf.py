def main():
	VAR1: int = None
	VAR2: int = None
	VAR1 = 2
	VAR2 = input()
	VAR1 *= VAR2
	if VAR1 <= 10:
		VAR1 = 15 * VAR2
	else:
		VAR1 -= VAR2
		VAR1 = VAR1 + 5
		VAR2 = 10 / 5
	VAR1 = VAR1 + VAR2
	print(VAR1)
