# Overview
解いたAtcoderを溜めておく場所

## dir構造
- abc/
- agc/
とかで分ける

## 命名規則
abc/146c.pyとかにする。
汎用性が高い問題は146c_xor.pyとかsuffixをつける。
いつかsuffixつきだけ別のdirに入れてもいいかも

## 目標
一日 300 3問,400 1問
## Docker環境の構築
```
#外側から動かすやつ
docker-compose build
docker-compose run dev bash

# 
cmake ..
cmake --build .
./hoge


```
