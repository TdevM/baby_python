# Global #

yoImAGlobalVariable = 'Everybody can see me'


def hidden_room():
    i_live_in_hidden_room = 'I have a lot of secrets'
    print(i_live_in_hidden_room)
    print('I can see you: ' + yoImAGlobalVariable)
    return 'I Refuse to return anything'


def another_bunker():
    global iAmAGlobal
    iAmAGlobal = 'You are a global from the bunker'
    return 'boom'


hidden_room()
another_bunker()

print(iAmAGlobal)
