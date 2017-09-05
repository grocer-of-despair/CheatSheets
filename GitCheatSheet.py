
mkdir NewFolder
Cd newFolder
git init

git pull <>

git status

git add <file> (. for all)

git commit -m "Changed items after carousel"
git remote add origin <remote repository url>
git push origin master

git log

Git show <commit-number>

To see all your commits on one line, which is useful if you have a lot of them, type in
git log --pretty=oneline

Git log —author=<username>
git log --graph --decorate --oneline

def Unstage
    git reset HEAD index.html

def Uncommit: # (Keep files unchanged)(1= most recent)
    git reset --soft HEAD~1

def Undo a push
    Git revert HEAD

def Check differences before you commit
    Git diff <file>

git fetch
git merge origin/master

git pull origin master

class BRANCHES:
Show all
Git branch -a

Create
Git branch <name>

Switch
Git checkout <name>

def CreateAndSwitch:
    Git checkout -b <name>

def Rename
    git branch -m <name> <new-name>

def Delete
    Git branch -d <name>

def Merge with current path
    Git merge <name>

def No FastForward
    Git merge —no-ff <name>

def Delete Remote
    git push origin --delete <name>
