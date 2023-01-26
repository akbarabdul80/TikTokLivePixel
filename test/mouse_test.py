from pynput.mouse import Controller

mouse = Controller()

while True :
    print('Now we have moved it to {0}'.format(
        mouse.position))
