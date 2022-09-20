#Mark Darling
#COMSC122-0940

num_shares_buy = int(input('Enter number of shares purchased: '))
buy_price_per_share = float(input('Enter the price per share [in dollars]: '))
buy_commission_percent = float(input('Enter the commission percentage paid broker [in %]: '))
num_shares_sold = int(input('Enter the number of shares sold: '))
sell_price_per_share = float(input('Enter the sales price per share [in dollars]: '))
sell_commission_percent = float(input('Enter the sales commission percentage paid broker [in %]: '))

print("Mark Darling's Stock Transaction App")
print('Joe paid: $', format(num_shares_buy * buy_price_per_share, ',.2f'), sep='')
print('Purchase Commission: $', format((buy_commission_percent/100) * (num_shares_buy * buy_price_per_share), ',.2f'), sep='')
print('Joe sold at: $', format(num_shares_sold * sell_price_per_share, ',.2f'), sep='')
print('Sales Commission: $', format((sell_commission_percent/100) * (num_shares_sold * sell_price_per_share), ',.2f'), sep='')
print("Joe's profit: $", format(
        #total amount paid (negative amount)
        (-(num_shares_buy * buy_price_per_share)
        -
        #minus commission paid to broker at purchase
        ((buy_commission_percent/100) * (num_shares_buy * buy_price_per_share))
        +
        #plus the total amount of money made when selling the shares
        (num_shares_sold * sell_price_per_share)
        -
        #minus commission paid to broker at sale
        (sell_commission_percent/100) * (num_shares_sold * sell_price_per_share)), ',.2f'), sep='')

print('Hit any key to Exit:')
input('')
