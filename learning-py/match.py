def http_errors(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:  # wildcard, similar to default in JS
            return 'Unknown Error'


print(http_errors(200))  # 'OK'
print(http_errors(404))  # 'Not Found'
print(http_errors(500))  # 'Internal Server Error'
print(http_errors(600))  # 'Unknown Error'
