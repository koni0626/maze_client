# coding:UTF-8
import json
import requests

class Mouse(object):

    def __init__(self):
        self.URL = "http://localhost:8000/maze/v1"
        #self.URL = "https://www.osumoi-stdio.com/maze/v1"
        self.API_KEY = "3b519d0a7f3782c67ba45e0fd4c81b1b1233b39c506b7ef88470218e9464dcf2"
        #self.API_KEY = "29d16337242edfcc24caa6e5a36bed5a0107d48e5af22e950ff4baa24cd5dcdd"
        self.token = None
        self.now_vec = 1

    def start(self, map_id):
        req_url = "{}/start/{}/{}".format(self.URL, self.API_KEY, map_id)

        r = requests.get(req_url)
        data = r.json()

        self.token = data['token']
        return data

    def sensor(self):
        req_url = "{}/sensor/{}".format(self.URL, self.token)

        r = requests.get(req_url)
        data = r.json()
        return data['sensor']

    def turn_left(self):
        req_url = "{}/turn_left/{}".format(self.URL, self.token)
        r = requests.get(req_url)
        data = r.json()
        return data

    def turn_right(self):
        req_url = "{}/turn_right/{}".format(self.URL, self.token)
        r = requests.get(req_url)
        data = r.json()
        return data

    def go_straight(self):
        req_url = "{}/go_straight/{}".format(self.URL, self.token)
        r = requests.get(req_url)
        data = r.json()
        return data


if __name__ == '__main__':
    print("client")
    mouse = Mouse()
    ret = mouse.start(1)
    print(ret)
    token = ret["token"]

    for i in range(100):
        print("{}ターン目".format(i+1))
        sensor = mouse.sensor()
        print(sensor)
        left = sensor[0]
        front = sensor[1]
        right = sensor[2]
        print(mouse.go_straight())
        if right == 0:
            print("右を向きます")
            mouse.turn_right()
        elif front == 0:
            print("直進します")
            mouse.go_straight()
        elif left == 0:
            print("左を向きます")
            mouse.turn_left()
        else:
            mouse.turn_right()

