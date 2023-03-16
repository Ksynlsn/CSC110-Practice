def checkout():
    total = 0
    count = 0
    moreItems = True
    print("Item Cost:", '\t', "Subtotal:")
    print("------", '\t', "     ------")
    while moreItems:
        price = float(input('Enter price of item (0 when done): '))
        if price < 0 and price != 0:
            priceNeg = float(input('Positive numbers only! Enter price of item (0 when done): '))
        elif price != 0:
            count = count + 1
            total = total + price
            print(price, '\t', '|     ', total) 
        else:
            moreItems = False
            
    average = total / count
    taxRate = 0.1
    salesTax = total * taxRate
    print('Total items:', count)
    print('Total $', total)
    print('Average price per item: $', round(average, 2))
    print('The sales tax for your order is: $', round(salesTax, 2))

checkout()
