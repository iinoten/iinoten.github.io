def set_new_article_to_index( title, date, file_name ):
  init_index_file = open('index.html','w')
  init_index_file.write(
    '''
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
    '''
  )
  file = open('index.html', 'r' )
  index_text = file.read()
  replaced_index_text = index_text.replace('<div id="empty__element"></div>', f'<div id="empty__element"></div>\n   <a href="./articles/{file_name}.html" class="article__box"><div class="article__title">{title}</div><div class="article__date">{date}</div></a>\n')

  write_file = open('index.html', 'w')
  write_file.write(replaced_index_text)
  
