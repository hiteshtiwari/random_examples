def best_time_to_buy_stock(input_list):
    profit = 0
    buy = input_list[0]
    
    for i in input_list[1:]:
        if i > buy:
            profit = max(profit, i-buy)
        else:
            buy = i
    return profit     

input = [3,8,1,4,7,5]
print(best_time_to_buy_stock(input))