from decimal import Decimal


class HourTooLowError(Exception): pass
class HourTooHighError(Exception): pass

tax_charges = {
    "Chico": Decimal('0.5'),
    "Groucho": Decimal("0.7"),
    "Harpo": Decimal("0.5"),
    "Zeppo": Decimal("0.4")
}


def time_percentage(hour):
    return hour/ Decimal("24.0")


def calcualt_tax(purchase, province, hour):
    if hour < 0:
        raise HourTooLowError(f"{hour} hour is less 0")
    return purchase + (purchase * tax_charges[province] * time_percentage(hour))




print(calcualt_tax(500, 'Harpo', 12))