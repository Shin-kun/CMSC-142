coin_changes = [4, 10, 25]
coin_change = len(coin_changes) - 1
output_change = []
money_amount = 41

while coin_change >= 0:
    while money_amount >= coin_changes[coin_change]:
        money_amount -= coin_changes[coin_change]
        output_change.append(coin_changes[coin_change])
    coin_change -= 1

print ('this is the smallest coin change: ', output_change)