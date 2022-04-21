def http_error(status):
    match status:
        case 200 if type(status) == int:  # доп проверки в case указываются после "if"
            return "Ok"
        case 404:
            return "Not found"
        case 403:
            return "Forbidden"
        case 501 | 510 | 500:
            return "Internal Server Error"
        case _:
            return "Other error"


def get_http_request():
    return int(input("input error code 200-500> "))


# start here

result = get_http_request()

print(http_error(result))
