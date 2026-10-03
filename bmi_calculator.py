def calculate_bmi(weight, height):
    return weight / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 40)
    print("        BMI CALCULATOR")
    print("=" * 40)

    while True:
        try:
            weight = float(input("Enter your weight in kg: "))
            height = float(input("Enter your height in meters: "))

            if weight <= 0:
                print("Error: Weight must be greater than zero.")
                continue

            if height <= 0:
                print("Error: Height must be greater than zero.")
                continue

            bmi = calculate_bmi(weight, height)
            category = classify_bmi(bmi)

            print()
            print("Your BMI is:", round(bmi, 2))
            print("Category:", category)
            print()

            break

        except ValueError:
            print("Error: Please enter numbers only.")


if __name__ == "__main__":
    main()