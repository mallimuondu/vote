def work():
    while True:
        try:
            age = int(input("pls input your age: "))
        except ValueError:
            print("sorry i did'nt understund that")
            continue
        else:
            if age < 18:
                print("you can not vote")
            elif age>18:
                print("you can vote")
            elif age == 18:
                print("you cant vote")
work()