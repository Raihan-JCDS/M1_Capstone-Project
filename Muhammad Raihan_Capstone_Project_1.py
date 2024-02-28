# Inisialisasi data awal inventory untuk CPU Intel dan AMD
inventory = {
    'Intel': [
        {'CPU_ID': 2001, 'Item': 'Core i3 10100F', 'Core_Thread': '4c/8t', 'Stock': 10, 'Price': 900000},
        {'CPU_ID': 2002, 'Item': 'Core i3 12100F', 'Core_Thread': '4c/8t', 'Stock': 10, 'Price': 1400000},
        {'CPU_ID': 2003, 'Item': 'Core i3 13100F', 'Core_Thread': '4c/8t', 'Stock': 10, 'Price': 1900000},
        {'CPU_ID': 2004, 'Item': 'Core i5 10400F', 'Core_Thread': '6c/12t', 'Stock': 10, 'Price': 1700000},
        {'CPU_ID': 2005, 'Item': 'Core i5 12400F', 'Core_Thread': '6c/12t', 'Stock': 10, 'Price': 2200000},
    ],
    'AMD': [
        {'CPU_ID': 1001, 'Item': 'Ryzen 5 5600', 'Core_Thread': '6c/12t', 'Stock': 10, 'Price': 2100000},
        {'CPU_ID': 1002, 'Item': 'Ryzen 5 7600', 'Core_Thread': '6c/12t', 'Stock': 10, 'Price': 3500000},
        {'CPU_ID': 1003, 'Item': 'Ryzen 7 5700X', 'Core_Thread': '8c/16t', 'Stock': 10, 'Price': 3000000},
        {'CPU_ID': 1004, 'Item': 'Ryzen 7 7700', 'Core_Thread': '8c/16t', 'Stock': 10, 'Price': 5650000},
        {'CPU_ID': 1005, 'Item': 'Ryzen 9 7900', 'Core_Thread': '10c/20t', 'Stock': 10, 'Price': 7000000},
    ]
}

edit_logs_list = []

# Fungsi untuk menampilkan inventory
def show_inventory(category):
    print(f"=== List CPU {category.upper()} ===")
    print(f"No.     |CPU_ID  |Item                    |Core/Thread    |Stock   |Price")
    for i, item in enumerate(inventory[category], 1):
        print(f"{i:<8}|{item['CPU_ID']:<8}|{item['Item']:<24}|{item['Core_Thread']:<15}|{item['Stock']:<8}|{item['Price']:<10}")

def show_inventory_all():
    print("\033c", end=' ')
    print("=== All Inventory ===")
    for category in inventory:
        show_inventory(category)

def show_single_item_by_id(category):
    cpu_id = int(input("Enter CPU_ID to display details (or 0 to go back): "))

    if cpu_id == 0:
        return

    # Check if the item with the given CPU_ID exists
    item_to_display = next((item for item in inventory[category] if item['CPU_ID'] == cpu_id), None)

    if item_to_display:
        print("\033c", end =' ')
        print("\n=== Item Details ===")
        show_inventory_table([item_to_display])
    else:
        print("\033c", end =' ')
        print("Data does not Exist. Please enter a valid CPU_ID.")

# Fungsi untuk menampilkan submenu konfirmasi
def show_submenu_confirmation():
    while True:
        print("=== Submenu Confirmation ===")
        print("1. Confirm Action")
        print("2. Cancel Action")
        print("3. Back to main menu")
        print("4. Exit program")

        submenu_choice = input("Enter your choice: ")

        if submenu_choice == '1':
            print("\033c", end =' ')
            return True
        elif submenu_choice == '2':
            print("\033c", end =' ')
            return False
        elif submenu_choice == '3':
            print("\033c", end =' ')
            break
        elif submenu_choice == '4':
            print("\033c", end =' ')
            print("Exiting program. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please enter a valid option.")

# Fungsi untuk memilih category CPU
def choose_category():
    print("Choose Category:")
    print("1. AMD")
    print("2. Intel")
    print("3. Back to main menu")
    print("4. Exit program")
    category_choice = input("Enter your choice: ")
    return category_choice


# Fungsi untuk menambahkan item ke inventory
def add_item(category):
    print(f"=== List CPU {category.upper()} ===")
    show_inventory(category)

    while True:
        try:
            cpu_id = int(input("Enter new CPU_ID number: "))

            # Check if CPU_ID already exists in either category
            if any(item['CPU_ID'] == cpu_id for cat in inventory.values() for item in cat):
                print("Data Already Exists. Enter a New CPU_ID.")
                continue

            item_name = input("Enter new item name: ").capitalize()

            # Check if item name already exists in either category
            if any(item['Item'].lower() == item_name.lower() for cat in inventory.values() for item in cat):
                print("Item Already Exists. Please Add a New Item.")
                continue

            # break  

            stock = int(input("Enter stock number: "))
            price = int(input("Enter price number: "))
            core = int(input("Enter core count number: "))
            thread = int(input("Enter thread count number: "))

        except:
            print("An Error Has Occured, Going back to main menu...")
            return

        break  

    if show_submenu_confirmation():
        new_item = {'CPU_ID': cpu_id, 'Item': item_name, 'Core_Thread': f'{core}c/{thread}t', 'Stock': stock, 'Price': price}
        inventory[category].append(new_item)
        edit_logs_list.append(f"Added item '{item_name}' with CPU_ID {cpu_id} to {category} inventory.")
        print("Item added successfully.")
        show_inventory(category)

# Fungsi untuk mengupdate item dalam inventory
def update_item(category):
    while True:
        show_inventory(category)
        cpu_id = int(input("Enter CPU_ID to update (or 0 to go back): "))

        if cpu_id == 0:
            print("\033c", end =' ')
            return

        # Check apakah CPU_ID ada
        item_to_update = next((item for item in inventory[category] if item['CPU_ID'] == cpu_id), None)

        if item_to_update:
            print("\033c", end =' ')
            print("\n=== Item Details ===")
            show_inventory_table([item_to_update])

            # Menampilkan submenu untuk memilih kolom
            print("\n=== Update Item ===")
            print("\nSelect Column to Update:")
            print("1. Item Name")
            print("2. Core/Thread")
            print("3. Stock")
            print("4. Price")
            print("5. Back to previous menu")
            print("6. Back to main menu")
            print("7. Exit program")

            column_choice = input("Enter the column number: ")

            if column_choice == '1':
                new_value = input("Enter the new item name: ")
                if any(existing_item['Item'] == new_value and existing_item['Core_Thread'] == item_to_update['Core_Thread']
                       for existing_item in inventory[category]):
                    print("Data Already Exists. Item not updated.")
                    continue
                old_name = item_to_update['Item']
                item_to_update['Item'] = new_value
                edit_logs_list.append(f"Updated Item Name of '{old_name}' to '{new_value}' in {category} inventory.")

            elif column_choice == '2':
                new_value = input("Enter the new core/thread value: ")
                if any(existing_item['Core_Thread'] == new_value and existing_item['Item'] == item_to_update['Item']
                       for existing_item in inventory[category]):
                    print("Data Already Exists. Item not updated.")
                    continue
                item_to_update['Core_Thread'] = new_value
                edit_logs_list.append(f"Updated Core/Thread of '{item_to_update['Item']}' to '{new_value}' in {category} inventory.")

            elif column_choice == '3':
                new_value = int(input("Enter the new stock value: "))
                item_to_update['Stock'] = new_value
                edit_logs_list.append(f"Updated Stock of '{item_to_update['Item']}' to '{new_value}' in {category} inventory.")

            elif column_choice == '4':
                new_value = int(input("Enter the new price value: "))
                item_to_update['Price'] = new_value
                edit_logs_list.append(f"Updated Price of '{item_to_update['Item']}' to '{new_value}' in {category} inventory.")

            elif column_choice == '5':
                print("Returning to previous menu.")
                break

            elif column_choice == '6':
                print("Returning to main menu.")
                return
            
            elif column_choice == '7':
                print("Exiting program. Goodbye!")
                exit()

            else:
                print("Invalid column choice.")

            # Menampilkan submenu konfirmasi setelah user memasukkan perubahan
            while True:
                print("\n=== Submenu Confirmation ===")
                print("1. Confirm Update")
                print("2. Back to Main Menu")
                print("3. Exit program")

                confirmation_choice = input("Enter your choice: ")

                if confirmation_choice == '1':
                    # Konfirmasi untuk melanjutkan proses update
                    print("\033c", end =' ')
                    print("Item Successfully Updated.")
                    break
                elif confirmation_choice == '2':
                    # Kembali ke main menu
                    print("\033c", end =' ')
                    print("Returning to main menu.")
                    return
                elif confirmation_choice == '3':
                    # Keluar dari program
                    print("\033c", end =' ')
                    print("Exiting program. Goodbye!")
                    exit()
                else:
                    print("Invalid choice. Returning to main menu.")
        else:
            print("\033c", end =' ')
            print("Data does not Exist. Please enter a valid CPU_ID.")


# Fungsi untuk menghapus item dari inventory
def delete_item(category):
    show_inventory(category)
    try:
        cpu_id = int(input("Enter CPU_ID to delete (or 0 to go back): "))

        if cpu_id == 0:
            return

        # Check if the item with the given CPU_ID exists
        item_to_delete = next((item for item in inventory[category] if item['CPU_ID'] == cpu_id), None)

        if item_to_delete:
            # Menampilkan submenu konfirmasi
            print("\n=== Submenu Confirmation ===")
            print("1. Confirm Delete")
            print("2. Back to previous menu")
            print("3. Back to main menu")
            print("4. Exit program")

            confirmation_choice = input("Enter your choice: ")

            if confirmation_choice == '1':
                deleted_item_name = item_to_delete['Item']
                inventory[category].remove(item_to_delete)
                edit_logs_list.append(f"Deleted item '{deleted_item_name}' with CPU_ID {cpu_id} in {category} inventory.")
                print("\033c", end =' ')
                print("\nItem deleted successfully.")
                show_inventory(category)
            elif confirmation_choice == '2':
                print("\033c", end =' ')
                return
            elif confirmation_choice == '3':
                print("Returning to main menu.")
                return
            elif confirmation_choice == '4':
                print("Exiting program. Goodbye!")
                exit()
            else:
                print("\033c", end =' ')
                print("Invalid choice. Returning to main menu.")
        else:
            print("\033c", end =' ')
            print("Data does not Exist. Please enter a valid CPU_ID.")
    except:
        print("An Error Has Occured, Going back to main menu...")
        return
    
# Fungsi mencari Item berdasarkan keyword
def search_item(category, keyword):
    # Menyimpan hasil pencarian
    found_items = []

    # Looping untuk mencari item berdasarkan keyword
    for item in inventory[category]:
        if keyword.lower() in item['Item'].lower():
            found_items.append(item)

    return found_items

def search_in_category():
    while True:
        category_choice = choose_category()

        if category_choice == '1' or category_choice == '2':
            search_category = 'AMD' if category_choice == '1' else 'Intel'
            keyword = input("Enter keyword to search: ")
            found_items = search_item(search_category, keyword)

            if found_items:
                print("\033c", end=' ')
                print(f"You Searched For: {keyword}")
                print("\n=== Search Results ===")
                show_inventory_table(found_items)
                print("\n=== Submenu ===")
                print("1. Search Again")
                print("2. Back to Main Menu")
                print("3. Exit Program")
                submenu_choice = input("Enter your choice: ")

                if submenu_choice == '1':
                    print("\033c", end=' ')
                    continue
                elif submenu_choice == '2':
                    print("\033c", end=' ')
                    break  # Keluar dari loop dan kembali ke Main Menu
                elif submenu_choice == '3':
                    print("\033c", end=' ')
                    print("Exiting program. Goodbye!")
                    exit()
                else:
                    print("\033c", end=' ')
                    print("Invalid choice. Returning to main menu.")
                    break
            else:
                print("\033c", end=' ')
                print("No items found.")
                break
        elif category_choice == '3':
            print("\033c", end=' ')
            break  # Keluar dari loop dan kembali ke Main Menu
        elif category_choice == '4':
            print("\033c", end=' ')
            print("Exiting program. Goodbye!")
            exit()
        else:
            print("\033c", end=' ')
            print("Invalid choice. Please enter a valid option.")
            continue

# fungsi memfilter item
def filter_items(category, filter_type, value):
    filtered_items = []
    for item in inventory[category]:
        if filter_type == 'price' and item['Price'] <= value:
            filtered_items.append(item)
        elif filter_type == 'stock' and item['Stock'] <= value:
            filtered_items.append(item)

    return filtered_items

def filter_in_category():
    while True:
        category_choice = choose_category()
        if category_choice == '1' or category_choice == '2':
            filter_category = 'AMD' if category_choice == '1' else 'Intel'
            filter_type = input("Enter filter type (price/stock): ")
            if filter_type == 'price' or filter_type == 'stock':
                value = int(input("Enter filter value: "))
                filtered_items = filter_items(filter_category, filter_type, value)
                if filtered_items:
                    print("\033c", end =' ')
                    print(f"Current Filters: {filter_type} and price/stock at {value} or less")
                    print("\n=== Filtered Results ===")
                    show_inventory_table(filtered_items)
                    print("\n=== Submenu ===")
                    print("1. Filter Again")
                    print("2. Back to Main Menu")
                    print("3. Exit Program")
                    submenu_choice = input("Enter your choice: ")
                    if submenu_choice == '1':
                        print("\033c", end =' ')
                        continue
                    elif submenu_choice == '2':
                        print("\033c", end =' ')
                        break  # Keluar dari loop dan kembali ke Main Menu
                    elif submenu_choice == '3':
                        print("\033c", end =' ')
                        print("Exiting program. Goodbye!")
                        exit()
                    else:
                        print("\033c", end =' ')
                        print("Invalid choice. Returning to main menu.")
                        print()
                        break
            else: 
                print("\033c", end =' ')
                print("Invalid Input, Please Try Again")
                print()
                continue    
        elif category_choice == '3':
            print("\033c", end =' ')
            break
        elif category_choice == '4':
            print("\033c", end =' ')
            print("Exiting program. Goodbye!")
            exit()       
        else:
            print("\033c", end =' ')
            print("Invalid Input, Please Try Again") 
            continue

# Fungsi untuk menampilkan perubahan-perubahan yang terjadi pada inventory
def show_edit_logs():
    print("\033c", end =' ')
    while True:
        print("=== Logs Submenu ===")
        print("1. View Logs")
        print("2. Back to main menu")
        print("3. Exit program")

        submenu_choice = input("Enter your choice: ")

        if submenu_choice == '1':
            print("\033c", end =' ')
            print("\n=== Logs ===")
            for log in edit_logs_list:
                print(log)
        elif submenu_choice == '2':
            print("\033c", end =' ')
            break
        elif submenu_choice == '3':
            print("\033c", end =' ')
            print("Exiting program. Goodbye!")
            exit()
        else:
            print("\033c", end =' ')
            print("Invalid choice. Please enter a valid option.")

# Fungsi untuk menampilkan tabel inventory
def show_inventory_table(items):
    if not items:
        print("No items to display.")
        return

    print("=== Inventory Table ===")
    print("CPU_ID  |Item                    |Core/Thread|Stock |Price")
    for i, item in enumerate(items, 1):
        print(f"{item['CPU_ID']:<8}|{item['Item']:<24}|{item['Core_Thread']:<11}|{item['Stock']:<6}|{item['Price']:<10}")

# Fungsi untuk menampilkan submenu inventory
def show_inventory_submenu():
    while True:
        print("=== Submenu Show Inventory ===")
        print("1. Show All Inventory")
        print("2. Inventory AMD")
        print("3. Inventory Intel")
        print("4. Back to main menu")
        print("5. Exit program")

        submenu_choice = input("Enter your choice: ")

        if submenu_choice == '1':
            show_inventory_all()

        elif submenu_choice == '2':
            print("\033c", end =' ')
            show_inventory('AMD')
            print()

        elif submenu_choice == '3':
            print("\033c", end =' ')
            show_inventory('Intel')
            print()

        elif submenu_choice == '4':
            print("\033c", end =' ')
            break

        elif submenu_choice == '5':
            print("\033c", end =' ')
            print("Exiting program. Goodbye!")
            exit()

        else: 
            print("\033c", end =' ')
            print("Invalid Input, Please Try Again")

# Fungsi utama untuk menjalankan program
def main():
    while True:   
        print("\n=== Sistem Inventory CPU Toko Komputer ===")
        print("1. Show Inventory")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Search Item")
        print("6. Filter Items")
        print("7. Edit Logs")
        print("8. Exit program")

        choice = input("Enter your choice: ")


        if choice == '1':
            print("\033c", end =' ')
            show_inventory_submenu()

        elif choice == '2':
            print("\033c", end =' ')
            category_choice = choose_category()
            if category_choice == '1':
                print("\033c", end =' ')
                add_item('AMD')
            elif category_choice == '2':
                print("\033c", end =' ')
                add_item('Intel')
            elif category_choice == '3':
                print("\033c", end =' ')
                continue
            elif category_choice == '4':
                print("\033c", end =' ')
                print("Exiting program. Goodbye!")
                exit()
            else:
                print("\033c", end =' ')
                print("Invalid choice. Please enter a valid option.")
                continue
            
            
        elif choice == '3':
            print("\033c", end =' ')
            category_choice = choose_category()
            if category_choice == '1':
                print("\033c", end =' ')
                update_category = 'AMD'
            elif category_choice == '2':
                print("\033c", end =' ')
                update_category = 'Intel'
            elif category_choice == '3':
                print("\033c", end =' ')
                continue
            elif category_choice == '4':
                print("\033c", end =' ')
                print("Exiting program. Goodbye!")
                exit()
            else:
                print("\033c", end =' ')
                print("Invalid choice. Please enter a valid option.")
                continue

            update_item(update_category)

        elif choice == '4':
            print("\033c", end =' ')
            category_choice = choose_category()
            if category_choice == '1':
                print("\033c", end =' ')
                delete_category = 'AMD'
            elif category_choice == '2':
                print("\033c", end =' ')
                delete_category = 'Intel'
            elif category_choice == '3':
                print("\033c", end =' ')
                continue
            elif category_choice == '4':
                print("\033c", end =' ')
                print("Exiting program. Goodbye!")
                exit()
            else:
                print("\033c", end =' ')
                print("Invalid choice. Please enter a valid option.")
                continue

            delete_item(delete_category)

        elif choice == '5':
            print("\033c", end =' ')
            search_in_category()

        elif choice == '6':
            print("\033c", end =' ')
            filter_in_category()

        elif choice == '7':
            show_edit_logs()

        elif choice == '8':
            print("\033c", end =' ')
            print("Exiting program. Goodbye!")
            exit()

        else:
            print("\033c", end =' ')
            print("Invalid choice. Please enter a valid option.")
            continue
 
main()