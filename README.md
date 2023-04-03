# Boston-house-prediction---End-to-End-ML-Project
Complete end to end ML project using flask web frame work, docker, ci/cd pipelines and delpoyment on Heroku cloud


STEPS: 

1. CREATE A NEW REPOSITORY - EG. BOSTON HOUSE PRICE PREDICTION  ( we also create a gitignore file and set license )
2. CLONE REPOSITORY - create a local folder on your computer say "projects". copy the link of the repo on github , go to cmd , navigate to that local folder you created by cd path  and then type: git clone <github repo link>      note: you may have to install git CLI

3. Create your ML model in anaconda and save your model as a pickle file.
4. SET UP GIT : set your user name  :               git config --global user.name  "username"
                set your email of github account :  git config --global user.email  "email"
5. ADD FILES (to push to github repo)   :  git add filename  or git add . to add all files from the local folder we create where we cloned our repo.
                                           git status      # to check what files ahev been added.

                                          # note : if we dont want to add a file , just put that filename in the gitignore file.
 NOW TO COMMIT :  git commit -m "this is our first commit and pushes a few important files"

 FINALLY WE NEED TO PUSH IT TO THE GITHUB REPO BY:  git push origin main     syntax: git push <remote>  <branch>

 6. CREATE Procfile , Dockerfile and push these files to github

 7. Now we need to set up the GIT CI/CD PIPELINE , to do this first we create a folder .github and inside that workflows folder and inside that create a main.yaml file which contains code to buuld the docker image and push the container to heroku.Note that inside this file you will find secret.heroku_appname,secret.heroku_api_key, and secret.heroku_email, now we need to set up these secret keys in our git hub repo

 8. Go to your repo in github, click settings(top right),scroll down , click secrets and variables(bottom left),click actions,click new repository secret,then:
 a. type HEROKU_EMAIL in the secret name and add the email id linked to your account in the secret section(eg. seanrodrigues12@gmail.com), click add secret.
 b. click new repository secret again , type HEROKU_APP_NAME in secret name and copy paste the name of the app in the secret section.To get the name of the app, you need to create a new app on heroku and copy paste the name (eg. boston-house-price-prediction1)
 c. click on new repo secret again, type HEROKU_API_KEY in the secret name , and the api key in the secret section.To get the api key of heroku, go to account settings(top right),scroll down and you will find the api key

 YOU HAVE SET UP GITHUB ACTIONS

