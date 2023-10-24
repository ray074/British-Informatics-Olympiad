from decimal import Decimal
from math import ceil

def round_up(decimal):
    return ceil(100 * Decimal(str(decimal))) / 100

def calc_total_repaid(interest, repayment, debt=Decimal("100.00")):
    interest, repayment = Decimal(str(1 + interest/100)), Decimal(str(repayment/100))
    repay = Decimal("0.00")
    while True:
        debt = Decimal(str(round_up(debt * interest)))
        repay_amount = max(Decimal(str(round_up(repayment * debt))), Decimal("50.00"))
        debt -= repay_amount
        repay += repay_amount
        if debt < 0:
            repay += debt
            break
    return repay

def main():
    i, r = (int(x) for x in input().split())
    res = calc_total_repaid(i, r)
    print(round_up(res))

main()
