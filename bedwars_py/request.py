import requests
from .errors import *
from .enums import Rank
from .__main__ import BedWarsPlayer
from .bedwars_stats import *

url = 'https://api.hypixel.net/player'

def Getbedwarsplayer(username: str,key: str):
    params = {
        'key':key,
        'name':username
    }
    res = requests.get(url,params=params)
    if res.status_code == 403: raise InvaildKey('요청할 수 있는 권한이 없습니다. 올바른 키를 입력했나요?')
    if res.status_code == 429: raise UsernotFound('이미 최근에 검색한 유저입니다.')
    data = res.json()
    if data["player"] == None: raise UsernotFound('유저를 찾을 수 없습니다.')
    if "rank" in data["player"] and not data["player"]["rank"] == "NORMAL": rank = data["player"]["rank"]
    elif "monthlyPackageRank" in data["player"] and not data["player"]["monthlyPackageRank"] == "NONE": rank = data["player"]["monthlyPackageRank"]
    elif "newPackageRank" in data["player"]: rank = data["player"]["newPackageRank"]
    elif "packageRank" in data["player"]: rank = data["player"]["packageRank"]
    else: rank = "None"
    ranks = {
        "None":Rank.norank,
        "VIP":Rank.vip,
        "VIP_PLUS":Rank.vipplus,
        "MVP":Rank.mvp,
        "MVP_PLUS":Rank.mvpplus,
        "SUPERSTAR":Rank.mvpplusplus,
        "YOUTUBER":Rank.youtuber,
        "ADMIN":Rank.admin
    }
    try: json_data = data['player']['stats']['Bedwars']
    except KeyError: raise DatanotFound('해당 유저는 베드워즈 플레이 기록을 가지고 있지 않습니다.')
    try: level = data['player']['achievements']['bedwars_level']
    except: level = 1
    data_stats = Stats_total(json_data=json_data,
        level=level,
        experience=GetSafedata(json_data,'Experience'),
        eight_one=Stats_eight_one(json_data=json_data,mode=BedWarsModeType.eight_one),
        eight_two=Stats_eight_two(json_data=json_data,mode=BedWarsModeType.eight_two),
        four_three=Stats_four_three(json_data=json_data,mode=BedWarsModeType.four_three),
        four_four=Stats_four_four(json_data=json_data,mode=BedWarsModeType.four_four),
        two_four=Stats_four_four(json_data=json_data,mode=BedWarsModeType.two_four)
    )
    return BedWarsPlayer(nickname=data["player"]["displayname"],rank=ranks[rank],json_data=data,stats=data_stats)