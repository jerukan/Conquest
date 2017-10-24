from eventhandlers.eventhandler import EventHandler

def run():

    eventhandler = EventHandler()

    eventhandler.resetGame()

    while True:
        eventhandler.gameLoop()



if __name__ == "__main__":
    run()