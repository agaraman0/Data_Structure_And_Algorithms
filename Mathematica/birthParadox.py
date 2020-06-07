# Birthdayparadox

def birthdayParaox(p):

	if p == 1:
		return 366

	prob = 1
	people = 0

	numer = 365
	denor = 365

	while p >= 1 - prob or people <2:

		prob = prob * (numer/denor)

		numer = numer - 1
		people = people + 1

		print(people,"People Required in Room for two People to have Birthday on Same Day with Probability",1-prob)

	return people

print(birthdayParaox(0.50))