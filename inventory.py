# _________import required modules __________________________________
from tabulate import tabulate
from miscellaneous import Miscellaneous


# __________required functions to build up dealer detail requirements __________

class Inventory:
    item_details_list = []

    @staticmethod
    def add_item_data():
        """This will add new items to the system."""
        global correct_item_purchased_date, item_code
        while True:
            # assigning item type details in a dictionary with default values
            item_details = {
                "item_code": "None",
                "item_name": "None",
                "item_brand": "None",
                "item_price": 0,
                "item_quantity": 0,
                "item_category": "None",
                "purchased_date": "None"
            }

            # Until the user input a correct Item code, this process will be repeated.
            while True:
                item_code = str(input("Enter Item Code : "))
                # Check whether the item code is already exist in the system
                if item_code in [time["item_code"] for time in Inventory.item_details_list]:
                    print("• Can't Input !!!, that item id already exists !!!")
                else:
                    # Check whether the given item code is in the correct format
                    try:
                        int_item_code = int(item_code)
                    except ValueError:
                        print("• Error !!!, Please use the numbered format for the item code !!!")
                    else:
                        break

            # Assign values in the above-mentioned item_details dictionary
            item_details.update({"item_code": item_code})
            item_details.update({"item_name": str(input("Enter Item name : "))})
            item_details.update({"item_brand": str(input("Enter Item brand : "))})

            # Until the user input a correct Item price, this process will be repeated
            while True:
                try:
                    item_price = float(input("Enter Item price : Rs. "))
                except ValueError:
                    print("• Error !!!, Please enter a valid input !!!")
                else:
                    item_details.update({"item_price": item_price})
                    break

            # Until the user input a correct Item Quantity, this process will be repeated
            while True:
                try:
                    item_quantity = int(input("Enter the quantity of the item : "))
                except ValueError:
                    print("• Error !!!, Please enter a valid input")
                else:
                    item_details.update({"item_quantity": item_quantity})
                    break

            # Assign other values in the above-mentioned item_details dictionary
            item_details.update({"item_category": str(input("Enter the category of the item : "))})
            item_details.update(Miscellaneous.date_month_year())

            # Add updated item_details to item_details_list
            Inventory.item_details_list.append(item_details)
            print("• Saved entered data !!!!")
            Miscellaneous.save_data(Inventory.item_details_list)

            # Check whether user wants to add data again
            entered_data_again_status = "default"
            while entered_data_again_status not in ["yes", "y", "no", "n"]:
                entered_data_again_status = str(input("Do you want to add more items (yes/ no) ? : ")).lower()
            if entered_data_again_status in ["no", "n"]:
                break

        print("")

    @staticmethod
    def delete_item_data():
        """This will delete item data"""
        while True:
            # Check whether item_details_list is empty
            if not Inventory.item_details_list:
                print("• Items Not found !!!")
                break

            delete_item_code = input("Enter the item code that you need to delete : ")

            if delete_item_code.lower() == "esc":
                break

            # Check whether user input item code is available in item_details_list
            found_item_status = False
            for item in Inventory.item_details_list:
                if item.get("item_code") == delete_item_code:
                    # if that item code exists delete that item row
                    Inventory.item_details_list.remove(item)
                    print("• Item Deleted !!!")
                    Miscellaneous.save_data(Inventory.item_details_list)
                    found_item_status = True
                    break

            if not found_item_status:
                print("• Item not found !!!")
            else:
                # Ask user whether they need to delete more data
                delete_item_status = "default"
                while delete_item_status not in ["yes", "y", "no", "n"]:
                    delete_item_status = input("Do you want to delete another Item (Yes/ No) ?: ").lower()
                if delete_item_status in ["no", "n"]:
                    break

        print("")

    @staticmethod
    def update_item_data():
        """This will update item data"""
        global item_found_status
        while True:
            # Check whether item_details_list is empty
            if not Inventory.item_details_list:
                print("• No saved Items in the current system.")
                break

            update_item_code = input("Enter the item code that you need to update details : ").lower()
            # if user enter esc, break the process
            if update_item_code in ["esc", "ESC"]:
                break

            # Check whether user input item code is available to update
            index_of_update_item = None
            for index in range(len(Inventory.item_details_list)):
                if Inventory.item_details_list[index]["item_code"] == update_item_code:
                    index_of_update_item = index
                    break

            if index_of_update_item is None:
                print("• Item not found, please enter the correct item")
                continue

            while True:
                Miscellaneous.display_update_details()

                while True:
                    # Check whether user input the item code in the numbered format
                    try:
                        update_choice = int(input("\n• Select a number from above list to update item details : "))
                        if 1 <= update_choice <= 7:
                            break
                    except ValueError:
                        print("• Error !!!, Please select a number.")

                if update_choice == 1:
                    # The following code is developed to update Item code without duplications
                    while True:
                        try:
                            new_item_code = str(input("Enter a New Item Code : "))
                            int(new_item_code)
                        except ValueError:
                            print("• Please enter item code in numbered format !!!")
                            continue

                        for item in Inventory.item_details_list:
                            if item["item_code"] == str(new_item_code):
                                # Item found status is assigned to continue the process
                                item_found_status = True
                                break
                            else:
                                # Set item_found_status to False if no match is found
                                item_found_status = False

                        # If the user give a duplicate value, print already exists!!!
                        if item_found_status:
                            print("• Can't update!!!, that item id already exists!!")
                            continue
                        else:
                            Inventory.item_details_list[index_of_update_item]["item_code"] = str(new_item_code)
                            Miscellaneous.save_data(Inventory.item_details_list)
                            print("• Item code Updated!!!")
                            break

                # This will update the purchased date
                elif update_choice == 7:
                    Inventory.item_details_list[index_of_update_item]["purchased_date"] = \
                        list(Miscellaneous.date_month_year().values())[0]
                    Miscellaneous.save_data(Inventory.item_details_list)
                    print("• Item code Updated !!!")
                else:
                    # This will update the following values mentioned in key
                    while True:
                        key_value = ["item_name", "item_brand", "item_price", "item_quantity", "item_category"][
                            update_choice - 2]
                        if key_value in ["item_price", "item_quantity"]:
                            try:
                                new_update_value = int(input(f"Enter the new {key_value.title()} : "))
                                Inventory.item_details_list[index_of_update_item][key_value] = float(new_update_value)
                            except ValueError:
                                print(f"• Please enter a number for the {key_value.lower()} !!!")
                                continue
                            else:
                                break
                        else:
                            new_update_value = input(f"Enter the new {key_value.title()} : ")
                            Inventory.item_details_list[index_of_update_item][key_value] = new_update_value
                            break

                    Miscellaneous.save_data(Inventory.item_details_list)
                    print(f"{key_value.title()} updated !!!")

                # Ask user whether they need to update more data in the same item
                update_item_status = input("Do you want to update another data in the same item (Yes/ No) ?: ").lower()
                while update_item_status not in ["yes", "y", "no", "n"]:
                    update_item_status = input(
                        "Do you want to update another data in the same item (Yes/ No) ?: ").lower()

                if update_item_status in ["no", "n"]:
                    break

            # Ask user whether they need to update more data
            update_item_status = input("\nDo you want to update another Item (Yes/ No) ?: ").lower()
            while update_item_status not in ["yes", "y", "no", "n"]:
                update_item_status = input("Do you want to update another Item (Yes/ No) ?: ").lower()

            if update_item_status in ["no", "n"]:
                break

            print("")

    @staticmethod
    def view_item_data():
        """This will print all saved data in the item_details_list"""

        item_description_list = ["item_code", "item_name", "item_brand", "item_price",
                                 "item_quantity", "item_category", "purchased_date"]

        # The following code is used to represent item data in a table
        while True:
            if len(Inventory.item_details_list) == 0:
                print("• No saved Items in the current system !!!!")
                break
            else:
                view_list = []
                for item in range(0, len(Inventory.item_details_list)):
                    sublist_view = []
                    for index in range(0, len(item_description_list)):
                        sublist_view.append(Inventory.item_details_list[item][item_description_list[index]])
                    view_list.append(sublist_view)

                table_value_sorting_list = []
                for count in range(0, len(view_list)):
                    table_value_sorting_list.append(view_list[count][0])

                # The following algorithm is used to sort item details
                # according to the descending order of item_code
                sorted_list = []
                while table_value_sorting_list:
                    max_value = table_value_sorting_list[0]
                    for value in table_value_sorting_list:
                        if len(value) > len(max_value):
                            # compare the length of each value
                            max_value = value
                        elif len(value) == len(max_value):
                            if value > max_value:
                                # applying the String value sorting methods
                                max_value = value
                    sorted_list.append(max_value)
                    table_value_sorting_list.remove(max_value)

                final_table_list = []
                item_description_list.append("total_item_price")
                final_table_list.append(item_description_list)

                for index in sorted_list:
                    for count in range(0, len(view_list)):
                        if index == view_list[count][0]:
                            final_table_list.append(view_list[count])
                            break

                total_price = 0
                for count in range(1, len(final_table_list)):
                    item_total_price = (final_table_list[count][3] * int(final_table_list[count][4]))
                    final_table_list[count].append(item_total_price)
                    total_price = float(total_price + float(item_total_price))

                # Generating the item data table
                print("\n• Item Data Table".ljust(15))
                print(tabulate(final_table_list[0: (len(final_table_list) + 1)], tablefmt="simple_grid"))
                # Source : https://pypi.org/project/tabulate/

                # Generating the table to find the total price of purchased Items.
                total_price_list = [["total_price_of_purchased_items"], [total_price]]
                print("\n• Total Price of Purchased Items given below.".ljust(30))
                print(tabulate(total_price_list[0: (len(total_price_list) + 1)], tablefmt="simple_grid"))

                break

        print("")

    @staticmethod
    def save_item_data():
        """This will save all added data in item_detail_list"""
        # Check whether the item details empty and save the data in a text
        # file
        if len(Inventory.item_details_list) > 1:
            Miscellaneous.save_data(Inventory.item_details_list)
            print("{} items Saved.".format(len(Inventory.item_details_list)))
        elif len(Inventory.item_details_list) == 1:
            Miscellaneous.save_data(Inventory.item_details_list)
            print("{} item Saved.".format(len(Inventory.item_details_list)))
        else:
            print("• No Items Found to Save !!!")
            pass
