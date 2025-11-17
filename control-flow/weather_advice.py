weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure you wear a warm coat and a scalf.")
else:
    print("Sorry, I don't have recommendetations for this weather.")