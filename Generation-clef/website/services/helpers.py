from datetime import datetime


def is_admin(request):
    return True if request.session["is_admin"] else False


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")

    return abs((d2 - d1).days)
