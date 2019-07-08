import re
import random

lines = None

def getLineRandom(source):
    dataHash = {}
    global lines
    if not lines:
        lines = [line.rstrip('\n') for line in open(source)]
    line  = lines[ random.randint(0, (len(lines)-1) )]
    linesSeparator = line.split('&amp;')
    
    usr = linesSeparator[0]
    dataHash['usr']=usr.replace('usr=','')
    nom = linesSeparator[1]
    dataHash['nom']=nom.replace('nom=','')
    txt = linesSeparator[2]
    dataHash['txt']=txt.replace('txt=','')

    
    searchTag =re.findall('#[^( |#|,|)]*',txt)
    #searchTag =re.findall('#[^( |#|,|)]*','¡Escuchá, esa es la canción que #otro,#otro quiero poner en mi casamiento! #crash')
    if searchTag:
        dataHash['categorys'] = searchTag[0]
    else:
        dataHash['categorys'] = ''
    return dataHash