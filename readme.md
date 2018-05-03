
# Scribble

![](https://dl.dropboxusercontent.com/s/8frf8rblw6pnpds/hipsterlogogenerator_1438007087793.png?dl=0)

Scribble is a Django application where users can read, write and interact
with the best content all around the world. It is designed to be built, refined and deployed over the course of four nights.

## Submitting

Fork this repo, and submit homework as a pull request on this repo...

```
$ git clone git@github.com:ga-dc-wdi-python/scribble.git
$ cd scribble
$ django-admin startapp .
```
> When asked if you want to overwrite the readme, enter "n" (for no).

The `.` creates a new Django app inside the *CURRENT* folder. Otherwise, it creates a new folder. 

<!-- For instance, if you did `rails new scribble` it would create a `scribble` folder and put the Rails app inside there. -->

> This is how a lot of people end up with a `scribble` folder inside another `scribble` folder.

## Specifications

### Models + Migrations

1. Create [models](https://git.generalassemb.ly/dc-wdi-python-django/django-models#models---james) for Post and Comment
2. Create [migrations](https://git.generalassemb.ly/dc-wdi-python-django/django-models#migrations---ali) for Post and Comment

We will start off with two models: `Post` and `Comment`.

A `Post` should have an `author`, `title`, and `body` (these can all be `CharField`s). A `Comment` should have an `author`, `body`, and a `post`. The `author` and `body` model attributes can be `CharField`s but `post` should be a `ForeignKey`.

### Templates

1. List template
  * Create an list template where a user can see all posts
  * Each post should link to its respective detail page
2. Detail template
  * Create a detail template where a user can see each individual post.
  * The show page should also list all of the post's comments.
3. Forms for creating Posts and Comments
  * Allow the user to create new posts and comments
4. Updating and Editing
  * Allow the user to edit existing posts and comments
5. Deletion
  * Allow the user to delete existing posts and comments
  * You can add this form or link in the detail view for posts

## Bonus

* Add users
* Create a many-to-many so that users can favorite posts
