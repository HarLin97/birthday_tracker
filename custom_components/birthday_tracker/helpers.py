from datetime import datetime, date, time
from lunar_python import Lunar


def parse_birth_date(birth_date_str: str) -> date:
    return datetime.strptime(birth_date_str, "%Y-%m-%d").date()


def calculate_age(birth_date: date, today: date) -> int:
    return (
        today.year
        - birth_date.year
        - ((today.month, today.day) < (birth_date.month, birth_date.day))
    )


def get_next_solar_birthday(birth_date: date, today: date) -> date:
    this_year_birthday = birth_date.replace(year=today.year)
    if this_year_birthday <= today:
        return birth_date.replace(year=today.year + 1)
    return this_year_birthday


def get_days_until(target_date: date, today: date) -> int:
    return (target_date - today).days


def get_lunar_birth_date(solar_birth_date: date) -> Lunar:
    return Lunar.fromDate(datetime.combine(solar_birth_date, time()))


def get_next_lunar_birthday(lunar_birth: Lunar, today: date) -> date:
    lunar_year = Lunar.fromDate(datetime.today()).getYear()
    lunar_this_year = Lunar(
        lunar_year, lunar_birth.getMonth(), lunar_birth.getDay(), 0, 0, 0
    )
    solar_this_year = lunar_this_year.getSolar()
    solar_date = date(
        solar_this_year.getYear(), solar_this_year.getMonth(), solar_this_year.getDay()
    )
    if solar_date <= today:
        lunar_next_year = Lunar(
            lunar_year + 1, lunar_birth.getMonth(), lunar_birth.getDay(), 0, 0, 0
        )
        solar_next_year = lunar_next_year.getSolar()
        return date(
            solar_next_year.getYear(),
            solar_next_year.getMonth(),
            solar_next_year.getDay(),
        )
    return solar_date


def is_today_birthday(birthday: date, today: date) -> bool:
    return birthday.month == today.month and birthday.day == today.day
