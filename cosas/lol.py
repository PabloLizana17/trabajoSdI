from riotwatcher import LolWatcher
import json
from cosas import bases1
#import bases1
lol_watcher = LolWatcher('RGAPI-0c749318-ee82-4c39-a2b2-f9e60b5a4583')


def UserGameData(id,region):
    game = UserLastMatch(id,region)

    for i in game['participantIdentities']:
        if(i['player']['accountId']==id):
            Gid = i['participantId']

    for j in game['participants']:
        if(j['participantId'] == Gid):
            data=j

    return data

def UserData(sum,region): 
    me=lol_watcher.summoner.by_name(region,sum)
    return me['accountId']

def Getid(name,region):
    me=lol_watcher.summoner.by_name(region,name)
    return me.get('id')

def GetIdC(name,region):
    me=lol_watcher.summoner.by_name(region,name)
    return me.get('accountId')

def GetLevel(name,region):
    me=lol_watcher.summoner.by_name(region,name)
    return me.get('summonerLevel')

def Userleagues(id,region):
    leagues = []
    leagueJ = lol_watcher.league.by_summoner(region,id)
    leagues.append("Unranked")
    leagues.append("Unranked")
    for i in leagueJ:
        if(i['queueType'] == "RANKED_SOLO_5x5"):
            leagues[1] = i["tier"] + " " + i['rank']
        if(i['queueType'] == "RANKED_FLEX_SR"):
            leagues[0] = i["tier"] + " " + i['rank']
            
    return leagues

def UserMatchlist(id,region):
    matchlist = lol_watcher.match.matchlist_by_account(region,id)
    return matchlist

def GetGameId(id, region):
    match = UserMatchlist(id,region)
    lastid = match['matches'][0]['gameId']
    return lastid

def GetRegion(id, region):
    match = UserMatchlist(id,region)
    region= match['matches'][0]['platformId']
    return region

def UserLastMatch(id,region):
    Lgame = lol_watcher.match.by_id(GetRegion(id,region) ,GetGameId(id,region))
    return Lgame

def GetPuntosV(id,region):
    Udata = UserGameData(id,region)
    stats = Udata['stats']
    return stats['visionScore']

def GetWardP(id,region):
    Udata = UserGameData(id,region)
    stats = Udata.get('stats')
    return stats.get('visionWardsBoughtInGame')

def GKDA(id,region):
    Udata = UserGameData(id,region)
    stats = Udata['stats']
    KDA= ""
    for i in stats:
        if i == 'kills':
            KDA = KDA + "Asesinatos: " + str(stats.get(i)) + ", "
        if i == 'deaths':
            KDA = KDA + "Muertes: " + str(stats.get(i)) + ", "
        if i == 'assists':
            KDA = KDA + "Asistencias: " + str(stats.get(i))

    return KDA

def Gettime(id,region):
    Lgame = UserLastMatch(id,region)
    return Lgame.get('gameDuration')

def GetFarmxmin(id,region):
    game = UserLastMatch(id,region)
    Ldata = UserGameData(id,region)
    stats = Ldata.get('stats')
    time = game.get('gameDuration')
    farm = stats.get('totalMinionsKilled')
    minutos = time / 60
    return (farm / minutos)

def GetLane(id,region):
    Ldata = UserGameData(id,region)
    timeline = Ldata.get('timeline')

    if timeline.get('lane')=='BOTTOM':
        return timeline.get('role')
    else:
        return timeline.get('lane')

def GetsoloQ(leagues):
    return leagues[1]

def GetFlex(leagues):
    return leagues[0]
   
def GetPromVision(id,region):    #henry
    game = UserLastMatch(bases1.Suid(id),region)
    time = game.get('gameDuration')
    rol = bases1.Lane(id)
    vision =bases1.watcheo(id)
    minutos = time / 60

    
    if rol == 'TOP' or 'JUNGLE' or 'MIDDLE'or 'DUO_CARRY':
        
        if vision>=minutos:
                return True
        else:
                return False  
            
    if rol == 'DUO_SUPPORT':
       
        if minutos<=35:

            x=minutos*2

            if vision>=x:
                return True
            else:
                return False

        elif minutos>=36:

            x=minutos*3

            if vision>=x:
                return True
            else:
                return False
        
def GetPromFarm(id):           #henry
    rol = bases1.Lane(id)
    farm = bases1.FarmXmin(id)
    promedio= 6

    if rol=='TOP' or rol=='MIDDLE' or rol=='DUO_CARRY':
        if farm>=promedio:
            return True
        else:
            return False
    
    elif rol =='DUO_SUPP':
            return True
    
    elif rol =='JUNGLE':
        promedio = 5
        if farm>=promedio:
            return True
        else:
            return False


def GetPromPinks(id):      #he

    pink=bases1.Pinks(id)
    prom=5
    if pink>=prom:
        return True
    else:
        return False

def muertes(id):

    Kda=bases1.KDA(id)
    rol = bases1.Lane(id)
    pal = ""
    muertes = 0

    for i in Kda:
        if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'ABCDEFGHIJKLMNOPQRSTUVXYZ' or i == ':' or i == ' ':
            pal = pal + i

        if pal == " Muertes: " and i in '0123456789':
            muertes = muertes*10 + int(i)
        elif pal != " Muertes: " and i in '0123456789':
            pal = ""
        
    if rol=='TOP'or rol=='JUNGLE' or rol=='MIDDLE' or rol=='DUO_CARRY':
        
        if muertes>=4:
            return True
        else:
            return False

    elif rol=='DUO_SUPPORT':

        if muertes>=6:
            return True
        else:
            return False

def Asesinato(id):

    Kda=bases1.KDA(id)
    rol = bases1.Lane(id)
    pal = ""
    Asesinatos = 0

    for i in Kda:
        if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'ABCDEFGHIJKLMNOPQRSTUVXYZ' or i == ':' or i == ' ':
            pal = pal + i

        if pal == "Asesinatos: " and i in '0123456789':
            Asesinatos = Asesinatos*10 + int(i)
        elif pal != "Asesinatos: " and i in '0123456789':
            pal = ""

    if rol=='TOP'or rol=='JUNGLE' or rol=='MIDDLE' or rol=='DUO_CARRY':

        if Asesinatos>=5:
            return True
        else:
            return False

    elif rol=='DUO_SUPPORT':
        if Asesinatos>=6:
            return False
        else:
            return True


def Asistencia(id):

    Kda=bases1.KDA(id)
    rol = bases1.Lane(id)
    pal = ""
    asistencias = 0

    for i in Kda:
        if i in 'abcdefghijklmnopqrstuvwxyz' or i in 'ABCDEFGHIJKLMNOPQRSTUVXYZ' or i == ':' or i == ' ':
            pal = pal + i

        if pal == " Asistencias: " and i in '0123456789':
            asistencias = asistencias*10 + int(i)
        elif pal != " Asistencias: " and i in '0123456789':
            pal = ""


    if rol=='TOP'or rol=='JUNGLE' or rol=='MIDDLE' or rol=='DUO_CARRY':
        
        if asistencias>=10:
            return True
        else:
            return False

    elif rol=='DUO_SUPPORT':

        if asistencias>=15:
            return True
        else:
            return False
