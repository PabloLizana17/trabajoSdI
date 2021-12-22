from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from cosas import bases1,lol

# Create your views here.

def indice(request):
     doc = open("plantillas/index.html")
     plt = Template(doc.read())
     doc.close()
     ctx =Context({})
     documento=plt.render(ctx)
     return HttpResponse(documento)

def error(request):
     doc = open("plantillas/Error.html")
     plt = Template(doc.read())
     doc.close()
     ctx =Context()
     documento=plt.render(ctx)
     return HttpResponse(documento)


def respuesta(request):
     sum= request.GET['Sname']
     reg= request.GET['Region']
     regm=reg.lower()
     rer=''
     doc = open("plantillas/Datos.html")
     try:
          if (bases1.buscar_usuario(sum) == False):
               if regm=="las":
                    bases1.LlenarUsuario(sum,'la2')
                    rer = 'la2'
               elif regm=="lan":
                    bases1.LlenarUsuario(sum,'la1')
                    rer = 'la1'
          else :
               if regm=="las":
                    bases1.agregar_partidas(sum,'la2')
                    rer = 'la2'
               elif regm=="lan":
                    bases1.agregar_partidas(sum,'la1')
                    rer = 'la1'
     except:
          error = open("plantillas/Error.html")
          plt=Template(error.read())
          ctx =Context()
          doc.close()
          documento=plt.render(ctx)
          return HttpResponse(documento)
         
     x = ""
     y = ""

     #vision= lol.GetPromVision(sum,reg)

     #if(vision==True):
     #    x= x + "\n Tus puntos son perfectos, pero no mas perfectos que DRAVEN"
     #else:
     #    y = y + "Que no inviertas en vision para tu equipo es detestable, nadie mas tiene el ego tan grande como DRAVEN"

     farm= lol.GetPromFarm(sum)

     if(farm==True):
          x = x + "Tu habilidad para asesinar pequeños e indefensos subditos es increible, la especialidad de DRAVEN!!!! "
     else:
          y = y + "Tu farmeo es bajo, DRAVEN lo hara mira y aprende.... ¡Que Bueno Soy!"  
    

     Pinks= lol.GetPromPinks(sum)

     if(Pinks==True):

          x = x + "\tQue buenas compras, pero DRAVEN lo haria con mas estilo"
     else:
          y= y +"\tPocos pinks comprados, DRAVEN tendria mas ¡Y ahora a admirarme un rato!"
     
     muertes = lol.muertes(sum)

     if(muertes==True):
          y = y + "\nDemasiadas muertes incluso para el historial de DRAVEN"
     else:
          x = x +"\nQue pocas muertes, ¡Y yo ya pense que era perfecto!"

     asesinato = lol.Asesinato(sum)

     if(asesinato==True):

          x = x + "\nQue buena cantidad de Asesinatos, ¡Dale donde les duele! "
     else:
          y= y +"\nDeberias Asesinar mas, ¡Estas hachas necesitan victimas!"

     asistencias = lol.Asistencia(sum)

     if(asistencias==True):
          x = x + "\nGracias por tu ayuda, ahora DRAVEN tendra mas tiempo para admirar a DRAVEN"
     else:
          y= y +"\nNecesitas ayudar mas a tu equipo, ¡Sal a jugar!"

     if x=="":
          x = x + "DRAVEN detesta tu manera de jugar League of DRAVEN!!!!!!"

     plt=Template(doc.read())
     doc.close()
     ctx =Context({'x':x, 'y':y})
     documento=plt.render(ctx)
     bases1.guardar()
     return HttpResponse(documento)

        
