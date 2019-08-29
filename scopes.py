# Global #

yoImAGlobalVariable = 'Everybody can see me'


def hidden_room():
    i_live_in_hidden_room = 'I have a lot of secrets'
    print(i_live_in_hidden_room)
    print('I can see you' + yoImAGlobalVariable)
    print(yoImAGlobalVariable)
    return 'I Refuse to return anything'


hidden_room()
