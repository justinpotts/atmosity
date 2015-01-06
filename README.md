Atmosity
========
View your outdoor weather statistics on a personalized dashboard from anywhere on your home network.
Check out our website in the making at https://atmosity.wordpress.com.

##Setup

First, you will need to install the following items:

#### Flask
> sudo pip install Flask

#### sqlite3
  1. Go to http://www.sqlite.org/download.html
  2. Download the latest version
  3. Follow these steps
  
> $ tar xvfz sqlite-autoconf-3071502.tar.gz

> $ cd sqlite-autoconf-3071502

> $ ./configure --prefix=/usr/local

> $ make

> $ make install

Setup your database:

> $ python

> \>\>\> from atmosity import init_db

> \>\>\> init_db()



#### Python Weather API (pywapi)

Run the command:

> $ pip install pywapi

That's it! Now you're ready to run Atmosity!

##Run

Navigate to the home directory and run the command:
>python atmosity.py

You should see something similar to

> \* Running on http://127.0.0.1:5000/

> \* Restarting with reloader

You may log into the admin control panel with the default username and password as 'admin'.

##Contribute
Contributions are always welcome! Atmosity is completely open, hackable, and free to the limits of your own imagination. 
Add on your own sensors, build your own dashboard, or host a server and share your information to the world.

Be sure that your code complies with Pep8 standards, although we are a bit loose on the 79 character line limit rule :).
Also remember to do all of your work on a branch something other than master. That way, your work is a bit safer from
accidental modifcations. 

You can find some issues to work on in our issues section of the Atmosity repository. Assign yourself one, or ask one of us for
permission to work on it and we will be sure to get it assigned! Do some work, then submit a pull request for review. Do us
a favor and comment on the issue with your pull request number for book keeping purposes. Keep your eyes open for some comments 
on your code, then update, push, and we will merge. Have fun!

Remember, the key to a great community is communication! If you have any questions, feel free to email me at moz dot justinpotts
@ gmail dot com.
