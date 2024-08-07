from datetime import datetime


def decoratorr(func):
    def wrapper():
        if datetime.now().hour >= 22:
            func()
            print("Finishing execution")
        else:
            pass
    print(wrapper)
    return wrapper


def silence_hour():
    print("Silence, please")


silence_hour = decoratorr(silence_hour)
