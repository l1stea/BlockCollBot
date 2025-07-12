command_handlers = {}

def command(cmd):
    def decorator(func):
        command_handlers[cmd] = func
        return func
    return decorator