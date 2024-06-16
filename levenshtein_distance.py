def levenshtein_distance(token1, token2):
    # Strip whitespace from the tokens
    token1 = token1.strip()
    token2 = token2.strip()
    
    if len(token1) < len(token2):
        token1, token2 = token2, token1

    # Initialize matrix of zeros with the size of (len(token1) + 1) x (len(token2) + 1)
    distances = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]

    # Populate the matrix with initial values
    for i in range(len(token1) + 1):
        distances[i][0] = i
    for j in range(len(token2) + 1):
        distances[0][j] = j

    # Iterate over the matrix to compute the Levenshtein distance
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1

            distances[i][j] = min(
                distances[i - 1][j] + 1,      # deletion
                distances[i][j - 1] + 1,      # insertion
                distances[i - 1][j - 1] + cost # substitution
            )

    # The distance is found in the bottom right corner of the matrix
    return float(distances[-1][-1])

# Example usage and assertions
assert levenshtein_distance("hi", "hello") == 4
print(levenshtein_distance("hola", "hello"))  