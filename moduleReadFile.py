import random
import xlrd

#constants
SIZEROWSCATE=28
SIZEROWSTRAF=179

sheetCategory = None
sheetTraffic  = None
def createInstanceFile():
    #gettin Instance from BDCategory
    locationCategory =("data/BDCategory.xlsx")
    wbCategory = xlrd.open_workbook(locationCategory)
    global sheetCategory
    sheetCategory = wbCategory.sheet_by_index(0)
    #gettin Instance from BDTraffic
    locationTraffic =("data/BDTraffic.xlsx")
    wbTraffic = xlrd.open_workbook(locationTraffic)
    global sheetTraffic
    sheetTraffic = wbTraffic.sheet_by_index(0)
    
def getRowRandom():
    global sheetCategory
    global SIZEROWSCATE
    #sheetCategory.cell_value(random.randint(1,SIZEROWSCATE), 0)
    for i in range(sheetCategory.ncols): 
        print(sheetCategory.cell_value(random.randint(1,SIZEROWSCATE), i))
    print('###########################\n')
    global sheetTraffic
    global SIZEROWSTRAF
    #sheetTraffic.cell_value(, 0)
    for i in range(sheetTraffic.ncols): 
        print(sheetTraffic.cell_value(random.randint(1,SIZEROWSTRAF), i))
    print('=====================================')