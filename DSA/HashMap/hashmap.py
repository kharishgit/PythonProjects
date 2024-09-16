# stock_prices = []
# with open('Book1.csv','r') as stock:
#     for line in stock:
#         tokens = line.split(',')
#         day = tokens[0]
#         price = float(tokens[1])
#         stock_prices.append([day,price])
# print(stock_prices)
# # To find any particular elements
#
# for i in stock_prices:
#     if i[0] == 'Mar-06':
#         print([i[1]])

# While using the dictionary the complexity can be reduced to 0(1)
stock_prices = {}
with open('Book1.csv','r') as stock:
    for line in stock:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price
print(stock_prices['Mar-06'])

