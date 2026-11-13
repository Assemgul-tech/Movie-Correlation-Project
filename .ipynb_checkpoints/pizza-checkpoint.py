def make_pizza(size, *args):
    print(f"Принесли пиццу, с размером {size},которая содержит: ")
    for arg in args:
        print(f" - {arg}")