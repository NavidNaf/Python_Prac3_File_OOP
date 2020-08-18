import os
import requests
import re
import sys


def main():
    directory = "dimikpub"
    createDirectory(directory)
    scrapedPrim = collectData("http://dimik.pub/")
    keytoEngine = re.compile(
        r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)
    keytoEngine2 = re.compile(r"(\d+)\/(\w+)\-(\w+)-")
    lsofData = scrapingEngine(keytoEngine, scrapedPrim)
    # printResult(lsofData, keytoEngine2)

    for i in lsofData:
        dir = getDirectory(keytoEngine2, i[0])
        # print(i[2], i[1])
        fulldirName = directory+"/"+dir
        try:
            os.mkdir(fulldirName)
        except FileExistsError:
            print("Folder Exists.")
            pass

        with open(fulldirName+"\info.txt", "w", encoding="utf-8") as info:
            info.write("Name:"+i[2]+"\n")
            info.write("URL:"+i[0])

        response = requests.get(i[1], headers={
                                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'})
        imageByte = response.content
        print(response, i[1])
        with open(fulldirName+"\cover.jpg", "wb") as image:
            image.write(imageByte)


def createDirectory(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print("Folder Already There.")
        pass


def collectData(url):
    response = requests.get(url)
    if response.ok == False:
        sys.exit("No Response")
    text = response.text
    return text


def scrapingEngine(key, content):
    data = re.findall(key, content)
    return data


def printResult(result):
    for i in range(len(result)):
        if i == 0:
            print(f"URL: {result[0]}")
        elif i == 1:
            print(f"Image: {result[1]}")
        else:
            print(f"Name: {result[2]}")


def getDirectory(key, result):
    dirTup = re.findall(key, result)
    dirname = list(dirTup[0])
    dirName = "_".join(dirname)
    return dirName


if __name__ == "__main__":
    main()
