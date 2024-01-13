
git init

git add .
git commit -m "update"


git checkout -b contribute


git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter


git pull --rebase Priyansh-666 contribute
git rebase --continue


git push Priyansh-666 contribute
