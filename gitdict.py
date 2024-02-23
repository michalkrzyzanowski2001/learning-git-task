my_dict = {
    "bakery": ["bread", "rolls", "donut"],
    "grocery store": ["carrots", "celery", "arugula"],
    "sweets shop": ["haribos", "chewing gum"]
}
for shop, item in my_dict.items():
   for i in range(len(item)):
        item[i] = item[i].capitalize()
   print(f'I am going to the {shop.capitalize()} where I will buy {my_dict[shop]}')