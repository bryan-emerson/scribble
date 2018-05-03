# Scribble

![](https://dl.dropboxusercontent.com/s/8frf8rblw6pnpds/hipsterlogogenerator_1438007087793.png?dl=0)

Scribble is a Django application where users can read, write and interact
with the best content all around the world. It is designed to be built, refined and deployed over the course of four nights.

We will start off with two models: `Post` and `Comment`.

## Submitting

Fork this repo, and submit homework as a pull request on this repo...

```
$ git clone git@github.com:ga-dc-wdi-python/scribble.git
$ cd scribble
$ django-admin startapp .
```
> When asked if you want to overwrite the readme, enter "n" (for no).

The `.` creates a new Django app inside the *CURRENT* folder. Otherwise, it creates a new folder. For instance, if you did `rails new scribble` it would create a `scribble` folder and put the Rails app inside there.

> This is how a lot of people end up with a `scribble` folder inside another `scribble` folder.

## Models + Migrations

- Create [models](https://git.generalassemb.ly/dc-wdi-python-django/django-models#models---james) for Post and Comment
- Create [migrations](https://git.generalassemb.ly/dc-wdi-python-django/django-models#migrations---ali) for Post and Comment

## Index

- Create an index where a user can see all posts
- Each post should link to its respective show page

## Show

- Create a show where a user can see each individual post.
- The show page should also show all of the post's comments.

## Create

- Allow the user to create new posts and comments

## Update

- Allow the user to edit existing posts and comments

## Delete

- Allow the user to delete existing posts and comments.

## Bonus

Create two additional models: Category and Tag.
* Tag represents the join table between Post and Category.

Update the `Post` show page so that it includes...
* A linkable list of that Post's Categories.
* When clicked, each Tag should link to its Category show page.

Create a form that allows you to create a Tag and/or Category.
*  If the Category exists, it will create a tag for that post.
*  If the Category does not yet exist, it will create that Category and create a Tag for that post.
*  If the Category exists AND the post already has that Tag, nothing will happen.

The Category show page should display all posts with that particular category.
