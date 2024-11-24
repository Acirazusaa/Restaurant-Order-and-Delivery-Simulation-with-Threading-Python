import threading
import time
import queue

class Restaurant:
    def __init__(self):
        self.order_queue = queue.Queue()

    def receive_order(self, order):
        print(f'Received order: {order}')
        self.order_queue.put(order)

class DeliveryTeam:
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def deliver_order(self):
        while True:
            if not self.restaurant.order_queue.empty():
                order = self.restaurant.order_queue.get()
                print(f'Delivering order: {order}')
                time.sleep(2)
                print(f'Order delivered: {order}')
            else:
                time.sleep(1)
                
    def stop_delivery(self):
        self.running = False

if __name__ == '__main__':
    restaurant = Restaurant()
    delivery_team = DeliveryTeam(restaurant)

    delivery_thread = threading.Thread(target=delivery_team.deliver_order)
    delivery_thread.start()

    orders = ['Pizza', 'Chicken', 'Pasta', 'Salad', 'Ice Cream', 'Sushi', 'Drinks']

    for order in orders:
        restaurant.receive_order(order)
        time.sleep(1) 

    delivery_thread.join()
    
    delivery_team.stop_delivery()
    
    print("All Orders Has Been Delivered!")
