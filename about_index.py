def set_new_article_to_index( title, date, file_name ):
  file = open('index.html', 'r' )
  index_text = file.read()
  replaced_index_text = index_text.replace('<div id="empty__element"></div>', f'<div id="empty__element"></div>\n   <a href="./articles/{file_name}.html" class="article__box"><div class="article__title">{title}</div><div class="article__date">{date}</div></a>\n')

  write_file = open('index.html', 'w')
  write_file.write(replaced_index_text)
  
