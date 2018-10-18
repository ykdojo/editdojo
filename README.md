# Edit Dojo
A web app to improve writing skills in any language.

## Inspiration
The inspiration for this came from the lack of these kind of resources. You can find a ton of resources to master reading, listening or speaking a language. But when it comes to writing, there simply aren't much. 

## How it works
The app will function in these steps:
1. A user A will sign up with 2 languages, one in which they are proficient(say, English) and the other which they want to learn(say, Japanese).
2. Then they will write anything they need in, say, Japanese.
3. A user B, who is proficient in Japanese, will then verify and propose corrections.
4. Similarly if someone wants to learn English, user A can verify their messages.
5. Everyone is happy.

Initially the app will be based on twitter, that is, users will be editing tweets. Eventually, you will able to use this app without using Twitter at all!

## Installation
These are the steps to install the project on your machine. What we actually need is a virtual environment running Django version 2.1.
1. Install python on your machine. Mac and Ubuntu have it pre-installed. For Windows head on to https://www.python.org/downloads/.
2. Using pip3, the package manager for python, install pipenv using the command below in the terminal.

```
pip3 install pipenv
```
3. Open terminal in the folder containing the project files. Install Django version 2.1 in the virtual environment with the following command.

```
pipenv install django==2.1
```
4. Go into the virtual environment: 
```
pipenv shell
```
5. Run the server:

```
python manage.py runserver
```
6. Start using the app by opening the link shown in the terminal on your browser.

## Resources
This is a part of the series of YouTube videos demonstrating how to build a real startup using Python and JavaScipt. These are the resources helpful for this project:
- YouTube video link: https://www.youtube.com/watch?v=UyQn0BhVqNU
- Our Slack group and source code: https://www.csdojo.io/edit
- Waiting list for this app: https://www.csdojo.io/wait
- The recommended beginner Django book: https://csdojo.io/dj
- The free chapters of this book: https://djangoforbeginners.com/

## Credits
- This project was initiated by: [ykdojo](https://github.com/ykdojo)
- This README was created by: [vvyomjjain](https://github.com/vvyomjjain)
