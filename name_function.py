def formatted_name(first, last, middle=''):
    """Return a neatly formatted full name.

    - first: first name (string)
    - last: last name (string)
    - middle: optional middle name (string)

    The function strips whitespace and capitalizes each name part (title case).
    If middle is not provided or empty, returns "First Last". Otherwise returns
    "First Middle Last".
    """
    # Guard against None input for required fields
    if first is None or last is None:
        raise ValueError('First and last names are required')

    # Normalize whitespace first
    first = first.strip()
    last = last.strip()
    middle = (middle or '').strip()

    # After stripping, ensure required parts are present
    if not first or not last:
        raise ValueError('First and last names are required')

    # Capitalize properly (title() handles hyphens and apostrophes well)
    if middle:
        full_name = f"{first.title()} {middle.title()} {last.title()}"
    else:
        full_name = f"{first.title()} {last.title()}"

    return full_name
