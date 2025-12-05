items = [
{
"name": "banana",
 "price": 0.50,
 "category": "Grocery",
 "description": "Long yellow thang"},

{
"name": "apple",
 "price": 1.00,
 "category": "Grocery",
 "description": "Keeps the doctor away"},

{
"name": "watermelon",
 "price": 4.00,
 "category": "Grocery",
 "description": "Big green fruit"},

 {
"name": "microwave",
 "price": 80.00,
 "category": "Technology",
 "description": "Heats food"},

{
"name": "air fryer",
 "price": 35.00,
 "category": "Technology",
 "description": "Relic of maan"},

{
"name": "tv remote",
 "price": 15.00,
 "category": "Technology",
 "description": "It's a remote for your tv"},

{
"name": "bird",
 "price": 50.00,
 "category": "livestock",
 "description": "Sneaky winged cat"},

{
"name": "cat",
"price": 1250.00,
"category": "livestock",
"description": "Liquid with sentient thoughts",},

{
"name": "hamster",
 "price": 25.00,
 "category": "livestock",
 "description": "Socially accepted mouse"}

]


Price = 0
cart = []
done = False
ItemReal = False
for index, item in enumerate(items):
    print (index, ":", item["name"])
while done == False:
    x = input("Pick an item")
    for item in items:
        if x.lower() == item["name"].lower():
            ItemReal = True
            cart.append(x)
            Price += item["price"]
    if ItemReal == False:
        print ("I dont think that exists")
    Price += (item["price"])
    ItemReal = False
    y = input("Is that all? yes/no")
    if y == "yes":
        done = True
        print("Ok, pay up")
        done = True
        if done == True:
            break
Price -= 25
print(cart)
print(f"Okay, your total is {Price} dollars.")





<<<<<<< HEAD
=======
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
>>>>>>> a2850493aa497c6c8f4dd750aa6c8a73c1163d67
