==================================
homefiles - github powered backups
==================================


`homefiles` backups your files to github so you can sync them anywhere.

The main use for `homefiles` is keeping a small set of files backed up,
versioned, and accessible, for example:

    * dotfiles (.vimrc, .screenrc)
    * TODO & IDEAS files
    * directory full of installation notes

`homefiles` uses symlinks to map the git-repo-location of a file to its
canonical location (see manifest.list)

`homefiles` recognizes additions, changes, and removals in watched
directories.


Installation
============

1. Download and install `homefiles`

2. Create a private github repo called 'homefiles-data'

3. Create the local checkout repo in the default location ~/.homefiles-data

    homefiles init < github username >

4. Add files to `homefiles`

    homefiles add TODO
    homefiles add .vimrc vimrc # no dot in repo copy

5. Sync (commit, push, rebuild symlinks)

    homefiles sync

6. OPTIONAL: Add crontab to sync hourly

    crontab etc/homefiles-crontab


Clone
=====

1. Clone the repo

    homefiles clone < github username >

2. There is no step 2.
