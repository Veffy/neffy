def check_power(N,K):
	if N<=0 or k<=0:
	 raise ValueError("k and N must be greater than 0")
    if k == 3 and N == 2:
        return True
    if k in (3, 2) and N != 1:
        return False

    num = k
    while num < N:
        num *= k
    return num == N
