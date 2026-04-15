import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud

with open("D:/中央一号文件/2023-中共中央国务院关于做好2023年全面推进乡村振兴重点工作的意见.txt", "r", encoding="utf-8") as f:
    txt = f.read()

words = jieba.lcut(txt)
words = [w for w in words if len(w.strip()) > 1]
result = " ".join(words)

img = Image.open("D:/china_mask.png").convert("L")
img = img.resize((1200, 900))
arr = np.array(img)

mask = np.where(arr > 240, 255, 0).astype(np.uint8)

wc = WordCloud(
    font_path="C:/Windows/Fonts/msyh.ttc",
    background_color="white",
    mask=mask,
    width=1200,
    height=900,
    max_words=400,
    collocations=False,
    prefer_horizontal=1.0,
    random_state=42,
    margin=2
)

wc.generate(result)
wc.to_file("D:/中央一号文件_中国地图词云.png")