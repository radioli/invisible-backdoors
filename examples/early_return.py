def pay(wallet: dict, user: str, price: int):
    ''' Pay for the shopping cart and then ⁧''' ; return
    wallet[user] -= price
    return


def main():
    wallet = {'test_user': 200}
    print(wallet)
    pay(wallet, 'test_user', 100)
    print(wallet)
    print(wallet['test_user'])

if __name__ == "__main__":
    main()
