# Ecommerce API

📖 **Overview**  
The Ecommerce API is a backend solution designed to manage an e-commerce platform. It provides APIs for handling products, orders, users, and product images, making it easy to integrate with frontend applications.

---

## 📂 **Project Structure**
- **`ecommerce_api/`**: Core Django project files.
- **`products/`**: Manages product-related APIs (CRUD operations).
- **`users/`**: Handles user management, authentication, and authorization.
- **`order/`**: Manages orders and transactions.
- **`product_images/`**: Handles product image storage and retrieval.
- **`db.sqlite3`**: Default database for development purposes.

---

## 🚀 **Features**
- **User Authentication and Authorization**:
  - Token-based authentication.
  - User registration and login.
- **Product Management**:
  - CRUD operations for products.
  - Product categorization.
- **Order Management**:
  - Create, view, and track orders.
- **Image Management**:
  - Upload and retrieve product images.

---

## 🛠️ **Setup Instructions**

### **Prerequisites**
- Python 3.x
- Django
- Django REST Framework

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/Omar-F-Shoman/Ecommerce_API-.git
   cd Ecommerce_API-
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser (optional, for admin access):
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

---

## 🌐 **API Endpoints**

### **Authentication**
- **Login**: `POST /api/auth/login/`
- **Register**: `POST /api/auth/register/`

### **Products**
- **List Products**: `GET /api/products/`
- **Create Product**: `POST /api/products/`
- **Product Details**: `GET /api/products/{id}/`
- **Update Product**: `PUT /api/products/{id}/`
- **Delete Product**: `DELETE /api/products/{id}/`

### **Orders**
- **Create Order**: `POST /api/orders/`
- **List Orders**: `GET /api/orders/`
- **Order Details**: `GET /api/orders/{id}/`

### **Users**
- **User Profile**: `GET /api/users/{id}/`
- **Update Profile**: `PUT /api/users/{id}/`

### **Product Images**
- **Upload Image**: `POST /api/product_images/`
- **Retrieve Image**: `GET /api/product_images/{id}/`

---

## 🔒 **Authentication**
- Use token-based authentication.
- Obtain a token by logging in at `/api/auth/login/`.
- Include the token in the `Authorization` header for authenticated requests:
  ```
  Authorization: Token <your_token_here>
  ```

---

## 🚀 **Deployment**
The API is deployed on **PythonAnywhere** and can be accessed at:  
[https://omarshoman.pythonanywhere.com/api/](https://omarshoman.pythonanywhere.com/api/)

---

## 📝 **Project Report**
For more details about the project, challenges faced, and key learnings, check out the [Project Report](https://docs.google.com/document/d/1FQG7rXPJJ08Tl9gbW9_Tg_hIwvYTqvwKo8f_jpfu0NU/edit?usp=sharing).

---

## 📧 **Contact**
For any questions or feedback, feel free to reach out:  
- **Name**: Omar Shoman  
- **Email**: shomanomar454@gmail.com  
- **GitHub**: [Omar-F-Shoman](https://github.com/Omar-F-Shoman)
```
