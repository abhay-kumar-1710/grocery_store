# Grocery Store Backend API

This is a RESTful backend API for a Grocery Store application built using Django and Django REST Framework. It supports role-based access for two types of users — **Manager** and **Customer** — with endpoints for product management, wishlist, cart, and order processing.

## Hosted URL

Base URL: [`https://memoriescollection.pythonanywhere.com/api/`](https://memoriescollection.pythonanywhere.com/api/)

---

## User Roles

- **Manager**  
  Can manage products and view sales reports.
- **Customer**  
  Can view products, manage wishlist/cart, and place orders.

### Registration & Authentication

Users must register using:
- `username`
- `password`
- `role` (Choose either `"customer"` or `"manager"`)

Authentication is required to access all endpoints expect products. Use token-based authentication (JWT) in this project.

##  API Endpoints

### 1.  User Registration & Login

-- **For Registeration**
   `POST /register/`
   → URL - "https://memoriescollection.pythonanywhere.com/api/register/"

-- **For Login And Refresh Token**
   `POST /token/`
   → URL - "https://memoriescollection.pythonanywhere.com/api/token/"
   `POST /token/refresh/`
   → URL - "https://memoriescollection.pythonanywhere.com/api/token/refresh"

### 2. Products (Accessible by All Users)

- **View All Products**  
  `GET /products/`  
  → Lists all available products (open to both customers and managers)
  → URL - "https://memoriescollection.pythonanywhere.com/api/products/"

### 3. Manager-Only Features

> Only users with role `manager` can access the following:

- **Add Product**  
  `POST /products/`  
  → Add a new product
  → URL - "https://memoriescollection.pythonanywhere.com/api/products/"

- **Update Product**  
  `PUT /products/<product_id>/`  
  → Update an existing product
  → URL - "https://memoriescollection.pythonanywhere.com/api/products/<product_id>/"

- **Delete Product**  
  `DELETE /products/<product_id>/`  
  → Delete a product
  → URL - "https://memoriescollection.pythonanywhere.com/api/products/<product_id>/"

- **Sales Report**  
  `GET /products/sales_report/`  
  → View sales report (with product count of how many times bought)
  → URL - "https://memoriescollection.pythonanywhere.com/api/products/sales_report/"

### 4. Customer-Only Features

#### Wishlist

- **View Wishlist**  
  `GET /wishlist/`
  → View wishlist of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/wishlist/"
- **Add to Wishlist**
  `POST /wishlist/`
  → Add wishlist of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/wishlist/"
    
  Body:
  ```json
  {
    "user": <user_id>,
    "product": <product_id>
  }
  
#### Add to Cart

- **View Cart**  
  `GET /cart/`
  → View cart of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/cart/"
- **Add to Cart**
  `POST /cart/`
  → Add Cart of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/cart/"
    
  Body:
  ```json
  {
    "user": <user_id>,
    "product": <product_id>,
    "quantity": <number_of_quantity>,
  }

#### Orders

- **View Orders**  
  `GET /orders/`
  → View Orders of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/orders/"
- **Post Orders**
  `POST /orders/`
  → Add Orders of loggedin user
  → URL - "https://memoriescollection.pythonanywhere.com/api/orders/"
  → This method will add the all products of logged in user to orders and display the bill summary and at the same time logged in user cart products will be deleted.
    
  Body:
  ```json
  {}
