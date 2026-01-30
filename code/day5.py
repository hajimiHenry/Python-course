#这部分只需要学一下match case这一块

status_code=int(input('相应状态码'))
match status_code:
    case 400:description = 'bad request'
    case 401:description = 'unauthorized'
    case 403:description = 'forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述',description)

