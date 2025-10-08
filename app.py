""" english = 't' or 'T'
french = 's' or 'S'
t_count = 0
s_count = 0
clause = input("What you wanna say") 
for char in clause:
        if char == english:
            t_count += 1
        elif char == french:
            s_count += 1
if s_count < t_count:
            print("English")
else:
    print ("French") """




""" 
Total = 0
Duped = 0
(yest, tod) = ("CC.C...", "..CC...")
Space = (yest, tod)
YEST = list(yest)
TOD = list(tod)

for char in YEST:
    Total += 1
    print (Total)

for i in range (0, Total):
    if YEST[i] == "C" and TOD[i] == "C":
        Duped += 1
print(Duped)

        
 """

""" Duped = 0
(yest, tod) = ("CCCCCCC", "C.C.C.C")

for i in range (len(yest)):
    if yest[i] == "C" and tod[i] == "C":
        Duped += 1
print(Duped)
 """




    