
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

Unstage
git reset HEAD index.html

Uncommit (Keep files unchanged)(1= most recent)
git reset --soft HEAD~1

Undo a push
Git revert HEAD

Check differences before you commit
Git diff <file>

git fetch
git merge origin/master

git pull origin master

BRANCHES
Show all
Git branch -a

Create
Git branch <name>

Switch
Git checkout <name>

Create and Switch
Git checkout -b <name>

Rename
git branch -m <name> <new-name>

Delete
Git branch -d <name>

Merge with current path
Git merge <name>

No FastForward
Git merge —no-ff <name>

Delete Remote
git push origin --delete <name>
