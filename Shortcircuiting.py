a = 2
p = (2 <= 10) or (a := 4)
print(f"a={a}")

b = 2
p = (2 > 10) or (b := 4)
print(f"b={b}")

c, d = 2, 2
p = (2 > 10) or (c := 4) or (d := 4)
print(f"c={c} d={d}")
