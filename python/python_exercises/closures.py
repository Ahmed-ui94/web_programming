def outer_function():
    message = "Hi"

    def inner_func():
        print(message)

    return inner_func


hi_func = outer_function()

hi_func()
