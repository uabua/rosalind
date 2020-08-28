"""
ID: LGIS
Title: Longest Increasing Subsequence
URL: http://rosalind.info/problems/lgis/
"""

def get_longest_increasing_subsequence(length, permutation):
    """
    Finds the longest increasing subsequence of permutation.

    Args:
        length {int}: length of permutation
        permutation {list}: permutation

    Returns:
        list: the longest increasing subsequence
    """
    sample = [None] * length
    permutations = [None] * length

    last = 1
    sample[0] = 0

    for index in range(1, length):
        lower = 0
        upper = last

        if permutation[sample[upper-1]] < permutation[index]:
            new_last = upper
        else:
            while (upper - lower) > 1:
                mid = (upper + lower) // 2

                if permutation[sample[mid - 1]] < permutation[index]:
                    lower = mid
                else:
                    upper = mid

            new_last = lower

        permutations[index] = sample[new_last-1]

        if new_last == last or permutation[index] < permutation[sample[new_last]]:
            sample[new_last] = index
            last = max(last, new_last+1)

    longest_increasing_subsequence = []
    index = sample[last-1]

    for _ in range(last):
        longest_increasing_subsequence.append(permutation[index])
        index = permutations[index]

    return longest_increasing_subsequence[::-1]

def read_file(file_path):
    """
    Reads input file.

    Args:
        file_path {str}: path of input file

    Returns:
        tuple: content of the file
    """
    with open(file_path, 'r') as file:
        length = file.readline().strip()
        permutation = [int(num) for num in file.readline().split()]

    return int(length), permutation

# after reading input file, we can assign values to length an permutation
# inputs = read_file("path")
# length = inputs[0]
# permutation = inputs[1]

def print_subsequences(length, permutation):
    """
    Prints longest increasing and decreasing subsequences of permutation.

    Args:
        length {int}: length of permutation
        permutation {list}: permutation

    Returns:
        None
    """
    longest_asc = map(str, get_longest_increasing_subsequence(length, permutation))
    longest_desc = map(str, get_longest_increasing_subsequence(length, permutation[::-1])[::-1])

    print(' '.join(longest_asc))
    print(' '.join(longest_desc))

