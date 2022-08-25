n = int(input("Please enter the number of days.."))

res = [] # containing all the permutations for n days
letters = ['A', 'P'] # A is for absent, P is for present

def perm(n,combo):
    """Function to generate all possible combinations of length n and store them in res"""
    if len(combo) == n:
        res.append(combo)
        return
    else:
        for letter in letters:
            perm(n, combo + letter)


#calling the function
perm(n, '')

# we cannot miss classes for 4 or more days
# hence strings containing AAAA are invalid days

#valid will contain all the ways in which classes can be attended
valid = list(filter(lambda x: 'AAAA' not in x, res)) 

# graduation ceremony will be missed when A occurs on the last day
# missed_grad contains all combos when A occurs last
missed_grad = list(filter(lambda x: x[-1]=='A', valid))

# Answer 1 - The number of ways to attend classes over N days.
# This will be length of valid
a1 = len(valid)

# Answer 2- The probability that you will miss your graduation ceremony.
a2 = str(len(missed_grad)) + '/' + str(a1)

print(f'Answer 1- The number of ways to attend classes over N = {n} days is {a1}')
print(f'Answer 2- The probability that you will miss your graduation ceremony is {a2}')


