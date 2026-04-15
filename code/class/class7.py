import jieba
import wordcloud
from pathlib import Path

fname = Path("C:/Users/Spane/Desktop/Python-course/code/class/material_for_wordcloud/中央一号文件/2004-中共中央国务院关于促进农民增加收入若干政策的意见.txt" )
with open(fname, "r", encoding="utf-8") as f:
    ls = jieba.lcut(f.read())
w = wordcloud.WordCloud( 
    width = 1000, height = 700,
    background_color = "white",
    font_path = "msyh.ttc"
    )
txt = " ".join(ls)
w.generate(txt)
w.to_file("RptOneWordle01.png")