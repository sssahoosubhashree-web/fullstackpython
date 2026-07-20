def print_info(**kwargs):
	for key,value in kwargs.items():
		print(key,":",value)
print_info(name="Alice",age=30,city="new york")
print_info(brand="Toyota",
model="Corolla",year=2020)