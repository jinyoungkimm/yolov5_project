from glob import glob

img_list = glob('C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/export/images/*.jpg')
print(len(img_list))

from sklearn.model_selection import train_test_split

train_img_list, val_img_list = train_test_split(img_list, test_size=0.2, random_state=2000)

print(len(train_img_list),len(val_img_list))

with open('C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/train.txt','w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/val.txt','w') as f:
    f.write('\n'.join(val_img_list) + '\n')

import yaml

with open('C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/data.yaml','r') as f:
    data = yaml.safe_load(f)

print(data)


data['train'] = 'C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/train.txt'
data['val'] = 'C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/val.txt'

with open('C:/Users/Nexcore/PycharmProjects/pythonProject4/datasets/data.yaml','w') as f:
    yaml.dump(data,f)

print(data)


