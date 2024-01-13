
    @echo off
    :: branch change
    git init
    git add .
    git commit -m "update"
    git checkout contribute
    git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter
    git branch contribute
    git push Priyansh-666 contribute
    