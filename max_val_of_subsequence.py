# if we generate all sequences, the time complexity is definilaity o(n^2), however, we can reduce by testing the max value of the subsequence dynamically
def max_val_of_subsequence(a):
    n = len(a)
    if n < 2:
        return float('-inf')
    
    a.sort()
    
    max_val = float('-inf')
    
    def mean(subseq):
        return sum(subseq) / len(subseq)
    
    def median(subseq):
        length = len(subseq)
        if length % 2 == 1:
            return subseq[length // 2]
        else:
            mid = length // 2
            return (subseq[mid - 1] + subseq[mid]) / 2
    
    left = 1
    right = n - 1
    
    while left <= right:
        
        subseq = a[:left] + a[right:]
        mean_val = mean(subseq)
        median_val = median(subseq)
        val = mean_val - median_val
        if val > max_val:
            max_val = val
        
        
        if mean_val > median_val:
            right -= 1
        else:
            left += 1
    
    return max_val

# Test cases
a = [1, 3, 5, 9]
result = max_val_of_subsequence(a)
print(result) 

