import os
import pandas as pd
import cv2
import argparse

parser = argparse.ArgumentParser(description="Input for opencv ")
parser.add_argument("--input_dir", action="store", dest="input_dir", required=False)
parser.add_argument("--csv_file_name", action="store", dest="csv_file_name", required=False)
parser.add_argument("--output_dir", action="store", dest="output_dir", required=False)

args = parser.parse_args()


input_dir = args.input_dir or 'cat'
csv_file_name = args.csv_file_name or 'data_labels.csv'

df = pd.read_csv(csv_file_name).iloc[1:]

final_images = []

for idx in range(len(df)):
  minx = int(df.iloc[idx]['xmin'])
  miny = int(df.iloc[idx]['ymin'])
  maxx = int(df.iloc[idx]['xmax'])
  maxy = int(df.iloc[idx]['ymax'])

  label = df.iloc[idx]['label']

  width = df.iloc[idx]['width']
  height = df.iloc[idx]['height']

  image_name = df.iloc[idx]['name']

  img = cv2.imread(os.path.join(input_dir,image_name))
  img = cv2.rectangle(img, (minx, miny), (maxx, maxy), color = (255,255,255), thickness = 2)
  img = cv2.putText(img,label,(minx,miny+50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),2)

  final_images.append({
    'name' : image_name,
    'image' : img
  })

output_dir = args.output_dir or 'output'
if not os.path.exists(output_dir):
  os.makedirs(output_dir)
  for final_image in final_images:
    cv2.imwrite(os.path.join(output_dir,final_image['name']),final_image['image'])
