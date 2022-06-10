def are_coprime(n, m):
    list_n = [i for i in range(1, n + 1) if n % i == 0]
    list_m = [i for i in range(1, m + 1) if m % i == 0]
    return len(list(set(list_n) & set(list_m))) == 1
