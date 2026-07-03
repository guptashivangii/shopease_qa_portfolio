# Jira Project Simulation: ShopEase Storefront

This document simulates a professional **Jira Software** board setup for the development and testing of the ShopEase storefront. It showcases how Epics, User Stories, Tasks, Subtasks, and Sprints are structured in an Agile development process.

---

## 1. Project Configuration
* **Project Name:** ShopEase Storefront
* **Project Key:** SE
* **Project Type:** Software Development (Scrum template)
* **Active Sprint:** Sprint 3 (Fulfillment & Checkout)

---

## 2. Epics List

| Epic Key | Epic Name | Description | Priority | Status |
| :--- | :--- | :--- | :--- | :--- |
| **SE-EP-01** | User Accounts & Profiles | Management of secure user registrations, logins, lockouts, profiles. | High | Done |
| **SE-EP-02** | Product Catalog & Search | Product listings, category filters, details display, stock status. | High | Done |
| **SE-EP-03** | Shopping Cart & Checkout | Cart CRUD operations, checkout progress, coupons, addresses. | High | In Progress |
| **SE-EP-04** | Payment & Order Mgmt | Gateway integrations, order placement, invoices, status tracking. | High | In Progress |
| **SE-EP-05** | Admin Panel & Catalog Mgmt| Product dashboard, catalog CRUD, low stock notification rules. | Medium | To Do |

---

## 3. Sprint Backlog (Sprint 3: Active)
**Sprint Goal:** Implement and verify shopping cart modifications, checkout address validations, and mock credit card payment processing.

### SE-101: User Story - Address Form Validation during Checkout
* **Epic:** SE-EP-03
* **Priority:** High
* **Story Points:** 5
* **Assignee:** developer_01
* **QA Owner:** qa_tester_01
* **Description:** As a registered shopper, I want the system to validate my shipping and billing addresses during checkout so that I don't submit orders with invalid contact details.
* **Acceptance Criteria:**
  1. Mandatory fields (Address Line 1, City, ZIP Code, Phone) cannot be blank.
  2. ZIP Code must be validated for alphanumeric format corresponding to target shipping countries.
  3. Phone number must only accept numeric characters and must be at least 10 digits long.
  4. Appropriate inline validation errors must be displayed under invalid inputs.
* **Sub-Tasks:**
  * **SE-101-ST1:** Implement address validation frontend fields. (Dev)
  * **SE-101-ST2:** Implement backend API address validations. (Dev)
  * **SE-101-ST3:** Write manual test cases for address fields (positive, negative, boundaries). (QA)
  * **SE-101-ST4:** Automate address input negative validations. (QA)

### SE-102: User Story - Credit Card Checkout Integration
* **Epic:** SE-EP-04
* **Priority:** High
* **Story Points:** 8
* **Assignee:** developer_02
* **QA Owner:** qa_tester_02
* **Description:** As a customer, I want to pay for my purchases using a Visa, Mastercard, or AMEX credit card so that I can complete my orders securely.
* **Acceptance Criteria:**
  1. The checkout payment screen must accept Cardholder Name, Card Number, Expiration Date (MM/YY), and CVV.
  2. Card numbers must be validated using the Luhn Algorithm.
  3. The Expiration Date must be in the future.
  4. CVV must be exactly 3 digits (or 4 digits for AMEX).
  5. The application must not store raw PAN (credit card number) or CVV in the database (PCI-DSS compliance).
  6. Successfully processed transactions must generate a confirmation receipt.
* **Sub-Tasks:**
  * **SE-102-ST1:** Integrate with mock payment processing gateway. (Dev)
  * **SE-102-ST2:** Set up checkout security token parameters. (Dev)
  * **SE-102-ST3:** Manually verify Luhn algorithm and CVV validations. (QA)
  * **SE-102-ST4:** Conduct database test to confirm card numbers/CVVs are not stored in cleartext. (QA)

---

## 4. Product Backlog (Prioritized)

### SE-103: User Story - Product Catalog Admin Panel
* **Epic:** SE-EP-05
* **Priority:** Medium
* **Story Points:** 8
* **Description:** As an Admin user, I want a secure admin panel where I can add, edit, and delete products in the catalog.
* **Acceptance Criteria:**
  1. URL `/admin` must redirect non-admin users to a 403 Forbidden page.
  2. Form fields for creating/editing products (Title, Price, Stock) must have validation bounds.
  3. Uploaded product images must be validated for acceptable formats (.jpg, .png, .webp) and size (< 2MB).

### SE-104: Technical Task - Database Migration & Table Optimizations
* **Epic:** SE-EP-04
* **Priority:** Medium
* **Story Points:** 3
* **Description:** Create database schema migration to add indexes to the `orders(user_id)` and `order_items(order_id)` foreign keys to optimize lookup speeds on the My Orders user page.

### SE-105: User Story - Order Tracking Status Indicators
* **Epic:** SE-EP-04
* **Priority:** High
* **Story Points:** 3
* **Description:** As a customer, I want to enter my Order ID on the Order Tracking page to see if my order is Pending, Shipped, or Delivered.
