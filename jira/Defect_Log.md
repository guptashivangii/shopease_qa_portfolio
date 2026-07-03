e# Defect Log (25 Bugs)

This document contains **25 realistic software defects** reported for the **ShopEase** application. Each report is structured in industry-standard Jira defect format, complete with steps to reproduce, actual/expected results, priority/severity classifications, assignee, status, and Root Cause Analysis (RCA).

---

## 1. Master Defect Summary Table

| Bug ID | Type | Severity | Priority | Summary | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SE-BUG-001** | Functional | Blocker | P0 (Critical)| Payment Gateway: CVV field accepts plain text letters, allowing unauthorized checkout bypass. | Resolved |
| **SE-BUG-002** | Security | Critical | P0 (Critical)| User credentials (passwords) stored in clear text inside database without hashing. | Closed |
| **SE-BUG-003** | Performance| Critical | P1 (High)   | Cart checkout API latency spikes to 12 seconds when database connections exceed 100. | Open |
| **SE-BUG-004** | Functional | Major | P1 (High)   | Quantity exceeding stock count can be added to cart using API request modification. | Resolved |
| **SE-BUG-005** | Functional | Major | P1 (High)   | Direct URL access bypasses login to display target user's shipping profile. | Closed |
| **SE-BUG-006** | Validation | Major | P1 (High)   | Phone field accepts special character strings, breaking order confirmation emails. | Resolved |
| **SE-BUG-007** | UI / Layout | Minor | P2 (Medium) | Search page: Pagination buttons overlap with footer on 768px tablet displays. | Closed |
| **SE-BUG-008** | Functional | Major | P1 (High)   | Session token not destroyed on logout; user can access account using previous token. | Closed |
| **SE-BUG-009** | Validation | Major | P1 (High)   | User Registration allows duplicate emails if uppercase/lowercase characters differ. | Resolved |
| **SE-BUG-010** | Validation | Major | P2 (Medium) | ZIP Code field allows inputs with 50 characters, crashing backend database entry. | Resolved |
| **SE-BUG-011** | Functional | Major | P1 (High)   | Inventory levels fail to decrement in database after a successful card transaction. | Open |
| **SE-BUG-012** | UI / Layout | Minor | P3 (Low)    | Forgot Password: "Send recovery link" button lacks hovering transitions/styles. | Closed |
| **SE-BUG-013** | Functional | Minor | P2 (Medium) | Wishlist: Adding an item that is already in the wishlist increments total count. | Closed |
| **SE-BUG-014** | Validation | Minor | P2 (Medium) | Product Details: Quantity selector allows inputs of negative numbers like `-5`. | Resolved |
| **SE-BUG-015** | Functional | Major | P1 (High)   | Coupon Code discounts apply to shipping fees even if coupon specifies item only. | Resolved |
| **SE-BUG-016** | Security | Critical | P1 (High)   | Search bar input is vulnerable to Cross-Site Scripting (XSS) injection. | Closed |
| **SE-BUG-017** | UI / Layout | Minor | P2 (Medium) | Product details page carousel displays broken image placeholders for missing files. | Closed |
| **SE-BUG-018** | Functional | Major | P1 (High)   | Forgot Password link does not expire after 30 minutes. | Closed |
| **SE-BUG-019** | Performance| Major | P2 (Medium) | Autocomplete search queries trigger API database lookups on every single keydown event. | Open |
| **SE-BUG-020** | Functional | Minor | P2 (Medium) | Checkout: Guest user is redirect-looped when attempting to access checkout URL. | Resolved |
| **SE-BUG-021** | Functional | Major | P1 (High)   | Credit card validation logic accepts Visa card numbers that fail the Luhn test. | Resolved |
| **SE-BUG-022** | UI / Layout | Minor | P3 (Low)    | Admin Portal: Low stock warning badge overlaps with the sidebar navigation. | Closed |
| **SE-BUG-023** | Functional | Major | P1 (High)   | Order Tracking: Entering trailing spaces in Order ID results in "Order Not Found". | Resolved |
| **SE-BUG-024** | Validation | Major | P1 (High)   | Admin Portal: Product creation accepts negative values for product prices. | Resolved |
| **SE-BUG-025** | Security | Critical | P0 (Critical)| SQL injection vulnerability on the product review search textbox. | Closed |

---

## 2. Detailed Bug Reports

Below are the 25 detailed bug reports in Jira format.

---

### SE-BUG-001: Payment Gateway: CVV field accepts letters
* **Environment:** Staging (Windows 11, Chrome v114, Database SQLite v3.39)
* **Severity:** Blocker  
* **Priority:** P0 (Critical)  
* **Status:** Resolved  
* **Assignee:** dev_payment_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Add any product to the cart and proceed to checkout.
  2. Enter shipping address and continue to Payment page.
  3. Enter valid card number and future expiry date.
  4. In the CVV input field, enter `ABC` instead of numbers.
  5. Click the "Pay Now" button.
* **Expected Result:** Payment validation blocks submission, showing error "CVV must be numeric".
* **Actual Result:** Form submits successfully and payment transaction completes.
* **Root Cause Analysis (RCA):** The regex filter on the CVV text field was omitted on the front-end, and the backend only verified the character length (`length == 3`) without verifying that all characters are numeric digits.

---

### SE-BUG-002: User passwords stored in clear text inside database
* **Environment:** Staging (PostgreSQL v14.2)
* **Severity:** Critical  
* **Priority:** P0 (Critical)  
* **Status:** Closed  
* **Assignee:** dev_sec_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Register a new user account with password `Pass@1234`.
  2. Open SQL client and query the `users` table: `SELECT username, password FROM users WHERE username = 'testuser';`.
* **Expected Result:** The password column contains a hashed string (e.g., BCrypt hash beginning with `$2b$`).
* **Actual Result:** The password column contains the literal string `Pass@1234`.
* **Root Cause Analysis (RCA):** The developer omitted calling the `bcrypt.hashSync()` method on password updates, saving the plain string payload directly.

---

### SE-BUG-003: Cart checkout API latency spikes under connection loads
* **Environment:** Load Staging Environment (AWS EC2 t3.medium, 100 concurrent DB connections)
* **Severity:** Critical  
* **Priority:** P1 (High)  
* **Status:** Open  
* **Assignee:** dev_db_lead  
* **Resolution:** Open  
* **Steps to Reproduce:**
  1. Trigger load testing script simulating 100 concurrent users performing checkouts.
  2. Monitor response times for endpoint `POST /api/checkout`.
* **Expected Result:** API response time stays below 2.0 seconds.
* **Actual Result:** Latency increases to 12.4 seconds, leading to connection timeouts.
* **Root Cause Analysis (RCA):** Database connections are opened inside a loop for checking stock and are not returned to the pool immediately, causing pool exhaustion.

---

### SE-BUG-004: Quantity exceeding stock count can be added to cart using API
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_api_dev  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Open a product details page with stock count = 2.
  2. Intercept API call `POST /api/cart/add` using Postman or Burp Suite.
  3. Modify JSON payload parameter `{"quantity": 100}`.
  4. Send the request.
* **Expected Result:** API returns HTTP `400 Bad Request` with message "Insufficient inventory".
* **Actual Result:** API returns HTTP `200 OK` and cart is populated with 100 units.
* **Root Cause Analysis (RCA):** The API controller only checked if the quantity was a positive integer, omitting the inventory bounds query from the database.

---

### SE-BUG-005: Direct URL access bypasses login to display user's profile
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Closed  
* **Assignee:** dev_auth_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Ensure you are not logged in (Clear all cookies).
  2. Type the URL `http://shopease.qa/user/profile/15` directly into the browser address bar.
* **Expected Result:** Redirected to `/login` page with error message.
* **Actual Result:** Profile page loads displaying address, full name, and phone number of user ID 15.
* **Root Cause Analysis (RCA):** The route handler in `profile_controller.py` lacked the `@login_required` middleware check.

---

### SE-BUG-006: Phone field accepts special character strings
* **Environment:** QA-Env (Firefox v113)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_frontend_02  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Navigate to User Profile Settings.
  2. In the phone number field, input: `+1-555-ABC-##$$`.
  3. Click Save.
* **Expected Result:** Input validation fails: "Enter a valid numeric phone number".
* **Actual Result:** Profile updates successfully. Later attempts to send automated order SMS alert fail.
* **Root Cause Analysis (RCA):** The input field type was set to text and lacked regex pattern matching (`^\+?[0-9]{10,15}$`).

---

### SE-BUG-007: Search page pagination buttons overlap footer on tablet screen
* **Environment:** QA-Env (iPad Mini Viewport 768x1024)
* **Severity:** Minor  
* **Priority:** P2 (Medium)  
* **Status:** Closed  
* **Assignee:** dev_design_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Perform a product search returning 50+ items to trigger pagination.
  2. Set browser viewport size to 768px width.
  3. Scroll down to the bottom of the page.
* **Expected Result:** Pagination buttons are positioned above the footer with proper margins.
* **Actual Result:** Pagination buttons overlap the footer, rendering text unreadable.
* **Root Cause Analysis (RCA):** Absolute CSS positioning was used instead of flexbox for the pagination container, combined with missing media queries for tablet viewports.

---

### SE-BUG-008: Session token not destroyed on logout
* **Environment:** Staging (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Closed  
* **Assignee:** dev_auth_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Log in to ShopEase and copy the active session token `jwt_token` from cookies.
  2. Click the Logout button.
  3. Using an API client, send a request to `GET /api/user/orders` including the copied `jwt_token` header.
* **Expected Result:** API returns HTTP `401 Unauthorized`.
* **Actual Result:** API returns HTTP `200 OK` along with order histories.
* **Root Cause Analysis (RCA):** Logout cleared client cookies but did not invalidate the JSON Web Token on the backend redis blocklist.

---

### SE-BUG-009: Registration allows duplicate email with casing variations
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_auth_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Register an account with email `test@domain.com`.
  2. Attempt to register a new account with email `TEST@domain.com`.
* **Expected Result:** Registration blocked: "Email already registered".
* **Actual Result:** Registration succeeds, creating a duplicate active email record.
* **Root Cause Analysis (RCA):** The email uniqueness query was case-sensitive and did not perform `.toLowerCase()` checks.

---

### SE-BUG-010: ZIP Code field allows 50 chars, crashing DB insert
* **Environment:** QA-Env (PostgreSQL v14.2)
* **Severity:** Major  
* **Priority:** P2 (Medium)  
* **Status:** Resolved  
* **Assignee:** dev_db_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Open checkout address page.
  2. Type a 50-character alphanumeric string in ZIP Code field and submit checkout.
* **Expected Result:** ZIP validation blocks submit, max limit = 10 chars.
* **Actual Result:** System crashes with a HTTP `500 Server Error` ("value too long for type character varying(10)").
* **Root Cause Analysis (RCA):** No character length limits were set in the frontend validation, allowing strings to bypass and violate the PostgreSQL column limit `VARCHAR(10)`.

---

### SE-BUG-011: Inventory levels fail to decrement after card transaction
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Open  
* **Assignee:** dev_inventory_lead  
* **Resolution:** Open  
* **Steps to Reproduce:**
  1. Check stock of "iPhone 15" (e.g., 5 items).
  2. Purchase 2 units of "iPhone 15" successfully.
  3. Query the product details again.
* **Expected Result:** Stock level is decremented to 3.
* **Actual Result:** Stock level remains 5.
* **Root Cause Analysis (RCA):** The inventory update script inside checkout transaction was commented out or failed to execute due to unhandled transaction commits.

---

### SE-BUG-012: Forgot Password button lacks hover styles
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Minor  
* **Priority:** P3 (Low)  
* **Status:** Closed  
* **Assignee:** dev_design_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Navigate to Forgot Password page.
  2. Hover the mouse cursor over the "Send Recovery Link" button.
* **Expected Result:** The button color transitions smoothly or shows cursor modification to hand pointer.
* **Actual Result:** The button styling is static; pointer cursor does not change, reducing feedback.
* **Root Cause Analysis (RCA):** The CSS file lacked a `:hover` pseudoclass definition for the specific button class `.btn-forgot-password`.

---

### SE-BUG-013: Wishlist duplicates items and increments count
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Minor  
* **Priority:** P2 (Medium)  
* **Status:** Closed  
* **Assignee:** dev_wishlist  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Add "iPhone 15" to Wishlist.
  2. Return to "iPhone 15" details page and click "Add to Wishlist" again.
* **Expected Result:** System shows "Already in Wishlist" or ignores click.
* **Actual Result:** The wishlist count increments to 2, and the item is listed twice.
* **Root Cause Analysis (RCA):** Wishlist database inserts did not run unique check queries matching user ID and product ID.

---

### SE-BUG-014: Product Details Qty allows negative numbers
* **Environment:** QA-Env (Firefox v113)
* **Severity:** Minor  
* **Priority:** P2 (Medium)  
* **Status:** Resolved  
* **Assignee:** dev_frontend_02  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Open details page for "iPhone 15".
  2. In the quantity text field, type `-5`.
  3. Click "Add to Cart".
* **Expected Result:** Button is disabled or input resets to `1`.
* **Actual Result:** Submits cart addition, cart displays negative total items.
* **Root Cause Analysis (RCA):** The input element tag lacked a `min="1"` attribute, and validation failed to check that the quantity must be positive.

---

### SE-BUG-015: Coupon Code discounts apply to shipping fees
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_checkout  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Add items to cart (Subtotal = $10.00, Shipping = $5.00, Total = $15.00).
  2. Apply a 100% item coupon `FREEITEMS`.
* **Expected Result:** Subtotal is $0.00, Shipping remains $5.00. Total = $5.00.
* **Actual Result:** Subtotal is $0.00, Shipping becomes $0.00. Total = $0.00.
* **Root Cause Analysis (RCA):** Discount calculations subtracted values directly from the final order total instead of the items subtotal.

---

### SE-BUG-016: Search bar input vulnerable to Cross-Site Scripting (XSS)
* **Environment:** Staging (Chrome v114)
* **Severity:** Critical  
* **Priority:** P1 (High)  
* **Status:** Closed  
* **Assignee:** dev_sec_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. In the homepage search box, type: `<script>alert('XSS')</script>`.
  2. Click Search.
* **Expected Result:** Search query displays text query directly, escaping character entities.
* **Actual Result:** An alert box pops up displaying "XSS".
* **Root Cause Analysis (RCA):** The query parameter output was rendered in the page HTML using an unescaped tag wrapper (e.g., `innerHTML` instead of `textContent`).

---

### SE-BUG-017: Product carousel displays broken image placeholders
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Minor  
* **Priority:** P2 (Medium)  
* **Status:** Closed  
* **Assignee:** dev_frontend_01  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Open a product details page where some secondary images are missing from the server.
* **Expected Result:** Broken images are hidden, or a standard placeholder image is shown.
* **Actual Result:** Red 'X' / broken image icons display on the carousel selector.
* **Root Cause Analysis (RCA):** The image `onerror` fallback handling was not implemented.

---

### SE-BUG-018: Forgot Password link does not expire after 30 minutes
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Closed  
* **Assignee:** dev_auth_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Trigger Forgot Password recovery email.
  2. Wait 2 hours.
  3. Click the link in the email and attempt to reset the password.
* **Expected Result:** Password reset is rejected: "Link has expired".
* **Actual Result:** Password reset succeeds.
* **Root Cause Analysis (RCA):** Password reset token verification logic did not check token creation timestamp against current system time.

---

### SE-BUG-019: Autocomplete queries trigger database lookup on every keydown
* **Environment:** Staging (Chrome v114)
* **Severity:** Major  
* **Priority:** P2 (Medium)  
* **Status:** Open  
* **Assignee:** dev_frontend_01  
* **Resolution:** Open  
* **Steps to Reproduce:**
  1. Open Chrome DevTools Network Tab.
  2. Type "electronics" very fast in the search bar.
* **Expected Result:** Single database request after typing pauses (Debouncing).
* **Actual Result:** 11 network API calls triggered in 1 second, overloading backend.
* **Root Cause Analysis (RCA):** Debouncing (e.g., lodash debounce) was not implemented on the keypress listener callback.

---

### SE-BUG-020: Guest user redirected to infinite loop at checkout
* **Environment:** QA-Env (Firefox v113)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_auth_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. As a Guest user with items in cart, click "Proceed to Checkout".
* **Expected Result:** Redirected to `/login` page.
* **Actual Result:** Page redirects repeatedly between `/checkout` and `/login`, causing browser "Too many redirects" error.
* **Root Cause Analysis (RCA):** The login check logic redirected guests back to checkout after auth check, which then redirected them back to login because they were not authenticated, creating a circular loop.

---

### SE-BUG-021: Card validation accepts cards that fail Luhn test
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_payment_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Use card number `4111 1111 1111 1112` during checkout (fails standard Luhn algorithm check).
  2. Submit payment.
* **Expected Result:** Verification error: "Invalid credit card number".
* **Actual Result:** Checkout succeeds.
* **Root Cause Analysis (RCA):** The Luhn check function returned `True` unconditionally due to a syntax bug where the check return line was misplaced.

---

### SE-BUG-022: Admin Dashboard low stock badge overlaps sidebar
* **Environment:** QA-Env (Viewport 1024x768)
* **Severity:** Minor  
* **Priority:** P3 (Low)  
* **Status:** Closed  
* **Assignee:** dev_design_team  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Navigate to `/admin`.
  2. Shrink window width to 1000px.
* **Expected Result:** Elements stack or sidebar folds out cleanly.
* **Actual Result:** The low stock warning badge text overlaps the sidebar links, making them unclickable.
* **Root Cause Analysis (RCA):** Sidebar z-index was lower than dashboard cards container, combined with fixed position layout.

---

### SE-BUG-023: Order Tracking rejects IDs with trailing spaces
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_tracking  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Place an order and get ID `ORD1001`.
  2. Search for order tracking using `ORD1001 ` (with trailing space).
* **Expected Result:** Order status displays correctly.
* **Actual Result:** Displays error: "Order not found".
* **Root Cause Analysis (RCA):** Input strings were not trimmed before querying the database, causing search mismatch.

---

### SE-BUG-024: Admin Portal accepts negative prices
* **Environment:** QA-Env (Chrome v114)
* **Severity:** Major  
* **Priority:** P1 (High)  
* **Status:** Resolved  
* **Assignee:** dev_admin_panel  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Go to Add Product.
  2. Input price `-150.00`.
  3. Click Save.
* **Expected Result:** Validation failure: "Price must be positive".
* **Actual Result:** Product created with negative price. Storefront displays negative costs.
* **Root Cause Analysis (RCA):** The backend model validator checked if price was a float but did not enforce `price > 0`.

---

### SE-BUG-025: SQL injection on review search textbox
* **Environment:** Staging (PostgreSQL v14.2)
* **Severity:** Critical  
* **Priority:** P0 (Critical)  
* **Status:** Closed  
* **Assignee:** dev_sec_lead  
* **Resolution:** Fixed  
* **Steps to Reproduce:**
  1. Go to Product Reviews search box.
  2. Input: `'; DROP TABLE reviews; --`.
  3. Click search reviews.
* **Expected Result:** Handled as a query string safely. No SQL commands are executed.
* **Actual Result:** Reviews table is dropped in database.
* **Root Cause Analysis (RCA):** The query was executed using string formatting instead of parameterized prepared statements: `query = f"SELECT * FROM reviews WHERE comment LIKE '%{user_input}%'"`
