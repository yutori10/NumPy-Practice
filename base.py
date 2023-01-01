#変数の宣言
x = 2
y = 3
#四則演算, print()を用いて結果を出力
print(x + y)
print(x - y)
print(x*y)
print(x/y)
#文字列の出力, 連結はcastする
print("text")
print("variable x:" + str(x))
#type()を用いてデータ型の確認
t_x = [1, 2, 3]#list
l_x = (-1, -2, -3)#tuple
print(type(t_x))
print(type(l_x))
print(t_x[0])#0番目から始まる
print(l_x[0])#listと同様
#ディクショナリは左のキーで値を呼び出す
dic = {'a':1, 'b':2, 'c':3}
print(dic['a'])
#for文で繰り返し処理
for i in range(3):#rangeも0から
    print(i)
#関数の定義
def func(x):
    return x + 5
print(func(2))
#以上よりPythonの基本は修了です