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

from utils import *


# Round amount to 3 decimal places
def round_up(amount):
    return format(amount, '.2f')


# Calculate Total tax amount (sales_tax + import_duty)
def total_item_tax(item_price, imported=False, tax_exempt=False):
    SALES_TAX = 0.1
    IMPORT_DUTY = .05
    import_duty = 0.0
    sales_tax = float(item_price) * SALES_TAX if not tax_exempt else 0.0

    if imported:
        import_duty = float(item_price) * IMPORT_DUTY

    return float(sales_tax + import_duty)


# Calculate Total item cost (ItemPrice + tax)
def total_item_cost(item_price, quantity, imported=False, tax_exempt=False):
    return round_up(quantity * (item_price + total_item_tax(item_price, imported, tax_exempt)))


# Print the Receipt
def display_receipt(basket):
    total_sales_taxes = 0.0
    total_amount = 0.0
    receipt: str = ""

    for quantity, item_name, price, imported, tax_exempt in basket:
        item_price = total_item_cost(price, quantity, imported, tax_exempt)
        sales_tax = total_item_tax(item_price, imported, tax_exempt)

        total_sales_taxes = float(total_sales_taxes) + float(sales_tax)
        total_amount = float(total_amount) + float(item_price)

        receipt += f'\n{quantity} {item_name}: {item_price} \n'

    receipt += f'Sales Taxes: {round_up(total_sales_taxes)} \n'

    receipt += f'Total: {round_up(total_amount)} \n'
    
    return receipt


def main():
    basket = list()
    imported = False

    while True:
        tax_exempt = False
        item_name = input('Enter the Item name: ')
        quantity = get_int('Enter the number of items: ')
        price = get_float('Enter the price of the purchase: ')
        tax_exempt = check_category(tax_exempt)
        imported = check_imported()

        item = [quantity, item_name, price, imported, tax_exempt]
        basket.append(item)

        if not check_add_item():
            break
        else:
            continue

    # print(basket)

    print(display_receipt(basket))


if __name__ == '__main__':
    main()
