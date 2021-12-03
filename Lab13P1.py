class dinner_combo():
    def __init__(self):
        self.main_dish = 0
        self.soup = 0
        self.total = 0

    def choose_dish(self):
        self.main_dish = int(input("Enter 1 for sweet and sour pork, 2 for sesame chicken, or 3 for shrimp fried rice: "))
        if self.main_dish == 1:
            self.total = self.total +7
        elif self.main_dish == 2:
            self.total = self.total + 8
        elif self.main_dish == 3:
            self.total = self.total + 9


    def choose_soup(self):
        self.main_dish = int(input("Enter 1 for egg drop soup, or 2 for wanton soup: "))
        if self.main_dish == 1:
            self.total = self.total + 1.25
        elif self.main_dish == 2:
            self.total = self.total + 1.50


    def displayorder(self):
        if self.main_dish == 1:
            print("Item ordered: Sweet and Sour Pork")
        if self.main_dish ==2:
            print("Item ordered: Sesame Chicken")
        if self.main_dish == 3:
            print("Item ordered: Shrimp Fried Rice")
        if self.soup == 1:
            print("Item ordered: Egg Drop Soup")
        if self.soup == 2:
            print("Item ordered: Wanton Soup")
        print("Please pay this amount: ", format(self.total))


class deluxe_dinner_combo(dinner_combo):
    def __init__(self):
        super().__init__()
        self.appetizer = 0


    def choose_appetizer(self):
        self.appetizer = int(input("Enter 1 for Spring Roll or 2 for Chicken Wing: "))
        if self.appetizer == 1:
            self.total = self.total + 1.25
        if self.appetizer == 2:
            self.total = self.total + 1.50

    def displayorder(self):
        super().displayorder()
        if self.appetizer == 1:
            print("spring roll ", end="")
        if self.appetizer == 2:
            print("Chicken Wing ", end="")

def main():
    dinner_type = None
    dinner_type_choice = int(input("Enter 1 for dinner combo or 2 for deluxe dinner combo: "))
    if dinner_type_choice == 1:
        dinner_type = dinner_combo()
    elif dinner_type_choice == 2:
        dinner_type = deluxe_dinner_combo()
        dinner_type.choose_appetizer()
    dinner_type.choose_dish()
    dinner_type.choose_soup()
    print("Items ordered:", end="")
    dinner_type.displayorder()

main()
