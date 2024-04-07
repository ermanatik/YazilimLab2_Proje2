def brute_force_min_differences(dizi):
    n = len(dizi)
    min_farklar = []

    for i in range(n-1):
        for j in range(i+1, n):
            fark = abs(dizi[i] - dizi[j])
            min_farklar.append(fark)

    min_farklar.sort()
    return min_farklar[:n//2]


def sirali_min_farklar(dizi):
    dizi.sort()
    n = len(dizi)
    min_farklar = []

    for i in range(n-1):
        fark = abs(dizi[i] - dizi[i+1])
        min_farklar.append(fark)

    min_farklar.sort()
    return min_farklar[:n//2]
