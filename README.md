# Heavenly Herb Company

![Responsiveness across devices](media/Mukta.png)


## Introduction

Live project can be found at [Heavenly Herb Company](https://heavenly-herb-company.herokuapp.com)

This an e-commerce website developed by Hugh Padmore. This website was built to be eventually used by heavenly herb company as their live site. The company
sells natural, homemade herbal products. 

## Table of Contents:

1. [UX](#UX)
    1. [Project Goals](#project-goals)
    2. [User Goals](#user-goals)
    3. [User Stories](#user-Stories)
    4. [Site Owner Goals](#site-owner-goals)
2. [User Requirements and Expectations](#user-requirements-and-expectations)
    1. [Requirements](#Requirements)
    2. [Expectations](#expectations)
3. [Wireframes](#wireframes)
4. [Features](#Features)
    1. [Existing Features](#existing-features)
    2. [Future Features](#future-features)
5. [Information Architecture](#Information-architecture)
    1. [Database Choice](#database-choice)
    2. [Data Models](#data-models)
6. [Technologies](#Technologies)
    1. [Languages](#Languages)
    2. [Libraries](#Libraries)
    3. [Tools](#Tools)
    4. [Databases](#Databases)
7. [Testing](#Testing)

8. [Deployment](#Deployment)
    1. [Instructions](#Instructions)
    2. [Deployment to Heroku](#Deployment-to-Heroku)
6. [Credits](#Credits)
    1. [Media](#Media)
7. [Acknowledgments](#Acknowledgments)

## UX

### Project Goals

The purpose of this project is to create a site which users can buy herbal products and learn more about the company. The site is focused around nature with 
blue, green and yellow as the primary colours which represent the sky, earth and sun respectively. The site also aims to have a personal feel to reflect the homemade aspect 
of the products so I have used Noto Sans Italic to give the text a handwritten look.  

#### **User Goals:**

- Browse herbal products
- Purchase herbal products
- To learn more 

#### **User Stories:**

- As a user, I expect to browse the products the website offers by category or price.
- As a user, I expect to be able to easily navigate the site using the menu.
- As a user, I expect to be able to learn and understand more about the products before purchase.
- As a user, I expect to be able to add products to the shopping bag and pay for it.
- As a user, I expect to be able to register to the website so I can check my previous purchases.
- As a user, I expect to be able to reset or change my password easily and securely.

#### **Site Owner Goals:**

As a superuser:

- I expect to be able to log in as a superuser and create, update and delete products on the website.
- I expect to provide users with a safe and secure e-commerce platform.
- I expect to provide users with clear instructions on how to use the products.
- I expect to be able to receive feedback from customers

## User Requirements and Expectations:

### **Requirements:**

- Navigate through the pages of the website intuitively.
- The content displayed in a visually appealing manner.
- Navigate the website on any device.
- Add products to the shopping cart and update the basket amounts.
- Buy items from the checkout safely and securely.
- View past orders and user details in profile section.

### **Expectations:**

- Navigation takes the user directly to the desired page of the website.
- The users' payment data will not be kept in the website's database.
- The website will guarantee the safe storage of user details.
- The website will have intuitive navigation.
- The website will have a responsive design.
- Content is well presented and visually satisfying.

## Wireframes

The wireframes for this project were created on [Figma](https://figma.com).
View my wireframes [here](https://www.dropbox.com/sh/ubsyfakp52eyzzp/AAB93rmfxmhLiIrMnD9aagmaa?dl=0).

## Features

### Existing Features

- Create account, easily view past orders
- Manage email addresses and passwords
- Product search 
- Product filtering
- View product detail pages
- Review Bag
- Checkout
- Contact Us form which anyone can use
- About Us section
- Superusers can add, edit, remove products from the store


### Future Features

- Social Media Login
- Order confirmation emails
- Recommended Items Blog
- Individual Ingredients info (herbs)
- Logged in users will have delivery information pre-filled on the checkout page


## Information Architecture

### Database Choice:

- During the development of this project, I worked with the standard **sqlite3** database that comes installed with Django.
- In the production version the database is a **PostgreSQL** database, hosted and provided by **Heroku**.

### Data Models:

The user model used in this project is provided by Django. You can find more information about this [here](https://docs.djangoproject.com/en/3.0/ref/contrib/auth/)

#### The Order Model

| _Title_          | _Key in DB_     | _Form Validation type_                                                               | _Data type_   |
| ---------------- | --------------- | ------------------------------------------------------------------------------------ | ------------- |
| Order Number     | order_number    | max_length=32, null=False, editable=False                                            | CharField     |
| User Profile     | user_profile    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' | ForeignKey    |
| Full Name        | full_name       | max_length=50, null=False, blank=False                                               | CharField     |
| Email            | email           | max_length=254, null=False, blank=False                                              | EmailField    |
| Phone Number     | phone_number    | max_length=20, null=False, blank=False                                               | CharField     |
| Country          | country         | blank_label='Country *', default='GB', null=False, blank=False                       | CountryField  |
| Post Code        | postcode        | max_length=20, null=True, blank=True                                                 | CharField     |
| Town or City     | town_or_city    | max_length=40, null=False, blank=False                                               | CharField     |
| Street Address 1 | street_address1 | max_length=80, null=False, blank=False                                               | CharField     |
| Street Address 2 | street_address2 | max_length=80, null=True, blank=True                                                 | CharField     |
| County           | county          | max_length=80, null=True, blank=True                                                 | CharField     |
| Date             | date            | auto_now_add=True                                                                    | DateTimeField |
| Delivery Cost    | delivery_cost   | max_digits=6, decimal_places=2, null=False, default=0                                | DecimalField  |
| Order Total      | order_total     | max_digits=10, decimal_places=2, null=False, default=0                               | DecimalField  |
| Grand Total      | grand_total     | max_digits=10, decimal_places=2, null=False, default=0                               | DecimalField  |
| Original Bag     | original_bag    | null=False, blank=False, default=''                                                  | TextField     |
| Stripe PID       | stripe_pid      | max_length=254, null=False, blank=False, default=''                                  | CharField     |

#### The OrderLineItem Model

| _Title_         | _Key in DB_    | _Form Validation type_                                                             | _Data Type_  |
| --------------- | -------------- | ---------------------------------------------------------------------------------- | ------------ |
| Order           | order          | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' | ForeignKey   |
| Product         | product        | Product, null=False, blank=False, on_delete=models.CASCADE                         | ForeignKey   |
| Quantity        | quantity       | null=False, blank=False, default=0                                                 | IntegerField |
| Line Item Total | lineitem_total | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            | DecimalField |

#### The Category Model

| _Title_       | _Key in DB_   | _Form Validation type_                | _Data Type_ |
| ------------- | ------------- | ------------------------------------- | ----------- |
| Name          | name          | max_length=254                        | CharField   |
| Friendly Name | friendly_name | max_length=254, null=True, blank=True | CharField   |

#### The Product Model

| _Title_     | _Key in DB_ | _Form Validation type_                                       | _Data Type_  |
| ----------- | ----------- | ------------------------------------------------------------ | ------------ |
| Category    | category    | 'Category', null=True, blank=True, on_delete=models.SET_NULL | ForeignKey   |
| SKU         | sku         | max_length=254, null=True, blank=True                        | CharField    |
| Name        | name        | max_length=254                                               | CharField    |
| Description | description |                                                              | TextField    |
| Directions  | directions  | blank=True                                                   | TextField    |
| Ingredients | ingredients | blank=True                                                   | TextField    |
| Price       | price       | max_digits=6, decimal_places=2                               | DecimalField |
| Image       | image       | upload_to='', null=True, blank=True                          | ImageField   |

#### The UserProfile Model

| _Title_                  | _Key in DB_             | _Form Validation type_                               | _Data Type_   |
| ------------------------ | ----------------------- | ---------------------------------------------------- | ------------- |
| User                     | user                    | User, on_delete=models.CASCADE                       | OneToOneField |
| Full Name                | full_name               | max_length=80, null=True, blank=True                 | CharField     |
| Email                    | email                   | default='', max_length=254, null=False, blank=False  | EmailField    |
| Phone Number             | phone_number            | default='', max_length=20, null=True, blank=True     | CharField     |
| Default Phone Number     | default_phone_number    | max_length=20, null=True, blank=True                 | CharField     |
| Default Street Address 1 | default_street_address1 | max_length=80, null=True, blank=True                 | CharField     |
| Default Street Address 2 | default_street_address2 | max_length=80, null=True, blank=True                 | CharField     |
| Default Country          | default_country         | blank_label='Country', null=True, blank=True         | CountryField  |
| Default Post Code        | default_postcode        | max_length=20, null=True, blank=True                 | CharField     |
| Default Town or City     | default_town_or_city    | max_length=40, null=True, blank=True                 | CharField     |
| Default County           | default_county          | max_length=80, null=True, blank=True                 | CharField     |

#### The Address Model

| _Title_          | _Key in DB_ | _Form Validation type_                                                                                    | _Data Type_   |
| -----------------| ----------- | ----------------------------------------------------------------------------------------------------------| ------------- |
| User Profile     | userprofile     | UserProfile, on_delete=models.CASCADE, null=True, blank=True, editable=False, related_name="addresses | ForeignKey    |
| Address Number   | address_number  | max_length=32, null=False, editable=False                                                             | CharField     |
| Full Name        | full_name       | default='', max_length=50, null=False, blank=False                                                    | CharField     |
| Street Address 1 | street_address1 | max_length=254                                                                                        | CharField     |
| Street Address 2 | street_address2 | max_length=254                                                                                        | CharField     |
| Town or City     | town_or_city    | max_length=254                                                                                        | CharField     |
| County           | county          | max_length=254                                                                                        | CharField     |
| Country          | country         | blank_label="Country *",default = 'UK', null=False, blank=False                                       | CountryField  |
| Post Code        | postcode        | max_length=254                                                                                        | CharField     |
| Phone Number     | phone_number    | default='', max_length=20, null=False, blank=False                                                    | CharField     |

#### The Workshop Model

| _Title_        | _Key in DB_    | _Form Validation type_                     | _Data Type_ |
| -------------- | ---------------| ------------------------------------------ | ----------- |
| Message_Number | message_number | max_length=32, null=False, editable=False  | CharField   |
| User Email     | user_email     | (max_length=254)                           | EmailField  |
| Subject        | subject        | max_length=254, null=True, blank=True      | CharField   |
| Message        | message        |                                            | TextField   |

## Technologies 

### Languages

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)

### Libraries

- [Bootstrap](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
- [Django](https://www.djangoproject.com/)
- [Font Awesome](https://fontawesome.com/icons)
- [Google Fonts](https://fonts.google.com/)
- [JQuery](https://jquery.com)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [Stripe](https://stripe.com/gb)

### Tools

- [Git](https://github.com/)
- [Heroku](http://www.heroku.com)
- [Figma](https://Figma.com/)
- [Gitpod](https://gitpod.io/workspaces/)

### Databases:

- [PostgreSQL - Production](https://www.postgresql.org/)
- [SQlite3 - Development](https://www.sqlite.org/index.html)

## Testing

Testing information can be found [here](https://github.com/OGMyst/Heavenly-Herb-Company/blob/master/TESTING.md).

## Deployment

### Instructions
  1. Download a copy of this repository from the link https://github.com/OGMyst/Heavenly-Herb-Company as a download zip file. Or at your terminal do the following git command:

      ```
      $ git clone https://github.com/OGMyst/Heavenly-Herb-Company 
      ```
  2. If you downloaded the project as a zip file, unzip it and add it in your directory.
  3. To not run in some unexpected behaviours during development, a virtual environment is advised to be used before the project be installed in your machine. So create a virtual environment with the command:

      ```
     $ python -m venv venv
      ```
 4. After you already created the virtual environment folder you need to activate it:

      ```
      $ source venv/bin/activate
      ```
5. Install requirements.txt file.

      ```
      $ pip install -r requirements.txt
      ```
6. Create a Stripe account
7. Create and setup an S3 bucket 
8. Create a file called "env.py" and store your: 
- **SECRET_KEY** variable
- **DATABASE_URL** 
- **STRIPE_PUBLIC_KEY**
- **STRIPE_SECRET_KEY**
- **STRIPE_WH_SECRET** 
- **AWS_ACCESS_KEY_ID** 
- **AWS_SECRET_ACESS_KEY** 
- **EMAIL_HOST_USER** 
- **EMAIL_HOST_PASS**

9. Add a git ignore file to not submit sensitive data to Github repository.

     ```
     $ touch .gitignore
     ```
     - Then add the `env.py` to the `.gitignore` file.

     ```
     $ git update-index --assume-unchanged env.py
     ```
     - Depending where the the `env.py` is locate the path will change.

### Deployment to Heroku

To make the deployment of this application to `Heroku` you will need to do the following steps.

1. Signup for [Heroku](https://signup.heroku.com/)
2. Install [Heroku-CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. After installing `Heroku toolbelt` add the following code into your termial and login into your account you already create.
     ```
     $ heroku login
      Enter your Heroku credentials.
      Email: your@email.com
      Password (typing will be hidden):
      Authentication successful.
     ```
4. Save all the requirements into the `requirements.txt` as mentioned before with the command:
     ```
     $ pip freeze > requirements.txt
     ```
5. Create a file named `Procfile` and add the following config.
     ```
     web: python app.py
     ```
6. After all the setup is done `git add .`, `git commit` and `git push` your application to a repository you created on Github.
7. In your `Heroku`account click new and create new app.
8. Select your region and create a name for your project.
9. In your `Heroku` settings click `reveal config vars`.
10. Add the following config variables:

- **SECRET_KEY** variable
- **DATABASE_URL** 
- **STRIPE_PUBLIC_KEY**
- **STRIPE_SECRET_KEY**
- **STRIPE_WH_SECRET** 
- **AWS_ACCESS_KEY_ID** 
- **AWS_SECRET_ACESS_KEY** 
- **EMAIL_HOST_USER** 
- **EMAIL_HOST_PASS**
- **USE_AWS** = True  

11.  After adding the config into your dashboard add the following commands.
  - `$ heroku login`
  - `heroku git:remote -a <your project name>`
  - `$ git push heroku master`

14. On your `Heroku` dashboard click on `open app` button and check if the application is running correctly.

## Credits

### Media

- Responsiveness across devices image from [Techsini](https://techsini.com/multi-mockup).
- All Images used in the site belong to heavenly herb company Ltd.

## Acknowledgements

- The code for the navbar transitioning on scroll came from https://css-tricks.com/styling-based-on-scroll-position/

- I used a lot of code from the Code institute example walkthrough [Boutique Ado](https://github.com/ckz8780/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546) This was to help structure this very large project but also to ensure that processes like logging in and making payments are secure and well tested, particularly since in the long term this site is going to go live. The site is very personalised and features lots of functionality not covered in the course. 
