import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="sedentary reminder",
            message="Light movement helps keep the muscles active, decreases stiff joints So please walk",
            timeout=10
        )
        time.sleep(60*60)
