
value = int(input())


if value >= 25:
	print("Error")


# "Inside the loop, my variable is {ค่าปัจจุบัน}"
else:
	for num in range(value, 25):
		print(f"Inside the loop, my variable is {num}")
