def hours_to_minutes(hours):
    return hours * 60


def hours_to_seconds(hours):
    return hours * 3600


def minutes_to_seconds(minutes):
    return minutes * 60


def minutes_to_hours(minutes):
    return minutes / 60


def seconds_to_minutes(seconds):
    return seconds / 60


def seconds_to_hours(seconds):
    return seconds / 3600


if __name__ == "__main__":
    print("1 hora é igual a", hours_to_minutes(1), "minutos")
    print("2 horas são iguais a", hours_to_seconds(2), "segundos")
    print("300 segundos são iguais a", seconds_to_minutes(300), "minutos")
    print("7200 segundos são iguais a", seconds_to_hours(7200), "horas")
    print("120 minutos são iguais a", minutes_to_hours(120), "horas")
