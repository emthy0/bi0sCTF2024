#! /opt/homebrew/bin/python3
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

# Example usage
prime_factors = [2]
possible_numbers = find_possible_numbers(prime_factors)
print(possible_numbers)