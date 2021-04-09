def no_loop():
    sales = float(input("Enter sales:$ "))
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(f"The bonus is ${bonus:.2f}")


def with_loop():
    sales = float(input("Enter sales:$ "))
    while sales >= 0:
        if sales < 1000:
            bonus = sales * 0.1
        else:
            bonus = sales * 0.15
        print(f"The bonus is ${bonus:.2f}")
        sales = float(input("Enter sales:$ "))
