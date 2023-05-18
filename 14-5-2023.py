def findMinimumDeletion(left, right, dp, string):
    """
    Calculates the minimum number of delete operations required to transform a substring of 'string' from index 'left' to index 'right'.

    Parameters:
        left (int): The left index of the current substring.
        right (int): The right index of the current substring.
        dp (list): The memoization array to store previously calculated minimum delete operations.
        string (str): The input string.

    Returns:
        int: The minimum number of delete operations required for the substring 'string[left:right]'.
    """
    # Base case: If there are no characters between 'left' and 'right', return 0
    if left > right:
        return 0

    # Base case: If there is only one character at 'left' and 'right', return 1
    if left == right:
        return 1

    # Check if minimum delete operations for the current substring have already been computed
    if dp[left][right] != -1:
        return dp[left][right]

    # Initialize 'result' with 1 + minimum delete operations for the next substring
    result = 1 + findMinimumDeletion(left + 1, right, dp, string)

    # Iterate through each index 'i' from 'left + 1' to 'right'
    for i in range(left + 1, right + 1):
        # If character at 'left' is equal to character at 'i'
        if string[left] == string[i]:
            # Calculate minimum delete operations for two scenarios:
            # 1. Delete characters between 'left + 1' and 'i - 1'
            # 2. Delete characters starting from 'i'
            result = min(
                result,
                findMinimumDeletion(left + 1, i - 1, dp, string) + findMinimumDeletion(i, right, dp, string)
            )

    # Store the calculated minimum delete operations in 'dp' for future reference
    dp[left][right] = result

    # Return the minimum delete operations for the current substring
    return result


series = "kjslaqpwoereeeeewwwefifjdksjdfhjdksdjfkdfdlddkjdjfjfjfjjjjfjffnefhkjgefkgjefkjgkefjekihutrieruhigtefhgbjkkkknbmssdsdsfdvneurghiueor"
n = len(series)
N = n + 1
dp = [[-1 for i in range(N)]
        for j in range(N)]
print("The minimum steps to delete the series is {}" .format(findMinimumDeletion(0, n - 1, dp, series)))