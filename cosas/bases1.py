import psycopg2
import json
import requests
from cosas import lol
#import lol

response = requests.get('http://ddragon.leagueoflegends.com/cdn/11.12.1/data/es_MX/champion.json').json()
response_1= requests.get('http://ddragon.leagueoflegends.com/cdn/11.12.1/data/es_MX/item.json').json()
response_2= requests.get('http://ddragon.leagueoflegends.com/cdn/11.12.1/data/es_MX/summoner.json').json()

base = psycopg2.connect(
    dbname = "Proyecto",
    user = 'postgres',
    password = '1234',
    host = '127.0.0.1',
    port = '5432'    
)

cursor = base.cursor()

queri = 'INSERT INTO "Academica_campeones"(nombre,idchamp,title) VALUES (%s,%s,%s)'
queri_1 = 'INSERT INTO "Academica_items"(nombre,iditem,descripcion) VALUES (%s,%s,%s)'
queri_2 = 'INSERT INTO "Academica_sumonerspells"(nombre,idspell,descripcion) VALUES (%s,%s,%s)'
queri_3 = 'INSERT INTO "Academica_usuario"(servidor,invocador) VALUES (%s,%s)'
queri_4 = 'INSERT INTO "Academica_jugador" (summon_id,id_summon,"accountId",level,"ligaS","ligaF") VALUES(%s,%s,%s,%s,%s,%s)'
queri_5 = 'INSERT INTO "Academica_partidas" ("idSummon_id","idGame") VALUES(%s,%s)'
queri_6 = 'INSERT INTO "Academica_game" (idgame_id,"KDA","Farmxmin",lane,vision,pinks) VALUES(%s,%s,%s,%s,%s,%s)'
queri_Buscar = 'SELECT nombre FROM "Academica_campeones"  WHERE idchamp = %s'
queri_Buscar_1 = 'SELECT * FROM "Academica_items"  WHERE iditem = %s'
queri_Buscar_2 = 'SELECT * FROM "Academica_sumonerspells"  WHERE idspell = %s'
queri_Buscar_3 = 'SELECT * FROM "Academica_usuario"  WHERE invocador = %s'            
queri_Buscar_4 = 'SELECT * FROM "Academica_jugador"  WHERE summon_id = %s'            #summon_id= key jugador
queri_Buscar_5 = 'SELECT * FROM "Academica_partidas"  WHERE idSummon_id = %s'         #idSummin_id=  partidas
queri_Buscar_6 = 'SELECT * FROM "Academica_game"  WHERE idgame_id = %s'               #idgame_id = fk partida
queri_I1 = 'SELECT id_summon FROM "Academica_jugador" WHERE summon_id= %s'
queri_I2='SELECT "idGame" FROM "Academica_partidas" WHERE "idSummon_id" = %s'
queri_farmxmin='SELECT "Farmxmin" FROM "Academica_game" WHERE idgame_id = %s'
queri_lane='SELECT lane FROM "Academica_game" WHERE idgame_id = %s'
queri_vision='SELECT vision FROM "Academica_game" WHERE idgame_id = %s'
queri_pink='SELECT pinks FROM "Academica_game" WHERE idgame_id = %s'
queri_id = 'SELECT "accountId" FROM "Academica_jugador" WHERE summon_id =%s'
queri_Kda = 'SELECT "KDA" FROM "Academica_game" WHERE idgame_id = %s'
campeones = response['data']
items = response_1['data']
Sspells = response_2['data']

def Llenarjson():
    for i in campeones:
        cursor.execute(queri,(i,campeones[i]['key'],campeones[i]['title']))
    
    for i in items:
        cursor.execute(queri_1,(items[i]['name'],i,items[i]['plaintext']) )
    
    for i in Sspells:
        cursor.execute(queri_2,(i,Sspells[i]["key"],Sspells[i]["description"]))

def LlenarUsuario(summon,region):
     
    cursor.execute(queri_3,(region,summon))
    id = lol.Getid(summon,region)
    accounyID = lol.GetIdC(summon,region)
    lvl = lol.GetLevel(summon,region)
    Solo = lol.GetsoloQ(lol.Userleagues(id,region))
    Flex = lol.GetFlex(lol.Userleagues(id,region))
    cursor.execute(queri_4,(summon,id,accounyID,lvl,Solo,Flex))
    cursor.execute(queri_5,(id,lol.GetGameId(accounyID,region)))
    cursor.execute(queri_6,(lol.GetGameId(accounyID,region),lol.GKDA(accounyID,region),lol.GetFarmxmin(accounyID,region),lol.GetLane(accounyID,region),lol.GetPuntosV(accounyID,region),lol.GetWardP(accounyID,region)))
     

def cerrar():
     
    base.commit()
    cursor.close()
    
def guardar():
    base.commit()

def buscar_campeones(cid):
     
    cursor.execute(queri_Buscar,(cid,))
    row= cursor.fetchall()
    print(row['nombre'])
     

def agregar_partidas(summon,region):
     
    id = lol.Getid(summon,region)
    accounyID = lol.GetIdC(summon,region)
    gameid = lol.GetGameId(accounyID,region)
    cursor.execute(queri_Buscar_6,(str(gameid),))
    row=cursor.fetchall()
    if(row == [] ):
        cursor.execute(queri_5,(id,str(gameid)))
        cursor.execute(queri_6,(str(gameid),lol.GKDA(accounyID,region),lol.GetFarmxmin(accounyID,region),lol.GetLane(accounyID,region),lol.GetPuntosV(accounyID,region),lol.GetWardP(accounyID,region)))
     

def buscar_usuario(sumon):
     
    cursor.execute(queri_Buscar_3,(sumon,))
    row= cursor.fetchall()
     
    if(row == [] ):
        return False
    else:
        return True  
    

def FarmXmin(sumonid):
     
    cursor.execute(queri_I1,(sumonid,))
    row= cursor.fetchall()
    cursor.execute(queri_I2,(row[0][0],))
    row= cursor.fetchall()
    cursor.execute(queri_farmxmin,((row[0][0],)))
    row= cursor.fetchall()
     
    return float(row[0][0]) 
    


def Lane(sumonid):

    cursor.execute(queri_I1,(sumonid,))
    row= cursor.fetchall()
    cursor.execute(queri_I2,(row[0][0],))
    row= cursor.fetchall()
    cursor.execute(queri_lane,((row[0][0],)))
    row= cursor.fetchall()
    return row[0][0]


def Pinks(sumonid):
    cursor.execute(queri_I1,(sumonid,))
    row= cursor.fetchall()
    cursor.execute(queri_I2,(row[0][0],))
    row= cursor.fetchall()
    cursor.execute(queri_pink,((row[0][0],)))
    row= cursor.fetchall()
    return float(row[0][0])
   
   
def watcheo(sumonid):
    cursor.execute(queri_I1,(sumonid,))
    row= cursor.fetchall()
    cursor.execute(queri_I2,(row[0][0],))
    row= cursor.fetchall()
    cursor.execute(queri_vision,((row[0][0],)))
    row= cursor.fetchall()
    return float(row[0][0])

def  Suid(name):
    cursor.execute(queri_id,(name,))
    row= cursor.fetchall()
    return(row[0][0])
    
def KDA(name):
    cursor.execute(queri_I1,(name,))
    row= cursor.fetchall()
    cursor.execute(queri_I2,(row[0][0],))
    row= cursor.fetchall()
    cursor.execute(queri_Kda,(row[0][0],))
    row= cursor.fetchall()
    return(row[0][0])

