# ________initialize variables ___________________________________

dealer_detail_list = []

# _________import required modules __________________________________

import os
import random
from ast import literal_eval
from tabulate import tabulate


# __________required functions to build up dealer detail requirements __________

class Dealer:

    @staticmethod
    def generate_randomly_selected_dealers():
        """This will display four randomly selected dealers"""
        # Reading the required text file
        try:
            with open("dealer.txt") as dealer:
                dealer_names = dealer.read().strip().split(", ")
        except FileNotFoundError:
            print("• File cannot find in the location!!!!")
        else:
            # This will select four dealers randomly without duplications
            randomly_selected_dealers_list = random.sample(dealer_names, 4)

            # generating randomly selected dealers list
            final_list_of_selected_dealers = [["Randomly_selected_dealers"]]
            for dealer in randomly_selected_dealers_list:
                final_list_of_selected_dealers.append([dealer])

            # Display randomly selected massage
            print("\n• 4 Dealers are Selected Randomly ")
            print("==================================")
            print(
                tabulate(final_list_of_selected_dealers[0:len(final_list_of_selected_dealers)], tablefmt="simple_grid"))
            return final_list_of_selected_dealers[1:]

    @staticmethod
    def dealers_system_operator(random_call_status, random_dealer=None, choice=None, ldi_status=1, run_count=0):
        """This will handle the main process of dealers data"""
        dealer_detail_keys = ['dealer_name', 'contact_no', 'location', 'item_name', 'item_brand', 'item_price',
                              'quantity']

        while True:
            # Check whether user has randomly generated dealer's before
            global required_dealers, final_dealer_item_details
            if random_dealer is None:
                random_dealer = []

            # If user has not randomly generated dealer's before, ask user to generate them first
            if not random_call_status:
                print("\n• System cannot display dealer details !!!")
                print("• First you have to randomly generate four dealers !!!")

                random_generate_status = "default"
                while random_generate_status not in ["yes", "y", "no", "n"]:
                    random_generate_status = str(
                        input("Do you want to generate random dealers now ? (yes / no) :")).lower()

                if random_generate_status in ["yes", "y"]:
                    required_dealers = Dealer.generate_randomly_selected_dealers()
                    random_call_status = True
                    ldi_status = 0

                else:
                    random_call_status = False
                    required_dealers = None
                    break
            # Build the basic criteria to format all the dealers, in a proper way
            else:
                required_dealers = random_dealer

            # Two temporary lists were built to make the dealer_detail_list
            temporary_list = []
            for index in range(0, 4):
                with open(f"{required_dealers[index][0]}.txt", "r") as fo:
                    temporary_list.append(literal_eval(fo.read()))

            temporary_list2 = []
            for index in range(0, len(temporary_list)):
                for count in range(0, 4):
                    temporary_list2.append(temporary_list[index][count])

            dealer_detail_list = temporary_list2
            # Making two lists to represent dealer personal details and dealer item details
            dealer_personal_details = []
            dealer_item_details = []

            for index in range(0, len(dealer_detail_list)):
                if index in [0, 4, 8, 12]:
                    dealer_personal_details.append(list(dealer_detail_list[index].values()))
                else:
                    dealer_item_details.append(list(dealer_detail_list[index].values()))

            # The following steps show the algorithm used to sort data according to dealer address
            location_details_list = []
            for index in dealer_personal_details:
                location_details_list.append(index[2])

            sorted_list_of_locations = []
            while len(location_details_list) != 0:
                # Assign the first value of the location detail list as min_value
                min_value = location_details_list[0].title()
                # Using string sorting methods to sort in the alphabetical order
                for item in location_details_list:
                    if item.title() < min_value:
                        min_value = item.title()
                sorted_list_of_locations.append(min_value)
                location_details_list.remove(min_value)

            # Creating the final list to complete all the details
            final_dealer_list = []
            for index in range(0, 4):
                for count in range(0, 4):
                    if sorted_list_of_locations[index] == dealer_personal_details[count][2]:
                        final_dealer_list.append(dealer_personal_details[count])
                        break
                    else:
                        pass

            # add the dealer's name to dealer item details list
            for index in range(0, 4):
                for count in range(0, 3):
                    dealer_item_details[(index * 3) + count].append(dealer_personal_details[index][0])

            # Sort dealer item's details
            sorted_dealer_item_details = []
            for index in range(0, len(final_dealer_list)):
                for count in range(0, len(dealer_item_details)):
                    if final_dealer_list[index][0] == dealer_item_details[count][4]:
                        sorted_dealer_item_details.append(dealer_item_details[count])

            # Get the user's name to the beginning of the all sublist in dealer item details
            final_dealer_item_details = []
            for index in sorted_dealer_item_details:
                sub_list = [index[-1]] + index[:-1]
                final_dealer_item_details.append(sub_list)

            # Check the user choice to generate the required output
            if choice == "VRL":
                Dealer.all_details_of_selected_dealers(final_dealer_list=final_dealer_list,
                                                       dealer_detail_keys=dealer_detail_keys,
                                                       dealer_item_details=final_dealer_item_details)
            else:

                Dealer.selected_dealer_items(dealer_name_list=required_dealers,
                                             main_dealer_item_list=final_dealer_item_details,
                                             ldi_status=ldi_status)

            break
        # these values will be returned to check whether user used sdd option before
        return random_call_status, required_dealers, ldi_status

    @staticmethod
    def all_details_of_selected_dealers(final_dealer_list=None, dealer_detail_keys=None, dealer_item_details=None):
        """This will display all details of randomly selected dealers"""

        # This prints the randomly selected four dealers personal details
        print("\n• All randomly selected dealer's personal details given below.\n• This table is sorted according "
              "to the dealer's location")
        print(tabulate(final_dealer_list[0:len(final_dealer_list)], tablefmt="simple_grid",
                       headers=dealer_detail_keys[0:3]))
        # Source : https://pypi.org/project/tabulate/

        # This process prints the randomly generated dealer's item details
        selected_dealer_item = []
        for index in range(0, 4):
            temporary_list = []
            for count in range(0, 3):
                temporary_list.append(dealer_item_details[(3 * index) + count])
            selected_dealer_item.append(temporary_list)
            print(f"\n• Dealer {temporary_list[0][0]}'s item details given below.")

            # This will generate the table
            print(tabulate(temporary_list[0:len(temporary_list)], tablefmt="simple_grid",
                           headers=['dealer_name', 'item_name', 'item_brand', 'item_price', 'quantity']))
            del temporary_list

    @staticmethod
    def selected_dealer_items(dealer_name_list, main_dealer_item_list=None, ldi_status=1):
        """This will display item details of a randomly selected dealer"""

        # print the randomly selected dealer's names if the user did not generate the random dealers
        # within the ldi process
        global open_text
        if ldi_status == 1:
            print(tabulate(dealer_name_list[0:len(dealer_name_list)], tablefmt="simple_grid",
                           headers=['Randomly_selected_dealers']))

        print("• Select one of the randomly selected dealers above to see the information about their items")
        # building up the criteria to display the items of randomly selected dealer given by user
        name_list = []
        for index in dealer_name_list:
            name_list.append(index[0])

        while True:
            # Ask user to input a randomly selected dealer
            selected_dealer = "None"
            while selected_dealer not in name_list:
                selected_dealer = str(input("Enter one of the dealers above :")).title()

            # Steps to find out item details of the user mentioned dealer
            display_item_list = []
            for index in range(0, len(main_dealer_item_list)):
                if selected_dealer == main_dealer_item_list[index][0]:
                    for count in range(0, 3):
                        display_item_list.append(main_dealer_item_list[index + count])
                    break
            # Display the selected users details in a table
            print("\n• Dealer {0}'s item details are given below.".format(selected_dealer))
            print(tabulate(display_item_list[0: (len(display_item_list))],
                           tablefmt="simple_grid", headers=['dealer_name', 'item_name',
                                                            'item_brand', 'item_price', 'quantity']))

            # Ask user whether they need to see the selected dealer's text file ?
            open_text_file_status = "default"
            while open_text_file_status not in ["yes", "y", "no", "n"]:
                open_text_file_status = str(input("• Do you want to see dealer's text file ? (yes/no):")).lower()
            if open_text_file_status in ["yes", "y"]:
                try:
                    os.startfile(f"{selected_dealer}.txt")
                    # Source : https://stackoverflow.com/questions/43204473/os-startfile-path-in-python-with-numbers
                except FileNotFoundError:
                    print("• Error on opening the file !!!")
                else:
                    pass

            # Ask user whether they need to see another randomly generated dealer's item details
            detail_repeat_status = "default"
            while detail_repeat_status not in ["yes", "y", "no", "n"]:
                detail_repeat_status = str(
                    input("• Do you want to see any other dealer's item details ? (yes/no):")).lower()

            if detail_repeat_status in ["no", "n"]:
                break
