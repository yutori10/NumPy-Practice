#import文, モジュールのインポート
#matplotlib.pyplotはグラフを描画するためのモジュール
import numpy as np
import matpoltlib.pyplot as plt

#独立変数xについて定義, 0~500の長さの横軸を2π毎に区切る
#np.linspaceは数字を指定した感覚で区切って配列を生成する関数
#np.piは円周率
x = np.linspace(0, 2*np.pi, 500)

#xの描画とそれに対応するsinxの描画
#y = np.sin(x)としてplt.plot(x, y)と書いても良い
plt.plot(x, np.sin(x))