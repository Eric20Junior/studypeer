# studypeeer

![screenshot](./static/images/studypeer1.png)

# Description
+ Study Peer is a platform which consists of rooms and for each rooms a certain group of people can join a study together, it also allows users to user the CRUD operations. Example users can create or delete a room of their choice.
- The purpose of this project is to test my ability on how well i understood django, The CRUD operations was implement, endpoints were created, a RESTful Api was built for others to utilize.

	+ Users can create new post
	+ Users can read post
	+ Users can update post
	+ Users can delete post
	+ Users can comment and delete comments
	+ A Users cant delete a post or comments which is not theirs
	+ Register/Login authentication was implemented

## Installation
+ Clone this repo ans `cd` to the cloned repository's directory
+ Run `python install -r requirements.txt

## Usage
+ `python manage.py makemigrations`
+ `python manage.py migrate`
+ Run `python manage.py runserver` to run the app
