import tweepy
import settings
from selenium.webdriver import Chrome, ChromeOptions
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse

LOG_FILE_PATH = "./log/log_{datetime}.log"
EXP_CSV_PATH="./exp_list_{search_keyword}_{datetime}.csv"
log_file_path = LOG_FILE_PATH.format(datetime=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S'))
INTERVAL = 60 * 5

class Search:
    ### Chromeを起動する関数
    def set_driver(self, headless_flg):
        # Chromeドライバーの読み込み
        options = ChromeOptions()

        # ヘッドレスモード（画面非表示モード）をの設定　
        if headless_flg == True:
            options.add_argument('--headless')

        # 起動オプションの設定
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
        # options.add_argument('log-level=3')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument('--incognito')          # シークレットモードの設定を付　与

        # ChromeのWebDriverオブジェクトを作成する。
        return Chrome(ChromeDriverManager().install(), options=options)

class Log:
    ### ログファイル及びコンソール出力
    def write_log(self, txt):
        now=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        logStr = '[%s: %s] %s' % ('log',now , txt)
        # ログ出力
        with open(log_file_path, 'a', encoding='utf-8_sig') as f:
            f.write(logStr + '\n')
        print(logStr)

class Tweet:
    def __init__(self):
        # Tweetに必要なキーを格納
        self.consumer_key = settings.CONSUMER_KEY
        self.consumer_secret = settings.CONSUMER_SECRET_KEY
        self.access_token = settings.ACCESS_TOKEN
        self.access_token_secret = settings.CONSUMER_TOKEN_SECRET__KEY

    def post_tweet(self, text):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        # tweetを投稿
        api.update_status(text)

### main処理
def main():
    log = Log()
    search = Search()
    log.write_log("処理開始")
    search_keyword = "シャープ-SHARP-SJ-AF50G-R-プラズマクラスター-グラデーションレッド"
    log.write_log(f"検索キーワード:{search_keyword}")

    # driverを起動
    driver = search.set_driver(False)
    # 検索URL作成
    url = "https://www.amazon.co.jp/{0}/dp/B08KJ85RJ5?ref_=fspcr_pl_dp_2_2272928051".format(urllib.parse.quote(search_keyword))
    # Webサイトを開く
    driver.get(url)
    time.sleep(5)
 
    try:
        exist_tweet_flag = False
        not_exist_tweet_flag = False
        while True:
            # カートを取得
            cart_button = driver.find_elements_by_css_selector("#add-to-cart-button")
            # 一定間隔で在庫を監視する
            if(len(cart_button) > 0):
                if not exist_tweet_flag:
                    now = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
                    tweet = Tweet()
                    tweet.post_tweet(f"{now}:指定商品の在庫があります。")
                    exist_tweet_flag = True
                    not_exist_tweet_flag = False
            else:
                if not not_exist_tweet_flag:
                    tweet.post_tweet("指定商品の在庫がなくなりました。")
                    exist_tweet_flag = False
                    not_exist_tweet_flag = True
                    
    except Exception as e:
        log.write_log("失敗")
        log.write_log(e)
        driver.close()

    log.write_log(f"処理終了")

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()