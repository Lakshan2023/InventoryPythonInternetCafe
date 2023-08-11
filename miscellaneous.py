# _________import required modules __________________________________
from ast import literal_eval
from datetime import datetime


# __________required functions to build up dealer detail requirements __________
class Miscellaneous:
    @staticmethod
    def read_saved_data(file_type, list_type):
        """This function reads the previously saved data in the system"""
        try:
            with open("{}.txt".format(file_type), "r") as rsd:
                data = rsd.read()

                # This will add the data to the selected list_type from text file list
                if data:
                    list_type.extend(literal_eval(data))

        except Exception:
            print("Error while reading saved data !!!")

    @staticmethod
    def display_details():
        """This will display the menu of this inventory system"""
        print("\t\tWelcome to One Net Cafe".center(30))
        print("   \t======================================\n".center(36))
        print(" • Type AID for adding item details.")
        print(" • Type DID for deleting item details.")
        print(" • Type UID for updating item details.")
        print(""" • Type VID for viewing the items table. 
   (Sort according to the items category) and print the current total.""")
        print(" • Type SID for saving the item details to the text file at any time.")
        print(" • Type SDD for selecting four dealers randomly from a file.")
        print(""" • Type VRL for displaying all the details of the randomly selected dealers.
   (Sorted according to the location.)""")
        print(" • Type LDI for display the items of the given dealer")
        print(" • Type ESC to exit the program. \n")

    @staticmethod
    def display_update_details():
        """This will display update details menu"""
        print("\n___Select what you need to update___\n")
        print(" 1• Type 1 to update Item Code.")
        print(" 2• Type 2 to update Item Name.")
        print(" 3• Type 3 to update Item Brand.")
        print(" 4• Type 4 to update Item Price.")
        print(" 5• Type 5 to update Item Quantity.")
        print(" 6• Type 6 to update Item Category.")
        print(" 7• Type 7 to update Item Purchase Date.")

    @staticmethod
    def save_data(item_details_list):
        """This will write all the saved data in the inventory in a text file"""
        with open("itemdata.txt", "w") as sd:
            # making item details list as a string to write in the text file
            string_item_details_list = str(item_details_list)
            sd.write(string_item_details_list)
            sd.close()

    @staticmethod
    def date_month_year():
        """This function is used to check whether user will enter a correct year/date/ month"""

        # Check the item purchased year
        global leap_year_status, item_purchased_month, correct_item_purchased_month
        while True:
            try:
                item_purchased_year = input("Enter the purchased year : ")
                if int(item_purchased_year) > datetime.now().year:
                    print("Enter a correct year !!!")
                    continue
                if item_purchased_year.isdigit() and len(item_purchased_year) == 4:
                    # Check whether user has given a leap year
                    leap_year_status = int(item_purchased_year) % 4 == 0 and (
                            int(item_purchased_year) % 100 != 0 or int(item_purchased_year) % 400 == 0)
                    break
                else:
                    print("Enter a correct year !!!")
            except ValueError:
                print("Please input a correct number for the year !!!")

        # Check the item purchased month
        while True:
            try:
                item_purchased_month = int(input("Enter the purchased month (number of the month): "))

                if (int(item_purchased_year) == datetime.now().year) and (
                        int(item_purchased_month) > int(datetime.now().month)):
                    print("Please input a correct month !!!")
                    continue

                # zfill will add zeros at the beginning of the string
                correct_item_purchased_month = str(item_purchased_month).zfill(2)
                if item_purchased_month < 1 or item_purchased_month > 12:
                    raise ValueError
                break

            except ValueError:
                print("Please input a correct number for the month !!!")

        # Check the item purchased date
        while True:
            try:
                # building up the criteria to check whether user input date is correct
                item_purchased_date = int(input("Enter the purchased date : "))

                if (int(item_purchased_year) == datetime.now().year) and (
                        int(item_purchased_month) == int(datetime.now().month) and
                        (int(item_purchased_date) > int(datetime.now().day))):
                    print("Please Input a correct date !!!")
                    continue

                if item_purchased_date < 1 or item_purchased_date > 31:
                    raise ValueError
                if correct_item_purchased_month == "02":
                    if leap_year_status:
                        if item_purchased_date > 29:
                            raise ValueError
                    else:
                        if item_purchased_date > 28:
                            raise ValueError

                elif correct_item_purchased_month in ["04", "06", "09", "11"]:
                    if item_purchased_date > 30:
                        raise ValueError
                break
            except ValueError:
                print("Please enter a correct date !!!")

        # this value is returned to take the correct purchased date
        return {
            "purchased_date": f"{item_purchased_year}/{correct_item_purchased_month}/{str(item_purchased_date).zfill(2)}"}

        # Source: https://www.w3schools.com/python/ref_string_zfill.asp


