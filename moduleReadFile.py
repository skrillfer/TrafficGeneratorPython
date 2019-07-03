import re

import random

arrayLines = []

def getLineRandom():
    dataHash = {}
    lines = [line.rstrip('\n') for line in open('data/example.txt')]
    line  = lines[ random.randint(0, (len(lines)-1) )]
    linesSeparator = line.split('&amp;')
    
    usr = linesSeparator[0]
    dataHash['usr']=usr.replace('usr=','')
    nom = linesSeparator[1]
    dataHash['nom']=nom.replace('nom=','')
    txt = linesSeparator[2]
    dataHash['txt']=txt.replace('txt=','')

    arrayCategory =[]
    searchTag =re.findall('#[^( |#|,|)]*',txt)
    #searchTag =re.findall('#[^( |#|,|)]*','¡Escuchá, esa es la canción que #otro,#otro quiero poner en mi casamiento! #crash')
    if searchTag:
        for tag in searchTag:
           arrayCategory.append(tag)
    dataHash['categorys'] = arrayCategory
    return dataHash