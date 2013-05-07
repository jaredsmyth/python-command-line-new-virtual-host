python-command-line-new-virtual-host
====================================

script to create a new virtual host with two arguments for name and directory that you can pass to it from the command line  

jared smith | http://jaredsmyth.info

jvst | http://jvst.us

usage
======

**1)** follow this tutorial to setup up vhosts on your mac if you are running vhosts for the frst time
http://foundationphp.com/tutorials/vhosts_leopard.php

**2)** place the newhost.py file in your '~/' directoy

**3)** you can begin using just like that by calling   
    sudo python ~/newhost.py "name_of_your_vhost" "directory"  
-- note that the directory parameter is optional.  if left blank it will create an entry using the current working directory as your host --  

**4)** if you want to make your life easier and type less you can add an alias for this in your '~/.bash_profile'  
    sudo nano ~/.bash_profile  
add the following line  
    alias newhost='sudo python ~/newhost.py'    
then restart your terminal for the changes to take effect  

**5)** if you added the alias in you '~/.bash_profile' in the above step you can now use this script to create new vhosts by simply typing  
    newhost "name_of_your_vhost" "directory"  
-- again, note that the directory parameter is optional --  

----------------------------------------

**requirements:**
- python
- apache setup and running for vhosts
