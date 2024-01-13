
    git init
    git add .
    git commit -m "update"
    git fetch Priyansh-666
    git rebase Priyansh-666/contribute

    git rebase --continue

    git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter
    git fetch Priyansh-666
    git merge Priyansh-666/contribute
    git rebase Priyansh-666/contribute
    git rebase --continue

    git merge --continue
    git branch contribute
    git push Priyansh-666 contribute
    