class Film:
    def __init__(self, titel):
        self.titel = titel


def wrong_input():
    print("\nFel: Du måste välja ett alternativ från listan (1-5).")
    

def film_not_found(film_search):
    print(f"\n{film_search} finns inte i registret!")


def film_found(film_search):
    print(f"\n{film_search} finns i registret!")

