import git

def save_article_to_remote( file_name ):
  github_url = 'https://github.com/iinoten/iinoten.github.io'
  repo = git.Repo('./')
  repo.git.add('./articles/'+file_name)
  repo.index.add("ブログ記事をcommit: ",file_name)

  origin = repo.remote(name='origin')
  origin.push()
  
def create_new_article( number, title, content ):
  breaked_content = content.replace('\n\n','<br><br>')
  file = open( './articles/'+str(number)+'.html', 'w' )
  file.write(f"""
  <h1>{title}</h1>
  <h4>{breaked_content}</h4>
  """)
  print("タイトル", title)
  print("本文", content)

  save_article_to_remote(str(number)+'.html')