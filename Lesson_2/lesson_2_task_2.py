def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2024  # Заменить на любой год для проверки
result = is_year_leap(year)
print(f"год {year}: {result}")
