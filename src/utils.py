def check_add_item():
    more_items = input('Add more items? [Y/n]')
    if more_items in list(map(str.lower, ["N", "NO"])):
        return False
    elif more_items in list(map(str.lower, ["Y", "YES"])):
        return True
    else:
        print('Please enter a valid input.')
        check_add_item()


def check_category(tax_exempt):
    category = get_int(
        'Select Category: \n 1. Books \n 2. Food \n 3. Medical \n 4. Other \n')
    if category in [1, 2, 3]:
        tax_exempt = True
    return tax_exempt


def check_imported():
    item_imported: str = input('Is the Item Imported? [Y/n]: ')
    if item_imported in list(map(str.lower, ["N", "NO"])):
        imported = False
    elif item_imported in list(map(str.lower, ["Y", "YES"])):
        imported = True
    else:
        print('Please enter a valid input.')
        check_imported()
    return imported


def get_string(prompt):
    try:
        value = input(prompt)
    except ValueError:
        print("Please enter a valid input.")
        return get_int(prompt)

    if type(prompt) is str and prompt != "":
        return value
    else:
        print("Please enter a valid input.")
        return get_string(prompt)


def get_int(prompt):
    try:
        value = int(input(prompt))
    except ValueError:
        print("Please enter a valid input.")
        return get_int(prompt)

    if value >= 0:
        return value
    else:
        print("Please enter a valid input.")
        return get_int(prompt)


def get_float(prompt):
    try:
        value = float(input(prompt))
    except ValueError:
        print("Please enter a valid input. eg. 12.00")
        return get_float(prompt)

    if value >= 0:
        return value
    else:
        print("Please enter a valid input.")
        return get_float(prompt)