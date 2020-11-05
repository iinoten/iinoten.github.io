#JSONとOAuth認証用のライブラリを使用
import json
from requests_oauthlib import OAuth1Session
import os
from dotenv import load_dotenv
import re
from search_reply import get_reply_target_tweet
from create_article import create_new_article
from create_article import save_article_to_remote

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
write_file = open('index.html', 'w')
write_file.write(
    """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="index.css">
        <title>Document</title>
    </head>
    <body>
        <div class="blog__description--Box">
            <div class="blog__description--text">このブログは、Twitterで特定のハッシュタグに反応して、botが内容を取得しブログ形式でまとめられています。</div>
        </div>
        <div class="title__box">
            <div class="title__text">記事一覧</div>
        </div>
        <div id="empty__element"></div>
    </body>
    </html>
    
    """
  )
timeline_req = twitter.get(timeline_url, params = params, stream=True)
if timeline_req.status_code == 200:
    res = json.loads(timeline_req.text)
    for tweet in res['statuses']:
      if tweet['user']['id'] == 3230712428:
        img_content = ''
        if(tweet['text'].find('\n\n') > 0 ):  #ツイート内容にタイトルが含まれているかどうか
          title = tweet['text'].split('\n\n')[0]
          if('media' in tweet['entities']):
            img_source = tweet['entities']['media'][0]['media_url']
            img_content = f'<div class="content__img--Box"><img class="content__img" src="{img_source}"></div>'
          content = '<div class="content__body--paragraph">'+tweet['text'].split('\n\n')[1]+ img_content + '</div>' + '\n\n' + get_reply_target_tweet(str(tweet['id']))
          create_new_article( tweet['id'], title, content )
          save_article_to_remote()