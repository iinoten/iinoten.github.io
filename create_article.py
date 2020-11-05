import git
from about_index import set_new_article_to_index

def save_article_to_remote( ):
  repo = git.Repo('')
  #最新を取り込むため一旦Pull
  o = repo.remotes.origin
  o.pull()

  #Add
  repo.git.add(A=True)
  
  #Commit(サブディレクトリ含めて全て)
  repo.git.commit('-m','\"ブログ記事をCommit\"')

  #Push
  origin = repo.remote(name='origin')
  origin.push()
  
def create_new_article( number, title, content ):
  set_new_article_to_index(title, '日付', number)    
  breaked_content = content.replace('\n\n','<br><br>')

  file = open( './articles/'+str(number)+'.html', 'w' )
  file.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="article.css">
        <title>Document</title>
        <meta name="viewport" content="width=device-width,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no">
    </head>
    <body>
        <div class="main__root">
            <div class="Header">
                <div class="Header__Image--Box">
                    <div class="Header__Image">
                        <div class="Header__Subtitle--Box">
                            <div class="Header__Subtitle--Text">Mobilis in Mobilis</div>
                        </div>
                        <div class="Header__Maintitle--Box">
                            <div class="Header__Maintitle--Text">#イイノテンのブログ</div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="content">
                <div class="content__title--box">
                    <div class="content__title--text">
                        {title}
                    </div>
                    <div class="content__title--date"> 2020.04.04   [ <a href=".">元ツイート</a> ]</div>
                </div>
                <div class="content__body--box">
                        {content}
                </div>
                <div class="author__box">
                    <div class="author__title">
                        Written By
                    </div>
                    <div class="author__content--box">
                        <div class="author__img--box">
                            <img src="./icon.jpg">
                        </div>
                        <div class="author__content--text">
                            職はアーティストです。20歳になりました。<br>
                            Reactを使った開発が好きで <br>
                            個人開発ではデザイン、フロント、バックエンド、インフラをやります =)<br>
                            <a href="https://github.com/iinoten">Github</a><br>
                            <a href="https://twitter.com/iinoten">Twitter</a><br>
                            <a href="https://www.facebook.com/ten.iine.9/">Facebook</a><br>
                        </div>
                    </div>
                </div>
                <div class="copywrite">&copy;#イイノテンのブログ by Iino Ten</div>
            </div>
        </div>
    </body>
    </html>
  """)
  print("タイトル", title)
  print("本文", content)