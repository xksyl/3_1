calls = 0

def count_calls ():
    global calls
    calls += 1

def string_info (string):
    count_calls()
    tuple = (len(string), string.upper(), string.lower())
    return tuple

def is_contains (string, list_to_search):
    count_calls()

    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower() or list_to_search[i].lower() in string.lower():
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

