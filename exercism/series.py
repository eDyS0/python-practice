def slices(number, n):
    slic = []

    if n > len(number) or n < 1:
        raise ValueError("Error. Length argument doesn't fit the series")

    for index in range(len(number) + 1 - n):
        substring = []
        substring_index = index
        while len(substring) < n:
            substring.append(int(number[substring_index]))
            substring_index += 1
        slic.append(substring)
    return(slic)