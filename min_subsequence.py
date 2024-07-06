def min_subsequences(source, target):
    source_dict = {}
    for index, char in enumerate(source):
        if char not in source_dict:
            source_dict[char] = []
        source_dict[char].append(index)
    
    min_subseq = 1
    source_len = len(source)
    source_index = -1 

    for char in target:
        if char not in source_dict:
            return -1
        found = False
        for index in source_dict[char]:
            if index > source_index:
                source_index = index
                found = True
                break
        if not found:
            min_subseq += 1
            source_index = source_dict[char][0]
    return min_subseq

# Test cases       
print(min_subsequences("abc", "abcbc"))  # Output: 2
print(min_subsequences("abc", "acdbc"))  # Output: -1
print(min_subsequences("xyz", "xzyxz"))  # Output: 3
