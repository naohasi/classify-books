# classify-books
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
