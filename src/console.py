
def search(consult):
    pass

def help(number = 0):
    pass

options = {
    'search': search,
    'help': help,
}

def dispatcher(option, options_dict):
    try:
        return options_dict[option]
    except:
        return None
