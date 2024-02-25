my_dict = {
    "bakery": ["bread", "rolls", "donut"],
    "grocery store": ["carrots", "celery", "arugula"],
    "sweets shop": ["haribos", "chewing gum"]
}
for shop, item in my_dict.items():
   for i in range(len(item)):
        item[i] = item[i].capitalize()
   print(f'I am going to the {shop.capitalize()} where I will buy {my_dict[shop]}')
x = 0
for word in my_dict.values():
    x = x + len(word)
print(f'I am buying {x} items')
print("1st commit of this task")
for i in range(1,5):
    for j in range(2):
        print(i*"**")   