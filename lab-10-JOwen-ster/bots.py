import threading
import time


inventory = dict()
with open('inventory.dat', 'r') as data:
    inventory = eval(data.read())
    

def bot_clerk(items):
    shopping_cart = []
    lock = threading.Lock()
    
    robot_1_items = [items[i] for i in range(len(items)) if i % 3 == 0]
    robot_2_items = [items[i] for i in range(len(items)) if i % 3 == 1]
    robot_3_items = [items[i] for i in range(len(items)) if i % 3 == 2]
    
    robot_1 = threading.Thread(target=bot_fetcher, args=(robot_1_items, shopping_cart, lock))
    robot_1.start()

    robot_2 = threading.Thread(target=bot_fetcher, args=(robot_2_items, shopping_cart, lock))
    robot_2.start()

    robot_3 = threading.Thread(target=bot_fetcher, args=(robot_3_items, shopping_cart, lock))
    robot_3.start()

    robot_1.join()
    robot_2.join()
    robot_3.join()

    return shopping_cart


def bot_fetcher(items, shopping_cart, lock: threading.Lock):
    for item in items:
        time.sleep(inventory[item][1])
        with lock:
            shopping_cart.append([item, inventory[item][0]])

