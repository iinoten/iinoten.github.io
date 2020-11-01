def create_new_article( number, title, content ):
  breaked_content = content.replace('\n\n','<br><br>')
  file = open( './articles/'+str(number)+'.html', 'w' )
  file.write(f"""
  <h1>{title}</h1>
  <h4>{breaked_content}</h4>
  """)
  print("タイトル", title)
  print("本文", content)