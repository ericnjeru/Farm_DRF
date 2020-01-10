## DRF_Products example

An example Django REST framework project for test driven development.

### Test Case Scenarios
* Test to verify registration with invalid password.
* Test to verify registration with already exists username.
* Test to verify registration with valid datas.
* Tested API authentication endpoint validations.
* Tested authenticated user authorization. 
* Create a product with API.
* Update a product with API.
* Update a product with API.
* Delete a product with API.
* Get product list for a user.

### API Endpoints

#### Users

* **/api/users/** (User registration endpoint)
* **/api/users/login/** (User login endpoint)
* **/api/users/logout/** (User logout endpoint)


#### Products

* **/api/products/** (product create and list endpoint)
* **/api/products/{product-id}/** (Product retrieve, update and destroy endpoint)

### Install 

    pip install -r requirements.txt

### Usage

    python manage.py test

