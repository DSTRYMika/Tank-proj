from StateType import StateType

class State :
    def __init__(self,Hit_origin,Hit_angle,pos_x,pos_y,state: StateType):
        self.Hit_origin = Hit_origin
        self.Hit_angle = Hit_angle
        self.pos_x : int = pos_x
        self.pos_y = pos_y
        self.state = state

    def get_state (self) ->StateType:
        return self.state

    def action_touched (self) :
        return None

    def action_hit (self) :
        return None
