def parse_applicant(text):
    try:
        if not isinstance(text, str):
            return None

        category, marks = text.split(':', 1)

        category = category.strip()
        marks = float(marks.strip())

        if not category:
            return None

        return category.title(), marks

    except (ValueError, TypeError):
        return None


def marks_average(marks_csv):
    try:
        if not isinstance(marks_csv, str):
            return None

        values = [int(r.strip()) for r in marks_csv.split(',')]

        if not values:
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return None


def payable_award(text):
    try:
        if not isinstance(text, str):
            return None

        award, deduction = text.split('|')

        award = float(award.strip())
        deduction = float(deduction.strip())

        total = award * 1.18 - deduction

        return max(total, 0)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_applicant ====")

    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result)

    print("\n==== Running marks_average ====")

    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result)

    print("\n==== Running payable_award ====")

    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result)


if __name__ == "__main__":
    main()
