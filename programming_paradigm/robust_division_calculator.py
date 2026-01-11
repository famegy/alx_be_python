def safe_divide(numerator, denominator):
    try:
        top = float(numerator)
        bottom = float(denominator)
        
        result = top / bottom
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
    
if __name__ == "__main__":
    print("=== Robust Division Calculator ===")

    numerator = input("Enter the numerator: ")
    denominator = input("Enter the denominator: ")

    Division_result = safe_divide(numerator, denominator)
    print(f"The result of the division is {Division_result}")
        