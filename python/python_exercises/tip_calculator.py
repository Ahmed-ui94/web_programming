def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    w = d.removeprefix('$')
    return float(w)


def percent_to_float(p):
  s = p.removesuffix("%")
  d = float(s)
  return d/100



main()