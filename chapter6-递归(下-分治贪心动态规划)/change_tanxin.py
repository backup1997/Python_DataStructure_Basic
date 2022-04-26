def change(money,coin_list):
    coin_kind=len(coin_list)
    coin_list.sort(reverse=True)
    count=0
    for coin in coin_list:
        if money!=0:
            coin_count=money//coin
            money=money%coin
            count=count+coin_count
        else:
            break
    return count

print(change(66,[1,5,10,20]))