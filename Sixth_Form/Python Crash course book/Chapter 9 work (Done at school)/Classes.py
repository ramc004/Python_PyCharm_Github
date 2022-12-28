class Restaurant():
    """This class mimics a restaurant"""

    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """This function describes the restaurant"""
        print("the name of our Restaurant is " + self.name + "\nand we sell " + self.cuisine)

    def open_restaurant(self):
        """This function tells us if the restaurant is open"""
        pass


## create an instance of the restaurant class
myRestaurant = Restaurant("Mexican", "Miller and Carter")
## call the describe method on the instance
myRestaurant.describe_restaurant()

