# coding:UTF-8
import sys
from MouseClient import Mouse, MouseError


def left_run(mouse):
    sensor = mouse.sensor()
    left = sensor[0]
    front = sensor[1]
    right = sensor[2]
    if left == 0 and front == 0 and right == 0:
        # 全部OK
        mouse.turn_left()
        
        mouse.go_straight()
        
    elif left == 0 and front == 0 and right == 1:
        # 左と前がOK
        mouse.turn_left()
        
        mouse.go_straight()
        
    elif left == 0 and front == 1 and right == 0:
        # 前だけNG
        mouse.turn_left()
        
        mouse.go_straight()
        
    elif left == 0 and front == 1 and right == 1:
        #  左だけOK
        mouse.turn_left()
        
        mouse.go_straight()
        
    elif left == 1 and front == 0 and right == 0:
        # 前と右がOK
        mouse.go_straight()
        
    elif left == 1 and front == 0 and right == 1:
        # 前だけOK
        mouse.go_straight()
        
    elif left == 1 and front == 1 and right == 0:
        # 右だけOK
        mouse.turn_right()
        
        mouse.go_straight()
        
    else:
        # 全部だめ
        mouse.turn_right()
        
        mouse.turn_right()
        
        mouse.go_straight()
        
    if mouse.is_goal() == 1:
        print("ゴールしました")


if __name__ == '__main__':
    print("client")
    #ローカルホスト
    mouse = Mouse("3b519d0a7f3782c67ba45e0fd4c81b1b1233b39c506b7ef88470218e9464dcf2",
                  url="http://localhost:8000/maze/v1")
    # 本サイト
    #mouse = Mouse("29d16337242edfcc24caa6e5a36bed5a0107d48e5af22e950ff4baa24cd5dcdd")
    try:
        mouse.start(10)
    except MouseError as e:
        print(e)

    for i in range(mouse.max_turn):
        while True:
            try:
                left_run(mouse)
            except:
                print("ステップオーバー")
                break
    print("ターンオーバー")
