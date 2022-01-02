class StringUtils:
    def is_blank(string: str):
        return not (string and string.strip() and len(string) > 0)

    def is_not_blank(string: str):
        return string and string.strip() and len(string) > 0
