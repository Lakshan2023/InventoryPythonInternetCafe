# RGU student_id : 2313081
# IIT student_id : 20221470

# __________ import modules _______
import time
from inventory import Inventory
from miscellaneous import Miscellaneous
from dealer import Dealer


# ________________Main Program ___________________________________

class Main:
    final_list_of_selected_dealers = []
    sublist_view = []

    def __init__(self):
        """This is the constructor of the main program"""
        # Calling the menu of the program
        Miscellaneous.display_details()

        # Reading previously saved data in the system
        Miscellaneous.read_saved_data(file_type="itemdata", list_type=Inventory.item_details_list)

        # Assigning the required variables
        self.choice = None
        self.run_count = 0
        self.random_call_status = False
        self.random_dealers = None

        # Calling the main process to constructor
        self.main_process_menu()

    def main_process_menu(self):
        """This will work as the main menu of the system"""

        while True:
            # Ask user to input their choice
            self.choice = input("Enter your choice: ").upper()
            system_actions = {
                "AID": Inventory.add_item_data,
                "DID": Inventory.delete_item_data,
                "UID": Inventory.update_item_data,
                "VID": Inventory.view_item_data,
                "SID": Inventory.save_item_data,
                "SDD": Dealer.generate_randomly_selected_dealers,
            }

            dealer_actions = {
                "VRL": Dealer.dealers_system_operator,
                "LDI": Dealer.dealers_system_operator,
            }

            # Selecting the user's choice options
            if self.choice in system_actions:
                if self.choice == "SDD":
                    self.random_call_status = True
                    self.random_dealers = system_actions[self.choice]()
                else:
                    system_actions[self.choice]()

            # If user put "ESC" break the process
            elif self.choice == "ESC":
                print("• Good Bye !!!")
                time.sleep(1.25)
                break

            # If user choice either VRl or LDI this will work
            if self.choice in dealer_actions:
                self.random_call_status, self.random_dealers, ldi_status = dealer_actions[self.choice](
                    random_call_status=self.random_call_status,
                    random_dealer=self.random_dealers,
                    choice=self.choice,
                    ldi_status=1, run_count=self.run_count)

            # If user choice is not in the given choices this will work
            elif self.choice in [system_actions and dealer_actions]:
                print("• Enter a correct value from the below list !!!\n")

            # sub menu will be printed at the end of all co functions
            print("\n• Choose AID, DID, UID, VID, SID, SDD, VRL, LDI, ESC")
            self.run_count += 1


# Calling the main program
Main()
