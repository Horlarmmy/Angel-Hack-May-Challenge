from itertools import permutations

def permute(string):
    # Convert the string to a list of characters
    char_list = list(string)

    # Generate all the permutations of the characters
    permutation_tuples = permutations(char_list)

    # Convert each permutation tuple to an integer
    permutations_int = [int(''.join(perm_tuple)) for perm_tuple in permutation_tuples]

    print("The possible permutations are {}" .format(permutations_int))
    new_list = []
    for i in permutations_int:
        if (i % 7 == 0):
            new_list.append(i)
    print("The ones that are divisible by 7 {}".format(sorted(new_list)))
    return ((max(new_list) + min(new_list))/2)

print("The average of the largest and smallest permutation is {}" .format(permute('1867')))