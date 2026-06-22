import pandas as pd 


df = pd.read_csv('demo.txt')
df
# 读取文件内容
with open('demo.txt', 'r') as file:
    content = file.read()
    print(content)
