import os, re
import random
from shutil import copyfile
from xml.dom.minidom import parse

rootdir = "../../data/original_data"

print('total image num = ', len(os.listdir(os.path.join(rootdir, "images"))))
w_num, wo_num, unsure = 0.0, 0.0, 0.0
w_image_num, wo_image_num = 0.0, 0.0

for root, folder, files in os.walk(rootdir+'/annotations'):
    for filename in files:
        dom = parse(os.path.join(rootdir+'/annotations', filename))
        root = dom.documentElement
        objects = root.getElementsByTagName("object")
        for o in objects:
            label_type = o.getElementsByTagName("name")[0].childNodes[0].data

            # print(label_type)

            if label_type in ["with_mask", "with-mask"]:
                w_num += 1
            elif label_type in ["without_mask", "without-mask"]:
                wo_num += 1
            elif label_type in ["mask_weared_incorrect", "unsure"]:
                unsure += 1

        w_image_num += 1

        for o in objects:
            label_type = o.getElementsByTagName("name")[0].childNodes[0].data
            if label_type in ["without_mask", "without-mask"]:
                wo_image_num += 1
                break

print('Total without mask object: ', wo_num)
print('Total with mask object: ', w_num)
print('Total unsure object: ', unsure)
print('Total images without mask object: ', wo_image_num)
print('Total images with mask object: ', w_image_num)

# if not os.path.exists('../../data/train'):
#     os.mkdir('../../data/train')
#     os.mkdir('../../data/train/images')
#     os.mkdir('../../data/train/annotations')
#     os.mkdir('../../data/test')
#     os.mkdir('../../data/test/images')
#     os.mkdir('../../data/test/annotations')
# annotation_list = os.listdir(rootdir+'/annotations')
#
# random.seed(10)
# random.shuffle(annotation_list)
# train_list = annotation_list[:int(len(annotation_list)/4*3)]
# test_list = annotation_list[int(len(annotation_list)/4*3):]
#
# print(len(train_list))
# print(len(test_list))
#
# train_num = 0
# for filename in train_list:
#     img_id = int(re.findall(r'\d+', filename)[0])
#     image_name = rootdir+'/images/maksssksksss' + str(img_id)+'.png'
#     dom = parse(os.path.join(rootdir+'/annotations', filename))
#     root = dom.documentElement
#     objects = root.getElementsByTagName("object")
#     wo_mask = False
#
#     for o in objects:
#         label_type = o.getElementsByTagName("name")[0].childNodes[0].data
#         if label_type == 'without_mask':
#             wo_mask = True
#             break
#
#     if wo_mask:
#         for ii in range(4):
#             copyfile(image_name, '../../data/train/images/maksssksksss' + str(train_num)+'.png')
#             copyfile(os.path.join(rootdir+'/annotations', filename), '../../data/train/annotations/maksssksksss' + str(train_num)+'.xml')
#             train_num += 1
#     else:
#         copyfile(image_name, '../../data/train/images/maksssksksss' + str(train_num) + '.png')
#         copyfile(os.path.join(rootdir+'/annotations', filename), '../../data/train/annotations/maksssksksss' + str(train_num) + '.xml')
#         train_num += 1
#
# test_num = 0
# for filename in test_list:
#     img_id = int(re.findall(r'\d+', filename)[0])
#     image_name = rootdir+'/images/maksssksksss' + str(img_id)+'.png'
#     dom = parse(os.path.join(rootdir+'/annotations', filename))
#     root = dom.documentElement
#     objects = root.getElementsByTagName("object")
#
#     copyfile(image_name, '../../data/test/images/maksssksksss' + str(test_num) + '.png')
#     copyfile(os.path.join(rootdir+'/annotations', filename), '../../data/test/annotations/maksssksksss' + str(test_num) + '.xml')
#     test_num += 1
#
# print('total training num: ', train_num)
# print('total testing num: ', test_num)

# ======================================================================================
# import os, re
# import random
# from shutil import copyfile
# from xml.dom.minidom import parse

# rootdir = "../../data/original_data"

# print('total image num = ', len(os.listdir(os.path.join(rootdir, "images"))))
# w_num, wo_num = 0.0, 0.0
# w_image_num, wo_image_num = 0.0, 0.0

# for root, folder, files in os.walk(rootdir+'/annotations'):
#     for filename in files:
#         dom = parse(os.path.join(rootdir+'/annotations', filename))
#         root = dom.documentElement
#         objects = root.getElementsByTagName("object")
#         for o in objects:
#             label_type = o.getElementsByTagName("name")[0].childNodes[0].data
#             if label_type == 'without_mask':
#                 wo_num += 1
#             else:
#                 w_num += 1
#         w_image_num += 1
#         for o in objects:
#             label_type = o.getElementsByTagName("name")[0].childNodes[0].data
#             if label_type == 'without_mask':
#                 wo_image_num += 1
#                 break
# print('Total without mask object: ', wo_num)
# print('Total with mask object: ', w_num)
# print('Total images without mask object: ', wo_image_num)
# print('Total images with mask object: ', w_image_num)

# if not os.path.exists('../../data/train'):
#     os.mkdir('../../data/train')
#     os.mkdir('../../data/train/images')
#     os.mkdir('../../data/train/annotations')
#     os.mkdir('../../data/test')
#     os.mkdir('../../data/test/images')
#     os.mkdir('../../data/test/annotations')
# annotation_list = os.listdir(rootdir+'/annotations')

# random.seed(10)
# random.shuffle(annotation_list)
# train_list = annotation_list[:int(len(annotation_list)/4*3)]
# test_list = annotation_list[int(len(annotation_list)/4*3):]

# train_num = 0
# for filename in train_list:
#     img_id = int(re.findall(r'\d+', filename)[0])
#     image_name = rootdir+'/images/maksssksksss' + str(img_id)+'.png'
#     dom = parse(os.path.join(rootdir+'/annotations', filename))
#     root = dom.documentElement
#     objects = root.getElementsByTagName("object")
#     wo_mask = False
#     for o in objects:
#         label_type = o.getElementsByTagName("name")[0].childNodes[0].data
#         if label_type == 'without_mask':
#             wo_mask = True
#             break
#     if wo_mask:
#         for ii in range(4):
#             copyfile(image_name, '../../data/train/images/maksssksksss' + str(train_num)+'.png')
#             copyfile(os.path.join(rootdir+'/annotations', filename), '../../data/train/annotations/maksssksksss' + str(train_num)+'.xml')
#             train_num += 1
#     else:
#         copyfile(image_name, '../../data/train/images/maksssksksss' + str(train_num) + '.png')
#         copyfile(os.path.join(rootdir+'/annotations', filename), \
#                  '../../data/train/annotations/maksssksksss' + str(train_num) + '.xml')
#         train_num += 1
        
# test_num = 0
# for filename in test_list:
#     img_id = int(re.findall(r'\d+', filename)[0])
#     image_name = rootdir+'/images/maksssksksss' + str(img_id)+'.png'
#     dom = parse(os.path.join(rootdir+'/annotations', filename))
#     root = dom.documentElement
#     objects = root.getElementsByTagName("object")

#     copyfile(image_name, '../../data/test/images/maksssksksss' + str(test_num) + '.png')
#     copyfile(os.path.join(rootdir+'/annotations', filename), '../../data/test/annotations/maksssksksss' + str(test_num) + '.xml')
#     test_num += 1

# print('total training num: ', train_num)
# print('total testing num: ', test_num)