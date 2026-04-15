import json

import jieba
import numpy as np
import wordcloud
from PIL import Image, ImageDraw


fname = r"C:\Users\Spane\Desktop\Python-course\code\class\material_for_wordcloud\中央一号文件\2023-中共中央国务院关于做好2023年全面推进乡村振兴重点工作的意见.txt"
map_file = r"C:\Users\Spane\Desktop\Python-course\code\class\material_for_wordcloud\china_boundary_100000_full.json"

with open(fname, "r", encoding="utf-8") as f:
    ls = jieba.lcut(f.read())

for item in reversed(ls):
    if len(item) == 1:
        ls.remove(item)

with open(map_file, "r", encoding="utf-8") as f:
    china = json.load(f)

polygons = []
for feature in china["features"]:
    geometry = feature["geometry"]
    if geometry["type"] == "Polygon":
        polygons.append(geometry["coordinates"])
    if geometry["type"] == "MultiPolygon":
        polygons.extend(geometry["coordinates"])

points = []
for polygon in polygons:
    for ring in polygon:
        points.extend(ring)

min_lon = min(point[0] for point in points)
max_lon = max(point[0] for point in points)
min_lat = min(point[1] for point in points)
max_lat = max(point[1] for point in points)

width = 1000
height = 700
padding = 20
scale_x = (width - 2 * padding) / (max_lon - min_lon)
scale_y = (height - 2 * padding) / (max_lat - min_lat)
scale = min(scale_x, scale_y)
offset_x = (width - (max_lon - min_lon) * scale) / 2
offset_y = (height - (max_lat - min_lat) * scale) / 2

img = Image.new("L", (width, height), 255)
draw = ImageDraw.Draw(img)

for polygon in polygons:
    outer = []
    for lon, lat in polygon[0]:
        x = offset_x + (lon - min_lon) * scale
        y = offset_y + (max_lat - lat) * scale
        outer.append((x, y))
    draw.polygon(outer, fill=0)

    for hole in polygon[1:]:
        inner = []
        for lon, lat in hole:
            x = offset_x + (lon - min_lon) * scale
            y = offset_y + (max_lat - lat) * scale
            inner.append((x, y))
        draw.polygon(inner, fill=255)

mask = np.array(img)
txt = " ".join(ls)
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color="white",
    font_path="msyh.ttc",
    mask=mask,
    contour_width=1,
    contour_color="darkgreen"
)

w.generate(txt)
w.to_file("RptOneWordleChina.png")

print("词云已生成：RptOneWordleChina.png")
