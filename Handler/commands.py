command_handlers = {}
command_descriptions = {}

def command(cmd, description=None):
    def decorator(func):
        command_handlers[cmd] = func
        if description:
            command_descriptions[cmd] = description
        return func
    return decorator