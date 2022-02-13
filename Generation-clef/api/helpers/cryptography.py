from datetime import datetime


def create_hash():
    return f"{datetime.now().timestamp() * 1000} + Magic"
