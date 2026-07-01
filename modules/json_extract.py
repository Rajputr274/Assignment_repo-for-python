import json

def json_extration():

    with open("product.json","r") as file:
        python_data=json.load(file)
        print(python_data["id"])
        print(python_data["title"])
        print(python_data["description"])
        print(python_data["category"])
        print(python_data["price"])
        print(python_data["discountPercentage"])
        print(python_data["rating"])
        print(python_data["stock"])
        print(python_data["tags"])

json_extration()
