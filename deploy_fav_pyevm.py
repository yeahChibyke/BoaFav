import boa 

def main():
    print("Reading into Fav contract for deployment >>> \n")

    # print("---------\n")
    fav_contract = boa.load("fav.vy")
    # print(fav_contract)
    # print("---------\n")

    fav_contract.add_person("Alice", 10)
    fav_contract.add_person("Bob", 20)
    fav_contract.add_person("Clara", 30)
    fav_contract.add_person("Dan", 40)
    fav_contract.add_person("Eli", 50)

    alice_fav_num = fav_contract.get_fav_num("Alice")
    bob_fav_num = fav_contract.get_fav_num("Bob")
    clara_fav_num = fav_contract.get_fav_num("Clara")
    dan_fav_num = fav_contract.get_fav_num("Dan")
    eli_fav_num = fav_contract.get_fav_num("Eli")

    print(f"This is Alice's favourite number: {alice_fav_num}\n")
    print(f"This is Bob's favourite number: {bob_fav_num}\n")
    print(f"This is Clara's favourite number: {clara_fav_num}\n")
    print(f"This is Dan's favourite number: {dan_fav_num}\n")
    print(f"This is Eli's favourite number: {eli_fav_num}\n")

    print("---------\n")

    fav_contract.update_fav_num("Alice", 11)
    fav_contract.update_fav_num("Bob", 22)
    fav_contract.update_fav_num("Clara", 33)
    fav_contract.update_fav_num("Dan", 44)
    fav_contract.update_fav_num("Eli", 55)

    alice_new_fav_num = fav_contract.get_fav_num("Alice")
    bob_new_fav_num = fav_contract.get_fav_num("Bob")
    clara_new_fav_num = fav_contract.get_fav_num("Clara")
    dan_new_fav_num = fav_contract.get_fav_num("Dan")
    eli_new_fav_num = fav_contract.get_fav_num("Eli")

    print(f"This is Alice's new favourite number: {alice_new_fav_num}\n")
    print(f"This is Bob's new favourite number: {bob_new_fav_num}\n")
    print(f"This is Clara's new favourite number: {clara_new_fav_num}\n")
    print(f"This is Dan's new favourite number: {dan_new_fav_num}\n")
    print(f"This is Eli's new favourite number: {eli_new_fav_num}\n")

if __name__ == "__main__":
    main()
