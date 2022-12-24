import xmltodict as xmlDict

# На заданом участке карты найти все рестораны,
# сгруппировать их по времени работы ( с 10, с 11, и тд)

def main():
    id = []
    restaurantsName = []
    timeList = []
    flag = False
    file = open('4 - 2.osm', 'r', encoding='utf-8')
    dictParse = xmlDict.parse((file.read()))

    # Поиск id у node ресторанов
    for node in dictParse['osm']['node']:
        if 'tag' in node and isinstance(node['tag'], list):
            for tag in node['tag']:
                if tag['@v'] == 'restaurant':
                    id.append(node['@id'])

        elif 'tag' in node and isinstance(node['tag'], dict):
            if node['tag']['@v'] == 'restaurant':
                id.append(node['@id'])


    # Ищем названия ресторанов по id
    for index in range(len(id)):
        for node in dictParse['osm']['node']:
            if id[index] == node['@id']:
                for tag in node['tag']:
                    if tag['@k'] == 'name':
                        restaurantsName.append(tag['@v'])

    # Поиск времени работы по id
    for index in range(len(id)):
        for node in dictParse['osm']['node']:
            if id[index] == node['@id']:
                for tag in node['tag']:
                    if tag['@k'] == 'opening_hours':
                        timeList.append(tag['@v'])
                        flag = True
                if flag == False:
                    timeList.append("Нет времени работы")
            flag = False

    resultTime = []
    for index in range(len(timeList)):
        if timeList[index] == "Нет времени работы":
            resultTime.append(timeList[index])
        elif timeList[index] == "Su-Th 11:00-00:00; Fr-Sa 11:00-02:00":
            s1 = timeList[index][:0] + timeList[index][5:]
            s2 = s1[:6] + s1[12:]
            s3 = s2[:5] + s2[24:]
            resultTime.append(s3)
        else:
            z1 = timeList[index][:0] + timeList[index][5:]
            z2 = z1[:6] + z1[12:]
            resultTime.append(z2)

    # print(resultTime)
    d = dict(zip(restaurantsName, resultTime))
    # изменение ебучего вывода
    noTime = []
    nineTime = []
    tenTime = []
    elevenTime = []
    twelveTime = []
    for key, val in d.items():
        if val == "Нет времени работы":
            noTime.append(key)
        elif val == ' 09:00':
            nineTime.append(key)
        elif val == ' 10:00':
            tenTime.append(key)
        elif val == ' 11:00':
            elevenTime.append(key)
        elif val == ' 12:00':
            twelveTime.append(key)

    print("Нет времени ", noTime)
    print("c 09:00 ", nineTime)
    print("с 10:00 ", tenTime)
    print("с 11:00 ", elevenTime)
    print("с 12:00 ", twelveTime)


if __name__ == '__main__':
    main()

'''0: id = 1110693910 времени нету
1: id = 1409424714 <tag k="opening_hours" v="Mo-Su 09:00-23:00"/>
2: id = 1409435087 времени нету
3: id = 1645776089 времени нету
4: id = 3233987114 <tag k="opening_hours" v="Mo-Su 12:00-23:00"/>
5: id = 6606417785 <tag k="opening_hours" v="Mo-Su 11:00-23:00"/>
6: id = 6708189697 <tag k="opening_hours" v="Su-Th 11:00-00:00; Fr-Sa 11:00-02:00"/>
7: id = 7088203219 <tag k="opening_hours" v="Mo-Su 10:00-23:00"/>
8: id = 8807361717 <tag k="opening_hours" v="Mo-Su 12:00-00:00"/>
9: id = 9690501017 <tag k="opening_hours" v="Mo-Su 12:00-00:00"/>
10: id = 9743571791 <tag k="opening_hours" v="Mo-Su 08:00-23:00"/>
11: id = 9743644776 <tag k="opening_hours" v="Mo-Su 12:00-24:00"/>
12: id = 9792728168 <tag k="opening_hours" v="Mo-Su 11:08-24:00"/>
13: id = 10004656717 нету времени'''