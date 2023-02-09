"""
The coffee shop module contains functions and contains variables
important to implementing a coffee shop.
"""

# Set some variables
shop_name = "Runestone Brew House"
coffee_sizes = ["small", "medium", "large"]
coffee_roasts = ["hot chocolate", "light", "medium", "dark", "espresso"]
bean_type = ["Kenya", "Brazil", "Mexico", "Hawaii"]

def order_coffee(size, roast, beans):
    """
    Take an order from a user
    :param size: a string containing one of the coffee_sizes
    :param roast: a string containing one of the coffee_roasts
    :return: a message about the coffee order
    """
    return "Here's your {} coffee roasted {} from {} beans".format(size, roast, beans)


def add_milk_please(fat_content):
    """
    Pretend like we're adding some milk to a coffee
    :param fat_content: a string or integer containing the milkfat content
    :return: a message about having added the milk
    """
    return "I've added the {}% milk".format(fat_content)