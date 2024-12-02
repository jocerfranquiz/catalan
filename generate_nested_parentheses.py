def generate_nested_parentheses(n):
    """
    Generate all strings of n pairs of nested parentheses in lexicographic order.
    Args:
        n (int): Number of pairs of parentheses (n >= 2)
    Yields:
        str: Each valid string of nested parentheses
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    
    # P1. Initialize
    a = [''] * (2*n + 1)  # +1 for the sentinel a[0]
    a[0] = ')'  # sentinel
    for k in range(1, n+1):
        a[2*k-1] = '('
        a[2*k] = ')'
    m = 2*n - 1
    
    while True:
        # P2. Visit
        yield ''.join(a[1:2*n+1])  # Convert to string, excluding sentinel
        
        # P3. Easy case?
        a[m] = ')'
        if a[m-1] == ')':
            a[m-1] = '('
            m -= 1
            continue
            
        # P4. Find j
        j = m - 1
        k = 2*n - 1
        while a[j] == '(':
            a[j] = ')'
            a[k] = '('
            j -= 1
            k -= 2
            
        # P5. Increase a[j]
        if j == 0:  # Termination condition
            break
        a[j] = '('
        m = 2*n - 1

# Example usage
def print_all_nested_parentheses(n):
    print(f"All nested parentheses strings for n = {n}:")
    for i, p in enumerate(generate_nested_parentheses(n), 1):
        print(f"{i}. {p}")

# Test cases
if __name__ == "__main__":
    # Test with n = 2
    print_all_nested_parentheses(2)
    print()
    
    # Test with n = 3
    print_all_nested_parentheses(3)
    print()
    
    # Test with n = 3
    print_all_nested_parentheses(4)
    print()
    
    # Test with n = 3
    print_all_nested_parentheses(5)
    print()
    
    # Test with n = 3
    print_all_nested_parentheses(6)
