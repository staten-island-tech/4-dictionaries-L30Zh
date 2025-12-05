Total = 77
m1 = 4
m2 = 9
m3 = 3
Totalp = 0

while Total != 0:
    Total -= 1
    m1 += 1
    Totalp += 1
    if m1 == 35:
        Total+=30
        m1 = 0
    if Total == 0:
        break
    Total -= 1
    m2 += 1
    Totalp += 1
    if m2 == 100:
        Total += 60
        m2 = 0
    if Total == 0:
        break
    Total -= 1
    m3 += 1
    Totalp += 1
    if m3 == 10:
        Total += 9
        m3 = 0
    if Total == 0:
        break

print (f"Martha plays {Totalp} times before going broke.")
