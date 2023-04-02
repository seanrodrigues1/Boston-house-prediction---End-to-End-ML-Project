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