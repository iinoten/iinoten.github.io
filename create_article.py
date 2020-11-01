import git

def save_article_to_remote( file_name ):
  repo = git.Repo()
  #最新を取り込むため一旦Pull
  o = repo.remotes.origin
  o.pull()

  #Commit(サブディレクトリ含めて全て)
  repo.git.commit('.','-m','\"Commit Log\"')

  #Push
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