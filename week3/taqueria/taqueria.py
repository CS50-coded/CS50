from typing import NoReturn

CONST_USER_PROMT = "Item"
CONST_MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def get_user_input(str) -> str:
    res: str = input(f"{str}: ").strip()
    return res


def main() -> NoReturn:
    total = 0
    while True:
        try:
            input = get_user_input(CONST_USER_PROMT)
            total += CONST_MENU.get(input.title(), 0)
        except EOFError:
            break

    print(f"\nTotal: ${total:.2f}")


if __name__ == "__main__":
    main()
