# Z Padel
Z Padel is a B2C business selling padel equipment to padel tennis players. We have products from all the major padel brands so the user is able to find the correct equipment. We sell everything from rackets to cloth and have a lot of different sizes to fit everyone.

This website can not be used as a template for a business since it's a project for educational purposes.

Live website: [Z Padel](https://z-padel.herokuapp.com/)

<img width="1024" alt="responsivee" src="https://user-images.githubusercontent.com/85236391/150960476-622e86e2-2a3b-4ac4-9974-d2179d0dbb74.png">

## Table of Contents

* [UX (User Experience)](#ux-user-experience)
  * [Target Audience](#target-audience)
  * [Business Goals](#business-goals)
  * [User Stories](#user-stories)
  * [Site Owner Goals](#site-owner-goals)
* [Scope](#scope)
* [Structure](#structure)
  * [Database Schema](#database-schema)
* [Design](#design)
  * [Fonts](#fonts)
  * [Colors](#colors)
  * [Wireframe](#wireframe)
* [Technologies](#technologies)
  * [Languages](#languages)
  * [Frameworks and Tools](#frameworks-and-tools)
  * [Contrast Checker](#contrast-checker)
* [Features](#features)
* [Testing](#testing)
  * [Test User Stories](#testing-user-stories)
  * [Functionality](#functionality)
  * [Code Validation](#code-validation)
  * [HTML](#html)
  * [CSS](#css)
  * [Python](#python)
  * [Security](#security)
  * [Different Screen Size](#different-screen-size)
  * [Issues found during site development](#issues-found-during-site-development)
* [Deployment](#deployment)
  * [Heroku](#heroku)
  * [AWS S3](#aws-s3)
  * [Cloning](#cloning)
* [Credits](#credits)

## UX (User Experience)

### Target Audience

The target audience for this site are for people who want to be able to buy padel equipment to a good price. It's easy for shoppers to read reviews from real customers on each product to really be sure the product is good or not. The site target all kind of people, it doesn't matter if you are an experienced padel player or if you just started your journey. Everyone is welcomed.

### Business Goals

* To provide a navigable site that can entice users to shop.
* Have a secure and trustworthy payment solution
* Connect customers to our social media platforms.

### User Stories

* As a shopper
  * I can view a different kind of products so that I can select something to buy
  * I can see individual product details so that I can take a closer look on price, information, pictures and different sizes
  * I can easy see how much the current shopping bag will cost so that I can see if I can afford everything
  * I can select size and quantity of product so that I can choose the correct size and how many I want to buy
  * I can see what I have in my shopping bag so that I can see how much I will spend on my purchase
  * I can change the quantity of individual items in my bag so that I can easy make a change to the products before checkout
  * I can enter my credit card so that I can pay for my items
  * I can get an order confirmation after purchase is successful so that I can see so everything is correct
  * I can get a email confirmation on my purchase so that I can know that my order was completed successful
  * I can read reviews about different products so that I can decide if this product is good or bad

* As a user
  * I can register for an account so that I can have a personal account
  * I can log in and out of my account so that I can access my private account
  * I can recover my password if i forget it so that I can get back in to my account
  * I can have a personalized profile so that I can see my old order history
  * I can search for different products so that I can find what I'm looking for
  * I can choose a specific category of product so that I can easily find the best product in that category
  * I can review a product so that other people can get better information about a product

### Site Owner Goals
* As a site owner
  * I can add a product so that I can update with new items
  * I can edit a product so that I can change product price, descriptions and other criteria
  * I can delete a product so that I can remove it from the store and it will no longer be able to purchase
  * I can see all bookings made on the site

* I planned the project [here](https://github.com/andrezeitz/z-padel/projects/1)

## Scope

The following features are must have for this site to function, and are correlated to the user stories above. Any features that are not included are optional and can be added later.

* Secure payment method
* Secure authentication
* Search for a product
* View products in cart
* Different size options
* User sign up and login
* User profile
* User order history.
* Save user profile information
* Clear and fully responsive design
* Full admin access
* Add, edit and delete product as admin
* Review a product

## Structure
Below is a description of the structure of the site. Note: The navbar and footer are included on all templates.

### Database Schema
<details>
<summary>Details</summary>
<br>

![Skärmavbild 2022-01-27 kl  11 46 32](https://user-images.githubusercontent.com/85236391/151344880-68b262f5-cb24-49e2-8773-8d244bd03e9f.png)
</details>

### User Model
The user model used for this site comes from django.contrib.auth.models

During development, the database used was SQLite which is the default database for Django. Once the site was deployed to Heroku, the database was migrated to PostgreSQL.

### Home App

#### HTML

index.html
* This is the home page of the site, it displays a big hero picture, our most visited categories with links to them, a mailchimp email subscription to our newsletter and reviews from some customers.

### Product App

#### HTML

products.html
* This is the main page for all products, user can filter this page with categories or search to easier find the product they are looking for.

product_detail.html
* This is the more detailed product page for each product. Here you can see more information about the product, add it to the cart and also write reviews about the product.

add_product.html
* This page is only for admin to be able to add new products to the database.

edit_product.html
* This page is only for admin to be able to edit a product from the database.

#### Models

Category
* It stores the categories for the products.
```
name = models.CharField(max_length=254)
friendly_name = models.CharField(max_length=254, null=True, blank=True)
category_text = models.TextField(null=True, blank=True)
```

Product
* It stores all the products.
```
category = models.ManyToManyField('Category', blank=True, related_name='categories')
sku = models.CharField(max_length=5, null=False, unique=False)
name = models.CharField(max_length=254)
slug = models.SlugField(max_length=50, null=False, unique=True)
description = models.TextField()
price = models.DecimalField(max_digits=6, decimal_places=2)
cloth_size = models.BooleanField(default=False, null=True, blank=True)
shoe_size_man = models.BooleanField(default=False, null=True, blank=True)
shoe_size_woman = models.BooleanField(default=False, null=True, blank=True)
image = models.ImageField(null=False)
```

Review
* It stores the reviews for each product.
```
user = models.ForeignKey(User, on_delete=models.CASCADE)
product = models.ForeignKey(Product, on_delete=models.CASCADE, default=True)
comment = models.TextField(max_length=250)
rate = models.IntegerField(default=0, null=True)
created_at = models.DateTimeField(auto_now_add=True)
```

### Bag App

#### HTML

bag.html
* This is the page for the cart. Each item added will displayed here where you also will be able to update or delete a product. Users can also continue securely to checkout.

### Checkout App

#### HTML

checkout.html
* This is the page for the checkout. It's the final step before the user can pay for their products. It shows all the products added and total price. It also ask the user for billing information which will be stored in the database for future use. There's a stripe input that will take the credit card information. It also has a button to pay.

checkout_success.html
* This page displays a success message after the user has successfully paid for their products. It also displays the order number, order date, the products and price.

#### Model
Order
* It stores the order information of each order and is created when the user completes the checkout.
```
order_number = models.CharField(max_length=32, null=False, editable=False)
user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
full_name = models.CharField(max_length=50, null=False, blank=False)
email = models.EmailField(max_length=254, null=False, blank=False)
phone_number = models.CharField(max_length=20, null=False, blank=False)
postcode = models.CharField(max_length=20, null=False, blank=False)
city = models.CharField(max_length=40, null=False, blank=False)
street_address = models.CharField(max_length=80, null=False, blank=False)
date = models.DateTimeField(auto_now_add=True)
delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
original_bag = models.TextField(null=False, blank=False, default='')
stripe_pid = models.CharField(max_length=254, null=False,
blank=False, default='')
```

OrderLineItem
* Contains information about each product that's added to the cart.
```
order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
product_size = models.CharField(max_length=2, null=True, blank=True)
quantity = models.IntegerField(null=False, blank=False, default=0)
lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
```

### Profiles App

#### HTML

profiles.html
* Displays the user's profile. It shows the users billing information and their previously orders.

admin.html
* This page is only for admin. It displays all orders made on the site with order number, name, email, phone number and the products.

#### Model

UserProfile
* Securely stores the user's billing information. It's used to store the user's billing information and pass it to the checkout form to speed up the purchase process.
```
user = models.OneToOneField(User, on_delete=models.CASCADE)
default_full_name = models.CharField(max_length=254, null=True, blank=True)
default_phone_number = models.CharField(max_length=20, null=True, blank=True)
default_street_address = models.CharField(max_length=80, null=True, blank=True)
default_postcode = models.CharField(max_length=20, null=True, blank=True)
default_city = models.CharField(max_length=40, null=True, blank=True)
```

## Design

### Fonts
I have chosen Lato for the headers as it is easy to read and has sufficient contrast to the main body font. Roboto for all other text.

### Colors
The site features complementary Azure, Davys Grey, Cadet Blue Crayola, white and black to create a good contrast and improve readability.

The colors chosen are:

![colorss](https://user-images.githubusercontent.com/85236391/150809793-160855e7-24e8-49a8-ba18-1850c920295b.png)

### Wireframe

#### Desktop

<img width="698" alt="WEB" src="https://user-images.githubusercontent.com/85236391/147922980-ef5683d9-9647-4777-9a3e-68ec68b2da39.png">

#### Mobile

<img width="696" alt="MOBILE" src="https://user-images.githubusercontent.com/85236391/147923016-761bbe79-8b11-4963-b383-79cc32be64f2.png">

## Technologies

### Languages
* HTML
* CSS
* Python
* JavaScript

### Frameworks and Tools
* [GitHub](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Django](https://www.djangoproject.com/)
* [Heroku](https://www.heroku.com/home)
* [jQuery](https://jquery.com/)
* [Postgres](https://www.postgresql.org/)
* [Bootstrap](https://www.bootstrap.com/)
* [AWS](https://aws.amazon.com/)
* [Google Fonts](https://fonts.google.com/)
* [Font Awesome](https://fontawesome.com/)
* [W3C HTML Validation](https://validator.w3.org/)
* [H3C CSS Validation](https://jigsaw.w3.org/css-validator/validator.html.en)
* [PEP8](http://pep8online.com/)
* [Am I responsive](http://ami.responsivedesign.is/)
* [WebAim](https://webaim.org/resources/contrastchecker/)

### Contrast Checker
All colors was checked in a contrast checker and pass the test.

![contrastcheck](https://user-images.githubusercontent.com/85236391/150809931-5dcd34eb-937d-4bd4-8945-cc9ab872a7c3.png)

## Features
The website has the following features:

### Navigation bar

* The navbar is included on all templates. On the desktop version the logo is located at the top center and take the user to the home page if clicked. The navbar has a search bar to the left for quick access to specific products and to the right is a profile dropdown menu and the cart. The profile dropdown show the name of the user if logged in and the font awesome icon will change color from black to blue. The cart will show the shopper how many items in the cart and also the total price for all of them. The font awesome icon will change to green when there is something in the cart. All the links have a black font colour and a blue under border colour when hovered over which match the colour scheme of the site. Each link within the navbar are linked to all the correct product categories.

<img width="1013" alt="Skärmavbild 2022-01-25 kl  11 36 11" src="https://user-images.githubusercontent.com/85236391/150961180-e9b0e335-9690-438c-977a-27f2f694d136.png">

* On the mobile version the home logo have been changed to a home font awesome icon to fit better, search and profile buttons work as dropdown. On the left is a dropdown list for all product categories and to the right is still the cart.

<img width="482" alt="Skärmavbild 2022-01-25 kl  11 36 47" src="https://user-images.githubusercontent.com/85236391/150961192-918da63f-158e-437d-8a83-718e934e2253.png">

### Toast

* Toast message will be displayed when you add, edit and delete a product. It will also show a success message when logged in/out or add a new product.

![Skärmavbild 2022-01-25 kl  14 47 12](https://user-images.githubusercontent.com/85236391/150988795-3bf9756d-dcf4-471a-8664-ba83fc399515.png)
![Skärmavbild 2022-01-25 kl  14 47 33](https://user-images.githubusercontent.com/85236391/150988801-8b5271a7-2189-48ce-a6a3-e6472328c4ea.png)
![Skärmavbild 2022-01-25 kl  14 47 47](https://user-images.githubusercontent.com/85236391/150988807-bf782e2c-d572-41be-ac52-52d5db060f39.png)

### Home

* The home page is displayed with a big hero picture of a padel rack to let the customer really understand what kind of website it is. Under the picture is our "Most visited category". It displays 3 big pictures that work like buttons and will expand and get a bit darker when hovering over them. The categories are Padel racks, padel balls and padel shoes. After that is a email subscription field that let user subscribe to our newsletter. Last is 3 different reviews from customers that like the site.

![Skärmavbild 2022-01-25 kl  14 36 03](https://user-images.githubusercontent.com/85236391/150986900-c504cc52-8d9e-4dc0-96c0-1547fd9e0a85.png)
![Skärmavbild 2022-01-25 kl  14 36 13](https://user-images.githubusercontent.com/85236391/150986915-ba46fd5d-bc09-4d41-92a9-1da1eadb10d5.png)

### Products

* Each product category page has its own information on the top of the page. First there is bredcrumb to each navigate on the site. On the right side there is a "Sort By" button that works as a dropdown to let the shopper sort the products after price low to high or high to low. They can also sort for oldest to newest or newest to oldest product. Under is the products displayed with picture, name and price. The pictures work as a link to the specific product.

From categories:
![Skärmavbild 2022-01-25 kl  14 37 03](https://user-images.githubusercontent.com/85236391/150987022-ae0fb412-865e-4742-8400-7626116ca2d0.png)

From search:
![Skärmavbild 2022-01-25 kl  14 37 45](https://user-images.githubusercontent.com/85236391/150987244-607649bd-39d8-47af-93d5-22bb5e25f879.png)

### Product Details

* On the top left side there will still be breadcrumb so the shopper can easy go back to the category page they just came from. Under it will be a big picture of the product. On the right side is the name and price once again and also a quantity box so the shopper can choose how many products they would like to buy. If the product has sizes it will be displayed as well. Under there is a box "Buy now" button to add the product to the cart and some additional description about the product. On the bottom of the page is a review text box that will let the customers review the product with a text and choose between 0-5 stars. After the review is saved it will be showed under with the profile name, date of the review, how many stars and the text. You will have to be logged in to be able to write a review. If you are not logged in the "save" button will not be visible and instead ask the customer to login with a link to the login page.

![Skärmavbild 2022-01-25 kl  14 40 31](https://user-images.githubusercontent.com/85236391/150987578-a2148ba0-1000-459f-9c36-55888498753b.png)

### Cart

* Inside of the cart the shopper will see all the products added to the cart. They will be able to change the quantity easy by just change number in the quantity box and press the update button. If they would like to delete a product from the cart they can easily do so by clicking on the red trash can. On the right side is a cart summary with the total price, sub price and delivery cost. If the shopper still hasn’t come up to free delivery a red text will be displayed and say how much more they will have to shop to get free delivery. Finally there is a support phone number if the shopper has any problem and a big "Checkout" button that will only be displayed if there is something in the cart.

<img width="1130" alt="Skärmavbild 2022-01-25 kl  12 36 34" src="https://user-images.githubusercontent.com/85236391/150972477-c2ae2086-51a3-4846-9314-412ee32ed827.png">

### Checkout

* The checkout page is the last step for the shopper. On the left side is all the field the shopper will need to fill out to complete the order. If the customer is logged in once they have completed this step the information will be stored in the profil for later purchases. Under is the card details field that will be required to checkout. If the card details is wrong a red text will be displayed to let the customer know something is wrong. On the right side is all the products and a summary of sub total, delivery and total price.

<img width="1136" alt="Skärmavbild 2022-01-25 kl  12 48 59" src="https://user-images.githubusercontent.com/85236391/150972430-02ee17c7-a24b-4c67-898b-9d4813e718ed.png">

### Checkout Success

* The checkout success is a simple page displaying your last order. It will show on what date you did the order, your order number and which products you ordered. On the bottom it will show where the order will be shipped and how much the total order was. This page will also be able to display again later if you was logged in when the order was made since all order will be saved in your profile.

<img width="777" alt="Skärmavbild 2022-01-25 kl  13 26 57" src="https://user-images.githubusercontent.com/85236391/150977273-9c135baf-bf8f-47b7-a016-b513d7900242.png">

### Email confirmation

* After each order made you will receive a order confirmation by email aswell. It will look like this:

<img width="687" alt="Skärmavbild 2022-01-25 kl  13 31 01" src="https://user-images.githubusercontent.com/85236391/150977447-fbb3334d-037f-465b-a75e-76e3822e6466.png">

### Profile

This page is only for users. Inside your profile you will see on the left field where you can update your personal information. If you already have made a purchase the field will already have saved your information. If you would like to update any you can do so by clicking on the "Update Profile" button. On the right side you will see all orders you have made. If you click on the order number you will see a more detailed page with your order.

<img width="1142" alt="Skärmavbild 2022-01-25 kl  13 34 59" src="https://user-images.githubusercontent.com/85236391/150978292-f2caf6bd-ebc3-46ca-a1a8-d09e1687f2eb.png">

### Admin Profile

This page is only for admin instead of the profile page. It will display all orders made from the site with booking number, date, full information about the user and the items ordered.

![Skärmavbild 2022-01-26 kl  00 10 21](https://user-images.githubusercontent.com/85236391/151147416-1b986eae-7701-48cd-ac23-6de24edf5515.png)

### Product Management 

This page is secured only for admin to access from the profile dropdown. Here you can easy add new products to the database. When you are logged in as Admin you will also see a edit and delete button on each product to be able to edit or delete them.

Add product page:

![Skärmavbild 2022-01-25 kl  14 43 24](https://user-images.githubusercontent.com/85236391/150988077-68e03ff1-f1d0-47fb-94c7-676f08e1fcfa.png)

Edit and delete buttons form admin on each product:

<img width="296" alt="Skärmavbild 2022-01-25 kl  13 45 22" src="https://user-images.githubusercontent.com/85236391/150979358-0927d976-c2ed-48b1-bc4e-8d0289bda436.png">

### Footer

The footer is sticky on the bottom of all pages. It display our facebook page, contact information, shipping details and privacy policy.

![new footer](https://user-images.githubusercontent.com/85236391/151232271-73c34dad-65e2-4bed-a426-7fdfdb344c1c.png)

### 403, 404 and 500 error pages

This page will be displayed from the templates folder when matching error occurs.

![Skärmavbild 2022-01-26 kl  15 49 48](https://user-images.githubusercontent.com/85236391/151186987-e6adc4b9-9071-4b04-ab7e-f62eae8dc2bd.png)

### Email Provider

I use SendGrid as email provider to be able to send out the verification email and the confirmation email after a user has made an order.

### Webhooks from Stripe

I use webhooks from Stripe and everyone is working and showing a 200 status messages.

![Skärmavbild 2022-01-27 kl  12 06 35](https://user-images.githubusercontent.com/85236391/151347018-4a3cac37-3b11-4ac3-b25a-4d34b19b414a.png)

### Facebook Page

I created a facebook pages called Z Padel and it's live right now and connected inside the footer. If the page would be deleted since it's not a real business I will post a print here.

<img width="1554" alt="facebook sida" src="https://user-images.githubusercontent.com/85236391/151178485-93f28df9-4e13-4d20-a5a9-f0755f9236e9.png">

## Testing

My testing was continuous through this build and not just all in one go at the end. See below for my validation testing results which I carried out when my code was finished, but all through my development as I came across various issues and challenges I was testing, updating and committing my code to make things work they way they should.

### Testing User Stories
As a shopper:

1. I can view a different kind of products so that I can select something to buy
  * Result: TEST PASSED 
2. I can see individual product details so that I can take a closer look on price, information, pictures and different sizes
  * Result: TEST PASSED
3. I can easy see how much the current shoppingbag will cost so that I can see if I can afford everything
  * Result: TEST PASSED
4. I can select size and quantity of product so that I can choose the correct size and how many I want to buy
  * Result: TEST PASSED
5. I can see what I have in my shoppingbag so that I can see how much I will spend on my purchase
  * Result: TEST PASSED
6. I can change the quantity of individual items in my bag so that I can easy make a change to the products before checkout
  * Result: TEST PASSED
7. I can enter my credit card so that I can pay for my items
  * Result: TEST PASSED
8. I can get an order confirmation after purchase is successful so that I can see so everything is correct
  * Result: TEST PASSED
9. I can get a email confirmation on my purchase so that I can know that my order was completed successful
  * Result: TEST PASSED
10.  I can read reviews about different products so that I can decide if this product is good or bad
  * Result: TEST PASSED

As a user:

1. I can register for an account so that I can have a personal account
  * Result: TEST PASSED 
2. I can login and out of my account so that I can access my private account
  * Result: TEST PASSED 
3. I can recover my password if i forget it so that I can get back in to my account
  * Result: TEST PASSED 
4. I can have a personalized profile so that I can see my old order history
  * Result: TEST PASSED 
5. I can search for different products so that I can find what I'm looking for
  * Result: TEST PASSED 
6.  I can choose a specific category of product so that I can easily find the best product in that category
  * Result: TEST PASSED 
7. I can review a product so that other people can get better information about a product
  * Result: TEST PASSED

As a site owner
1. I can add a product so that I can update with new items
  * Result: TEST PASSED 
2. I can edit a product so that I can change product price, descriptions and other criteria
  * Result: TEST PASSED 
3. I can delete a product so that I can remove it from the store and it will no longer be able to purchase
  * Result: TEST PASSED
4. I can see all bookings made on the site
  * Result: TEST PASSED

### Functionality

#### Home Page
* All the correct images are connected to the correct products.
* The pictures are responsive and change to a mobile version when the screen is too small.
* The mailchimp subscription is responsive and change to a mobile version when the screen is to small.
* Site reviews are responsive and have the correct review stars.

#### Product Page
* Image is connected to the correct products.
* All the correct information is displayed.
* All products are responsive and get fewer colums on smaller screens.
* When searched in the search bar the correct search fiels show up to display what they search for.
* All categories is connected to the correct category text.
* Sort by is working when customer comes from categories or search.

#### Product Details Page
* All the correct information is displayed.
* The product details page is responsive and changes to a mobile version when the screen is too small.
* All breadcrumb are correct for each product.
* When clicking the "Buy now" button a toast success message will be visible
* Reviews show reviews from users for that specific product.
* The user can only leave a review if they are logged in.
* The user need to write something in the review box but can choose 0-5 stars.
* If there are no reviews the review topic will be hidden.

#### Cart Page
* Total adds correctly if more than on product is added.
* The cart page is responsive and changes to a mobile version when the screen is too small.
* The "Checkout" button leads the user to the checkout page.
* The "Continue shopping" button leads the user to the home page.
* The "Update" button update the quantity of each product.
* The "Remove" button removes the product from the cart.
* Toast messages will show when products are updated or removed.
* When no products are in the cart there is a text saying there are no products in the cart and checkout button is not visible.

#### Checkout Page
* The checkout page is responsive and changes to a mobile version when the screen is too small.
* The order summary is correct and displays the correct information.
* Checkout form is correctly displayed to the user and auto fills the correct information if it was saved to the database.
* Default stripe card is used for payments and have no issues.
* Payment won't be processed if the form is not filled out correctly, errors will be displayed.
* Payment won't be processed if the card details are incorrect, errors will be displayed.
* The "Back to bag" button leads the user to the cart page.
* The "Checkout" button leads the user to the checkout success page.

#### Checkout Success Page
* The correct information is displayed.
* The user will see a button that will redirect to the home page.
* If the user is coming from the profile page the user will see a button that will redirect to the profile page.
* If the admin checking the order from the admin profile page the admin will see a button to take him back to all orders.

#### Profile Page
* The profile page is responsive and changes to a mobile version when the screen is too small.
* The correct information is displayed.
* Updated information is saved to the database and displayed the next time the user goes to the checkout page.
* All orders the user have made will be saved in order history.
* Order number is clickable and will display the detailed order.

#### Admin Profile Page
* The correct information is displayed.
* All bookings is showed here with the correct name, email and phone numbers.
* Order number is clickable and will let the admin see the full order.

### Error Pages
* I only test the 404 page but the structure is the same as the other pages and they're all in the right directory.
* The "Go back" button leads the user to the home page.

#### Add/Edit Products
* The correct form is displayed for each page.
* Removing an image will remove the image from the product.
* Adding an image will add the image to the product.
* Cancel button will lead the user to the home page.
* Save button will save the product to the database.

#### Sign Up / Login Page
* The correct form is displayed for each page.
* The sign up form allows the user to sign up using their email and password.
* The user will receive a confirmation email to connect the email.
* The user is able to get a new password in there email if they forget it.
* The login form allows the user to login using their email and password.
* The user can only sign up if the email is not already in use.

#### The Navigation Bar
* The nav bar is fixed to the top of the screen and is always visible.
* The nav bar is responsive and will change to a mobile version when the screen is too small.
* All links in the nav bar are connected to the correct pages.
* The drop down menus are responsive and are always visible.
* The search bar is responsive and functional.
* All links change bottom border color when hovered over them.

#### The Footer
* The footer is fixed to the bottom of all content.
* Facebook and privacy link in the footer is connected to the correct pages.
* The footer is fully responsive and will change to a mobile version when the screen is too small.

### Code Validation

### HTML
The W3C Markup Validation Service was used to validate the HTML page of the project. No errors or warnings to show.

![Skärmavbild 2022-01-26 kl  12 53 12](https://user-images.githubusercontent.com/85236391/151158655-97dedce0-6cee-4918-b9c1-762fad8b745f.png)

### CSS
The W3C CSS Validation Service was used to validate the CSS file used for the project. No errors or warnings to show.

![Skärmavbild 2022-01-26 kl  12 51 23](https://user-images.githubusercontent.com/85236391/151158486-4abfd1c1-cfa0-4716-aeaa-c5331d8271e1.png)

### Python
The PEP8 Online Check was used to validate all Python code. No errors or warnings to show

PLEASE NOTE: Warnings and errors were given on most pages due to template logic being used. Certain files failed PEP* due to base code set by Django.

### Security
All pages were tested with a basic account without any special permissions to make sure that no special features were available. Attempt to access a page that requires special permissions will result in a 403 error or a redirect to the login page.

### Different Screen Size
The site is optimized for all screen sizes and tested with a Macbook Pro 13" and iPhone 13 Pro.
I use media queries to make everything look and feel good on mobile devices.

### Issues found during site development

1. I had a problem to get the slug-field to work properly on all pages. When I tried to add it from a current categories it would work from all category pages but not the search page.

##### Solution:

Instead of just using the product_details view to display the slug I made a function inside of the product models that look like this.

<img width="479" alt="Skärmavbild 2022-01-25 kl  13 48 08" src="https://user-images.githubusercontent.com/85236391/150979864-489835fa-f13f-4c86-bc9b-c6af5f50183a.png">

2. I had this problem where "sum" was not defined.

<img width="391" alt="NameError at checkout" src="https://user-images.githubusercontent.com/85236391/150980102-bcee1a35-ea65-496f-b7c1-573d4332d064.png">

##### Solution:

Import sum inside checkout.models

3. If delivery was not free it would price the delivery a lot more then expected.
 
![Order number](https://user-images.githubusercontent.com/85236391/150981434-dd500749-f09e-41f7-affc-acf40473adcc.png)

##### Solution:

Found the bug in checkout.models that I had put * 10 to the total amount when it should be divided by 100 to calculate the correct delivery fee.

Wrong:

![def update total(self)](https://user-images.githubusercontent.com/85236391/150981504-e205c8a9-e228-4174-be3e-fb3f7dab457e.png)

Correct:

<img width="592" alt="Skärmavbild 2022-01-25 kl  14 01 33" src="https://user-images.githubusercontent.com/85236391/150981654-933804b0-7449-4eed-80af-d27499ed1f7a.png">

![Skärmavbild 2022-01-27 kl  15 53 15](https://user-images.githubusercontent.com/85236391/151384944-9c4fbf03-7c3d-47e2-a9d3-18d8e33019bd.png)

4. Problem to connect the webhook to the site and get status 400 message.

![payment_intent created](https://user-images.githubusercontent.com/85236391/150981812-866ed198-86c4-4b4a-80ed-81cd6d86a9a0.png)

##### Solution:

![import env](https://user-images.githubusercontent.com/85236391/150981855-ea38ef3a-d2e5-499e-a48a-f3de7750b4a9.png)

Had to import the env file in to the settings so it would read the secret wh password correct.

5. Problem to get the handle_payment_intent_succeeded to read the billing information and adress from the shopper.

##### Solution

I had the light verion of jQuery so it would not work correct. After adding the full version everything worked perfectly.

## Deployment

Below describes the deployment of the site on Heroku and set up process to store static files and images on AWS.

### Heroku

#### From your browser:

1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser
17. Click on Resources in your Heroku app.
18. In the add-ons field search for Heroku Postgres and press submit.

The program is set to be deployed automatically after each push from gitpod.

#### From IDE:

1. In the consolse type pip install dj_database_url and psycopg2-binary to be able to use the postgres database.
2. Add the new dj_database_url in setting.py
3. Comment out the existing sqlite3 database.
4. Login to Heroku using the command line by typing heroku login -i
5. Once logged in you will need migrate the models to the postgres database.
6. You will now need to create a new superuser to access the admin side of the site.
7. Install the gunicorn package by typing pip install gunicorn
8. Now you can create your requirements.txt file by typing pip freeze > requirements.txt
9. Create a Procfile file by typing touch Procfile

### AWS S3

#### How to set up AWS S3:
1. Go to AWS and login to your account. If you don't have an account, create one. If you have to create an account be mindful that you will need to enter your card details, no billing will occur unless you go over the free tier limit.
2. After logging in, go to the S3 and create a bucket.
3. Make sure you name your bucket the same as you did for Heroku and choose the nearest region to your location.
4. Scroll down to the "Block Public Access" section and unchecked the "Block public access" checkbox. Confirm that you want to allow access to the bucket. Scroll down to the bottom of the page and click on "Create bucket"

#### Customizing the bucket properties:
1. Click on the Properties tab. Scroll to the end of that page and click on edit button.
2. At the top it will allow you to choose between "Enable" and "Disable" static website hosting. Choose Enable.
3. The section below will allow you to select "Host a static website", Select "Host a static website" and then scroll down to the index "Document inputs"
4. In the input field, enter the home file which is the "index.html" file and in the error field, enter "error.html".
5. Leave the redirection rules empty and click on "Save changes".

#### Setting up the Permissions
1. Next, go to the permissions tab. Scroll down to the bottom of the page and click edit the "Cross-Origin Resource Sharing (CORS)" section.
2. Add the following lines:
```
[{
  "AllowedHeaders": ["
  Authorization"
  ],
  "AllowedMethods": [
    "Get"
    ],
  "AllowedOrigins": [
    "*"
    ],
  "ExposeHeaders": [],
}]
```
3. Save the changes. Navigate to "Bucket Policy" section and click "edit".

#### Generating A Bucket Policy
1. Click on the "Policy Generator" button. Select "S3 Bucket Policy" from the dropdown list.
2. You will need to set following permissions:
* Effect – Allow
* Principle - *
* Actions – GetObject, GetObjectAcl, PutObject, PutObjectAcl and DeleteObject
* Amazon Resource Name – This can be found on the previous page, under "Bucket ARN". Copy and paste it into this box
3. After these have been entered, click "Add Statemen" and "Generate Policy".
4. Copy the policy into the bucket policy editor, adding /* onto the end, the click "Save Changes".

#### Access Control List
1. While in the permissions tab, click "edit" under the "Access Control List" section.
2. Next, navigate to "Everyone (public access)" and tick the box on the left, "List" under the "Objects" heading. Tick the box that you understand the effect then click on "Save Changes".

#### Creating A Group and Policy with IAM
1. Next, search for IAM in the search bar at the top, and click on it to set up a group policy.
2. Under "Access Management", Select "User Groups" and create a new group.
3. Give the group a name (try keep it relational to the project name) and click "Create Group".
4. This will bring you to the IAM dashboard. Go to the "Access Management" section, and click on "Policies".
5. Click "Create Policy" and click on the JSON tab, and select "Import Managed Policy".
6. Search for "AmazonS3FullAccess" and select it, then Import".
7. Copy your ARN and place it in the code twice (the second time with /*).
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::YOUR-ARN",
                "arn:aws:s3:::YOUR-ARN/*"
            ]
        }
    ]
}
```
9. Select "Next: Tags", "Next: Review", Enter a name and click on "Create Policy".

#### Attaching the Group Policy
1. Go to "User Groups", under "Access Management". Click on the your newly created group and go over to the "Permissions" tab
2. Select the "Add Permissions" button, and select "Attach Policy".
3. Search for and click on the checkbox next to the policy you have just created, then Select "Add Permissions".

#### Create User for IAM
1. Head back to the IAM dashboard, click on "Users", then "Add User".
2. Choose a name and tick the checkbox to give the user access, then select "Next: Permissions".
3. Select the group to put the user in and keep clicking the next buttons until the very end and click "Create user".
4. Click on “Download .csv” file (Keep this is a secure location as you wont be able to get these details again), as you will not have access to this page again! This file will contain information required as shown in the Heroku table above.

#### Saving Images To S3 Bucket
1. If you need to save images to your S3 bucket, you will need to do the following;
2. Go to the s3 dashboard and click on the bucket you want to save the images to.
3. Click "Create Folder", call it "media" and click the second "Create Folder" button.
4. When you are in this folder, click "Upload", then 'Add Files" or "Add Folder", then "Upload".

### Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

## Credits

* How to modify the toast from [here](https://www.cssscript.com/pure-javascript-library-clean-toast-notifications-prophet-js/)
* How to use many-to-many fields [here](https://docs.djangoproject.com/en/3.2/topics/db/models/#many-to-many-relationships)
* How to use extra fields on many-to-many relationship [here](https://docs.djangoproject.com/en/3.2/topics/db/models/#extra-fields-on-many-to-many-relationships)
* How to create review stars [here](https://www.w3schools.com/howto/howto_css_star_rating.asp)
* How to make breadcrumb with bootstrap [here](https://getbootstrap.com/docs/4.1/components/breadcrumb/)

I would like to give a special thank you to Maria Hynes for her mentorship during this course. She has been a great mentor along the way.
