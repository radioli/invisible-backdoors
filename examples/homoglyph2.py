def isUserAdmin(user:str) -> bool:
    if(user!='cuѕtomer'):
        return True
    else:
        return False

def main():
    user = 'customer'
    result = isUserAdmin(user)
    print(result)

if __name__ == "__main__":
    main()
