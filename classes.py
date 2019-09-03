class Pizza:

    def __init__(self):
        # Establish the properties of each pizza
        # with a default value
        self.size = ""
        self.style = ""
        self.crust = ""
        self.toppings = []

    def add_topping(self, topping):
        self.toppings.append(topping)
        print(f"added {topping} to toppings")
        

    def print_order(self):
        tops = ""
        list_length = len(self.toppings)
        for food in self.toppings:
            if self.toppings.index(food) < list_length-1:
                tops += f"{food} and "
            else:
                tops += f"{food}"
        print(f"I would like a {self.size}-in, {self.style} pizza with {tops}.")


meat_lovers = Pizza()
meat_lovers.size = 16
meat_lovers.style = "Deep dish"
meat_lovers.add_topping("Pepperoni")
meat_lovers.add_topping("Sausage")
meat_lovers.print_order()

cheese_lovers = Pizza()
cheese_lovers.size = 16
cheese_lovers.style = "thin crust"
cheese_lovers.add_topping("Pepperoni")
cheese_lovers.add_topping("Extra Cheese")
cheese_lovers.print_order()