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


""" 
l = 0
notl = 0
x = input("Yo yo what you gotta say?")
for i in range (len(x)):
    if x[i] == "l":
        l += 1
    elif x[i] in "qwertyuiopasdfghjkzxcvbnm":
        notl += 1
   
if l >= (notl / 5):
    print ("Love Letter")
else:
    print ("Just talking")
 """

""" Total = 0
HONI = 0
Clause = ("HONHINOHINOHINOHINOIHONIOHINOHINOHIONIHONIOHINOIHONIHONIOHINOHINOHIONHONIHONIOHNIOHNIHONIOHINHONHONIOHNOHIONIHONIHOINHOINOHINHOINOHINOHIONIHONIOHINOHIONHIOHNIO")
length = (len(Clause))
for i in range (length):
    if Clause[i] == "H" and HONI == 0:
        HONI += 1
    if Clause[i] == "O" and HONI == 1:
        HONI += 1
    if Clause[i] == "N" and HONI == 2:
        HONI += 1
    if Clause[i] == "I" and HONI == 3:
        HONI = 0
        Total += 1
print (Total)
 """


""" 

x = input("Gimmie password")
length = len(x)
char = False
Cap = 0
Capital = False
Low = 0
Lowercase = False
Dig = 0
Digit = False
Invalid = False
Valid = False

for i in range (length):
    if x[i] in ("abcdefghijklmnopqrstuvwxyz"):
        Low += 1
    elif x[i] in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        Cap += 1
    elif x[i] in ("1234567890"):
        Dig += 1
    else:
        Invalid = True

if Low >= 2:
    Lowercase = True
if Cap >= 3:
    Capital = True
if Dig >= 1:
    Digit = True
if length >= 8 and length <=12:
    char = True

if Lowercase == True and Capital == True and Digit == True and char == True and Invalid == False:
    Valid = True
else:
    Valid = False

if Valid == True:
    print ("Valid")
elif Valid == False:
    print ("Invalid") """



""" m1 = 10
m2 = 62
m3 = 35
Total = 1003
Totalp = 0
Broke = False

while Broke == False:
    Total -= 1
    m1 += 1
    Totalp += 1
    if m1 == 35:
        Total += 30
    if Total == 0:
        Broke = True
    if Broke == True:
        break
        Total -= 1
    m2 += 1
    Totalp += 1
    if m2 == 100:
        Total += 60
    if Total == 0:
        Broke = True
    if Broke == True:
        break
    Total -= 1
    m3 += 1
    Totalp += 1
    if m3 == 10:
        Total += 9
    if Total == 0:
        Broke = True
    if Broke == True:
        break 

print (f"She played {Totalp} games before she went broke")
print (m1)
print (m2)
print (m3)
print (Total) """