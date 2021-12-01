hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0;
total_revenue = 0;


# looping through prices and adding each price to the total price
for price in prices:
  total_price= total_price + price;



for i in range(len(hairstyles)):
    # total_revenue += prices[i] * last_week[i]
     product = prices[i] * last_week[i]
     total_revenue = total_revenue + product
  

average_price = total_price / len(prices)

new_prices = [ num -5 for num in prices]

average_daily_revenue = total_revenue/7;


# cuts whose prices are under 30
custs_under_30 = [hairstyles[i] for i in range(len(hairstyles[i])-1) if new_prices[i] < 30]


print(" Average daily revenue : " + str(average_daily_revenue))

print(" Total revenue : " + str(total_revenue));
print(new_prices);
print(" The average price for Haircut: " + str(average_price))

print(" Cuts under 30: " + str(custs_under_30))
