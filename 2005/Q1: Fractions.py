from decimal import Decimal


def convert(dec_val):
    num, denom = dec_val.as_integer_ratio()
    return f"{num} / {denom}"


def main():
    dec_val = Decimal(input())
    print(convert(dec_val))


main()
