import os
from tqdm import tqdm

img_dir = "/fashionpedia-training/images"

for img_name in tqdm(os.listdir(img_dir)):
	command = f"python3 apply_net.py dump configs/densepose_rcnn_R_50_FPN_s1x.yaml \
	https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x/165712039/model_final_162be9.pkl \
	/fashionpedia-training/images/{img_name} --output /fashionpedia-training/dp_results.pkl -v"

	os.system(command)