# serve unique names everytime when asked for

def get_uniq_name():
    new_name = "N" + str(get_uniq_name.counter)
    get_uniq_name.counter = get_uniq_name.counter + 1
    return new_name

get_uniq_name.counter = 0
