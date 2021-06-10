# Amazonの在庫をチェックして、在庫があった場合にツイートするボットを作成する
設定ファイルは.envファイルとして管理
seleniumは使用せずにtweepyモジュールを使用
https://tech-blog.rakus.co.jp/entry/20201106/api
  
## １
TwitterAPIキーを取得<BR>
https://www.itti.jp/web-direction/how-to-apply-for-twitter-api/

## ２
Amazonの在庫チェックを実装<BR>
在庫チェックは以下のような商品ページで「カートに入れる」ボタンの有無で判断<BR>
https://www.amazon.co.jp/%E3%82%B7%E3%83%A3%E3%83%BC%E3%83%97-SHARP-SJ-AF50G-R-%E3%83%97%E3%83%A9%E3%82%BA%E3%83%9E%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B0%E3%83%A9%E3%83%87%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051

## ３
任意の文のTweetを実装<BR>

## ４
Amazonの在庫が見つかったらツイート

## ５
一度ツイートした商品は、再度在庫切れになるまではツイートしない

## ６
無限ループのプログラムとして、起動したら一定間隔で指定したURLを監視して、在庫が見つかったらツイートする
