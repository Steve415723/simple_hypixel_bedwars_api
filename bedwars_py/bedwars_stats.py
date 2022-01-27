from .enums import DamageType, BedWarsModeType
import math

def GetSafedata(json_data: dict,findof: str):
    try: return json_data[findof]
    except: return 0

def GetKD(kill: int,death: int):
    if death == 0 or kill == 0: return 0
    return math.floor((kill / death) * 1000) / 1000

def GetDamageTypes(json_data: dict,mode: BedWarsModeType,isFinal: bool,isKill: bool):
    if mode == BedWarsModeType.total: mode_text = ''
    else: mode_text = str(mode) + '_'
    if isFinal: final_text = 'final_'
    else: final_text = ''
    if isKill: death_text = 'kills'
    else: death_text = 'deaths'
    return {
        DamageType.entityattack: GetSafedata(json_data,f'{mode_text}entity_attack_{final_text}{death_text}_bedwars'),
        DamageType.entityexplosion: GetSafedata(json_data,f'{mode_text}entity_explosion_{final_text}{death_text}_bedwars'),
        DamageType.void: GetSafedata(json_data,f'{mode_text}void_{final_text}{death_text}_bedwars'),
        DamageType.fall: GetSafedata(json_data,f'{mode_text}fall_{final_text}{death_text}_bedwars'),
        DamageType.projectile: GetSafedata(json_data,f'{mode_text}projectile_{final_text}{death_text}_bedwars'),
        DamageType.firetick: GetSafedata(json_data,f'{mode_text}fire_tick_{final_text}{death_text}_bedwars'),
        DamageType.magic: GetSafedata(json_data,f'{mode_text}magic_{final_text}{death_text}_bedwars'),
        DamageType.suffocation: GetSafedata(json_data,f'{mode_text}suffocation_{final_text}{death_text}_bedwars')
    }

class Stats:
    def __init__(self,json_data: dict,mode: BedWarsModeType):
        if mode == BedWarsModeType.total: mode_text = ''
        else: mode_text = str(mode) + '_'
        self.json_data = json_data
        self.winstreak = GetSafedata(json_data,f'{mode_text}winstreak')
        self.win = GetSafedata(json_data,f'{mode_text}wins_bedwars')
        self.lose = GetSafedata(json_data,f'{mode_text}losses_bedwars')
        self.bedbroken = GetSafedata(json_data,f'{mode_text}beds_broken_bedwars')
        self.bedlost = GetSafedata(json_data,f'{mode_text}beds_lost_bedwars')
        self.bedkd = GetKD(self.bedbroken, self.bedlost)
        self.kill = GetSafedata(json_data,f'{mode_text}kills_bedwars')
        self.death = GetSafedata(json_data,f'{mode_text}deaths_bedwars')
        self.killtype = GetDamageTypes(self.json_data,mode=mode,isFinal=False,isKill=True)
        self.deathtype = GetDamageTypes(self.json_data,mode=mode,isFinal=False,isKill=False)
        self.kd = GetKD(self.kill, self.death)
        self.finalkill = GetSafedata(json_data,f'{mode_text}final_kills_bedwars')
        self.finaldeath = GetSafedata(json_data,f'{mode_text}final_deaths_bedwars')
        self.finalkilltype = GetDamageTypes(self.json_data,mode=mode,isFinal=True,isKill=True)
        self.finaldeathtype = GetDamageTypes(self.json_data,mode=mode,isFinal=True,isKill=False)
        self.finalkd = GetKD(self.finalkill, self.finaldeath)

class Stats_eight_one(Stats):
    pass

class Stats_eight_two(Stats):
    pass

class Stats_four_three(Stats):
    pass

class Stats_four_four(Stats):
    pass

class Stats_two_four(Stats):
    pass

class Stats_total(Stats):
    def __init__(self,json_data: dict,level: int,experience: int,
        eight_one: Stats_eight_one,
        eight_two: Stats_eight_two,
        four_three: Stats_four_three,
        four_four: Stats_four_four,
        two_four: Stats_two_four
    ):
        super().__init__(json_data=json_data,mode=BedWarsModeType.total)
        self.level = level
        self.experience = experience
        self.eight_one = eight_one
        self.eight_two = eight_two
        self.four_three = four_three
        self.four_four = four_four
        self.two_four = two_four