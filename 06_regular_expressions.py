import re


def main():

    text = """
    Contact: shweta@example.com
    Phone: 9876543210
    Website: https://example.com
    """

    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    phone_pattern = r"\b[6-9]\d{9}\b"
    number_pattern = r"\b\d+\b"

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)
    numbers = re.findall(number_pattern, text)

    print("Emails:")
    print(emails)

    print("\nPhone Numbers:")
    print(phones)

    print("\nNumbers:")
    print(numbers)


if __name__ == "__main__":
    main()
