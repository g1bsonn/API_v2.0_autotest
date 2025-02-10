import uuid
def generate_test_data(test_case):
    if test_case == "object_meters":
        return [
            (44, None),  # object_id, date
            (44, "2024-01-04T16:41:24"),
        ]
    elif test_case == "company_indications":
        return [
            (44, "2024-01-04T16:41:24+0200"),  # object_id, date
            (None, None),
        ]
    elif test_case == "company_balance":
        return [
            (44, None, f"{uuid.uuid4()}", 100.0, "Пополнение баланса API autotest"),  # object_id, account_id, payment_id, value, text
            (None, "ACC12345", "550e8400-e29b-41d4-a716-446655440001", -50.0, "Списание баланса API autotest"),
        ]
    else:
        return []