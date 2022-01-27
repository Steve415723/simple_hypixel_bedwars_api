from enum import Enum

class Rank(Enum):
    norank = "NONE"
    vip = "VIP"
    vipplus = "VIP_PLUS"
    mvp = "MVP"
    mvpplus = "MVP_PLUS"
    mvpplusplus = "SUPERSTAR"
    youtuber = "YOUTUBER"
    admin = "ADMIN"

    def __str__(self):
        return self.value

class DamageType(Enum):
    void = "void"
    entityattack = "entity_attack"
    fall = "fall"
    entityexplosion = "entity_explosion"
    projectile = "projectile"
    firetick = "fire_tick"
    magic = "magic"
    suffocation = "suffocation"

    def __str__(self):
        return self.value

class BedWarsModeType(Enum):
    total = "total"
    eight_one = "eight_one"
    eight_two = "eight_two"
    four_three = "four_three"
    four_four = "four_four"
    two_four = "two_four"

    def __str__(self):
        return self.value