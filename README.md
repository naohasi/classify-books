# classify-books

## 開発環境
- Python 2.7
- pip 9.0.1
- Mac

## tensorflowを入れる
- https://www.tensorflow.org/versions/master/install/install_mac
- EasyInstallはPythonのためのパッケージ管理システムである

```
$ sudo easy_install pip
$ sudo pip install --upgrade virtualenv
$ virtualenv --system-site-packages tensorflow
$ source tensorflow/bin/activate
```

(tensorflow) ```
$ easy_install -U pip
$ pip install --upgrade tensorflow

```

## 仕様
- 青空文庫のタイトル一覧を利用
 - http://www.aozora.gr.jp/index_pages/person_all.html
- 作りたい学習データ
  - age(10-60)
  - gender(1: male, 2:female)
  - clicked(1:買った, 2:買わなかった)
  - title_id(青空文庫の作品ID)
  - title(青空文庫の作品名)

| age        | gender          | clicked |title_id                 | title|
| -: |-:| -: | -:| -: |
| 20 | 1 | 1 | 1234 | 吾輩は猫である |
| 32 | 2 | 0 | 1235 | 羅生門 |

- NN
  - https://www.tensorflow.org/get_started/tflearn
  - input:age,gender,clicked
  - output:title_id
