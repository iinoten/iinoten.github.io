#JSONとOAuth認証用のライブラリを使用
import json
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv

load_dotenv()

#取得した認証キーを設定
CONSUMER_KEY = os.environ['CK']
CONSUMER_SECRET = os.environ['CS']
ACCESS_TOKEN = os.environ['AT']
ACCESS_SECRET = os.environ['ATS']

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

#API用のURLを設定（●にはデベロッパー管理画面のDev environment labelを入力）
timeline_url = "https://api.twitter.com/1.1/search/tweets.json"

#paramsに検索ワードや件数、日付などを入力
params = {'q' : '#イイノテンのブログ', "maxResults" : "100"}#取得件数

#上記で設定したパラメーターをget関数を使い指定URLから取得
params ={
         'count' : 1000,      # 取得するtweet数
         'q'     :  ["#イイノテンのブログ"],# 検索キーワード
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }
timeline_req = twitter.get(timeline_url, params = params, stream=True)
if timeline_req.status_code == 200:
    res = json.loads(timeline_req.text)
    print(res)