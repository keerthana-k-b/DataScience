def find_absent_digits(mobile_number):
    present_digits = set(str(mobile_number))
    all_digits = set('0123456789')
    absent_digits = sorted(list(all_digits - present_digits))
    return absent_digits

mobile_number = input("Enter a 10-digit mobile number: ")
if len(mobile_number) == 10 and mobile_number.isdigit():
    absent_digits = find_absent_digits(mobile_number)
    print("Absent digits:", absent_digits)
else:
    print("Invalid mobile number. Please enter a 10-digit number.")
