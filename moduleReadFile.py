import random
import xlrd

#constants
SIZEROWSCATE=28
SIZEROWSTRAF=179

sheetCategory = None
sheetTraffic  = None
def createInstanceFile():
    global sheetCategory
    global sheetTraffic
    if sheetCategory != None or sheetTraffic!=None:
        return
    #gettin Instance from BDCategory
    locationCategory =("data/BDCategory.xlsx")
    wbCategory = xlrd.open_workbook(locationCategory)
    sheetCategory = wbCategory.sheet_by_index(0)
    #gettin Instance from BDTraffic
    locationTraffic =("data/BDTraffic.xlsx")
    wbTraffic = xlrd.open_workbook(locationTraffic)
    sheetTraffic = wbTraffic.sheet_by_index(0)
    
def getRowRandom():
    global sheetTraffic
    global SIZEROWSTRAF
    global sheetCategory
    global SIZEROWSCATE
    dataHash = {}
    #Reading all columns from random row in sheetCategory
    arrayCategory=[]
    for i in range(sheetCategory.ncols):
        arrayCategory.append(sheetCategory.cell_value(random.randint(1,SIZEROWSCATE), i))
    print('#Read Row in Category Success')
    #Reading all columns from random row in sheetTraffic
    arrayCredentialUser=[]
    for i in range(sheetTraffic.ncols): 
        arrayCredentialUser.append(sheetTraffic.cell_value(random.randint(1,SIZEROWSTRAF), i))
    print('#Read Row in Traffic Success')
    dataHash["category"] = arrayCategory
    dataHash["credentials"] = arrayCredentialUser
    return dataHash