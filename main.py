#!/usr/bin/env python
#coding:UTF-8

################### Load Module ###################
import sys
import datetime
import os
import urllib
import urllib2
import re
###################################################

################### Define Function ###################
# 初期メッセージを表示する関数を定義,引数・返り値なし
def message():
    print ('##### Picture Getter #####\n'\
           '1：画像を取得\n'\
           '2：プログラムの終了\n'\
           '##########################'\
           )

# 除外リストを読み込み,引数なし・返り値あり（除外リスト）
def exclusion_load():
    os.chdir('exclusion')
    with open('list','r') as f:
        unload = f.read()
    os.chdir('../')
    return unload
###################################################

################### Main ###################
message()
start = raw_input('input：')

# 画像取得処理
if start == '1':

    # 除外リストの取得
    unload = exclusion_load()

    # 今日の日付を取得し,ディレクトリを作成
    d = datetime.datetime.today()
    today = d.strftime('%Y%m%d')
    os.chdir('data')
    if os.path.exists(today) == False:
        os.mkdir(today)
    os.chdir(today)

    url = raw_input('画像を取得するページのURLを入力：')
    response = urllib.urlopen(url)
    page_source = response.read()

    time = d.strftime('%H%M%S')
    os.mkdir(time)
    os.chdir(time)

    
    matchsearch = re.search('http\S+?\.jpe?g',page_source)
    if matchsearch == None:
        print 'Not Found Picture!'
    else:
        match = re.findall('http\S+?\.jpe?g',page_source)
        qty = len(match)
        print 'Found picture Link is ' + str(qty)

        counter = 0
        for i in match:
            if re.search(i,unload) == None:
                pict_binary = urllib2.urlopen(i)
                filename = re.findall('[A-Za-z0-9\.\-_]+\.jpe?g',i)
                with open(str(filename[0]),'wb') as f:
                    f.write(pict_binary.read())
                    counter += 1
                
    print 'Download Complete!'
    print 'Downloads Picture is ' + str(counter)
    sys.exit(0)

# 正常終了処理
if start == '2':
    print ('exit Picture Getter')
    sys.exit(0)

# 例外終了処理
else:
    print ('Error check of inputcode')
    sys.exit(1)
