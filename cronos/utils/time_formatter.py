def format_time(seconds):
    """Formata o tempo em segundos para o formato hh:mm:ss."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    sec = [4800, 7821, 9999, 480, 22390]
    for num in sec:
        formated_sec = format_time(num)
        print(formated_sec)
