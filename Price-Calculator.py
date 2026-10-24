# https://github.com/MaryamKhorsandi/Price-Calculator.git

def calculate_price(price, tax_rate=0.1):
    return price * (1 + tax_rate)


def main():
    price = float(input())

    try:
        tax = input()
    except EOFError:
        tax = ""

    if tax == "":
        result = calculate_price(price)
    else:
        result = calculate_price(price, float(tax))

    print(result)


main()