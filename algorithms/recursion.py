def n_sum(n):
    if n == 1:
        return 1
    return n + n_sum(n-1)


if __name__ == "__main__":
    n = 5
    result = n_sum(n)
    print(result)
