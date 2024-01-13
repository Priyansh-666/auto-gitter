@echo off
:: Initialize Git repository
git init

:: Add and commit changes to the main branch
git add .
git commit -m "update"
git branch remotebat

:: Add remote repository with branch-specific URL
git remote add Priyansh-666 https://github.com/Priyansh-666/auto-gitter.git

:: Push changes to the remote contribute branch
git push Priyansh-666 remotebat
