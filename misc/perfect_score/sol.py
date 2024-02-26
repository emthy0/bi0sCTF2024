#! /opt/homebrew/bin/python3
import sympy
import pwn
import math
from itertools import product



def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

def find_possible_numbers(prime_factors, limit=10000):
    """
    Finds all possible numbers within a limit that can be formed from the given prime factors.

    Args:
        prime_factors: A list of prime factors.
        limit: The maximum value for the possible numbers.

    Returns:
        A set of all possible numbers.
    """

    results = set()
    def generate_combinations(index, current_product):
        if current_product >= limit:
            return

        if index == len(prime_factors):
            results.add(current_product)
            return

        # Calculate the maximum power of the current prime factor 
        max_power = 0
        while current_product * prime_factors[index] < limit:
            current_product *= prime_factors[index]
            max_power += 1

        # Generate combinations including all powers of the current prime factor
        for power in range(max_power + 1):
            generate_combinations(index + 1, current_product)
            current_product //= prime_factors[index] 

    generate_combinations(0, 1) 
    return results


# primeList = [list(sympy.primerange(0, 1000*i)) for i in range(1, 11)]
# print(primeList)
r = pwn.remote('13.201.224.182', 30951)
print("> " + r.recv().decode("utf-8"))
for _ in range(10):
	queue = [*split_list(list(sympy.primerange(0, 10000)))]
	lowerbound = 0
	upperbound = 10000
	step = 0
	outQueue = []
	while len(queue) > 0:
		primeList = queue.pop(0)
		if len(primeList) <= 1:
			print(primeList)
			outQueue.append(primeList[0])
			continue
			# step = 1
			# break
		r.recvuntil(">> ".encode("utf-8"))
		# print(r.recvuntil(">> ".encode("utf-8")).decode("utf-8"))
		# r.send("2\n".encode("utf-8"))
		r.sendline(b'2')
		r.recv()
		# print("> " + r.recv().decode("utf-8"))
		# print(r.recvuntil(b"Array : ").decode("utf-8"))
		# print("> " + r.recv().decode("utf-8"))
		r.sendline(",".join([str(x) for x in primeList]).encode("utf-8"))
		r.recvuntil(b"such that gcd(x, y) > 1? ").decode("utf-8")
		isGCD = r.recvuntil(b"\n").decode("utf-8").strip()
		# print(half, i, isGCD)
		if isGCD == "Yes":
			l, h = split_list(primeList)
			queue += [l, h]
			# print(half)
	factorList = []
	for i in outQueue:
		r.recvuntil(">> ".encode("utf-8"))
		r.sendline(b'1')
		r.recv()
		r.sendline(str(i).encode("utf-8"))
		r.recvuntil(b"? ").decode("utf-8")
		isFactor = r.recvuntil(b"\n").decode("utf-8").strip()
		if isFactor == "Yes":
			print(i)
			factorList.append(i)
		# print(r.recvuntil(b"Congratulations!").decode("utf-8"))
		# print("> " + r.recv().decode("utf-8"))
	print(factorList)

	possible_numbers = find_possible_numbers(factorList)
	possible_numbers = sorted(list(possible_numbers), reverse=True)
	print(possible_numbers)

	for i in possible_numbers:
		r.recvuntil(">> ".encode("utf-8"))
		r.sendline(b'1')
		r.recv()
		r.sendline(str(i).encode("utf-8"))
		r.recvuntil(b"? ").decode("utf-8")
		isNumber = r.recvuntil(b"\n").decode("utf-8").strip()
		if isNumber == "Yes":
			print(i)
			r.recvuntil(">> ".encode("utf-8"))
			r.sendline(b'3')
			r.recvuntil(b"guess : ").decode("utf-8")
			r.sendline(str(i).encode("utf-8"))
			print(r.recvuntil(b'correct').decode("utf-8"))
			break
r.interactive()
