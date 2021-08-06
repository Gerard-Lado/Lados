products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    for k, v in products.items():
        if k == code:
            return v
        else:
            pass
    
get_product("espresso")

def get_property(code, property):
    for l, m in products.items():
        if l == code:
            return m[property]
        else:
            pass
get_property("espresso", "name")

def main():
    total = 0
    entered_code = input("Input order code: ")
    order_quantity = int(input("Quantity: "))
    name = get_property(entered_code, "name")
    subtotal = order_quantity * int(get_property(entered_code, "price"))
    total = total + subtotal
    with open("receipt.txt", "w") as order_list:
        order_list.write(f"""==
                        CODE\t\t\t\t\tNAME\t\t\t\tQUANTITY\t\tSUBTOTAL
                        {entered_code}\t\t\t{name}\t\t\t{order_quantity}\t\t\t{subtotal}
                        """)
    while entered_code != "/":
        entered_code = input("Input order code: ")
        if entered_code == "/":
            break
        order_quantity = int(input("Quantity: "))
        name = get_property(entered_code, "name")
        subtotal = order_quantity * int(get_property(entered_code, "price"))
        total = total + subtotal
        with open("receipt.txt", "a") as order_list:
            order_list.write(f"""
                        {entered_code}\t\t\t{name}\t\t\t{order_quantity}\t\t\t{subtotal}
                        """)
    with open("receipt.txt", "a") as receipt:
        receipt.write(f"""
                        Total:\t\t\t\t\t\t\t\t\t\t{total}
==""")                        

main()
