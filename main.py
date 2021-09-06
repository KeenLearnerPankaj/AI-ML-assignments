import json

print("Hello Sir, It's Pankaj Sangle.\nWelcome to Inventory management System 🐥 ")


should_continue = True
while should_continue:
    entry = input("Type 'add' to add product or 'buy' to purchase any product.\n").lower()

    def add_item():

        file = open("record.json", 'r')
        r = file.read()
        file.close()
        record = json.loads(r)
        print(record)

        # Adding  new product

        prod_id = int(input("Enter product id:\n"))
        name = (input("Enter product name:\n"))
        price = int(input("Enter the price of product:\n"))
        quantity = int(input("Enter quantity:\n"))

        record[prod_id] = {'name': name, 'price': price, 'quantity': quantity}  # For adding new item
        js = json.dumps(record)                                      # dumps for making string cause write function
        print(js)                                                    # only works on string not on dict
                                                                     # for below code to execute
        fd = open("record.json", 'w')
        fd.write(js)
        fd.close()

    def buy_item():

        file = open("record.json", 'r')
        r = file.read()
        file.close()
        record = json.loads(r)
        print(record)

        ui_product = (input("Enter the product_Id: "))
        ui_quantity = int(input("Enter the quantity: "))

        print("Product: ", record[ui_product]['name'])
        print("Price: ", record[ui_product]['price'])
        print("Billing Amount: ", record[ui_product]['price'] * ui_quantity)

        record[ui_product]['quantity'] = record[ui_product]['quantity'] - ui_quantity

        js = json.dumps(record)
        fd = open("record.json", 'w')
        fd.write(js)
        fd.close()

        # For sale.json file to add sales info.

        # fd = open("sales.json", 'r')
        # s = fd.read()
        # fd.close()
        # sales = json.loads(s)

        sales =  {'product id': ui_product, 'quantity-purchased': ui_quantity, 'amount-paid':            record[ui_product]['price'] * ui_quantity}

        string_sale = json.dumps(sales)+"\n"
        print(string_sale)
        fd = open("sales.json", 'a')
        fd.write(string_sale)
        fd.close()


    if entry == "add":
        add_item()
    elif entry == "buy":
        buy_item()
    else:
        print("Your choice is wrong! choose again!")

    loop = input("type 'Y' to continue or 'N' to stop\n").lower()
    if loop == "n":
        should_continue = False
    elif loop == "y":
        should_continue = True




