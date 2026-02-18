def lcs_dp(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtracking to get LCS string
    i, j = m, n
    lcs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs.reverse()
    return dp[m][n], "".join(lcs)


# Example
s1 = "ABCBDAB"
s2 = "BDCABA"

length, sequence = lcs_dp(s1, s2)

print("LCS Length:", length)
print("LCS:", sequence)
