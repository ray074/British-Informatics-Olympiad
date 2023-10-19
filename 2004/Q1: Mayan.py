from datetime import date, timedelta

def mayan(baktun, katun, tun, uinal, kin):
    total = (baktun * 144000) + (katun * 7200) + (tun * 360) + (uinal * 20) + kin
    start_value = 2018843
    diff = total - start_value
    g = (2000, 1, 1)
    
    gregorian_date = date(year=g[0], month=g[1], day=g[2]) + timedelta(days=diff)
    output = [str(gregorian_date.day), str(gregorian_date.month), str(gregorian_date.year)]
    return output

def main():
    baktun, katun, tun, uinal, kin = (int(x) for x in input().split())
    result = mayan(baktun, katun, tun, uinal, kin)
    print(" ".join(result))

main()
