from colorama import Fore


class Logger:
    def __init__(self) -> None:
        self.log_level = 2 # Exclude hints

    def set_log_level(self, log_level: int):
        self.log_level = log_level

    def write_error(self, error, func) -> None:
        if self.log_level > 4: return

        print(Fore.RED + f"from: {func}\n{error}")

    def write_warning(self, warning, func) -> None:
        if self.log_level > 4: return

        print(Fore.LIGHTRED_EX + f"from: {func}\n{warning}")

    def write_hint(self, hint, func) -> None:
        if self.log_level > 4: return

        print(Fore.LIGHTBLUE_EX + f"from: {func}\n{hint}")
