def format_time(seconds):
    """Formata o tempo em segundos para o formato hh:mm:ss."""

    # 101 / 4 = 4 * 25 + 1
    # 101 // 4 = 25
    # 101 % 4 = 1

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


if __name__ == "__main__":
    sec = [4800, 7821, 9999, 480, 22390]

    # deve resultar nos seguintes valores
    # 01:20:00 (1)
    # 02:10:21 (2)
    # 02:46:39 (3)
    # 00:08:00 (4)
    # 06:13:10 (5)

    for num in sec:
        formated_sec = format_time(num)
        print(formated_sec)
