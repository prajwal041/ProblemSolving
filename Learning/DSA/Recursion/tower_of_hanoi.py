def toh(n, f, t, aux):
    if n == 1:
        print(f"Move disk {n} from {f} to {t}")
        return
    toh(n-1, f, aux, t)
    print(f"Move disk {n} from {f} to {t}")
    toh(n-1, aux, t, f)

n= 100
toh(n,"A","B","C")