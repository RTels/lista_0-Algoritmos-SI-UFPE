import math

N = int(input())
comp_1 = input().split(" - ")
comp_2 = input().split(" - ")


def calculation(computer):
    if "n^2" in computer[3]:
        return 2 * (N ** 2) / int(computer[1])
    elif "n.logn" in computer[3]:
        return N * math.log10(N) / int(computer[1])
    elif "2^n" in computer[3]:
        return 2 ** N / int(computer[1])
    elif "n" in computer[3]:
        return N / int(computer[1])
    else:
        raise ValueError("Invalid complexity format")

comp_1_time = calculation(comp_1)
comp_2_time = calculation(comp_2)


print(f"Velocidade do {comp_1[0]}: {comp_1_time:.2f} segundos")
print(f"Velocidade do {comp_2[0]}: {comp_2_time:.2f} segundos")

if comp_1_time < comp_2_time:
    print(f"O {comp_1[0]} foi mais rápido!")
elif comp_2_time < comp_1_time:
    print(f"O {comp_2[0]} foi mais rápido!")
else:
    print("Ambos os computadores têm a mesma velocidade!")


"""
1. ask for number of instructions; OK
2. input computer 1 + instructions per second + algo name + complexity (2n^2, nlogn, 2^n and n.); OK
3. input computer 2 + instructions per second + algo name + complexity (2n^2, nlogn, 2^n and n.); OK
4. calculate the fastest PC; OK
5. print computer 1 speed: T seconds; OK
6. print computer 2 speed: T seconds; OK
7: print the fastest PC; OK
"""