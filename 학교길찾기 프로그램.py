import pandas as pd
import folium
import webbrowser
from haversine import haversine
import tkinter

# 파일 오픈해서 이중리스트로 반환
def readFile(a):
    inList = []
    f = open(a, 'r', encoding="UTF-8")
    while True:
        line = f.readline()
        if not line: break
        li = line.strip("\n").split(',')
        l = []
        for i in li:
            j = i.strip().strip('\t')
            l.append(j)
        inList.append(l)
    f.close()
    return inList


# 기능3: 현재 위치/시설물 입력했을 때 가장 가까운 시설물 출력
def leastdis(lat, long, facility):
    lat = float(lat)
    long = float(long)
    newlist = [x for x in list_ if facility in x]
    poslist = []
    finlist = []
    dislist = []
    for i in range(len(newlist)):
        poslist.append(newlist[i][3:])
        finlist.append(list(map(float, poslist[i])))
    for i in range(len(finlist)):
        dislist.append(distance(lat, long, finlist[i][0], finlist[i][1]))
    index = dislist.index(min(dislist))
    #print(newlist[index])
    mapMarker(float(newlist[index][3]), float(newlist[index][4]), newlist[index][0]+newlist[index][1]+newlist[index][2])
    return newlist[index]


#기능2: 위치,시설 입력하면 위치,시설 포함한 리스트 출력
def readList(a,b,orglist):
    newlist = [x for x in orglist if a in x]
    finlist = [y for y in newlist if b in y]
    #print(finlist)
    for i in finlist:
        mapMarker(float(i[3]), float(i[4]), i[0]+i[1]+i[2])
    showmap()
    return finlist

#기능1: 시설 입력했을 때 출력
def readList_Inst(thing, orglist):
    newlist = [x for x in orglist if thing in x]
    #print(newlist)
    for i in newlist:
        mapMarker(float(i[3]), float(i[4]), i[0]+i[1]+i[2])
    showmap()
    return newlist

# 거리 구하는 함수
def distance(Latitude1, Longitude1, Latitude2, Longitude2):
    a = (Latitude1, Longitude1)
    b = (Latitude2, Longitude2)
    return haversine(a, b, unit='m')

# 맵 마커
def mapMarker(latitude, longitude, ms):
    folium.Marker([latitude, longitude], popup=ms,tooltip=ms).add_to(myMap)

# 현재위치마커
def mapMyPositionMarker(latitude, longitude):
    folium.Marker([latitude, longitude],popup="현재위치", tooltip="현재위치",icon=folium.Icon('red', icon='star'),).add_to(myMap)

def showmap():
    myMap.save('map.html')
    filepath = "map.html"
    webbrowser.open_new_tab(filepath)

def search1():
    global new
    new = tkinter.Tk()
    new.title("이거 어디있지?")
    new.geometry("320x240")
    label=tkinter.Label(new, text="시설을 입력하세요.")
    label.grid(column=0, row=0)
    
    ent1=tkinter.Entry(new)
    ent1.grid(column=0, row=2)
    
    button = tkinter.Button(new, text="확인", command=lambda: readList_Inst(ent1.get(), list_))
    button.grid(column=1, row=2)

    new.mainloop()
    
def search2():
    global new
    new = tkinter.Tk()
    new.title("이거 어디있지?")
    new.geometry("320x240")
    label=tkinter.Label(new, text="위치(건물)를 입력하세요.")
    label.grid(column=0, row=0)
    
    ent1=tkinter.Entry(new)
    ent1.grid(column=0, row=2)

    label2=tkinter.Label(new, text="시설을 입력하세요.")
    label2.grid(column=1, row=0)
    
    ent2=tkinter.Entry(new)
    ent2.grid(column=1, row=2)
    
    button = tkinter.Button(new, text="확인", command=lambda: readList(ent1.get(),ent2.get(), list_))
    button.grid(column=2, row=2)

    new.mainloop()

def search3():
    global new
    new = tkinter.Tk()
    new.title("이거 어디있지?")
    new.geometry("720x240")
    
    label=tkinter.Label(new, text="현재 위치의 위도를 입력하세요.")
    label.grid(column=0, row=0)
    
    ent1=tkinter.Entry(new)
    ent1.grid(column=0, row=2)
    
    label2=tkinter.Label(new, text="현재 위치의 경도를 입력하세요.")
    label2.grid(column=1, row=0)
    
    ent2=tkinter.Entry(new)
    ent2.grid(column=1, row=2)

    label3=tkinter.Label(new, text="찾고자 하는 시설을 입력하세요.")
    label3.grid(column=2, row=0)
    
    ent3=tkinter.Entry(new)
    ent3.grid(column=2, row=2)
    
    button = tkinter.Button(new, text="확인", command=lambda: [leastdis(ent1.get(),ent2.get(),ent3.get()), mapMyPositionMarker(float(ent1.get()),float(ent2.get())), showmap()])
    button.grid(column=3, row=2)

    new.mainloop()

def exit_window():
    window.destroy()

def GUI():
    global window
    window=tkinter.Tk()
    window.title("이거 어디있지?")
    window.geometry("640x400+100+100")
    label=tkinter.Label(window, text="이거 어디 있지?", font=('Arial', 30))
    label.pack()
    label2=tkinter.Label(window, text="박희수, 박세원, 백서연, 이다인")
    label2.pack()
    b2 = tkinter.Button(window, text = "이거 찾기",width =20, height =2,command = search1)
    b2.pack()
    b3 = tkinter.Button(window, text = "어느 건물의 이거 찾기",width =20, height =2,command =search2)
    b3.pack()
    b1 = tkinter.Button(window, text = "현재위치로 이거 찾기",width =20, height =2,command =search3)
    b1.pack()
    b4 = tkinter.Button(window, text = "종료",width =20, height =2,command =exit_window)
    b4.pack()
    window.mainloop()


# 메인

# 숙명여대 정문 좌표
sookLat = 37.54511898
sookLong = 126.96517343

# 숙명여대 중심으로 맵 생성
global myMap
myMap = folium.Map(location=[sookLat, sookLong],zoom_start=18,width=1200,height=800)
global list_
list_=readFile("학교구조.txt") #텍스트파일 입력받기
GUI()
