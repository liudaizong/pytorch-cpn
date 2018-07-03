import json 
import os 
import cv2 

with open('./result.json','r') as load_f:
	load_dict = json.load(load_f)

pic1 = '872'
pic2 = '4134'

pic_id = []
for result in load_dict:
	pic_id.append(result['image_id'])
# print pic_id

pic_dic = {}
for i in pic_id:
	pic_dic.setdefault(str(i), 0)
	pic_dic[str(i)] += 1
# print pic_dic

if not os.path.exists('./bb'):
	os.mkdir('./bb')

num = 0
while num < len(pic_id):
	image_id = str(pic_id[num]).zfill(12)
	image_path = os.path.join('./val2017', image_id+'.jpg')
	img = cv2.imread(image_path)
	for i in range(pic_dic[str(pic_id[num])]):
		result = load_dict[num]['keypoints']
		clss = len(result)/3
		for i in range(clss):
			x = result[3*i]
			y = result[3*i+1]
			cv2.circle(img, (int(x),int(y)), 2, (0, 0, 255),2)
		num += 1
	save_path = os.path.join('./bb', image_id+'.jpg')
	cv2.imwrite(save_path, img)
	print image_id
	# cv2.imshow('image', img)
	# cv2.waitKey(0)

# for result in set(pic_id):
	# print result
# for result in load_dict:
# 	print result['image_id']
# 	image_id = str(result['image_id']).zfill(12)
# 	image_path = os.path.join('./val2017', image_id+'.jpg')
# 	clss = len(result['keypoints'])/3
# 	# print result['keypoints']
# 	img = cv2.imread(image_path)
# 	for i in range(clss):
# 		# print 3*i
# 		x = result['keypoints'][3*i]
# 		y = result['keypoints'][3*i+1]
# 		cv2.circle(img, (int(x),int(y)), 2, (0, 0, 255),2)
# 	cv2.imshow('image', img)
# 	cv2.waitKey(0)