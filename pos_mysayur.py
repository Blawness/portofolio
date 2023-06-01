#Login function
def login(users):
    username = input("Username: ")
    password = input("Password: ")
    if username in users and password == users[username]:
        print(f"Welcome, {username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

#Register function
def register(users):
    username = input("Username: ")
    password = input("Password: ")
    users[username] = password
    print(f"User {username} has been registered.")

#Display list product
def display_products(products):
    print("************************************************************")
    print("                         PRODUCT LIST                       ")
    print("************************************************************")
    print("| No. |          Product          |          Price          |")
    print("************************************************************")
    for i, (name, price) in enumerate(products.items()):
        print(f"| {str(i+1).ljust(4)} | {name.ljust(26)} | Rp.{str(price).rjust(9)} |")
    print("************************************************************")


#Memproses order user
def process_order(products):
    order = {}
    while True:
        display_products(products)
        product_input = input("Masukan nomor produk (Ketik 'ok' jika ingin lanjut membayar): ")
        if product_input == "ok":
            break
        try:
            product_index = int(product_input) - 1
            if product_index < 0 or product_index >= len(products):
                print("Invalid product number")
                continue
            product_name = list(products.keys())[product_index]
            quantity = input("Quantity: ")
            try:
                quantity = int(quantity)
            except ValueError:
                print("Invalid quantity")
                continue
            order[product_name] = {"price": products[product_name], "quantity": quantity}
        except ValueError:
            print("Invalid product number")
            continue

    return order

#Mengkalkulasi harga total
def calc_total(order, tax_rate):
    subtotal = sum(details['price'] * details['quantity'] for details in order.values())
    tax = subtotal * tax_rate
    total = subtotal + tax
    return subtotal, tax, total

#Kembalian uang
def give_change(total, amount):
    change = amount - total
    return change

#Menjalankan POS
def execute_pos(products, tax_rate):
    order = process_order(products)
    subtotal, tax, total = calc_total(order, tax_rate)
    print("Ringkasan Pesanan")
    print("==============")
    for product, details in order.items():
        print(f"{product}: {details['quantity']} x Rp.{details['price']} = Rp.{details['price'] * details['quantity']}")
    print(f"Subtotal: Rp.{subtotal}")
    print(f"Pajak (10%): Rp.{tax}")
    print(f"Total: Rp.{total}")
    while True:
        amount = input("Masukkan jumlah pembayaran Anda: ")
        try:
            amount = int(amount)
            if amount < total:
                print("Maaf, uang Anda tidak cukup.")
                continue
            break
        except ValueError:
            print("Input tidak valid.")
    change = give_change(total, amount)
    print(f"Kembalian: Rp.{change}")
    print("Terima kasih telah berbelanja di MySayur.")

#Menu display
def display_menu():
    store_name = "MySayur"
    print("=" * 50)
    print(" " * 15 + "Selamat datang di" + " " + store_name)
    print("=" * 50)
    print("1. Registrasi")
    print("2. Login")
    print("3. Keluar")

#Data program
users_id = {"yudha" : "123",
            "ramdhan" : "ganteng",
            "fathan" : "pro123",
            "cakra" : "skuuds",
         }
tax_rate = 0.1
products_dict = {
    "Wortel": 8000,
    "Brokoli": 7000,
    "Jagung": 10000,
    "Cabai Merah": 15000,
    "Jamur": 12000,
    "Bawang Putih": 14000,
    "Oyong": 9000,
    "Tomat": 11000,
    "Kentang": 10000,
}

#Main program function

while True:
    display_menu()
    choice = input("Masukkan pilihan Anda: ")
    if choice == "1":
        register(users_id)
    elif choice == "2":
        if login(users_id):
            execute_pos(products_dict, tax_rate)
            break
    elif choice == "3":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
