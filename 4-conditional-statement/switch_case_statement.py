animal_name = "Tiger"

# Switch statement implementation
match animal_name:
    case "Lion":
        print("Lion case")
    case "Elephant":
        print("Elephant case")
    case "Leopard":
        print("Leopard case")
    case "Tiger":
        print("Tiger case")
    case "Cow":
        print("Cow case")
# Result: case "Tiger"

animal_name = "Cat"
# Switch statement if there is no any case match example
match animal_name:
    case "Lion":
        print("Lion case")
    case "Elephant":
        print("Elephant case")
    case "Leopard":
        print("Leopard case")
    case "Tiger":
        print("Tiger case")
    case "Cow":
        print("Cow case")
    case _:
        print("Unknown case")
# Result: case `_`
