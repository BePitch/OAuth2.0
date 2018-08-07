#Copy Repo
Fork GitHub repository

#Bootup Vagrant 
once in the directory in terminal or GitBash, 
    run vagrant up
        then
    run vagrant ssh
    run cd /vagrant
    type ls to make sure you are in the proper directory that contains project.py

#Install Python Libraries - make sure they are installed
    sudo pip install datetime
    sudo pip install requests
    sudo pip install httplib2
    sudo pip install oauth2client
    sudo pip install 

#Create Database and Insert data    
    run python database_setup.py
    run python lotsofsoftware.py

#Run Web App
    run python project.py

Type http://localhost:5000/  in your browser

When creating a new manufacturer you can test out this template

Name = Apple
City= Cupertino
Picture=Apple.png (i have preloaded an image for this exmaple as I did not have time to build out the upload image code to store it in Static) The image should appear on the manufactuer page.

Google and Facebook authentication installed

JSON endpoints working

All CRUD operations and page security working as well.

