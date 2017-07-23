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

# 実行結果
```
$ tree ./
./
├── README.md
├── classifyBooks.py
├── list_person_all_utf8.csv
├── makeTrainingData.py
└── trainingDate100.csv

0 directories, 5 files
$ python makeTrainingData.py
$  source ~/tensorflow/bin/activate
(tensorflow) $ python classiferSample.py
python: can't open file 'classiferSample.py': [Errno 2] No such file or directory
(tensorflow) $ python classifyBooks.py
WARNING:tensorflow:From /Users/hoge/tensorflow/lib/python2.7/site-packages/tensorflow/contrib/learn/python/learn/estimators/head.py:625: scalar_summary (from tensorflow.python.ops.logging_ops) is deprecated and will be removed after 2016-11-30.
Instructions for updating:
Please switch to tf.summary.scalar. Note that tf.summary.scalar uses the node name instead of the tag. This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in. Also, passing a tensor or list of tags to a scalar summary op is no longer supported.
2017-07-23 15:23:26.635018: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use SSE4.2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-23 15:23:26.635052: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX instructions, but these are available on your machine and could speed up CPU computations.
2017-07-23 15:23:26.635059: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use AVX2 instructions, but these are available on your machine and could speed up CPU computations.
2017-07-23 15:23:26.635066: W tensorflow/core/platform/cpu_feature_guard.cc:45] The TensorFlow library wasn't compiled to use FMA instructions, but these are available on your machine and could speed up CPU computations.
WARNING:tensorflow:From /Users/hoge/tensorflow/lib/python2.7/site-packages/tensorflow/python/util/deprecation.py:347: calling predict (from tensorflow.contrib.learn.python.learn.estimators.dnn) with outputs=None is deprecated and will be removed after 2017-03-01.
Instructions for updating:
Please switch to predict_classes, or set `outputs` argument.
New Samples, Class Predictions:    [64]

```