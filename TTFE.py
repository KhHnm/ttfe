#coding:utf-8
import random
import collections

class TTFE:
    def __init__(self,row_num=7,coloum_num=5,init_max_num=3):
        self.row_num = row_num
        self.coloum_num = coloum_num
        self.init_max_num = init_max_num
        self.max_fallen_num = init_max_num-1 
        self.point = 0
    
    def initialize_board(self):
        tmp_board_state = None
        while(True):
            tmp_board_state = [[random.randint(1,self.init_max_num) for _ in range(self.coloum_num)] \
                for _ in range(self.row_num)]
            if self.check_continuable(tmp_board_state):
                break
        self.board_state = tmp_board_state
        self.initialize_touched_state()
    
    def initialize_touched_state(self):
        self.touched_state = []

    def check_continuable(self,is_search=False):
        return True

    def calc_point(self):
        delta_point = 0
        for i in self.touched_state:
            delta_point += i[0]
        
        update_num = self.touched_state[-1][0] * 2

        return delta_point, update_num

    def update_board(self, update_num):
        coord = self.touched_state[-1][-1]
        self.board_state[coord[1]][coord[0]] = update_num


    def take_action(self,touched_coord):
        touchable_flag = None
        continuable_flag = None
        if touched_coord is None: # 離した場合
            touchable_flag = True
            # self.board_stateの更新
            delta_point, update_num = self.calc_point()
            # board_stateの更新
            self.update_board(update_num)
            # point計算
            self.point += delta_point
            # self.touched_stateの更新
            self.initialize_touched_state()
            # 継続可能かチェック
            continuable_flag = self.check_continuable()

        else: # どこかを指定した場合
            continuable_flag = True

            if not self.check_touchable(touched_coord):
                touchable_flag = False
            else:
                touchable_flag = True
                # self.touched_stateの更新
                num = self.board_state[touched_coord[1]][touched_coord[0]]
                self.touched_state.append([num,touched_coord])
        
        assert touchable_flag is not None
        assert continuable_flag is not None
        
        return self.board_state, self.touched_state, touchable_flag, continuable_flag,self.point
    
    def check_touchable(self, touched_coord):
        return True


def main():
    game = TTFE()
    print(game.board_state)


if __name__ == "__main__":
    main()
    