from github import Github

g = Github('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')
repo = g.get_repo('tksolution-com-br/tks-ffc-totvs')
pulls = repo.get_pulls(state='closed', base='develop')

for pr in pulls:
    print(pr.body)
