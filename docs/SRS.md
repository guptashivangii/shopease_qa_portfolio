# Software Requirements Specification (SRS)

## Project: ShopEase E-Commerce Web Application
**Document Version:** 1.0  
**Author:** Shivangi Gupta 
**Date:** June 23, 2026  

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) details the functional and non-functional requirements for the **ShopEase E-Commerce Web Application** (Version 1.0). This document serves as the single source of truth for the development and quality assurance teams, providing clear criteria for code verification and system acceptance.

### 1.2 Document Conventions
Each requirement has a unique identifier for traceability:
* **SRS-FUN-XXX:** Functional Requirement for user-facing features.
* **SRS-NFR-XXX:** Non-Functional Requirement (Performance, Security, etc.).
* **SRS-ADM-XXX:** Administrative Dashboard Requirement.

---

## 2. Overall Description

### 2.1 Product Perspective
ShopEase is a web-based e-commerce platform that communicates with a backend RESTful API and a relational database (SQLite/PostgreSQL). The application acts as a standalone storefront.

### 2.2 System Functions (Core Modules)
1. **User Registration:** Allow new shoppers to sign up.
2. **Login/Logout:** Secure session management.
3. **Forgot Password:** Automated email recovery flow.
4. **Product Search:** Keyword and category filtering.
5. **Product Details:** Viewing specifications, images, pricing, and ratings.
6. **Add to Cart:** Session-based persistent cart for active checkouts.
7. **Wishlist:** Storing items for future consideration.
8. **Checkout:** Address input, summary validation.
9. **Payment Gateway:** Mock credit card processing.
10. **Order Tracking:** Track transit stage (Pending, Shipped, Delivered).
11. **User Profile Management:** Update personal information, addresses, and view order history.
12. **Admin Product Management:** Backoffice dashboard for stock control and catalog updates.

---

## 3. Functional Requirements (SRS-FUN)

### 3.1 User Account Management
* **SRS-FUN-001 (User Registration):** 
  * The system shall allow users to register using a valid email, unique username, password, and confirmation password.
  * *Validation:* Email must follow standard format (`user@domain.com`). Password must be at least 8 characters, containing at least one uppercase letter, one lowercase letter, one digit, and one special character.
* **SRS-FUN-002 (User Login):** 
  * The system shall authenticate users with their username/email and password.
  * *Behavior:* On login failure, show generic error "Invalid credentials". Block account after 5 consecutive failed attempts for 15 minutes.
* **SRS-FUN-003 (Logout):** 
  * The system shall terminate the active session and redirect the user to the Home page.
* **SRS-FUN-004 (Forgot Password):** 
  * The system shall allow users to input their email. If the email exists, the system sends an automated recovery link valid for 30 minutes.

### 3.2 Product Catalog & Interaction
* **SRS-FUN-005 (Product Search):** 
  * Users shall be able to search for products using keywords.
  * *Behavior:* Support autocomplete search. If no products match, display "No products found matching your search".
* **SRS-FUN-006 (Product Filters):** 
  * Users shall be able to filter search results by Category, Price Range, and Rating.
* **SRS-FUN-007 (Product Details Page):** 
  * The system shall display the product name, price, stock status, ratings, description, and high-quality images.

### 3.3 Shopping Cart & Wishlist
* **SRS-FUN-008 (Add to Cart):** 
  * Users shall be able to add products to the shopping cart from the Product List or Product Details pages.
  * *Validation:* Users cannot add more units than are currently available in inventory.
* **SRS-FUN-009 (Cart Persistence):** 
  * Shopping cart data shall persist in the user session for guest users, and in the database for logged-in users.
* **SRS-FUN-010 (Wishlist Management):** 
  * Registered users shall be able to add/remove products to/from a personal Wishlist.

### 3.4 Checkout & Orders
* **SRS-FUN-011 (Checkout Flow):** 
  * The checkout process shall guide users through: (1) Shipping Address selection, (2) Billing Address entry, (3) Order Summary review, and (4) Payment.
* **SRS-FUN-012 (Payment Processing):** 
  * The system shall integrate with a mock payment gateway.
  * *Validation:* Visa, Mastercard, and American Express formats must be validated (Luhn Algorithm).
* **SRS-FUN-013 (Order Invoice Generation):** 
  * On successful checkout, the system shall generate a unique Order ID and email an invoice summary to the customer.
* **SRS-FUN-014 (Order Tracking):** 
  * Users shall be able to input an Order ID to view current fulfillment progress (Pending, Processing, Shipped, Delivered).

### 3.5 Admin Portal Requirements (SRS-ADM)
* **SRS-ADM-001 (CRUD Operations on Catalog):** 
  * Users with "Admin" role shall be able to Create, Read, Update, and Delete products, categories, and inventory counts.
* **SRS-ADM-002 (Inventory Threshold Alert):** 
  * The admin dashboard shall flag products with stock levels lower than 5 units.

---

## 4. Non-Functional Requirements (SRS-NFR)

### 4.1 Security
* **SRS-NFR-001 (Data Encryption):** All communication must be encrypted using HTTPS/TLS 1.3. User passwords must be stored using a salted hashing algorithm (BCrypt).
* **SRS-NFR-002 (PCI-DSS Compliance):** The application must not store raw Credit Card numbers (PAN) or security codes (CVV) in the local database.

### 4.2 Performance
* **SRS-NFR-003 (Response Time):** 95% of API transactions and page requests must complete in under 2.0 seconds under normal load.
* **SRS-NFR-004 (Concurrency):** The system must support up to 5,000 concurrent active shopping sessions without service degradation.

### 4.3 Compatibility & Usability
* **SRS-NFR-005 (Cross-Browser Compatibility):** The system must be fully operational on Google Chrome (v100+), Mozilla Firefox (v100+), Apple Safari (v15+), and Microsoft Edge (v100+).
* **SRS-NFR-006 (Mobile Responsiveness):** The layout must dynamically adjust for screen widths ranging from 320px (Mobile) to 1920px (Desktop).

---

## 5. Assumptions and Constraints

* **Assumptions:**
  * Email deliveries depend on an external SMTP server remaining responsive.
  * Users have JavaScript enabled on their browsers.
* **Constraints:**
  * Relational Database constraints require database schema consistency.
  * Payment simulations must not perform real financial transfers.
