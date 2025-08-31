import random
import math

from enum import Enum


class BEHAVIOUR(Enum):
    # Not moving (start state)
    SHOOT = (6, 0)
    STOP = (0, 0.0)
    # Touching target, stop and turn back
    BUMP = (1, 30.0)
    # Too close to target, evade
    RUNNING_AWAY = (2, 100.0)
    # Not too close, not too far, random move, but no shooting
    MOVING = (3, 150)
    # In shooting range, will point to target without moving
    SHOOTING_RANGE = (4, 200)
    # Too far from target, getting closer
    COMING_BACK = (5, 350)

    def __init__(self, code: int, distance: float):
        self.code = code
        self.distance = distance


class EntityMover:
    debug: bool = False

    def __init__(self, x, y):
        # Current position
        self.x: float = x
        self.y: float = y
        # Current orientation
        self.current_orientation: float = 0.0  # degrees
        # Current motion speed
        self.current_acceleration: float = 0.0
        # Current motion speed
        self.current_speed: float = 0.0
        # Maximum speed
        self.max_speed = 1.5
        # Behaviour state
        self.current_behaviour: BEHAVIOUR = BEHAVIOUR.STOP
        # When is_aiming is true, it stop and turns before firing
        self.is_aiming: bool = False
        # How much is the aiming slower than turning
        self.aim_speed_divider: float = 3
        # How fast can it turn
        self.angle_step: float = 2  # degrees
        # How fast can if go forward
        self.normal_acceleration: float = 1
        self.previous_behaviour: BEHAVIOUR = BEHAVIOUR.STOP
        # Random chance on n:1 that it will stop and shoot
        self.shoot_probability = 0.12
        # By how much must it turn on the side before moving again when in bump mode
        self.bump_turn: float = 90
        # Delay in tick to freeze before changing behaviour or performing next move
        self.freeze_delay: int = 0
        # Delay before shooting again
        self.cooldown_delay: int = 0
        # Random direction when in move
        self.random_move_direction: float = 0

    def get_behavior_for_distance(self, d: float) -> BEHAVIOUR:
        for behaviour in BEHAVIOUR:
            # Skip the <= 0 distance states (not triggered by distance)
            if behaviour.distance <= 0:
                continue
            if d <= behaviour.distance:
                return behaviour
        return BEHAVIOUR.COMING_BACK  # fallback

    def _calculate_motion(self) -> None:
        self.current_speed += (self.current_acceleration - self.normal_acceleration / 1.15) / 25
        self.current_speed = min(max(0.0, self.current_speed), self.max_speed)
        dx: float = self.current_speed * math.cos(math.radians(self.current_orientation))
        dy: float = self.current_speed * math.sin(math.radians(self.current_orientation))
        self.x += dx
        self.y += dy

    def _roll_angle_to_180(self, angle: float) -> float:
        return ((angle + 180) % 360) - 180

    def _behave_generic(self, target_distance: float, away_angle: float, aim_speed: bool = False) -> float:
        # Choose how far we are from that, either left or right
        delta_angle: float = self.angle_delta(away_angle, self.current_orientation)

        step: float = self.angle_step
        if aim_speed:
            step /= self.aim_speed_divider

        # turn a fixed angle to aim to our destination
        if delta_angle > step:
            self.current_orientation -= step
        if delta_angle < step:
            self.current_orientation += step
        self.current_orientation = self._roll_angle_to_180(self.current_orientation)
        if self.debug:
            print(f"  target angle : {away_angle}   current angle: {self.current_orientation}   delta: {delta_angle}")
        return delta_angle

    def _behave_bump(self, target_distance, opposite_angle):
        away_angle = self._roll_angle_to_180(opposite_angle)
        self.current_behaviour = BEHAVIOUR.BUMP
        delta: float = self._behave_generic(target_distance, away_angle)
        delta_out: float = self.angle_delta(opposite_angle, self.current_orientation)
        if self.debug:
            print(f"  bump delta_out: {delta_out}   bump_turn: {self.bump_turn}")
        if abs(delta_out) > self.bump_turn:
            if self.debug:
                print("Hard bump ! - Freeze")
            self.current_acceleration = 0
            self.current_speed = 0
        else:
            if self.debug:
                print("Hard bump ! - Move again")
            self.current_acceleration = self.normal_acceleration

    def _behave_run_away(self, target_distance, opposite_angle):
        self.current_behaviour = BEHAVIOUR.RUNNING_AWAY
        self.current_acceleration = self.normal_acceleration
        self._behave_generic(target_distance, opposite_angle)

    def _behave_come_back(self, target_distance: float, away_angle):
        # Same as run away, but opposite direction
        away_angle = self._roll_angle_to_180(away_angle + 180)
        self.current_behaviour = BEHAVIOUR.COMING_BACK
        self.current_acceleration = self.normal_acceleration
        self._behave_generic(target_distance, away_angle)

    def angle_delta(self, a1: float, a2: float) -> float:
        """
        Calculate the shortest signed delta (degrees) from angle a1 to a2.
        Result is in range [-180, 180].
        """
        delta = (a2 - a1 + 180) % 360 - 180
        return delta

    def _behave_shoot_range(self, target_distance: float, away_angle) -> bool:
        away_angle = self._roll_angle_to_180(away_angle + 180)
        self.current_behaviour = BEHAVIOUR.SHOOTING_RANGE
        shoot_angle: float = abs(self.angle_delta(away_angle, self.current_orientation))
        if not self.is_aiming:

            # Only aim if not too close, not in direct line, not looking too far away, not in cooldown
            if target_distance > 50 and 120 > shoot_angle > 30 and random.random() < self.shoot_probability and self.cooldown_delay == 0:
                self.is_aiming = True
                self.freeze_delay = 50
                self.current_acceleration = 0
            else:
                self.current_acceleration = self.normal_acceleration
        else:
            # AIMING MODE - other moves are blocked
            # Same as run away, but opposite direction NO MOVE
            self.current_acceleration = 0.0  # disable movement
            delta: float = self._behave_generic(target_distance, away_angle, aim_speed=True)
            # aim for target !
            if abs(delta) <= self.angle_step / self.aim_speed_divider:
                # Aimed - will shoot after delay
                self.current_behaviour = BEHAVIOUR.SHOOT
                self.freeze_delay = 75
            else:
                # if self.debug:
                print(f"Aiming {delta}")
        return False

    def _behave_move(self, target_distance: float, away_angle) -> bool:
        # Don't change direction - just keep on moving
        self.current_acceleration = self.normal_acceleration
        self.current_behaviour = BEHAVIOUR.MOVING
        if random.random() < 0.03:
            if random.random() < 0.5:
                self.random_move_direction = self.angle_step
            else:
                self.random_move_direction = -self.angle_step
        if self.random_move_direction != 0:
            self.current_orientation += self.random_move_direction
        return False

    # Check and update behavior, and return if shooting or not
    def _update_behavior(self, target_x: float, target_y: float) -> bool:
        # Calculate distance to target
        target_distance = math.sqrt((target_x - self.x) ** 2 + (target_y - self.y) ** 2)
        # Calculate the angle between the target and the entity
        away_angle: float = math.degrees(math.atan2(self.y - target_y, self.x - target_x))
        wanted_behavior = self.get_behavior_for_distance(target_distance)

        # Aiming blocks other moves and behaviors
        if self.is_aiming:
            return self._behave_shoot_range(target_distance, away_angle)
        else:
            match wanted_behavior:
                case BEHAVIOUR.BUMP:
                    self._behave_bump(target_distance, away_angle)
                case BEHAVIOUR.RUNNING_AWAY:
                    self._behave_run_away(target_distance, away_angle)
                case BEHAVIOUR.MOVING:
                    self._behave_move(target_distance, away_angle)
                case BEHAVIOUR.SHOOTING_RANGE:
                    self._behave_shoot_range(target_distance, away_angle)
                case BEHAVIOUR.COMING_BACK:
                    self._behave_come_back(target_distance, away_angle)
        # Reset random direction when not in moving mode
        if self.current_behaviour != BEHAVIOUR.MOVING:
            self.random_move_direction = 0
        return False

    def update_position(self, target_x: float, target_y: float) -> bool:
        self._calculate_motion()
        # Burn through delay first
        if self.freeze_delay > 0:
            self.freeze_delay -= 1
            return False

        if self.cooldown_delay > 0:
            self.cooldown_delay -= 1

        if self.current_behaviour == BEHAVIOUR.SHOOT:
            print("### SHOOT ###")
            self.is_aiming = False
            # Freeze motion after shooting
            self.freeze_delay = 50
            # Go to stop mode-  don't move.
            self.current_behaviour = BEHAVIOUR.STOP
            # Add a cooldown so it doesn't shoot multiple times in a row
            self.cooldown_delay = 200
            return True

        shoot: bool = self._update_behavior(target_x, target_y)
        if self.current_behaviour != self.previous_behaviour:
            if self.debug:
                print(f"New behaviour: {self.current_behaviour}")
            self.previous_behaviour = self.current_behaviour
            if self.debug:
                print(f"Orientation: {self.current_orientation}")
        return shoot

    def get_position(self):
        return int(self.x), int(self.y)

    def get_orientation(self):
        return 90 - self.current_orientation

    def force_position(self, x, y):
        self.x = x
        self.y = y
