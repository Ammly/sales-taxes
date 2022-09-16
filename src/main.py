"""
Problem Two: Sales Taxes

- 10% sales Tax on all goods except books,food, and medical products.
- 5% import duty on all imported goods with no exceptions

Rounding rules for sales tax
- for a tax rate of n%, a shelf price of p contains 
    (np/100 rounded up to the nearest 0.05) amount of sales tax.

Example

Input Basket #1:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85

Output for Basket #1:
1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85
Sales Taxes: 1.50
Total: 29.83

"""


# Rount amount to 3 decimal places
def round_up(amount):
    return format(amount, '.2f')


# Calculate Total taxe amount (sales_tax + import_duty)
def total_item_taxes(item_price, imported=False, tax_exempt=False):
    SALES_TAX = 0.1
    IMPORT_DUTY = .05
    import_duty = 0.0
    sales_tax = float(item_price) * SALES_TAX if not tax_exempt else 0.0

    if imported:
        import_duty = float(item_price) * IMPORT_DUTY

    return float(sales_tax + import_duty)


# Calculate Total item cost (ItemPrice + tax)
def total_item_cost(item_price, quantity, imported=False, tax_exempt=False):
    total_item_cost = quantity * (item_price + total_item_taxes(item_price, imported, tax_exempt))

    return round_up(total_item_cost)


# Print the Receipt
def display_receipt(basket):
    total_sales_taxes = 0.0
    total_amount = 0.0

    for quantity, item_name, price, imported, tax_exempt in basket:
        item_price = total_item_cost(price, quantity, imported, tax_exempt)
        sales_tax = total_item_taxes(item_price, imported, tax_exempt)

        total_sales_taxes = float(total_sales_taxes) + float(sales_tax)
        total_amount = float(total_amount) + float(item_price)

        print(f'{quantity} {item_name}: {item_price}')

    print(f'Sales Taxes: {round_up(total_sales_taxes)}')
    print(f'Total: {round_up(total_amount)}')


# @TODO refactor Yes/No questions to a function
def check_response(response):
    if response in list(map(str.lower, ["N", "NO"])):
        return False
    elif response in list(map(str.lower, ["Y", "YES"])):
        return True
    else:
        print('Please enter a valid input [Y/n]')
        return check_response()


def main():
    basket = list()
    imported = False
    tax_exempt = False

    while True:
        tax_exempt = False
        item_name = input('Enter the Item name: ')
        quantity = int(input('Enter the number of items: '))
        price = float(input('Enter the price of the purchase: '))
        # Category [books,food, and medical products]
        category = int(input(
            'Select Category: \n 1. Books \n 2. Food \n 3. Medical \n 4. Other \n'))
        if category in [1, 2, 3]:
            tax_exempt = True

        item_imported = input('Is the Item Imported? [Y/n]: ')
        if item_imported in list(map(str.lower, ["N", "NO"])):
            imported = False
        elif item_imported in list(map(str.lower, ["Y", "YES"])):
            imported = True
        else:
            print('Please enter a valid input. Is the Item Imported? [Y/n]')

        item = (quantity, item_name, price, imported, tax_exempt)
        basket.append(item)

        more_items = input('Add more items? [Y/n]')

        if more_items in list(map(str.lower, ["N", "NO"])):
            break
        elif more_items in list(map(str.lower, ["Y", "YES"])):
            continue
        else:
            print('Please enter a valid input. Add more items? [Y/n]')

    # print(basket)

    display_receipt(basket)


if __name__ == '__main__':
    main()
