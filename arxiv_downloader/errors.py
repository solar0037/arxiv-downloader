class StatusCodeError(Exception):
    def __str__(self) -> str:
        return "Wrong status code"


class ParsingError(Exception):
    def __str__(self) -> str:
        return "Failed to parse html"


class SavingError(Exception):
    def __str__(self) -> str:
        return "Failed to save pdf"
