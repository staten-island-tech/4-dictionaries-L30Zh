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





