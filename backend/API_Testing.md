# API Testing & Postman Documentation

This document covers backend API test scenarios, specific API test cases, authentication protocols, request/response JSON payload samples, and a JSON representation of a Postman collection for the **ShopEase RESTful API**.

---

## 1. API Test Scenarios

* **TS-API-AUTH:** Verify user authentication, registration, token generation, and role identification.
* **TS-API-CATALOG:** Verify catalog requests (search, get product details, and category listings).
* **TS-API-CART:** Verify cart manipulation (add item, edit quantities, session checks, and clear cart).
* **TS-API-CHECKOUT:** Verify order submissions, payment validations, stock status constraints, and coupon application.

---

## 2. API Test Cases

| API Case ID | Endpoint | Method | Expected Status | Description & Payload Validations | Priority |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **TC-API-001** | `/api/auth/register` | POST | 201 Created | Validate successful account creation and response message. | High |
| **TC-API-002** | `/api/auth/register` | POST | 400 Bad Request| Mismatching passwords or email duplication returns appropriate validation error. | High |
| **TC-API-003** | `/api/auth/login` | POST | 200 OK | Authenticate credentials and return JWT token in JSON response body. | High |
| **TC-API-004** | `/api/auth/login` | POST | 401 Unauthorized| Invalid password or username returns generic error string. | High |
| **TC-API-005** | `/api/products` | GET | 200 OK | Retrieve all products page by page. Verify schema structure. | Medium |
| **TC-API-006** | `/api/products?search=phone`| GET | 200 OK | Search catalog by string. Response must only contain matching items. | High |
| **TC-API-007** | `/api/products/1` | GET | 200 OK | Retrieve detail metadata for product ID 1. | High |
| **TC-API-008** | `/api/products/999` | GET | 404 Not Found | Requesting non-existent product returns error. | Medium |
| **TC-API-009** | `/api/cart` | GET | 200 OK | Retrieve shopping cart items. | High |
| **TC-API-010** | `/api/cart/add` | POST | 200 OK | Add item to cart. JWT auth header required. | High |
| **TC-API-011** | `/api/cart/add` | POST | 400 Bad Request| Requesting item quantity exceeding stock is rejected with error payload. | High |
| **TC-API-012** | `/api/checkout` | POST | 201 Created | Submit billing/shipping address and payment details. Creates order. | High |
| **TC-API-013** | `/api/checkout` | POST | 401 Unauthorized| Checkout without active JWT header is blocked. | High |
| **TC-API-014** | `/api/orders/track/1001` | GET | 200 OK | Retrieve fulfillment tracking status for order ID 1001. | Medium |

---

## 3. Authentication & Header Testing

* **Authentication Protocol:** JSON Web Tokens (JWT)
* **Header Structure:**
  ```http
  Authorization: Bearer <jwt_access_token>
  Content-Type: application/json
  Accept: application/json
  ```
* **Auth Verification Flow:**
  1. Login request returns a base64 encoded token: `access_token`.
  2. For subsequent requests to protected endpoints (e.g. `/api/cart`, `/api/checkout`), the client includes the token in the header.
  3. If the token is expired, missing, or malformed, the API must reject the request with a **HTTP 401 Unauthorized** status code and a JSON response body:
     ```json
     {
       "error": "Unauthorized",
       "message": "Signature has expired or token is invalid."
     }
     ```

---

## 4. Request & Response Payload Samples

### 4.1 User Login (`POST /api/auth/login`)

* **Request Body:**
  ```json
  {
    "username": "testuser1",
    "password": "Pass@1234"
  }
  ```
* **Response Body (200 OK):**
  ```json
  {
    "status": "success",
    "message": "Authentication successful",
    "user": {
      "id": 15,
      "username": "testuser1",
      "email": "testuser1@example.com",
      "role": "Customer"
    },
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxNSwicm9sZSI6IkN1c3RvbWVyIiwiZXhwIjoxNzg5OTg5OTk5fQ.signature_hash"
  }
  ```

### 4.2 Add to Cart (`POST /api/cart/add`)

* **Headers:** Include JWT token in the `Authorization` header.
* **Request Body:**
  ```json
  {
    "product_id": 1,
    "quantity": 2
  }
  ```
* **Response Body (200 OK):**
  ```json
  {
    "status": "success",
    "message": "Product added to cart",
    "cart_summary": {
      "total_items": 2,
      "items": [
        {
          "product_id": 1,
          "title": "iPhone 15",
          "quantity": 2,
          "unit_price": 999.99,
          "subtotal": 1999.98
        }
      ],
      "total_price": 1999.98
    }
  }
  ```

---

## 5. Postman Collection Template

Below is the standard JSON structure of a **Postman Collection v2.1** for ShopEase. Save this code block as `ShopEase_API_Collection.json` to import directly into Postman.

```json
{
  "info": {
    "_postman_id": "a987d654-b321-4def-9f87-654321fedcba",
    "name": "ShopEase Storefront API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Authentication",
      "item": [
        {
          "name": "Login",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"username\": \"testuser1\",\n  \"password\": \"Pass@1234\"\n}"
            },
            "url": {
              "raw": "{{base_url}}/api/auth/login",
              "host": ["{{base_url}}"],
              "path": ["api", "auth", "login"]
            }
          }
        }
      ]
    },
    {
      "name": "Product Catalog",
      "item": [
        {
          "name": "Get All Products",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{base_url}}/api/products",
              "host": ["{{base_url}}"],
              "path": ["api", "products"]
            }
          }
        },
        {
          "name": "Search Products",
          "request": {
            "method": "GET",
            "url": {
              "raw": "{{base_url}}/api/products?search=phone",
              "host": ["{{base_url}}"],
              "path": ["api", "products"],
              "query": [
                {
                  "key": "search",
                  "value": "phone"
                }
              ]
            }
          }
        }
      ]
    },
    {
      "name": "Checkout",
      "item": [
        {
          "name": "Submit Order",
          "request": {
            "method": "POST",
            "header": [
              {
                "key": "Authorization",
                "value": "Bearer {{jwt_token}}"
              },
              {
                "key": "Content-Type",
                "value": "application/json"
              }
            ],
            "body": {
              "mode": "raw",
              "raw": "{\n  \"shipping_address\": {\n    \"address_line1\": \"123 Main St\",\n    \"city\": \"New York\",\n    \"zip_code\": \"10001\",\n    \"phone\": \"1234567890\"\n  },\n  \"payment_method\": \"credit_card\",\n  \"card_details\": {\n    \"card_number\": \"4111111111111111\",\n    \"expiry\": \"12/30\",\n    \"cvv\": \"123\"\n  }\n}"
            },
            "url": {
              "raw": "{{base_url}}/api/checkout",
              "host": ["{{base_url}}"],
              "path": ["api", "checkout"]
            }
          }
        }
      ]
    }
  ]
}
```
