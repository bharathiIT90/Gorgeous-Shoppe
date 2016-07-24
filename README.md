# GorgeousShoppe.com
Know more about the developer on <a href="https://www.linkedin.com/in/bharathi-ranganathan">Linkedin</a>

## Table of Contents
- [Introduction](#introduction)
- [Features](#Features)
  - [Front-end](#Front-end)
  - [Back-end](#Back-end)
- [Technologies](#technologies)
  - [Current Features](#Current Features)
  - [Future Enhancements](#Future Enhancements)
- [API Test Function](#API Test Function)
- [Exploration through GorgeousShoppe:](#Exploration through GorgeousShoppe:)
-
## Inroduction

A full stack online shopping web application which allows user to select their desired product, make payment and checkout. When the user logs into the application, they are able to choose the products from a list of products. The products are grouped according to various categories. The user is allowed to apply filters and make their selection. The application allows both guest user and registered user for checking out. The user also has freedom to choose a product from various options under each product. 

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
Python runs the back end of GorgeousShoppe. Django web framework is used to create relations between different applications and databases. AJAX is used for querying the database to update the cart quickly once the quantity and product is updated. Braintree is used for providing payments options using paypal and credit card. 


## API test function
1. Created a cart.<br/>
2. Created a Json cart token.<br/>
3. Generated new url and checkout url using Json token.<br/>
4. An arbitary email is passed as argument in the test case function.<br/>
5. Requested address from the user.<br/>
6. Returned the addresses related to user checkout if addresses already available.<br/>
7. Created an arbitrary user_id.<br/>
8. Updated the checkout url to produce the order details of billing address, shipping address and cart and checkout token.<br/>

## <h2>Exploration through GorgeousShoppe</h2>

<b>Homepage:</b><br/>

![image](https://cloud.githubusercontent.com/assets/16948906/17043326/828485ae-4f6a-11e6-95f1-43b187c862a9.png)

<b>CartView:</b><br/>

<img width="1259" alt="cartview" src="https://cloud.githubusercontent.com/assets/16948906/17046550/83a5df72-4f89-11e6-867f-826ce5adba58.png">

<b>Guest/ Registered-user login:</b>

<img width="1263" alt="guest login" src="https://cloud.githubusercontent.com/assets/16948906/17046606/0f5e9126-4f8a-11e6-963b-e88569b6409f.png">

<b>Product Categories/Filter:</b>

<img width="1259" alt="filters" src="https://cloud.githubusercontent.com/assets/16948906/17046608/11079d24-4f8a-11e6-9dba-04c3071fe4db.png">

<b>Order Summary:</b>

<img width="1259" alt="ordersummary" src="https://cloud.githubusercontent.com/assets/16948906/17046609/1290ea56-4f8a-11e6-8a25-8b7b39fbbcb6.png">
