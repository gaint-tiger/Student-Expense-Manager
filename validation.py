def validate_amount(amount):
    """
    Amount validate karta hai.
    Amount positive number hona chahiye.
    """

    try:
        value = float(amount)

        if value <= 0:
            raise ValueError(
                "Amount must be greater than 0."
            )

        return value

    except (ValueError, TypeError):
        raise ValueError(
            "Please enter a valid positive amount."
        )


def validate_name(name):
    """
    Student name validate karta hai.
    """

    if name is None:
        raise ValueError(
            "Name cannot be empty."
        )

    name = name.strip()

    if not name:
        raise ValueError(
            "Name cannot be empty."
        )

    if len(name) < 2:
        raise ValueError(
            "Name must contain at least 2 characters."
        )

    return name


def validate_category(category):
    """
    Expense category ya income source validate karta hai.
    """

    if category is None:
        raise ValueError(
            "Category cannot be empty."
        )

    category = category.strip()

    if not category:
        raise ValueError(
            "Category cannot be empty."
        )

    return category


def validate_email(email):
    """
    Basic email validation.
    """

    if email is None:
        raise ValueError(
            "Email cannot be empty."
        )

    email = email.strip()

    if "@" not in email or "." not in email:
        raise ValueError(
            "Please enter a valid email address."
        )

    return email


def validate_transaction_type(transaction_type):
    """
    Transaction type validate karta hai.
    """

    transaction_type = transaction_type.strip().lower()

    if transaction_type not in ("income", "expense"):
        raise ValueError(
            "Transaction type must be income or expense."
        )

    return transaction_type