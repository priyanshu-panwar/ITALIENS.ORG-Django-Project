# djangoItaliens

## SCOPE: 
We currently have a website (https://italiens.org/) which is based on node.js and requires 'manual' intervention to update pages by redeploying website through github (by me, but I have less and less time). Hence, I'd like to have the same layout as the existing one but migrating the back end in django so that an authorised, non technical user can add a post without technical support;

## Requirements:

_Must_
Functional
1. An authorised non technical user shall be able to post new articles on the website;
2. An authorised user shall be able to edit previously posted posts;
3. An authorised user shall be able to cancel previously posted posts;
4. An anonymous user can comment on posts;
5. the website can be deployed through Heroku;

Non functional
1. App shall be django based
2. App shall be deployable with a standard script
3. Code shall be commented properly

## Nice to have:
1. An anonymous user can dynamically create a new user for the website;
2. Only logged users can add comments to existing posts;
3. An admin can ban/remove users;

## Note: the code shall be delivered in a github repository that will be communicated at later stage.
## Note2: website to be converted: https://italiens.org/

# Script to run locally:
1. Install python latest version 3.7
2. Download the project or clone it.
3. Go to the project folder.
4. Open bash or command prompt.
5. Type in ```pip install -r requirements.txt```
6. Type in ```python manage.py runserver```
7. Open browser, go to: http://127.0.0.1:8000/

# Script to host on heroku:
1. Download heroku Client.
2. Login with the account inside the cmd or terminal: ```heroku login```
3. Type in: ```heroku create <appname>```
4. Then is the use of simple git commands.
5. ```git status```
6. ```git add --all```
7. ```git commit -m "<message>"```
8. ```heroku git:remote -a <appname>```
9. ```git push heroku master```
10. Site is deployed.
11. If collectstatic error occurs follow this: ```heroku config:set DISABLE_COLLECTSTATIC=1```
12. ```git push heroku master```
13. Site is deployed.
14. We need migrations now.
15. Open the bash in heroku: ```heroku run bash``` 
16. ```python manage.py migrate```
17. Create superuser: ```python manage.py createsuperuser```
18. Admin Panel: <appname>.herokuapp.com/admin
19. Change Password: ```python manage.py changepassword <user_name>```

# How to change Social Links:
1. Go to the ITALIENS Backend Portal
2. Under the Socials Section, there is Social Object (0).
3. Click on it and update the links.
Note: Do not create a new object, only update the first object.
