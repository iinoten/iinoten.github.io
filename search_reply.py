#JSONとOAuth認証用のライブラリを使用
import json
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv
import re

load_dotenv()

#取得した認証キーを設定
CONSUMER_KEY = os.environ['CK']
CONSUMER_SECRET = os.environ['CS']
ACCESS_TOKEN = os.environ['AT']
ACCESS_SECRET = os.environ['ATS']

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

#API用のURLを設定（●にはデベロッパー管理画面のDev environment labelを入力）
timeline_url = "https://api.twitter.com/1.1/statuses/user_timeline.json"

#paramsに検索ワードや件数、日付などを入力
params = {'q' : '#イイノテンのブログ', "maxResults" : "10"}#取得件数

#上記で設定したパラメーターをget関数を使い指定URLから取得
params ={
        'screen_name': 'iinoten',
         'count' : 10,      # 取得するtweet数
         'q'     :  ["あ"],# 検索キーワード
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }
def get_reply_target_tweet( tweet_id ):
  timeline_req = twitter.get(timeline_url, params = params, stream=True)
  if timeline_req.status_code == 200:
      res = json.loads(timeline_req.text)
      for tweet in res:
        if(tweet['in_reply_to_status_id_str'] == tweet_id):
          print(tweet['user']['name']+'::'+tweet['text'])
          print(tweet['created_at'])
          print('*******************************************')

get_reply_target_tweet('1322416478495203334')