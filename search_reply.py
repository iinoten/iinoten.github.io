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
         'count' : 100,      # 取得するtweet数
         'result_type': 'mixed',#時系列で取得
         'exclude': 'retweets'#RTされて表示されているツイートを除外
         }
def get_reply_target_tweet( parent_tweet_id ):
  timeline_req = twitter.get(timeline_url, params = params, stream=True)
  if timeline_req.status_code == 200:
      res = json.loads(timeline_req.text)
      for tweet in res:
        if(tweet['in_reply_to_status_id_str'] == parent_tweet_id):
          img_content = ''
          if('media' in tweet['entities']):
            print("画像アリ")
            img_source = tweet['entities']['media'][0]['media_url']
            img_content = f'<div class="content__img--Box"><img class="content__img" src="{img_source}"></div>'
          else: 
            print("画像ナシ")
          result_tweet_tree_text = '<div class="content__body--paragraph">'+ tweet['text'] + img_content + '</div>'
          result_tweet_tree_text += '\n\n' + get_reply_target_tweet( str( tweet['id'] ) )
          return(result_tweet_tree_text)
      else:
        return("")
  else:
    return('ほげ')