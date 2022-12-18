# estimate value after exhange
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


#calculate currency left after an exchange
def get_change(budget, exchanging_value):
    return budget - exchanging_value


#calculate value of bills
def get_value_of_bills(denomination, number_of_bills):
    return number_of_bills * denomination


#calculate number of bills
def get_number_of_bills(budget, denomination):
    return int(budget // denomination)


#calculate leftover after exchanging into bills
def get_leftover_of_bills(budget, denomination):
    return budget % denomination


#calculate value after exchange
def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate = round((exchange_rate * (spread / 100)) + exchange_rate,2)
    return exchange_rate

