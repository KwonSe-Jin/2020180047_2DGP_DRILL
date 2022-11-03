from pico2d import *

# 이벤트 정의
RD, LD, RU, LU, A, TIMER = range(6)

# 키입력확인을 단순화 시켜서 이벤트로 해석
key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_a): A
}

#aglobal dir, face_dir


class IDLE:
    # @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        print('enter idle')
        self.dir = 0
        self.timer = 1000
        pass

    # @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        print('exit idle')
        pass

    # @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass

    # @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)


class RUN:
    @staticmethod
    def enter(self, event):
        print('run idle')
        # 방향을 결정 해야하는데 , 뭘 근거로 ? 어떤 키가 눌렸기때문에
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        print('run exit')
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800)

        pass

    # @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)


class SLEEP:
    # @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        pass

    # @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        pass

    # @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        pass

    # @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592 / 2, '',
                                           self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                           3.141592 / 2, '',
                                           self.x - 25, self.y - 25, 100, 100)


class AUTO_RUN:
    # @staticmethod
    def enter(self, event):  # 상태에 들어갈 때 행하는 액션
        if event == A:
            if self.face_dir == -1:
                self.dir -= 1
            elif self.face_dir == 1:
                self.dir += 1
        pass

    # @staticmethod
    def exit(self):  # 상태를 나올 때 행하는 액션
        pass

    # @staticmethod
    def do(self):  # 상태에 있을때 지속적으로 행하는 액션
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

        #self.x = clamp(0, self.x, 800)
        pass

    # @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x , self.y, 200, 200)
        else:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x , self.y, 200, 200)


# 실행 변황 기술
next_state = {
    AUTO_RUN: { RD: RUN, LD: RUN, A: IDLE },
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, TIMER: SLEEP},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, A: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, A: AUTO_RUN}
}


class Boy:
    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]

            self.add_event(key_event)

    # if event.type == SDL_KEYDOWN:
    # match event.key:
    #  case pico2d.SDLK_LEFT:
    #    self.dir -= 1
    # case pico2d.SDLK_RIGHT:
    #   self.dir += 1

    # elif event.type == SDL_KEYUP:
    #   match event.key:
    #      case pico2d.SDLK_LEFT:
    #         self.dir += 1
    #        self.face_dir = -1
    #   case pico2d.SDLK_RIGHT:
    #      self.dir -= 1
    #     self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self)
            self.cur_state = next_state[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)