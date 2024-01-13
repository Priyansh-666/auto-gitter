
    @echo off
    git init
    git add .
    git commit -m "update"
    git checkout master
    git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter
    git branch master
    git push Priyansh-666 master
    