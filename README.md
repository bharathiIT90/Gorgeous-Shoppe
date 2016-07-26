# GorgeousShoppe.com
Know more about the developer on <a href="https://www.linkedin.com/in/bharathi-ranganathan">Linkedin</a>

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
	- [Current Features](#current-features)
	- [Future Enhancements](#future-enhancements)
- [Technologies](#technologies)
	- [Front-end](#front-end)
	- [Back-end](#back-end)
- [REST API Testing](#rest-api-testing)
- [File Guide](#file-guide)
- [Technical Run](#technical-run)


## Introduction

A full stack online shopping web application which allows user to select their desired product, make payment and checkout. When the user logs into the application, they are able to choose the products from a list of recommended and featured products. The application also gives the priviledge to select from related products to make search process easier. The products are grouped according to various categories and the user can apply filters and make their selection. The application also implements product variations for each product.The application allows both guest user and registered user for checking out. There are two payment option provided- Paypal and credit card. 

## Features
### Current Features
1. Product selection according to different product variation. <br/>
2. Quantity selection and cart updation accordingly. <br/>
3. Tax, shipping and order total calculations. <br/>
4. Product category and price range filters. <br/>
5. Guest User and registered User login. <br/>
6. User Address and payment options. <br/>

### Future Enhancements
1. Improving the front end UI by showing flashy product promotions that change every few seconds. <br/>
2. Updating the product view to display different images for every product variations provided. <br/>

## Technologies
Python, Django framework, sqlite3, AJAX, Jquery, HTML, CSS, Bootstrap, Braintree for payment, Jquery flash messages, Django REST framework.

### Front-end
HTML, custom CSS paired with bootstrap is the main part of the Front end. Flash messages for the cart update is run through Jquery. 

### Back-end
Python runs the back end of GorgeousShoppe. Django web framework is used to create relations between different applications and databases. AJAX is used for querying the database to update the cart quickly once the quantity and product is updated. Braintree is used for providing payments options using paypal and credit card. <br/>
Dependencies are given in Gorgeous-Shoppe/src/requirements.txt.


## REST API Testing 
1. Created a cart.
2. Created a Json cart token.
3. Generated new url and checkout url using Json token.
4. An arbitary email is passed as argument in the test case function.Requested address from the user.
5. Returned the addresses related to user checkout if addresses already available.
6. Created an arbitrary user_id.
7. Updated the checkout url to produce the order details of billing address, shipping address and cart and checkout token.

## File Guide
* <kbd>src/</kbd> Contains the main source code for various application.
* <kbd>src/products/</kbd> Contains the model.py, views.py for the products app.
* <kbd>src/carts/</kbd> Contains the model.py, views.py for the carts app.
* <kbd>src/orders/</kbd> Contains the model.py, views.py for the orders app.
* <kbd>src/manage.py</kbd> Implements the backend Python server using Django Framework.
* <kbd>src/templates/</kbd> Contains all the HTML, CSS and Jquery files.
* <kbd>src/requirements.txt</kbd> Dependencies are provided. 

## Technical Run

<h3> Home Page</h3>
![homepage](https://cloud.githubusercontent.com/assets/16948906/17109637/a94434f6-524d-11e6-9fb1-722dc9772e33.gif)


<h3>Product and Product Variation</h3>
![productview](https://cloud.githubusercontent.com/assets/16948906/17109639/aa621a10-524d-11e6-8164-be2668b70ad8.gif)


<h3>Cart and Cart Updation</h3>
![cart](https://cloud.githubusercontent.com/assets/16948906/17109640/ac3ab50e-524d-11e6-8b8d-6d0d2dbcc2f0.gif)


<h3>Order Summary and Payment Options</h3>
![ordersummary](https://cloud.githubusercontent.com/assets/16948906/17109643/ada6a02e-524d-11e6-8886-87a62958b303.gif)





