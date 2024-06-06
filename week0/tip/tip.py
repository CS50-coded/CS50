def main() -> None:
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d: str) -> float:
    return float(d.lstrip("$"))


def percent_to_float(p: str) -> float:
    return float(p.rstrip("%")) / 100


if __name__ == "__main__":
    main()
