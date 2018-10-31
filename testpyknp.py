#!/usr/bin/env python3
from pyknp import Juman
import csv

jumanpp = Juman()
result = jumanpp.analysis('お疲れさまです。今週のトップ報告を行います。')
title = [['キーワード','原形','品詞','品詞細分類']]
top_list=[]
every_row = result.mrph_list()
for i in every_row:
    top_list.append([i.midasi,i.genkei,i.hinsi,i.bunrui])
    # print(i.midasi,i.genkei,i.hinsi, i.bunrui,sep='\t')
with open(r'/opt/aaa.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(title)
    writer.writerows(top_list)

