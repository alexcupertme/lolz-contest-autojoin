import base64
import threading
import cv2
import requests
import time
import json
import os

def get_xfToken(headers):
    try:
        time.sleep(0.5)
        xf = requests.get('https://lolz.guru/', headers = headers).text
        return xf.split('name="_xfToken" value="')[1].split('"')[0]
    except:
        time.sleep(3)

def parseCookies(cookies):
    everything = json.loads(cookies)
    result = ''
    for i in everything:
        if i['name'] != 'df_id':
            result = result + i['name'] + '=' + i['value'] + '; '
        else:
            response = requests.get('https://lolz.guru/process-qv9ypsgmv9.js', headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}).text.split('[')[1].split(']')[0].replace('\'', '').replace('+', '').split(',')[-1]
            df_id = str(base64.b64decode(str(response)))[2:-1]
            result = result + i['name'] + '=' + str(df_id) + '; '

    return result[:-1]

def participate(id, headers, hash, x, y):
    try:
        xf = get_xfToken(headers)
        print(xf, 'xf')
        time.sleep(0.5)
        response = requests.post(f'https://lolz.guru/threads/{id}/participate', headers = headers, data = {'captcha_hash': hash, 'captcha_type': 'ClickCaptcha', 'x': x, 'y': y, '_xfRequestUri': f'/threads/{id}/', '_xfNoRedirect': 1, '_xfToken': xf, '_xfResponseType': 'json'}).json()
        return response
    except:
        time.sleep(3)

def captchainfo(headers, id):
    time.sleep(0.5)
    try:
        response = requests.get(f'https://lolz.guru/threads/{id}/', headers = headers).text
        hash = response.split('name="captcha_hash" value="')[1].split('"')[0]
        captcha = response.split('XenForo.ClickCaptcha.imgData = "')[1].split('"')[0]
        with open(f"captcha\\{id}_captcha.png", "wb") as fh:
            fh.write(base64.b64decode(captcha))

        return hash
    except:
        time.sleep(3)

def getids(headers):
    time.sleep(0.5)
    try:
        response = requests.get('https://lolz.guru/forums/contests/', headers = headers).text
        ids = response.split('<div id="thread-')
        del ids[0]

        for i in range(len(ids)):
            ids[i] = ids[i].split('"')[0]

        return ids
    except:
        time.sleep(3)

def getanscol(id):
    ansy = 0
    ansx = 0
    pause = False

    img = cv2.imread(f'captcha\\{id}_captcha.png', cv2.IMREAD_GRAYSCALE)
    cv2.imwrite(f'captcha\\{id}_gray.png', img)
    ans = []

    for x in range(250):
        for y in range(250):
            try:
                if img[x][y] != 64:
                    if img[x][y] == img[x+9][y] == img[x][y+9] == img[x+9][y+9]:
                        anscol = img[x][y]
                        break
            except:
                pass

    for x in range(250):
        for y in range(250):
            try:
                if img[x][y] != 64 and img[x][y] != anscol:
                    img[x][y] = anscol
            except:
                pass

    cv2.imwrite(f'captcha\\{id}_nortach1.png', img)

    for y in range(250):
        for x in range(250):
            try:
                if img[y][x] == anscol:
                    #print(x, y, '(', img[x][y], ')', '===', anscol)
                    if img[y][x] == img[y][x + 1] == img[y][x + 2] == img[y][x + 3] == img[y][x + 4] == img[y][x + 5] == img[y][x + 6] == img[y][x + 7] == img[y][x + 8] == img[y][x + 9] == img[y][x + 10] == img[y][x + 11] == img[y][x + 12] == img[y][x + 13] == img[y][x + 14] == img[y][x + 15] == img[y][x + 16] == img[y][x + 17] == img[y][x + 18] == img[y][x + 19] == img[y][x + 20] == img[y + 1][x] == img[y + 1][x + 1] == img[y + 1][x + 2] == img[y + 1][x + 3] == img[y + 1][x + 4] == img[y + 1][x + 5] == img[y + 1][x + 6] == img[y + 1][x + 7] == img[y + 1][x + 8] == img[y + 1][x + 9] == img[y + 1][x + 10] == img[y + 1][x + 11] == img[y + 1][x + 12] == img[y + 1][x + 13] == img[y + 1][x + 14] == img[y + 1][x + 15] == img[y + 1][x + 16] == img[y + 1][x + 17] == img[y + 1][x + 18] == img[y + 1][x + 19] == img[y + 1][x + 20]: #== img[y + 2][x] == img[y + 2][x + 1] == img[y + 2][x + 2] == img[y + 2][x + 3] == img[y + 2][x + 4] == img[y + 2][x + 5] == img[y + 2][x + 6] == img[y + 2][x + 7] == img[y + 2][x + 8] == img[y + 2][x + 9] == img[y + 2][x + 10] == img[y + 2][x + 11] == img[y + 2][x + 12] == img[y + 2][x + 13] == img[y + 2][x + 14] == img[y + 2][x + 15] == img[y + 2][x + 16] == img[y + 2][x + 17] == img[y + 2][x + 18] == img[y + 2][x + 19] == img[y + 2][x + 20]: #== img[x][y+3] == img[x+1][y+3] == img[x+2][y+3] == img[x+3][y+3] == img[x+4][y+3] == img[x+5][y+3] == img[x+6][y+3] == img[x+7][y+3] == img[x+8][y+3] == img[x+9][y+3] == img[x+10][y+3] == img[x+11][y+3] == img[x+12][y+3] == img[x+13][y+3] == img[x+14][y+3] == img[x+15][y+3] == img[x+16][y+3] == img[x+17][y+3] == img[x+18][y+3] == img[x+19][y+3] == img[x+20][y+3] == img[x][y+4] == img[x+1][y+4] == img[x+2][y+4] == img[x+3][y+4] == img[x+4][y+4] == img[x+5][y+4] == img[x+6][y+4] == img[x+7][y+4] == img[x+8][y+4] == img[x+9][y+4] == img[x+10][y+4] == img[x+11][y+4] == img[x+12][y+4] == img[x+13][y+4] == img[x+14][y+4] == img[x+15][y+4] == img[x+16][y+4] == img[x+17][y+4] == img[x+18][y+4] == img[x+19][y+4] == img[x+20][y+4] == img[x][y+5] == img[x+1][y+5] == img[x+2][y+5] == img[x+3][y+5] == img[x+4][y+5] == img[x+5][y+5] == img[x+6][y+5] == img[x+7][y+5] == img[x+8][y+5] == img[x+9][y+5] == img[x+10][y+5] == img[x+11][y+5] == img[x+12][y+5] == img[x+13][y+5] == img[x+14][y+5] == img[x+15][y+5] == img[x+16][y+5] == img[x+17][y+5] == img[x+18][y+5] == img[x+19][y+5] == img[x+20][y+5] == img[x][y+6] == img[x+1][y+6] == img[x+2][y+6] == img[x+3][y+6] == img[x+4][y+6] == img[x+5][y+6] == img[x+6][y+6] == img[x+7][y+6] == img[x+8][y+6] == img[x+9][y+6] == img[x+10][y+6] == img[x+11][y+6] == img[x+12][y+6] == img[x+13][y+6] == img[x+14][y+6] == img[x+15][y+6] == img[x+16][y+6] == img[x+17][y+6] == img[x+18][y+6] == img[x+19][y+6] == img[x+20][y+6] == img[x][y+7] == img[x+1][y+7] == img[x+2][y+7] == img[x+3][y+7] == img[x+4][y+7] == img[x+5][y+7] == img[x+6][y+7] == img[x+7][y+7] == img[x+8][y+7] == img[x+9][y+7] == img[x+10][y+7] == img[x+11][y+7] == img[x+12][y+7] == img[x+13][y+7] == img[x+14][y+7] == img[x+15][y+7] == img[x+16][y+7] == img[x+17][y+7] == img[x+18][y+7] == img[x+19][y+7] == img[x+20][y+7] == img[x][y+8] == img[x+1][y+8] == img[x+2][y+8] == img[x+3][y+8] == img[x+4][y+8] == img[x+5][y+8] == img[x+6][y+8] == img[x+7][y+8] == img[x+8][y+8] == img[x+9][y+8] == img[x+10][y+8] == img[x+11][y+8] == img[x+12][y+8] == img[x+13][y+8] == img[x+14][y+8] == img[x+15][y+8] == img[x+16][y+8] == img[x+17][y+8] == img[x+18][y+8] == img[x+19][y+8] == img[x+20][y+8] == img[x][y+9] == img[x+1][y+9] == img[x+2][y+9] == img[x+3][y+9] == img[x+4][y+9] == img[x+5][y+9] == img[x+6][y+9] == img[x+7][y+9] == img[x+8][y+9] == img[x+9][y+9] == img[x+10][y+9] == img[x+11][y+9] == img[x+12][y+9] == img[x+13][y+9] == img[x+14][y+9] == img[x+15][y+9] == img[x+16][y+9] == img[x+17][y+9] == img[x+18][y+9] == img[x+19][y+9] == img[x+20][y+9] == img[x][y+10] == img[x+1][y+10] == img[x+2][y+10] == img[x+3][y+10] == img[x+4][y+10] == img[x+5][y+10] == img[x+6][y+10] == img[x+7][y+10] == img[x+8][y+10] == img[x+9][y+10] == img[x+10][y+10] == img[x+11][y+10] == img[x+12][y+10] == img[x+13][y+10] == img[x+14][y+10] == img[x+15][y+10] == img[x+16][y+10] == img[x+17][y+10] == img[x+18][y+10] == img[x+19][y+10] == img[x+20][y+10] == img[x][y+11] == img[x+1][y+11] == img[x+2][y+11] == img[x+3][y+11] == img[x+4][y+11] == img[x+5][y+11] == img[x+6][y+11] == img[x+7][y+11] == img[x+8][y+11] == img[x+9][y+11] == img[x+10][y+11] == img[x+11][y+11] == img[x+12][y+11] == img[x+13][y+11] == img[x+14][y+11] == img[x+15][y+11] == img[x+16][y+11] == img[x+17][y+11] == img[x+18][y+11] == img[x+19][y+11] == img[x+20][y+11] == img[x][y+12] == img[x+1][y+12] == img[x+2][y+12] == img[x+3][y+12] == img[x+4][y+12] == img[x+5][y+12] == img[x+6][y+12] == img[x+7][y+12] == img[x+8][y+12] == img[x+9][y+12] == img[x+10][y+12] == img[x+11][y+12] == img[x+12][y+12] == img[x+13][y+12] == img[x+14][y+12] == img[x+15][y+12] == img[x+16][y+12] == img[x+17][y+12] == img[x+18][y+12] == img[x+19][y+12] == img[x+20][y+12] == img[x][y+13] == img[x+1][y+13] == img[x+2][y+13] == img[x+3][y+13] == img[x+4][y+13] == img[x+5][y+13] == img[x+6][y+13] == img[x+7][y+13] == img[x+8][y+13] == img[x+9][y+13] == img[x+10][y+13] == img[x+11][y+13] == img[x+12][y+13] == img[x+13][y+13] == img[x+14][y+13] == img[x+15][y+13] == img[x+16][y+13] == img[x+17][y+13] == img[x+18][y+13] == img[x+19][y+13] == img[x+20][y+13] == img[x][y+14] == img[x+1][y+14] == img[x+2][y+14] == img[x+3][y+14] == img[x+4][y+14] == img[x+5][y+14] == img[x+6][y+14] == img[x+7][y+14] == img[x+8][y+14] == img[x+9][y+14] == img[x+10][y+14] == img[x+11][y+14] == img[x+12][y+14] == img[x+13][y+14] == img[x+14][y+14] == img[x+15][y+14] == img[x+16][y+14] == img[x+17][y+14] == img[x+18][y+14] == img[x+19][y+14] == img[x+20][y+14] == img[x][y+15] == img[x+1][y+15] == img[x+2][y+15] == img[x+3][y+15] == img[x+4][y+15] == img[x+5][y+15] == img[x+6][y+15] == img[x+7][y+15] == img[x+8][y+15] == img[x+9][y+15] == img[x+10][y+15] == img[x+11][y+15] == img[x+12][y+15] == img[x+13][y+15] == img[x+14][y+15] == img[x+15][y+15] == img[x+16][y+15] == img[x+17][y+15] == img[x+18][y+15] == img[x+19][y+15] == img[x+20][y+15] == img[x][y+16] == img[x+1][y+16] == img[x+2][y+16] == img[x+3][y+16] == img[x+4][y+16] == img[x+5][y+16] == img[x+6][y+16] == img[x+7][y+16] == img[x+8][y+16] == img[x+9][y+16] == img[x+10][y+16] == img[x+11][y+16] == img[x+12][y+16] == img[x+13][y+16] == img[x+14][y+16] == img[x+15][y+16] == img[x+16][y+16] == img[x+17][y+16] == img[x+18][y+16] == img[x+19][y+16] == img[x+20][y+16] == img[x][y+17] == img[x+1][y+17] == img[x+2][y+17] == img[x+3][y+17] == img[x+4][y+17] == img[x+5][y+17] == img[x+6][y+17] == img[x+7][y+17] == img[x+8][y+17] == img[x+9][y+17] == img[x+10][y+17] == img[x+11][y+17] == img[x+12][y+17] == img[x+13][y+17] == img[x+14][y+17] == img[x+15][y+17] == img[x+16][y+17] == img[x+17][y+17] == img[x+18][y+17] == img[x+19][y+17] == img[x+20][y+17] == img[x][y+18] == img[x+1][y+18] == img[x+2][y+18] == img[x+3][y+18] == img[x+4][y+18] == img[x+5][y+18] == img[x+6][y+18] == img[x+7][y+18] == img[x+8][y+18] == img[x+9][y+18] == img[x+10][y+18] == img[x+11][y+18] == img[x+12][y+18] == img[x+13][y+18] == img[x+14][y+18] == img[x+15][y+18] == img[x+16][y+18] == img[x+17][y+18] == img[x+18][y+18] == img[x+19][y+18] == img[x+20][y+18] == img[x][y+19] == img[x+1][y+19] == img[x+2][y+19] == img[x+3][y+19] == img[x+4][y+19] == img[x+5][y+19] == img[x+6][y+19] == img[x+7][y+19] == img[x+8][y+19] == img[x+9][y+19] == img[x+10][y+19] == img[x+11][y+19] == img[x+12][y+19] == img[x+13][y+19] == img[x+14][y+19] == img[x+15][y+19] == img[x+16][y+19] == img[x+17][y+19] == img[x+18][y+19] == img[x+19][y+19] == img[x+20][y+19] == img[x][y+20] == img[x+1][y+20] == img[x+2][y+20] == img[x+3][y+20] == img[x+4][y+20] == img[x+5][y+20] == img[x+6][y+20] == img[x+7][y+20] == img[x+8][y+20] == img[x+9][y+20] == img[x+10][y+20] == img[x+11][y+20] == img[x+12][y+20] == img[x+13][y+20] == img[x+14][y+20] == img[x+15][y+20] == img[x+16][y+20] == img[x+17][y+20] == img[x+18][y+20] == img[x+19][y+20] == img[x+20][y+20]:
                        #print(x, y, 'чемпион')
                        for i in range(21):
                            for o in range(2):
                                img[y + o][x + i] = 64

            except:
                pass

    for y in range(250):
        for x in range(250):
            try:
                if img[x][y] == anscol:
                    #print(x, y, '(', img[x][y], ')', '==', anscol)
                    if img[x][y] == img[x+1][y] == img[x+2][y] == img[x+3][y] == img[x+4][y] == img[x+5][y] == img[x+6][y] == img[x+7][y] == img[x+8][y] == img[x+9][y] == img[x+10][y] == img[x+11][y] == img[x+12][y] == img[x+13][y] == img[x+14][y] == img[x+15][y] == img[x+16][y] == img[x+17][y] == img[x+18][y] == img[x+19][y] == img[x+20][y] == img[x][y+1] == img[x+1][y+1] == img[x+2][y+1] == img[x+3][y+1] == img[x+4][y+1] == img[x+5][y+1] == img[x+6][y+1] == img[x+7][y+1] == img[x+8][y+1] == img[x+9][y+1] == img[x+10][y+1] == img[x+11][y+1] == img[x+12][y+1] == img[x+13][y+1] == img[x+14][y+1] == img[x+15][y+1] == img[x+16][y+1] == img[x+17][y+1] == img[x+18][y+1] == img[x+19][y+1] == img[x+20][y+1]: #== img[x][y+2] == img[x+1][y+2] == img[x+2][y+2] == img[x+3][y+2] == img[x+4][y+2] == img[x+5][y+2] == img[x+6][y+2] == img[x+7][y+2] == img[x+8][y+2] == img[x+9][y+2] == img[x+10][y+2] == img[x+11][y+2] == img[x+12][y+2] == img[x+13][y+2] == img[x+14][y+2] == img[x+15][y+2] == img[x+16][y+2] == img[x+17][y+2] == img[x+18][y+2] == img[x+19][y+2] == img[x+20][y+2]: #== img[x][y+3] == img[x+1][y+3] == img[x+2][y+3] == img[x+3][y+3] == img[x+4][y+3] == img[x+5][y+3] == img[x+6][y+3] == img[x+7][y+3] == img[x+8][y+3] == img[x+9][y+3] == img[x+10][y+3] == img[x+11][y+3] == img[x+12][y+3] == img[x+13][y+3] == img[x+14][y+3] == img[x+15][y+3] == img[x+16][y+3] == img[x+17][y+3] == img[x+18][y+3] == img[x+19][y+3] == img[x+20][y+3] == img[x][y+4] == img[x+1][y+4] == img[x+2][y+4] == img[x+3][y+4] == img[x+4][y+4] == img[x+5][y+4] == img[x+6][y+4] == img[x+7][y+4] == img[x+8][y+4] == img[x+9][y+4] == img[x+10][y+4] == img[x+11][y+4] == img[x+12][y+4] == img[x+13][y+4] == img[x+14][y+4] == img[x+15][y+4] == img[x+16][y+4] == img[x+17][y+4] == img[x+18][y+4] == img[x+19][y+4] == img[x+20][y+4] == img[x][y+5] == img[x+1][y+5] == img[x+2][y+5] == img[x+3][y+5] == img[x+4][y+5] == img[x+5][y+5] == img[x+6][y+5] == img[x+7][y+5] == img[x+8][y+5] == img[x+9][y+5] == img[x+10][y+5] == img[x+11][y+5] == img[x+12][y+5] == img[x+13][y+5] == img[x+14][y+5] == img[x+15][y+5] == img[x+16][y+5] == img[x+17][y+5] == img[x+18][y+5] == img[x+19][y+5] == img[x+20][y+5] == img[x][y+6] == img[x+1][y+6] == img[x+2][y+6] == img[x+3][y+6] == img[x+4][y+6] == img[x+5][y+6] == img[x+6][y+6] == img[x+7][y+6] == img[x+8][y+6] == img[x+9][y+6] == img[x+10][y+6] == img[x+11][y+6] == img[x+12][y+6] == img[x+13][y+6] == img[x+14][y+6] == img[x+15][y+6] == img[x+16][y+6] == img[x+17][y+6] == img[x+18][y+6] == img[x+19][y+6] == img[x+20][y+6] == img[x][y+7] == img[x+1][y+7] == img[x+2][y+7] == img[x+3][y+7] == img[x+4][y+7] == img[x+5][y+7] == img[x+6][y+7] == img[x+7][y+7] == img[x+8][y+7] == img[x+9][y+7] == img[x+10][y+7] == img[x+11][y+7] == img[x+12][y+7] == img[x+13][y+7] == img[x+14][y+7] == img[x+15][y+7] == img[x+16][y+7] == img[x+17][y+7] == img[x+18][y+7] == img[x+19][y+7] == img[x+20][y+7] == img[x][y+8] == img[x+1][y+8] == img[x+2][y+8] == img[x+3][y+8] == img[x+4][y+8] == img[x+5][y+8] == img[x+6][y+8] == img[x+7][y+8] == img[x+8][y+8] == img[x+9][y+8] == img[x+10][y+8] == img[x+11][y+8] == img[x+12][y+8] == img[x+13][y+8] == img[x+14][y+8] == img[x+15][y+8] == img[x+16][y+8] == img[x+17][y+8] == img[x+18][y+8] == img[x+19][y+8] == img[x+20][y+8] == img[x][y+9] == img[x+1][y+9] == img[x+2][y+9] == img[x+3][y+9] == img[x+4][y+9] == img[x+5][y+9] == img[x+6][y+9] == img[x+7][y+9] == img[x+8][y+9] == img[x+9][y+9] == img[x+10][y+9] == img[x+11][y+9] == img[x+12][y+9] == img[x+13][y+9] == img[x+14][y+9] == img[x+15][y+9] == img[x+16][y+9] == img[x+17][y+9] == img[x+18][y+9] == img[x+19][y+9] == img[x+20][y+9] == img[x][y+10] == img[x+1][y+10] == img[x+2][y+10] == img[x+3][y+10] == img[x+4][y+10] == img[x+5][y+10] == img[x+6][y+10] == img[x+7][y+10] == img[x+8][y+10] == img[x+9][y+10] == img[x+10][y+10] == img[x+11][y+10] == img[x+12][y+10] == img[x+13][y+10] == img[x+14][y+10] == img[x+15][y+10] == img[x+16][y+10] == img[x+17][y+10] == img[x+18][y+10] == img[x+19][y+10] == img[x+20][y+10] == img[x][y+11] == img[x+1][y+11] == img[x+2][y+11] == img[x+3][y+11] == img[x+4][y+11] == img[x+5][y+11] == img[x+6][y+11] == img[x+7][y+11] == img[x+8][y+11] == img[x+9][y+11] == img[x+10][y+11] == img[x+11][y+11] == img[x+12][y+11] == img[x+13][y+11] == img[x+14][y+11] == img[x+15][y+11] == img[x+16][y+11] == img[x+17][y+11] == img[x+18][y+11] == img[x+19][y+11] == img[x+20][y+11] == img[x][y+12] == img[x+1][y+12] == img[x+2][y+12] == img[x+3][y+12] == img[x+4][y+12] == img[x+5][y+12] == img[x+6][y+12] == img[x+7][y+12] == img[x+8][y+12] == img[x+9][y+12] == img[x+10][y+12] == img[x+11][y+12] == img[x+12][y+12] == img[x+13][y+12] == img[x+14][y+12] == img[x+15][y+12] == img[x+16][y+12] == img[x+17][y+12] == img[x+18][y+12] == img[x+19][y+12] == img[x+20][y+12] == img[x][y+13] == img[x+1][y+13] == img[x+2][y+13] == img[x+3][y+13] == img[x+4][y+13] == img[x+5][y+13] == img[x+6][y+13] == img[x+7][y+13] == img[x+8][y+13] == img[x+9][y+13] == img[x+10][y+13] == img[x+11][y+13] == img[x+12][y+13] == img[x+13][y+13] == img[x+14][y+13] == img[x+15][y+13] == img[x+16][y+13] == img[x+17][y+13] == img[x+18][y+13] == img[x+19][y+13] == img[x+20][y+13] == img[x][y+14] == img[x+1][y+14] == img[x+2][y+14] == img[x+3][y+14] == img[x+4][y+14] == img[x+5][y+14] == img[x+6][y+14] == img[x+7][y+14] == img[x+8][y+14] == img[x+9][y+14] == img[x+10][y+14] == img[x+11][y+14] == img[x+12][y+14] == img[x+13][y+14] == img[x+14][y+14] == img[x+15][y+14] == img[x+16][y+14] == img[x+17][y+14] == img[x+18][y+14] == img[x+19][y+14] == img[x+20][y+14] == img[x][y+15] == img[x+1][y+15] == img[x+2][y+15] == img[x+3][y+15] == img[x+4][y+15] == img[x+5][y+15] == img[x+6][y+15] == img[x+7][y+15] == img[x+8][y+15] == img[x+9][y+15] == img[x+10][y+15] == img[x+11][y+15] == img[x+12][y+15] == img[x+13][y+15] == img[x+14][y+15] == img[x+15][y+15] == img[x+16][y+15] == img[x+17][y+15] == img[x+18][y+15] == img[x+19][y+15] == img[x+20][y+15] == img[x][y+16] == img[x+1][y+16] == img[x+2][y+16] == img[x+3][y+16] == img[x+4][y+16] == img[x+5][y+16] == img[x+6][y+16] == img[x+7][y+16] == img[x+8][y+16] == img[x+9][y+16] == img[x+10][y+16] == img[x+11][y+16] == img[x+12][y+16] == img[x+13][y+16] == img[x+14][y+16] == img[x+15][y+16] == img[x+16][y+16] == img[x+17][y+16] == img[x+18][y+16] == img[x+19][y+16] == img[x+20][y+16] == img[x][y+17] == img[x+1][y+17] == img[x+2][y+17] == img[x+3][y+17] == img[x+4][y+17] == img[x+5][y+17] == img[x+6][y+17] == img[x+7][y+17] == img[x+8][y+17] == img[x+9][y+17] == img[x+10][y+17] == img[x+11][y+17] == img[x+12][y+17] == img[x+13][y+17] == img[x+14][y+17] == img[x+15][y+17] == img[x+16][y+17] == img[x+17][y+17] == img[x+18][y+17] == img[x+19][y+17] == img[x+20][y+17] == img[x][y+18] == img[x+1][y+18] == img[x+2][y+18] == img[x+3][y+18] == img[x+4][y+18] == img[x+5][y+18] == img[x+6][y+18] == img[x+7][y+18] == img[x+8][y+18] == img[x+9][y+18] == img[x+10][y+18] == img[x+11][y+18] == img[x+12][y+18] == img[x+13][y+18] == img[x+14][y+18] == img[x+15][y+18] == img[x+16][y+18] == img[x+17][y+18] == img[x+18][y+18] == img[x+19][y+18] == img[x+20][y+18] == img[x][y+19] == img[x+1][y+19] == img[x+2][y+19] == img[x+3][y+19] == img[x+4][y+19] == img[x+5][y+19] == img[x+6][y+19] == img[x+7][y+19] == img[x+8][y+19] == img[x+9][y+19] == img[x+10][y+19] == img[x+11][y+19] == img[x+12][y+19] == img[x+13][y+19] == img[x+14][y+19] == img[x+15][y+19] == img[x+16][y+19] == img[x+17][y+19] == img[x+18][y+19] == img[x+19][y+19] == img[x+20][y+19] == img[x][y+20] == img[x+1][y+20] == img[x+2][y+20] == img[x+3][y+20] == img[x+4][y+20] == img[x+5][y+20] == img[x+6][y+20] == img[x+7][y+20] == img[x+8][y+20] == img[x+9][y+20] == img[x+10][y+20] == img[x+11][y+20] == img[x+12][y+20] == img[x+13][y+20] == img[x+14][y+20] == img[x+15][y+20] == img[x+16][y+20] == img[x+17][y+20] == img[x+18][y+20] == img[x+19][y+20] == img[x+20][y+20]:
                        #print(x,y, 'чемпион')
                        for i in range(21):
                            for o in range(2):
                                img[x+i][y+o] = 64

            except:
                pass

    cv2.imwrite(f'captcha\\{id}_nortach1LOL.png', img)



    cv2.imwrite(f'captcha\\{id}_nortach1LOL2.png', img)


    img[6][6] = 1
    img[6][12] = 1
    img[12][6] = 1
    img[12][12] = 1
    img[-7][6] = 1
    img[-7][12] = 1
    img[-13][6] = 1
    img[-13][12] = 1
    img[6][-7] = 1
    img[12][-13] = 1
    img[12][-7] = 1
    img[6][-13] = 1
    img[-7][-7] = 1
    img[-7][-13] = 1
    img[-13][-13] = 1
    img[-13][-7] = 1

    stop = False
    img2 = cv2.imread(f'captcha\\{id}_captcha.png', cv2.IMREAD_GRAYSCALE)

    for y in range(250):
        for x in range(250):
            try:
                if stop == True:
                    pass
                else:  #верх лево
                    if stop == False and img[y][x] == img[y+1][x] == img[y+2][x] == img[y+3][x] == img[y+4][x] == img[y+5][x] == img[y+6][x] == img[y+7][x] == img[y+8][x] == img[y+9][x] == img[y+10][x] == img[y+1][x-1] == img[y+2][x-1] == img[y+3][x-1] == img[y+4][x-1] == img[y+5][x-1] == img[y+6][x-1] == img[y+7][x-1] == img[y+8][x-1] == img[y+9][x-1] == img[y+10][x] == img[y+1][x-2] == img[y+2][x-2] == img[y+3][x-2] == img[y+4][x-2] == img[y+5][x-2] == img[y+6][x-2] == img[y+7][x-2] == img[y+8][x-2] == img[y+9][x-2] == img[y+10][x-2] == img[y+1][x-3] == img[y+2][x-3] == img[y+3][x-3] == img[y+4][x-3] == img[y+5][x-3] == img[y+6][x-3] == img[y+7][x-3] == img[y+8][x-3] == img[y+9][x-3] == img[y+10][x-3] == img[y+1][x-4] == img[y+2][x-4] == img[y+3][x-4] == img[y+4][x-4] == img[y+5][x-4] == img[y+6][x-4] == img[y+7][x-4] == img[y+8][x-4] == img[y+9][x-4] == img[y+10][x-4] == img[y+2][x-5] == img[y+3][x-5] == img[y+4][x-5] == img[y+5][x-5] == img[y+6][x-5] == img[y+7][x-5] == img[y+8][x-5] == img[y+9][x-5] == img[y+10][x-5] == img[y+3][x-6] == img[y+4][x-6] == img[y+5][x-6] == img[y+6][x-6] == img[y+7][x-6] == img[y+8][x-6] == img[y+9][x-6] == img[y+10][x-6] == img[y+3][x-7] == img[y+4][x-7] == img[y+5][x-7] == img[y+6][x-7] == img[y+7][x-7] == img[y+8][x-7] == img[y+9][x-7] == img[y+10][x-7] == img[y+5][x-8] == img[y+6][x-8] == img[y+7][x-8] == img[y+8][x-8] == img[y+9][x-8] == img[y+10][x-8] == img[y+6][x-9] == img[y+7][x-9] == img[y+8][x-9] == img[y+9][x-9] == img[y+10][x-9] == img[y+10][x-10] == anscol:
                        if img[y][x] != img[y-9][x-9]:
                            print(x,y, 'i think its answer (1)')
                            ansx = x
                            ansy = y
                            stop = True
                            break

                        #верх право
                    elif stop == False and img[y][x] == img[y+1][x] == img[y+2][x] == img[y+3][x] == img[y+4][x] == img[y+5][x] == img[y+6][x] == img[y+7][x] == img[y+8][x] == img[y+9][x] == img[y][x+1] == img[y+1][x+1] == img[y+2][x+1] == img[y+3][x+1] == img[y+4][x+1] == img[y+5][x+1] == img[y+6][x+1] == img[y+7][x+1] == img[y+8][x+1] == img[y+9][x+1] ==  img[y][x+2] == img[y+1][x+2] == img[y+2][x+2] == img[y+3][x+2] == img[y+4][x+2] == img[y+5][x+2] == img[y+6][x+2] == img[y+7][x+2] == img[y+8][x+2] == img[y+9][x+2] ==  img[y][x+3] == img[y+1][x+3] == img[y+2][x+3] == img[y+3][x+3] == img[y+4][x+3] == img[y+5][x+3] == img[y+6][x+3] == img[y+7][x+3] == img[y+8][x+3] == img[y+9][x+3] == img[y][x+4] == img[y+1][x+4] == img[y+2][x+4] == img[y+3][x+4] == img[y+4][x+4] == img[y+5][x+4] == img[y+6][x+4] == img[y+7][x+4] == img[y+8][x+4] == img[y+9][x+4] == img[y][x+5] == img[y+1][x+5] == img[y+2][x+5] == img[y+3][x+5] == img[y+4][x+5] == img[y+5][x+5] == img[y+6][x+5] == img[y+7][x+5] == img[y+8][x+5] == img[y][x+6] == img[y+1][x+6] == img[y+2][x+6] == img[y+3][x+6] == img[y+4][x+6] == img[y+5][x+6] == img[y+6][x+6] == img[y+7][x+6] == img[y][x+7] == img[y+1][x+7] == img[y+2][x+7] == img[y+3][x+7] == img[y+4][x+7] == img[y+5][x+7] == img[y+6][x+7] == img[y+7][x+7] == img[y][x+8] == img[y+1][x+8] == img[y+2][x+8] == img[y+3][x+8] == img[y+4][x+8] == img[y+5][x+8] == img[y][x+9] == img[y+1][x+9] == img[y+2][x+9] == img[y+3][x+9] == img[y+4][x+9] == anscol:
                        if img[y][x] != img[x+9][y-9]:
                            print(x,y, 'i think its answer (2)', x+13, y+7)
                            ansx = x
                            ansy = y
                            stop = True
                            break

                        #низ право

                    elif stop == False and img[y][x] == img[y+1][x] == img[y+2][x] == img[y+3][x] == img[y+4][x] == img[y+5][x] == img[y+6][x] == img[y+7][x] == img[y+8][x] == img[y+9][x] == img[y][x+1] == img[y+1][x+1] == img[y+2][x+1] == img[y+3][x+1] == img[y+4][x+1] == img[y+5][x+1] == img[y+6][x+1] == img[y+7][x+1] == img[y+8][x+1] == img[y+9][x+1] == img[y][x+2] == img[y+1][x+2] == img[y+2][x+2] == img[y+3][x+2] == img[y+4][x+2] == img[y+5][x+2] == img[y+6][x+2] == img[y+7][x+2] == img[y+8][x+2] == img[y+9][x+2] == img[y][x+3] == img[y+1][x+3] == img[y+2][x+3] == img[y+3][x+3] == img[y+4][x+3] == img[y+5][x+3] == img[y+6][x+3] == img[y+7][x+3] == img[y+8][x+3] == img[y][x+4] == img[y+1][x+4] == img[y+2][x+4] == img[y+3][x+4] == img[y+4][x+4] == img[y+5][x+4] == img[y+6][x+4] == img[y+7][x+4] == img[y+8][x+4] == img[y][x+5] == img[y+1][x+5] == img[y+2][x+5] == img[y+3][x+5] == img[y+4][x+5] == img[y+5][x+5] == img[y+6][x+5] == img[y+7][x+5] == img[y][x+6] == img[y+1][x+6] == img[y+2][x+6] == img[y+3][x+6] == img[y+4][x+6] == img[y+5][x+6] == img[y+6][x+6] == img[y][x+7] == img[y+1][x+7] == img[y+2][x+7] == img[y+3][x+7] == img[y+4][x+7] == img[y+5][x+7] == img[y+6][x+7] == img[y][x+8] == img[y+1][x+8] == img[y+2][x+8] == img[y+3][x+8] == img[y+4][x+8] == img[y][x+9] == img[y+1][x+9] == img[y+2][x+9] == img[y+3][x+9] == anscol:
                        if img[y][x] != img[y+9][x+9]:
                            print(x,y, 'i think its answer (3)', x, y+6)
                            ansx = x
                            ansy = y
                            stop = True
                            break

                        #низ лево
                    elif stop == False and img[y][x] == img[y][x+1] == img[y][x+2] == img[y][x+3] == img[y][x+4] == img[y][x+5] == img[y][x+6] == img[y][x+7] == img[y][x+8] == img[y][x+9] == img[y+1][x] == img[y+1][x+1] == img[y+1][x+2] == img[y+1][x+3] == img[y+1][x+4] == img[y+1][x+5] == img[y+1][x+6] == img[y+1][x+7] == img[y+1][x+8] == img[y+1][x+9] == img[y+2][x] == img[y+2][x+1] == img[y+2][x+2] == img[y+2][x+3] == img[y+2][x+4] == img[y+2][x+5] == img[y+2][x+6] == img[y+2][x+7] == img[y+2][x+8] == img[y+2][x+9] == img[y+3][x] == img[y+3][x+1] == img[y+3][x+2] == img[y+3][x+3] == img[y+3][x+4] == img[y+3][x+5] == img[y+3][x+6] == img[y+3][x+7] == img[y+3][x+8] == img[y+3][x+9] == img[y+4][x] == img[y+4][x+1] == img[y+4][x+2] == img[y+4][x+3] == img[y+4][x+4] == img[y+4][x+5] == img[y+4][x+6] == img[y+4][x+7] == img[y+4][x+8] == img[y+4][x+9] == img[y+5][x+1] == img[y+5][x+2] == img[y+5][x+3] == img[y+5][x+4] == img[y+5][x+5] == img[y+5][x+6] == img[y+5][x+7] == img[y+5][x+8] == img[y+5][x+9] == img[y+6][x+2] == img[y+6][x+3] == img[y+6][x+4] == img[y+6][x+5] == img[y+6][x+6] == img[y+6][x+7] == img[y+6][x+8] == img[y+6][x+9] == img[y+7][x+2] == img[y+7][x+3] == img[y+7][x+4] == img[y+7][x+5] == img[y+7][x+6] == img[y+7][x+7] == img[y+7][x+8] == img[y+7][x+9] == img[y+8][x+4] == img[y+8][x+5] == img[y+8][x+6] == img[y+8][x+7] == img[y+8][x+8] == img[y+8][x+9] == img[y+9][x+5] == img[y+9][x+6] == img[y+9][x+7] == img[y+9][x+8] == img[y+9][x+9] == anscol:
                        if img[y][x] != img[y+9][x]:
                            print(x,y, 'i think its answer (4)', x, y+6)
                            ansx = x
                            ansy = y
                            stop = True
                            break


                    try:
                        if img2[ansx][ansy] != anscol:
                            stop = False
                            #print('renewed')
                    except:
                        pass

            except:
                pass
    cv2.imwrite(f'captcha\\{id}_noTrash.png', img)

    return ansx//20, ansy//20

def dogo(headers, id):
    global done
    global failed
    try:
        hash = captchainfo(headers, id)
        answer = getanscol(id)
        print(answer, 'answer')

        resp = participate(id, headers, hash, answer[0], answer[1])

        print(resp)

        if "'_redirectStatus': 'ok'" in str(resp):
            done += 1
        else:
            failed += 1

        os.remove(f'captcha\\{id}_captcha.png')
        os.remove(f'captcha\\{id}_gray.png')
        os.remove(f'captcha\\{id}_nortach1.png')
        os.remove(f'captcha\\{id}_nortach1LOL.png')
        os.remove(f'captcha\\{id}_nortach1LOL2.png')
        os.remove(f'captcha\\{id}_noTrash.png')

        print(f'\n\nУспешно: {done}, Неудачно: {failed}\n\n')
        time.sleep(2)
    except:
        try:
            os.remove(f'captcha\\{id}_captcha.png')
            os.remove(f'captcha\\{id}_gray.png')
            os.remove(f'captcha\\{id}_nortach1.png')
            os.remove(f'captcha\\{id}_nortach1LOL.png')
            os.remove(f'captcha\\{id}_nortach1LOL2.png')
            os.remove(f'captcha\\{id}_noTrash.png')
        except:
            time.sleep(1)

f = open('cookies.txt')
cookies = parseCookies(f.read())

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36', 'cookie': cookies}

done = 0
failed = 0

thcount = int(input('введите количество потоков (не больше 30, советую 1-5 для стабильной работы): '))

while True:
    try:
        ids = getids(headers)
        print(ids)
        th = []
        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        for i in range(thcount):
            th.append(threading.Thread(target=dogo, args=(headers, ids[i],)))

        for i in th:
            i.start()

        for i in th:
            i.join()
    except:
        print('error')
        time.sleep(1)