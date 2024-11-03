calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    list_1 = []
    list_1.extend((len(string), string.upper(), string.lower()))
    list_2 = tuple(list_1)
    count_calls()
    return list_2

def is_contains (string, list_to_search):
    logical_ = False
    list_ = [x.lower() for x in list_to_search]
    set_ = set(list_)
    for i in set_:
        if string.lower() == i:
            logical_ = True
    count_calls()
    return logical_

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)