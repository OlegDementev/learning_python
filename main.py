def print_given(*args, **kwargs):
    print(args, kwargs)
    return args, kwargs


print_given(1, s=2)
