@echo off
:: Initialize Git repository
git init

:: Add and commit changes to the main branch
git add .
git commit -m "update"

:: Create and switch to the contribute branch
git checkout -b contribute

:: Add remote repository with branch-specific URL
git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter.git

:: Fetch and rebase changes from the remote contribute branch
git pull --rebase Priyansh-666 contribute

:: Push changes to the remote contribute branch
git push Priyansh-666 contribute
