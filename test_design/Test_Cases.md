# Test Cases (100+)

This document contains **102 detailed manual test cases** covering all ShopEase requirements and modules.

---

## 1. User Registration (TC-REG)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-REG-001** | SRS-FUN-001 | Successful registration with valid data. | ShopEase Home page is open. User is not logged in. | 1. Click "Sign Up".<br>2. Fill all mandatory fields.<br>3. Click "Submit". | Username: `testuser1`<br>Email: `testuser1@example.com`<br>Password: `Pass@1234`<br>Confirm Password: `Pass@1234` | Account created successfully. Redirection to login page. | As Expected | PASS | High |
| **TC-REG-002** | SRS-FUN-001 | Registration with missing mandatory fields. | Sign Up page is open. | 1. Leave Username field empty.<br>2. Fill other fields.<br>3. Click "Submit". | Email: `test@ex.com`<br>Password: `Pass@1234`<br>Confirm Password: `Pass@1234` | Registration blocked. Validation error: "Username is required". | As Expected | PASS | High |
| **TC-REG-003** | SRS-FUN-001 | Registration with duplicate email address. | An account with `dup@example.com` already exists. | 1. Fill all fields.<br>2. Enter `dup@example.com` in email.<br>3. Click "Submit". | Username: `newuser`<br>Email: `dup@example.com`<br>Password: `Pass@1234`<br>Confirm Password: `Pass@1234` | Registration blocked. Validation error: "Email already registered". | As Expected | PASS | High |
| **TC-REG-004** | SRS-FUN-001 | Registration with duplicate username. | Username `testuser1` already exists. | 1. Fill all fields.<br>2. Enter `testuser1` in Username.<br>3. Click "Submit". | Username: `testuser1`<br>Email: `newemail@test.com`<br>Password: `Pass@1234`<br>Confirm Password: `Pass@1234` | Registration blocked. Validation error: "Username already taken". | As Expected | PASS | High |
| **TC-REG-005** | SRS-FUN-001 | Registration with invalid email format. | Sign Up page is open. | 1. Enter invalid email string.<br>2. Click "Submit". | Email: `invalidemail.com` | Registration blocked. Validation error: "Enter a valid email address". | As Expected | PASS | Medium |
| **TC-REG-006** | SRS-FUN-001 | Registration with password length < 8 chars. | Sign Up page is open. | 1. Enter password with 7 chars.<br>2. Click "Submit". | Password: `Pas@123`<br>Confirm Password: `Pas@123` | Registration blocked. Validation error: "Password must be at least 8 characters". | As Expected | PASS | Medium |
| **TC-REG-007** | SRS-FUN-001 | Registration with password lacking uppercase. | Sign Up page is open. | 1. Enter password without uppercase.<br>2. Click "Submit". | Password: `pass@1234`<br>Confirm Password: `pass@1234` | Registration blocked. Validation error: "Password must contain an uppercase letter". | As Expected | PASS | Medium |
| **TC-REG-008** | SRS-FUN-001 | Registration with password lacking special character. | Sign Up page is open. | 1. Enter password without special char.<br>2. Click "Submit". | Password: `Password1234`<br>Confirm Password: `Password1234` | Registration blocked. Validation error: "Password must contain a special character". | As Expected | PASS | Medium |
| **TC-REG-009** | SRS-FUN-001 | Password and Confirm Password mismatch. | Sign Up page is open. | 1. Enter mismatching passwords.<br>2. Click "Submit". | Password: `Pass@1234`<br>Confirm Password: `Pass@9999` | Registration blocked. Validation error: "Passwords do not match". | As Expected | PASS | High |
| **TC-REG-010** | SRS-FUN-001 | SQL Injection vulnerability check. | Sign Up page is open. | 1. Enter SQL injection payload in Username.<br>2. Submit form. | Username: `' OR '1'='1` | Input sanitized or rejected with validation error. Account not created. | As Expected | PASS | High |

---

## 2. Login/Logout (TC-LOG)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-LOG-011** | SRS-FUN-002 | Successful login with registered username. | User is registered. | 1. Go to Login page.<br>2. Enter Username and correct Password.<br>3. Click "Login". | Username: `testuser1`<br>Password: `Pass@1234` | Login successful. Redirected to dashboard/home with active session. | As Expected | PASS | High |
| **TC-LOG-012** | SRS-FUN-002 | Successful login with registered email. | User is registered. | 1. Go to Login page.<br>2. Enter Email and correct Password.<br>3. Click "Login". | Email: `testuser1@example.com`<br>Password: `Pass@1234` | Login successful. Redirected to dashboard/home with active session. | As Expected | PASS | High |
| **TC-LOG-013** | SRS-FUN-002 | Login failure with incorrect password. | User is registered. | 1. Go to Login page.<br>2. Enter correct Username and wrong Password.<br>3. Click "Login". | Username: `testuser1`<br>Password: `WrongPass` | Login fails. Display "Invalid credentials". | As Expected | PASS | High |
| **TC-LOG-014** | SRS-FUN-002 | Login failure with unregistered username. | Username `nonexistent` does not exist. | 1. Enter unregistered username.<br>2. Enter any password.<br>3. Click "Login". | Username: `nonexistent`<br>Password: `Pass@1234` | Login fails. Display "Invalid credentials". | As Expected | PASS | High |
| **TC-LOG-015** | SRS-FUN-002 | Login fields SQL Injection check. | Login page is open. | 1. Enter SQL injection payload in Username.<br>2. Click Login. | Username: `admin' --`<br>Password: `password` | Authentication fails safely. SQL injection blocked. | As Expected | PASS | High |
| **TC-LOG-016** | SRS-FUN-002 | Account lockout after 5 failed attempts. | User account `testuser1` is registered. | 1. Perform 5 consecutive logins with incorrect password.<br>2. Try 6th login with correct password. | Correct Password: `Pass@1234` | Account locked on 5th attempt. 6th attempt blocked with "Account locked for 15 mins". | As Expected | PASS | High |
| **TC-LOG-017** | SRS-FUN-002 | Username case sensitivity check. | Username is `TestUser` (mixed case). | 1. Log in with lowercase username `testuser`. | Username: `testuser`<br>Password: `Pass@1234` | Login successful (usernames are case-insensitive or resolved). | As Expected | PASS | Medium |
| **TC-LOG-018** | SRS-FUN-002 | Blank username and password login attempt. | Login page is open. | 1. Keep fields blank.<br>2. Click Login. | N/A | Validation errors: "Username is required", "Password is required". | As Expected | PASS | High |
| **TC-LOG-019** | SRS-FUN-003 | Successful logout from dashboard. | User is logged in. | 1. Click "Logout" button in navbar. | N/A | Logged out. Session terminated. Redirected to home. | As Expected | PASS | High |
| **TC-LOG-020** | SRS-FUN-003 | Session boundary test after logout. | User just logged out. | 1. Click browser "Back" button to return to dashboard. | N/A | Dashboard page is not accessible. Redirection to Login page. | As Expected | PASS | High |

---

## 3. Forgot Password (TC-FGP)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-FGP-021** | SRS-FUN-004 | Send recovery email with registered email. | User account exists with email `testuser1@example.com`. | 1. Go to Forgot Password page.<br>2. Enter email.<br>3. Click "Send Recovery Link". | Email: `testuser1@example.com` | Success message "Recovery link sent". Email delivered. | As Expected | PASS | High |
| **TC-FGP-022** | SRS-FUN-004 | Request recovery with unregistered email. | Email `unreg@example.com` does not exist. | 1. Enter email.<br>2. Click "Send Recovery Link". | Email: `unreg@example.com` | User receives standard message (to avoid user enumeration) or error handled. | As Expected | PASS | Medium |
| **TC-FGP-023** | SRS-FUN-004 | Request recovery with invalid email format. | Forgot Password page is open. | 1. Enter invalid email format.<br>2. Click "Send Recovery Link". | Email: `invalidemail` | Validation error: "Enter a valid email address". | As Expected | PASS | Medium |
| **TC-FGP-024** | SRS-FUN-004 | Reset password using valid link within 30 mins. | Recovery email received 5 minutes ago. | 1. Click link in email.<br>2. Enter new password.<br>3. Save. | New Password: `NewPass@1234` | Password updated. Successful login using new password. | As Expected | PASS | High |
| **TC-FGP-025** | SRS-FUN-004 | Reset password using expired link (> 30 mins). | Recovery email received 45 minutes ago. | 1. Click recovery link. | Link expired token. | Error page: "The reset link has expired". Password unchanged. | As Expected | PASS | High |
| **TC-FGP-026** | SRS-FUN-004 | Reset password link single-use check. | Password reset link was already used once. | 1. Click the same recovery link again. | N/A | Error page: "Invalid or already used token". Access blocked. | As Expected | PASS | High |

---

## 4. Product Search & Filters (TC-SCH)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-SCH-027** | SRS-FUN-005 | Product search with exact name match. | Products exist in DB (e.g. "iPhone 15"). | 1. Type exact name in search bar.<br>2. Click Search. | Query: `iPhone 15` | Results page displays "iPhone 15". | As Expected | PASS | High |
| **TC-SCH-028** | SRS-FUN-005 | Search by partial product name. | Products exist in DB. | 1. Type partial query.<br>2. Click Search. | Query: `iPhone` | Displays all products matching partial name (iPhone 15, iPhone 14). | As Expected | PASS | High |
| **TC-SCH-029** | SRS-FUN-005 | Search with non-existent keyword. | Search bar is active. | 1. Enter random string.<br>2. Click Search. | Query: `xyzabc123` | Shows message "No products found matching your search". | As Expected | PASS | High |
| **TC-SCH-029b**| SRS-FUN-005 | Empty search submission. | Home page is open. | 1. Leave search bar blank.<br>2. Click Search button. | Query: ` ` (blank) | Search not executed, or displays default search list. | As Expected | PASS | Low |
| **TC-SCH-030** | SRS-FUN-006 | Filter search results by Category. | Search results are displayed. | 1. Select "Electronics" category checkbox. | Category: `Electronics` | Only electronics products are displayed. | As Expected | PASS | Medium |
| **TC-SCH-031** | SRS-FUN-006 | Filter search results by Price Range. | Search results are displayed. | 1. Set Min Price = $100 and Max Price = $500. | Price Range: `$100 - $500` | Displays only products with price >= $100 and <= $500. | As Expected | PASS | Medium |
| **TC-SCH-032** | SRS-FUN-006 | Filter search results by Customer Rating. | Search results are displayed. | 1. Select Filter "4 Stars & Up". | Rating: `4+ Stars` | Displays only products with rating >= 4 stars. | As Expected | PASS | Medium |
| **TC-SCH-033** | SRS-FUN-005 | Special characters in search input. | Search bar is active. | 1. Type special characters in search bar.<br>2. Click Search. | Query: `* & % @ !` | Handled gracefully without crash; shows no results or sanitized query search. | As Expected | PASS | Medium |
| **TC-SCH-034** | SRS-FUN-005 | Search input boundary limit. | Search bar is active. | 1. Input string of 256 characters.<br>2. Click Search. | Query: 256 char string | Text truncated or validation prevents extra inputs. Application does not crash. | As Expected | PASS | Low |

---

## 5. Product Details (TC-DET)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-DET-035** | SRS-FUN-007 | Verify details display for a standard product. | Product "iPhone 15" is active and exists. | 1. Click on "iPhone 15" from list. | N/A | Displayed: Name, description, image, price ($999), ratings, stock status. | As Expected | PASS | High |
| **TC-DET-036** | SRS-FUN-007 | Direct URL access to non-existent Product ID. | Product ID `9999` does not exist. | 1. Navigate directly to URL `/product/9999`. | URL: `/product/9999` | 404 Error page shown: "Product not found". | As Expected | PASS | Medium |
| **TC-DET-037** | SRS-FUN-007 | Display of Out of Stock status. | Product stock level is 0 in DB. | 1. Open details page for that product. | Product: `Wireless Mouse` | Displays "Out of Stock" status. Add to Cart button disabled. | As Expected | PASS | High |
| **TC-DET-038** | SRS-FUN-007 | Display of low stock alert. | Product stock level is 3. | 1. Open details page for that product. | Product: `Keychron Keyboard` | Displays "Only 3 left in stock!". | As Expected | PASS | Medium |
| **TC-DET-039** | SRS-FUN-007 | Product images gallery carousel check. | Product has multiple images. | 1. Click next image arrow in detail gallery. | N/A | Image carousel transitions to display next image successfully. | As Expected | PASS | Low |
| **TC-DET-040** | SRS-FUN-007 | Product specifications alignment and tabs. | Details page is open. | 1. Click on "Specifications" tab. | N/A | Spec details sheet displays correctly with correct alignments. | As Expected | PASS | Low |

---

## 6. Add to Cart (TC-CRT)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CRT-041** | SRS-FUN-008 | Add standard active product to cart. | User is on Product details page. Cart is empty. | 1. Click "Add to Cart". | Product: `iPhone 15` | Cart count badges updates to 1. Success toast displayed. | As Expected | PASS | High |
| **TC-CRT-042** | SRS-FUN-008 | Add multiple quantities of a product to cart. | Product stock is 10. | 1. Select quantity = 3.<br>2. Click "Add to Cart". | Product: `iPhone 15`<br>Qty: 3 | Cart contains item with quantity = 3. Cart count shows 3. | As Expected | PASS | High |
| **TC-CRT-043** | SRS-FUN-008 | Increment quantity on Cart view page. | Product in cart has qty = 1. Stock = 10. | 1. Open Cart view page.<br>2. Click "+" button next to product. | N/A | Quantity updates to 2. Subtotal and total updates. | As Expected | PASS | High |
| **TC-CRT-044** | SRS-FUN-008 | Decrement quantity on Cart view page. | Product in cart has qty = 2. | 1. Open Cart page.<br>2. Click "-" button. | N/A | Quantity updates to 1. Subtotal and total updates. | As Expected | PASS | High |
| **TC-CRT-045** | SRS-FUN-008 | Remove product from Cart. | Product is in the cart. | 1. Open Cart page.<br>2. Click "Remove/Delete" icon. | N/A | Product is removed from cart. Total updates to $0.00. | As Expected | PASS | High |
| **TC-CRT-046** | SRS-FUN-008 | Add quantity equal to max stock limit. | Product stock is 5 in DB. | 1. Enter quantity = 5.<br>2. Click "Add to Cart". | Qty: 5 | Cart successfully updated with 5 items. | As Expected | PASS | High |
| **TC-CRT-047** | SRS-FUN-008 | Try to add quantity exceeding stock limit. | Product stock is 5. | 1. Enter quantity = 6.<br>2. Click "Add to Cart". | Qty: 6 | Blocked. Error shown: "Cannot add more than available stock (5)". | As Expected | PASS | High |
| **TC-CRT-047b**| SRS-FUN-008 | Add negative or zero quantity to cart. | Product details page is open. | 1. Type `-1` or `0` in quantity field.<br>2. Click "Add to Cart". | Qty: `-1` | Field resets to 1, or validation error blocks action. | As Expected | PASS | Medium |
| **TC-CRT-048** | SRS-FUN-009 | Guest cart persistence during active session. | User is not logged in. | 1. Add product to cart.<br>2. Browse other pages.<br>3. Return to Cart. | N/A | Cart items remain saved. | As Expected | PASS | Medium |
| **TC-LO-049**  | SRS-FUN-009 | Guest cart merges with user account on Login. | Cart has "iPhone 15" for guest. User is registered. | 1. Log in to user account. | Username: `testuser1`<br>Password: `Pass@1234` | "iPhone 15" is merged and visible in logged-in user's cart. | As Expected | PASS | High |

---

## 7. Wishlist (TC-WSH)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-WSH-050** | SRS-FUN-010 | Add product to wishlist (logged-in user). | User is logged in. | 1. Go to product detail page.<br>2. Click "Add to Wishlist". | Product: `iPhone 15` | Success message. Wishlist count updates to 1. | As Expected | PASS | High |
| **TC-WSH-051** | SRS-FUN-010 | Add product to wishlist (guest user). | User is NOT logged in. | 1. Click "Add to Wishlist". | Product: `iPhone 15` | Blocked. User is redirected to Login page with notification. | As Expected | PASS | High |
| **TC-WSH-052** | SRS-FUN-010 | Remove product from Wishlist. | Product is in the wishlist. | 1. Open Wishlist page.<br>2. Click "Remove" icon. | N/A | Product is removed from wishlist. Message: "Removed from wishlist". | As Expected | PASS | Medium |
| **TC-WSH-053** | SRS-FUN-010 | Add duplicate item to Wishlist. | Product already exists in user's wishlist. | 1. Click "Add to Wishlist" on product details. | Product: `iPhone 15` | Item not duplicated. Shows "Already in Wishlist" or toggles off. | As Expected | PASS | Medium |
| **TC-WSH-054** | SRS-FUN-010 | Move item from Wishlist to Cart. | Product in wishlist. Stock is available. | 1. Open Wishlist page.<br>2. Click "Add to Cart" button. | N/A | Product added to Cart and removed or kept in wishlist as desired. | As Expected | PASS | High |
| **TC-WSH-055** | SRS-FUN-010 | Move out-of-stock item from Wishlist to Cart. | Product in wishlist is Out of Stock. | 1. Click "Add to Cart" button in wishlist. | Product: `Wireless Mouse` | Blocked. Button disabled or error shown: "Product is out of stock". | As Expected | PASS | Medium |

---

## 8. Checkout (TC-CHK)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-CHK-056** | SRS-FUN-011 | Proceed to checkout with items in cart. | User logged in. Cart has 1 item. | 1. Click "Proceed to Checkout" from cart page. | N/A | Navigates to shipping address step. | As Expected | PASS | High |
| **TC-CHK-057** | SRS-FUN-011 | Submit checkout with new shipping address. | Checkout flow active. | 1. Fill shipping form.<br>2. Click "Continue to Payment". | Address: `123 Main St`<br>City: `New York`<br>ZIP: `10001`<br>Phone: `1234567890` | Validates details. Navigates to payment screen. | As Expected | PASS | High |
| **TC-CHK-058** | SRS-FUN-011 | Checkout with missing mandatory address fields. | Checkout flow active. | 1. Leave ZIP code empty.<br>2. Click Continue. | ZIP: ` ` | Blocked. Validation error: "ZIP code is required". | As Expected | PASS | High |
| **TC-CHK-059** | SRS-FUN-011 | ZIP code format validation check. | Checkout flow active. | 1. Enter invalid ZIP code alphanumeric characters. | ZIP: `ABCDE` | Blocked. Validation error: "Enter a valid ZIP code". | As Expected | PASS | Medium |
| **TC-CHK-060** | SRS-FUN-011 | Phone number validation check. | Checkout flow active. | 1. Enter alphabet string in Phone. | Phone: `abcdefghij` | Blocked. Validation error: "Enter a valid phone number". | As Expected | PASS | Medium |
| **TC-CHK-061** | SRS-FUN-011 | Use coupon code for checkout discount. | Valid coupon code `SAVE10` offers 10% off. | 1. Enter coupon code.<br>2. Click Apply. | Coupon: `SAVE10` | 10% discount deducted from order subtotal. Total updates. | As Expected | PASS | High |
| **TC-CHK-062** | SRS-FUN-011 | Use expired coupon code. | Coupon code `EXPIRED` is expired. | 1. Enter coupon.<br>2. Click Apply. | Coupon: `EXPIRED` | Error: "Coupon has expired". Total is unchanged. | As Expected | PASS | Medium |
| **TC-CHK-063** | SRS-FUN-011 | Checkout block for guest users. | User is guest. Cart has 1 item. | 1. Click "Proceed to Checkout". | N/A | Redirected to login/registration page before address entry. | As Expected | PASS | High |
| **TC-CHK-064** | SRS-FUN-011 | Verify Order Summary matches cart contents. | Checkout flow active. | 1. Review Order Summary page. | Product: `iPhone 15`<br>Price: `$999`<br>Qty: 2 | Order Summary displays Qty 2, Unit Price $999, Total $1998 + Tax. | As Expected | PASS | High |
| **TC-CHK-065** | SRS-FUN-011 | Try to checkout with empty cart via direct URL. | Cart is empty. | 1. Type URL `/checkout` directly in browser. | URL: `/checkout` | Redirected to home/cart page with message: "Your cart is empty". | As Expected | PASS | High |

---

## 9. Payment Gateway (TC-PAY)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-PAY-066** | SRS-FUN-012 | Successful transaction with valid Credit Card. | Payment screen active. | 1. Enter valid card number, future expiry, CVV.<br>2. Click "Pay Now". | Card: `4111 1111 1111 1111`<br>Expiry: `12/30`<br>CVV: `123` | Payment approved. Navigates to success page. Order created. | As Expected | PASS | High |
| **TC-PAY-067** | SRS-FUN-012 | Payment declined with expired credit card. | Payment screen active. | 1. Enter expired date.<br>2. Click "Pay Now". | Card: `4111 1111 1111 1111`<br>Expiry: `12/22`<br>CVV: `123` | Blocked. Error: "Card expiry date must be in the future". | As Expected | PASS | High |
| **TC-PAY-068** | SRS-FUN-012 | Payment declined with invalid card number format. | Payment screen active. | 1. Enter invalid length card number.<br>2. Click "Pay Now". | Card: `12345`<br>Expiry: `12/30`<br>CVV: `123` | Blocked. Error: "Card number is invalid". | As Expected | PASS | High |
| **TC-PAY-069** | SRS-FUN-012 | Luhn Algorithm validation failure check. | Payment screen active. | 1. Enter card failing Luhn check. | Card: `4111 1111 1111 1112` | Blocked. Error: "Invalid card number". | As Expected | PASS | Medium |
| **TC-PAY-070** | SRS-FUN-012 | CVV field character length constraint. | Payment screen active. | 1. Type 2 or 5 digits CVV.<br>2. Pay. | CVV: `1` or `12345` | Blocked. Error: "CVV must be 3 or 4 digits". | As Expected | PASS | High |
| **TC-PAY-071** | SRS-FUN-012 | Successful payment with mock PayPal. | Payment screen active. | 1. Select PayPal option.<br>2. Log in with sandbox details. | User: `paypal@sandbox.com` | Redirected back. Payment approved. | As Expected | PASS | High |
| **TC-PAY-072** | SRS-FUN-013 | Invoice email receipt check on success. | Payment just succeeded. | 1. Open customer email inbox. | Email: `testuser1@example.com` | Email received with invoice detailing order, price, and Order ID. | As Expected | PASS | Medium |
| **TC-PAY-073** | SRS-FUN-013 | Check stock count decrements in DB post-payment. | Stock of product before payment was 10. | 1. Pay for 2 units.<br>2. Query product stock in DB. | Order qty: 2 | Product stock level is decremented to 8. | As Expected | PASS | High |
| **TC-PAY-074** | SRS-FUN-012 | Resubmitting payment during processing block. | Payment processing screen active. | 1. Click "Pay Now" multiple times quickly. | N/A | Duplicate payment request is rejected. Only one transaction is processed. | As Expected | PASS | High |
| **TC-PAY-075** | SRS-NFR-002 | PCI-DSS Compliance security verification. | Database client active. | 1. Check `orders` and `payments` tables for transaction. | N/A | Raw CVV and credit card numbers are NOT stored in the database. | As Expected | PASS | Critical |

---

## 10. Order Tracking (TC-TRK)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-TRK-076** | SRS-FUN-014 | View tracking status of valid active order. | Order `ORD1001` status is "Shipped". | 1. Go to Order Tracking page.<br>2. Enter Order ID.<br>3. Click Track. | Order ID: `ORD1001` | Status page shows "Shipped" with timestamps. | As Expected | PASS | High |
| **TC-TRK-077** | SRS-FUN-014 | Try to track non-existent Order ID. | Order ID `ORD9999` does not exist. | 1. Go to Order Tracking page.<br>2. Enter Order ID.<br>3. Click Track. | Order ID: `ORD9999` | Shows message: "Order ID not found". | As Expected | PASS | High |
| **TC-TRK-078** | SRS-FUN-014 | Empty Order ID field validation. | Order Tracking page is open. | 1. Leave field blank.<br>2. Click Track. | Order ID: ` ` | Validation error: "Order ID cannot be empty". | As Expected | PASS | Low |
| **TC-TRK-079** | SRS-FUN-014 | Special characters check in tracking input. | Order Tracking page is open. | 1. Type SQL syntax in Order ID.<br>2. Click Track. | Order ID: `' OR '1'='1` | Input rejected or sanitized safely; database is not compromised. | As Expected | PASS | High |
| **TC-TRK-080** | SRS-FUN-014 | Click tracking link in confirmation email. | Confirmation email is open. | 1. Click tracking hyperlink. | N/A | Browser opens tracking page for that Order ID automatically. | As Expected | PASS | Medium |
| **TC-TRK-081** | SRS-FUN-014 | Guest tracking permission check. | User is guest. | 1. Enter Order ID.<br>2. Click Track. | Order ID: `ORD1001` | Guest user can track order (does not require login if they have ID). | As Expected | PASS | Medium |

---

## 11. User Profile Management (TC-PRF)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-PRF-082** | SRS-FUN-015 | Edit and update personal name details. | User is logged in. | 1. Open Profile Settings.<br>2. Edit Name.<br>3. Save changes. | Name: `Alex Smith` | Success message. Profile displays updated name. | As Expected | PASS | High |
| **TC-PRF-083** | SRS-FUN-015 | Update profile with invalid phone length. | Profile Settings open. | 1. Input phone with 5 digits.<br>2. Save. | Phone: `12345` | Validation error: "Phone number must be at least 10 digits". | As Expected | PASS | Medium |
| **TC-PRF-084** | SRS-FUN-015 | Update profile with non-numeric phone format. | Profile Settings open. | 1. Input alphabetic phone string. | Phone: `abcd12345` | Validation error: "Phone number can only contain digits". | As Expected | PASS | Medium |
| **TC-PRF-085** | SRS-FUN-015 | Add shipping address to profile. | User is logged in. | 1. Click "Add Address".<br>2. Fill details.<br>3. Save. | Address: `456 Elm St`<br>ZIP: `20002` | Address added to saved addresses list. | As Expected | PASS | High |
| **TC-PRF-086** | SRS-FUN-015 | Delete address from profile. | Profile has 1 saved address. | 1. Click "Delete Address". | N/A | Address removed. Saved address list is empty. | As Expected | PASS | Medium |
| **TC-PRF-087** | SRS-FUN-015 | View order history logs. | User has placed 2 previous orders. | 1. Navigate to "My Orders". | N/A | List shows 2 orders with correct Order IDs, dates, and prices. | As Expected | PASS | High |
| **TC-PRF-088** | SRS-FUN-015 | Direct URL access to another user's profile. | User `testuser1` logged in. User `testuser2` ID is 12. | 1. Try to open `/user/profile/12` directly. | URL: `/user/profile/12` | Access blocked. 403 Forbidden or redirected with error. | As Expected | PASS | High |
| **TC-PRF-089** | SRS-FUN-015 | Update profile with blank name. | Profile Settings open. | 1. Clear Name field.<br>2. Click Save. | Name: ` ` | Validation error: "Name field cannot be blank". | As Expected | PASS | High |
| **TC-PRF-090** | SRS-FUN-015 | Change password from profile. | User is logged in. | 1. Enter Current Password.<br>2. Enter New Password.<br>3. Click Update. | Current: `Pass@1234`<br>New: `NewPass@1234` | Password changed successfully. Previous password no longer works. | As Expected | PASS | High |
| **TC-PRF-091** | SRS-FUN-015 | Re-registration attempt with profile email. | Profile contains `testuser1@example.com`. | 1. Go to register page.<br>2. Try to sign up with that email. | Email: `testuser1@example.com` | Blocked. Validation error displays email already in use. | As Expected | PASS | High |

---

## 12. Admin Product Management (TC-ADM)

| Test Case ID | Requirement ID | Test Objective | Preconditions | Test Steps | Test Data | Expected Result | Actual Result | Status | Priority |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-ADM-092** | SRS-ADM-001 | Successful admin login and access. | User has "Admin" role in DB. | 1. Log in to account.<br>2. Go to `/admin`. | Username: `adminuser`<br>Password: `AdminPass@123` | Access granted. Admin Dashboard page displays catalog statistics. | As Expected | PASS | High |
| **TC-ADM-093** | SRS-ADM-001 | Standard user blocked from admin panel. | User has "Customer" role in DB. | 1. Log in.<br>2. Attempt to open `/admin` URL. | Username: `testuser1`<br>Password: `Pass@1234` | Access blocked. Redirected to 403 Page or Home page. | As Expected | PASS | High |
| **TC-ADM-094** | SRS-ADM-001 | Create new product with complete data. | Admin is logged in. | 1. Click "Add Product".<br>2. Fill metadata.<br>3. Click Save. | Title: `iPad Pro`<br>Category: `Electronics`<br>Price: `799.99`<br>Stock: `15` | Product created. Visible on storefront search page. | As Expected | PASS | High |
| **TC-ADM-095** | SRS-ADM-001 | Edit and update product pricing. | Product "iPad Pro" exists. | 1. Click Edit on product.<br>2. Change price.<br>3. Save. | New Price: `849.99` | Product price updated on details page to $849.99. | As Expected | PASS | High |
| **TC-ADM-096** | SRS-ADM-001 | Delete product from catalog. | Product "iPad Pro" exists. | 1. Click Delete next to product.<br>2. Confirm. | N/A | Product removed from admin list and no longer searchable on storefront. | As Expected | PASS | High |
| **TC-ADM-097** | SRS-ADM-001 | Create product with negative price. | Admin is logged in. | 1. Set Price = `-10.00`.<br>2. Click Save. | Price: `-10.00` | Blocked. Validation error: "Price must be greater than zero". | As Expected | PASS | High |
| **TC-ADM-098** | SRS-ADM-001 | Create product with negative stock. | Admin is logged in. | 1. Set Stock = `-5`.<br>2. Click Save. | Stock: `-5` | Blocked. Validation error: "Stock count cannot be negative". | As Expected | PASS | High |
| **TC-ADM-099** | SRS-ADM-002 | Low inventory threshold alert trigger. | Product stock level is updated to 4. | 1. Update product stock = 4. | Stock: 4 | Admin Dashboard displays warning badge: "Low Stock: iPad Pro (4)". | As Expected | PASS | Medium |
| **TC-ADM-099b**| SRS-ADM-001 | Missing product title validation. | Admin is logged in. | 1. Leave Title blank.<br>2. Click Save. | Title: ` ` | Validation error: "Product title is required". | As Expected | PASS | Medium |
| **TC-ADM-100** | SRS-ADM-001 | Upload invalid image format for product. | Admin is logged in. | 1. Click upload image.<br>2. Select non-image file. | File: `data.txt` | Blocked. Validation error: "Invalid file format. Only JPEG, PNG, WEBP". | As Expected | PASS | Medium |
