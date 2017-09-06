def SHA:
    Secure Hash Algorithm, an ID number for each commit

git init # Initialize as Git Repository

git pull <>

git status

class add:

    git add <file> (. for all)
    git add <file> <file> # For adding multiple files
    git rm --cached <file> # Unstages a file

class commit:
    git commit -m "Changed items after carousel"
    git reset --soft HEAD~1 # Uncommit (Keep files unchanged)(1= most recent)

    git commit --amend # Most recent commit
    git revert <SHA-of-commit-to-revert> # Create a new commit that Reverts project to this commit

    def reset:
        'HEAD^', 'HEAD~', 'HEAD~1' # First Parent commit
        'HEAD^2' # 2nd parent of commit
        git reset <reference-to-commit>
        --mixed # Returns the files commited to the WORKING DIRECTORY
        --soft # Returns the files commited to the STAGING INDEX
        --hard # Moves the files to the TRASH

git remote add origin <remote repository url>

class push:
    git push origin master
    git revert HEAD # Undo Push

class log:
    git log

    git show <commit-number> # git show only shows 1 log, so either most recent or specified SHA

    To see all your commits on one line, which is useful if you have a lot of them, type in
        git log --pretty=oneline

        git log —author=<username>
        git log --graph --all # shows a graphical representation of all branches and commits

        git log --stat # Gives detailed stats on what files were Changed, and how many lines deleted/added
        git log -p # Displays the actual changes made to a file, code
        git log -w -p # Ignores Whitespace Changes

        try:
            diff --git a/css/app.css b/css/app.css # a=Old Version b=New Version
            index 78cef20..07c36fa 100644
            --- a/css/app.css # Old version lines have a -
            +++ b/css/app.css # new version lines have a +
            @@ -142,6 +142,37 @@ # Line 142,6 Lines Line 142,37 Lines

    def Navigation:
        for scroll down:
            'j' or '↓' to move down one line at a time
            'd' to move by half the page screen
            'f' to move by a whole page screen
        for scroll up:
            'k' or '↑' to move up one line at a time
            'u' to move by half the page screen
            'b' to move by a whole page screen
        for quit:
            press 'q'

class ignore:
    Create a new file .gitignore
    Paste filenames you want to ignore in here
    samples/*.jpg # Ignore all .jpg files
    try:
        blank lines can be used for spacing
        '#' - marks line as a comment
        '*' - matches 0 or more characters
        '?' - matches 1 character
        '[abc]' - matches a, b, or c
        '**' - matches nested directories - a/**/z matches
            - a/z
            - a/b/z
            - a/b/c/z

for Unstage
    git reset HEAD index.html

class tag:
    git tag -a <tag> # -a gives an annotated tag which supplies more information than normal lightweight (Without -a)
    git tag # Displays Tag
    git tag -d <tag> # Delete Specific tag
    git tag -a <tag> <SHA> # To tag a specific Past Commit

class diff:
    git diff <file> # Changes that have been made but not committed yet

git fetch
class merge:
    git merge <name> # Merge 2 <name> with current checked out branch
    git reset --hard HEAD^ # Undo last merge
    git merge —no-ff <name> # No Fast-Forward

for Delete Remote
    git push origin --delete <name>

    git pull origin master

class Clone:
    git clone <repository>
    git clone <repository> <asName>



class BRANCHES:
    git branch # Show current BRANCH
    git branch -a # Show all

    git branch <name> <SHA> # CREATE Branch at SHA
    git checkout <name>
    git checkout -b <name> # Create and Checkout

    git branch -m <name> <new-name> # RENAME Branch
    git branch -d <name> # DELETE






class FirstSetup:
    # sets up Git with your name
    git config --global user.name "<Your-Full-Name>"

    # sets up Git with your email
    git config --global user.email "<your-email-address>"

    # makes sure that Git output is colored
    git config --global color.ui auto

    # displays the original state in a conflict
    git config --global merge.conflictstyle diff3

    git config --list
