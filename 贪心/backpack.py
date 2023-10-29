
goods = [(60, 10),(120,30),(100,20)]    # （价格，重量）
def fractional_backpack(goods, w):
    goods.sort(key=lambda x: x[0]/x[1], reverse= True)
    total_v = 0
    m = [0 for _ in range(len(goods))]
    for i, (prize,weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
            total_v += prize
        else:
            m[i] = w / weight
            total_v += m[i] * prize
            w = 0
            break
    return m,goods,total_v
    # print(goods)

print(fractional_backpack(goods, 50))