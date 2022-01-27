from .enums import *
from .request import *
from .errors import *
from .bedwars_stats import *

class BedWarsPlayer():
    def __init__(self,
    nickname: str,
    rank: Rank,
    json_data: dict,
    stats: Stats_total):
        self.nickname = nickname
        self.rank = rank
        self.json_data = json_data
        self.stats = stats
