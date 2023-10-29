import torch
from torch import nn
# nn.MultiheadAttention
# from transformers import BertTokenizer
# tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
# text = ['hello my name is da ming']
# encoding = tokenizer(text,max_length=10,padding='max_length')
# print(encoding['attention_mask'])
a = torch.Tensor(2,10,100)
print(a.shape)
ffc = nn.Linear(100,1)
mask = torch.tensor([[1,1,1,1,1,1,1,1,0,0],
        [1,1,1,1,1,1,1,0,0,0]])

a_ = ffc(a).squeeze()
a_1 = a_.masked_fill_(mask,float(-10))
print(a_1)
# score = nn.Softmax(dim=1)(score)

# a = torch.tensor([[[1,2,3,4,5,6,7,8,9],
#      [4,2,7,4,7,9,6,5,3]],
#      [[1,2,3,4,5,6,3,2,4],
#      [4,2,7,4,7,9,10,4,6]],
#      [[1,2,3,4,5,6,19,6,8],
#      [4,2,7,4,7,9,2,1,20]]])
# print(a.shape)
# a = a.view(1,6,9)
# print(a)
# # print(a.shape)
# a = a.permute(0,2,1)
# print(a)
# mpl = nn.AdaptiveMaxPool1d(3)
# b = mpl((a.to(torch.float)))
# # print(a)
# print(b)

# c = a.pop()
# d = [1,2,3,4].pop(1)

# # print(a.pop())
# print(c)
# print(d)

class zoo:
    def __init__(self):
        # self.name = name
        self.ok = 1
    
    def eat(self):
        return '1'
    
    def drink(self):
        return '喝'

class pig(zoo):
    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def eat_all_day(self):
        return '一直吃'
    
    def drink_all_day(self):
        return '吨吨吨'

class rabbit(zoo):
    def __init__(self,name):
        super().__init__()
        self.name = name
    
    def eat_a_bit(self):
        return '只吃一点'


# fat_two = pig('fat_two')
# tuzi = rabbit('tuzi')
# print(fat_two.name)
# print(tuzi.name)



