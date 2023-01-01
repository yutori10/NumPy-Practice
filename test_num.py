import numpy as np#importでモジュールを読み込み, asで名前を省略する
#配列の宣言, 配列に大して演算をするとすべての要素に対して適用される
a = np.array([1, 2, 3])
b = np.array([2, 2, 0])
print(a*3)
print(a+2)
print([1, 2, 3]*3)#listの場合複製される
#すべての要素への作用や、形の違う配列同士の演算をブロードキャストという
#配列の同士の四則演算
print(a+b)
print(a/b)#0で割ってしまっているのでinfとエラーが出る
print(a*b)#アダマール積
#行列の内積はnp.dot()を使って表す
print(np.dot(a, b))
