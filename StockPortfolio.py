
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "TCS": 3500,
    "Infosys": 1800,
    "Reliance": 1400,
    "Wipro": 500,
    "HDFC": 1700
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")

# Display available stocks
print("\nAvailable Stocks and Prices:")
for stock, price in stock_prices.items():
    print(stock, ":", "Rs.", price)

# Take user input
n = int(input("\nHow many different stocks do you want to buy? "))

for i in range(n):
    stock = input("\nEnter stock name: ")

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity > 0:
            portfolio[stock] = quantity
            investment = stock_prices[stock] * quantity
            total_investment += investment

            print("Investment in", stock, "= Rs.", investment)
        else:
            print("Quantity must be greater than zero.")
    else:
        print("Stock not available!")

# Display portfolio
print("\n===== Your Stock Portfolio =====")

for stock, quantity in portfolio.items():
    print(stock, "- Quantity:", quantity,
          "- Price: Rs.", stock_prices[stock],
          "- Total: Rs.", stock_prices[stock] * quantity)

print("\nTotal Investment = Rs.", total_investment)
