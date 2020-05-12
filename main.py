import os
train = open("/AI/sources/user-space/Merve/datasets/PT/coco/yolov2/train.txt","w+")
for filename in os.listdir('/AI/sources/user-space/Merve/datasets/PT/coco/images/train/'):
     (prefix, sep, suffix) = filename.rpartition('.')
     print(prefix)
     train.write('AI/sources/user-space/Merve/datasets/PT/coco/yolov2/train/'+prefix + '.jpg' + '\n')

val = open("/AI/sources/user-space/Merve/datasets/PT/coco/yolov2/val.txt","w+")
for filename in os.listdir('/AI/sources/user-space/Merve/datasets/PT/coco/images/val'):
     (prefix, sep, suffix) = filename.rpartition('.')
     print(prefix)
     val.write('AI/sources/user-space/Merve/datasets/PT/coco/yolov2/val/'+prefix + '.jpg' + '\n')