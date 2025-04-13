
def validate_age(age):
    try:
        age = int(age)
        if age <= 0:
            raise ValueError("Age cannot be less than 1")
        elif age 0> 120:
            raise ValueError("Age is not realistic (must be less than 120)")
        return True
    except ValueError as e:
        if str(e).startswith("Age"):
            print(f"Error: {e}")
        else:
            print("Error: Please enter a valid number for age")
        return False

def main():
    while True:
        age = input("Enter your age: ")
        if validate_age(age):
            print(f"Age {age} is valid!")
            print(f"You will be {int(age) + 5} years old in 5 years.")
            break

if __name__ == "__main__":
    main()
