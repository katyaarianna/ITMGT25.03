# product dictionary
products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# problem 1
def get_product(code):
    return products[code]

# problem 2
def get_property(code,property):
    return products[code][property]

# problem 3
def main():
    americano_count = 0
    brewedcoffee_count = 0
    cappuccino_count = 0
    dalgona_count = 0
    espresso_count = 0
    frappuccino_count = 0
    total = 0
    orders = []
    customer_order = ""

    print("Welcome to the Coffee Shop!\n")
    while customer_order != "/":
        print("Follow the format {product_code},{quantity} when placing your order.\n")
        customer_order = input("Enter your order or '/' to quit: ")
        if customer_order != "/":
            code = customer_order.split(",")[0]
            if code not in orders:
                orders.append(code)
                orders.sort()
            else:
                pass

            quantity = int(customer_order.split(",")[1])
            if code == "americano":
                americano_count += quantity
            elif code == "brewedcoffee":
                brewedcoffee_count += quantity
            elif code == "cappuccino":
                cappuccino_count += quantity
            elif code == "dalgona":
                dalgona_count += quantity
            elif code == "espresso":
                espresso_count += quantity
            elif code == "frappuccino":
                frappuccino_count += quantity

    with open("receipt.txt", "w") as new_file:
        new_file.write(f'''==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n''')

        for code in orders:
            if code == "americano":
                quantity = americano_count
            elif code == "brewedcoffee":
                quantity = brewedcoffee_count
            elif code == "cappuccino":
                quantity = cappuccino_count
            elif code == "dalgona":
                quantity = dalgona_count
            elif code == "espresso":
                quantity = espresso_count
            elif code == "frappuccino":
                quantity = frappuccino_count

            name = get_product(code)["name"]
            subtotal = float(quantity) * get_property(code, "price")
            total += subtotal

            # dalgona formatting
            if code == "dalgona":
                new_file.write(f'''{code}\t\t\t{name}\t\t\t{quantity}\t\t\t\t{subtotal}\n''')
            elif code != "dalgona":
                new_file.write(f'''{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}\n''')

        new_file.write("\n")
        new_file.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{total}
==
    ''')

    with open("receipt.txt", "r") as read_file:
        reader = read_file.read()
        print(reader)


main()
# code end