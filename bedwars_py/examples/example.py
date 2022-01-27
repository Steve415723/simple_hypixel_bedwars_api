from bedwars_py import Getbedwarsplayer

key = "여기에 당신의 하이핑셀 API 키를 입력하세요. 하핑 인게임에서 /api 명령어로 확인할 수 있습니다."
username = "여기에 검색할 유저의 이름을 입력하세요."

player = Getbedwarsplayer(username=username,key=key) # 플레이어의 정보가 많을수록 로딩 시간이 오래 걸릴 수 있습니다.

print(f'{player.nickname} 님의 간단한 베드워즈 정보')
print(f'파이널 킬: {player.stats.finalkill}, 파이널 데스: {player.stats.finaldeath}, 킬뎃: {player.stats.finalkd}')
