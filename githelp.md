# A Brief Walkthrough of Some Git Commands

Here are some useful Git commands to keep in mind.

* `git status`
  * This is how you can see the current status of your git repository.
  * Here you can see which files have been modified along with files that Git doesn't yet know about that are new in your repo.

* `git add <file or directory path>`
  * This command is how you identify changes that should be prepared for a commit.
  * The file or directory named at the end of the command can be something modified or something entirely new that is not yet being tracked by Git.
  * To add all new, untracked items at once, use `git add -A`.
  
* `git commit -m '<Commit message here>'`
  * This command will initiate a commit based on everything that has been added thus far using the `git add` command.
  * Try to pick a commit message that concisely describes the changes represented in this commit.
  * All the changes made in a single sitting need not be in one commit. If the previous point is challenging, try breaking the commit into multiple commits.
  * If the only changes indicated by `git status` are modifications to files already being tracked by Git, use `git commit -am '<Commit message>'` to add and commit them all in one step.

* `git push origin master`
  * Takes all changes that have been committed thus far and pushes them up to the master branch.
  * If there are unpulled changes to master, you will be forced to accept these first before your push is made (potentially resulting in merge conflicts).
  * If you are on a branch that is not master, then simply swap the last argument to be the name of the branch where you would like to push your changes.

* `git log`
  * Lists all of the latest commits with authors, timestamps, and commit messages.
  * If the commit messages are helpful, looking at the log should be very helpful in getting up to speed on the most recent changes to a repo.
  
* `git checkout <file or directory path>`
  * Effectively the reverse of `git add`, this command will remove all changes to the specified file or directory making it identical to the most recent pull from the master branch
  * Useful for selectively reversing modifications in a project.
  * Not to be confused with the command for switching branches (`git checkout <branch name>`).

* `git branch <new branch name>`
  * This command will create a new branch with the specified name using the current local instance of the repository.

* `git checkout <branch name>`
  * Switches the local working branch to be the specified branch (if it exists).
  
* `git diff <optional file or directory>`
  * Shows (with colors) the insertions/deletions made to a particular file or directory.
  * If no argument is given, shows the diff for all modified files in the repo.
  
* `git stash` and `git stash pop`
  * The former command all uncommitted modifications to the local copy of the repo and pushes the onto a stack.
  * The latter command takes the most recent set of changes pushed onto that stack and pops them off, bringing them back into the local repo.
  * Stashing will remove the changes from the local copy of the repo. This would then, for example, make pulls possible without merge conflicts.
  * To recover the changes, simply pop the stash and potentially bring back merge conflicts to be resolved by hand.

* `git blame <file path>`
  * A useful command for when there are multiple editors of a single file and something breaks
  * The command will print each line of the supplied file along with the name of the person last responsible for editing that line (and when the edit was made).
  
* When things go wrong...
  * Try checking online resources like [this](http://ohshitgit.com/).
