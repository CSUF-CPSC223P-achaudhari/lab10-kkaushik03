# bots.py

import threading
import time
import json

def load_inventory():
    with open('inventory.dat', 'r') as file:
        inventory_data = json.load(file)
    return inventory_data

def bot_clerk(items):
    cart = []
    lock = threading.Lock()
    robot_fetcher_lists = {1: [], 2: [], 3: []}
    for i, item in enumerate(items, start=1):
        robot_fetcher_lists[i % 3 + 1].append(item)
    threads = []
    for i in range(1, 4):
        thread = threading.Thread(target=bot_fetcher, args=(robot_fetcher_lists[i], cart, lock))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return cart

def bot_fetcher(items, cart, lock):
    inventory = load_inventory()

    for item_number in items:
        description = get_item_description(item_number, inventory)
        sleep_seconds = get_sleep_seconds(item_number, inventory)
        time.sleep(sleep_seconds)
        with lock:
            cart.append([item_number, description])

def get_item_description(item_number, inventory):
    return inventory[item_number][0]

def get_sleep_seconds(item_number, inventory):
    return inventory[item_number][1]



