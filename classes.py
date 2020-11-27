import colorama


class parking:
    def __init__(self, car_slot_no, car_registration_no, car_color):
        self.car_slot_no = car_slot_no
        self.car_registration_no = car_registration_no
        self.car_color = car_color

    def Registration_numbers_for_cars_with_colour(self, user_input):
        if user_input == self.car_color:
            print(self.car_registration_no)
            return 1

        return 0

    def Slot_numbers_for_cars_with_colour(self, user_input):
        if user_input == self.car_color:
            print(self.car_slot_no)
            return 1
        return 0

    def Slot_number_for_registration_number(self, user_input):
        if user_input == self.car_registration_no:
            print(self.car_slot_no)
            return 1
        return 0

    def Check_status(self):
        print(colorama.Fore.RED + "", self.car_slot_no, end="\t\t")
        print(colorama.Fore.GREEN + "", self.car_registration_no, end="\t\t")
        print(colorama.Fore.YELLOW + "", self.car_color, end="")
        print(colorama.Style.RESET_ALL)