#Mark Darling
#COMSC122-0940
#Homework 02B

#collect all of the necessary input from the user in the correct variable type
num_shares_buy = int(input('Enter number of shares purchased: '))
buy_price_per_share = float(input('Enter the price per share [in dollars]: '))
buy_commission_percent = float(input('Enter the commission percentage paid broker [in %]: '))
num_shares_sold = int(input('Enter the number of shares sold: '))
sell_price_per_share = float(input('Enter the sales price per share [in dollars]: '))
sell_commission_percent = float(input('Enter the sales commission percentage paid broker [in %]: '))

#perform all of the necessary calculations
total_cost = (num_shares_buy) * (buy_price_per_share)
purchase_commission_cost = (buy_commission_percent/100) * (total_cost)
total_sale = (num_shares_sold) * (sell_price_per_share)
sale_commission_cost = (sell_commission_percent/100) * (total_sale)
net_result =(
        #total amount paid made negative (since it's not actually our money and we start with zero)
        -(total_cost)
        -
        #minus commission paid to broker at purchase
        (purchase_commission_cost)
        +
        #plus the total amount of money made when selling the shares
        (total_sale)
        -
        #minus commission paid to broker at sale
        (sale_commission_cost) )

#output the final results properly formatted
print("\nMark Darling's Stock Transaction App")
print('Joe paid: $', format(total_cost, ',.2f'), sep='')
print('Purchase Commission: $', format(purchase_commission_cost, ',.2f'), sep='')
print('Joe sold at: $', format(total_sale, ',.2f'), sep='')
print('Sales Commission: $', format(sale_commission_cost, ',.2f'), sep='')
print("Joe's net financial result: $", format(net_result, ',.2f'), sep='')

print('Hit any key to Exit:')
input('')
