"""Print out all the melons in our inventory."""


from melons import melon_data

def print_melons():
    """Print each melon with corresponding attribute information."""

    for name in melon_data:                     #for each melon in the melon_data dict,

        traits = melon_data[name]               #get the value of melon_data at that melon (gets inner dictionary)

        print(f'\n{name.upper()}')

        for trait in traits:
            print(f'{trait}: {traits[trait]}')
            

print_melons()