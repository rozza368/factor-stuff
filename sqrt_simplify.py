# Input a surd, get a simplified surd

###   start plan
"""
input integer

for every integer above 0 until the
square root of input, check if the
square of that integer is a factor of
input

return sqrt of largest solution
then sqrt sign, then input divided
by square
"""

def main():
	to_sim = int(input("I want to simplify √"))
	sqrt = to_sim**0.5
	
	# no decimal places
	if sqrt % 1 == 0:
		print(int(sqrt), "\n")
		return

	factors = []
	for i in range(2, int(sqrt)):
		if is_factor(i**2, to_sim):
			factors.append(i**2)
	
	if factors:
		mx = max(factors)
		# returns in the format 2√5
		print(f"{int(mx**0.5)}√{to_sim//mx}")
	else:
		print(f"√{to_sim}")
	print()


def is_factor(fac, num):
	# impossible for factor > num/2
	if fac > num // 2:
		return False
	factors = set()
	for i in range(1, num//2):
		# if divides evenly
		if not num % i:
			factors.add(i)
	# true if the arg is a factor
	return fac in factors


# unit test for is_factor
def test(amt):
	for i in range(amt):
		print(i, is_factor(i, amt))


if __name__ == "__main__":
	while True:
		main()