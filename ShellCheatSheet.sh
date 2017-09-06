bin # Binary

sudo -i # Run terminal as ROOT

echo $COLUMNS x $LINES  #Returns the size of the Terminal Window

cd Pictures; ls # Lets you write 2+ commands on the same LINE

pwd # Print Working Directory
.. # Parent Directory
. # This Directory
~ # Home Directory

-l # longer list with more detail
ls -l Documents/*.pdf # Lists all files that are PDF
ls bear* # Lists files that start with bear

mv 'Documents/File' Documents/Folder/ # To Move from one folder to another without cd

curl # C URL
curl -L 'http://google.com' # -L Follows redirects
curl -o google.html -L 'http://google.com' # Save as google.html
cmd+k OR clear# Clear Terminal Window

cat # Reads a file and outputs the contents (Catenate)
less # Reads a file and outputs a section of it at a time, just press SPACE

rm # Remove a File
rm -i # Interactive, always throws a prompt to make sure you wnat to delete

grep # Searches file for STRING
grep string file.txt
grep string file.txt | less # Send it to the less program to output one page at a time
curl -L https://tinyurl.com/zeyq9vc | grep string # Searches for string in a remote file
grep -c string # Count

wc # Word Count program
wc -l # Ask WorCount to count LINES

for Variables:
    numbers='one two three'
    echo $numbers
    def Shell Variables:
        eg $COLUMNS, $LINES
        Internal to Shell program

    def Environment Variable:
        $PATH
        Shared with Programs you run within the SHELL

PATH=$PATH:/new/dir/here # To change PATH Directory, Resets every time you reset SHELL

# Use the bash_profile, this runs certain functions on Shell Startup
# Linux
open bashrc

# Mac/Windows
open .bash_profile

# For linux
if [-f ~/.bashrc ] ; then
  source ~/.bashrc
fi

date
echo "Message!"

for Aliases:
  alias # Lists all current aliases
  alias ll='ls -la' # Allows you to create shortcuts for commands
  # To keep them put them in .bash_profile
