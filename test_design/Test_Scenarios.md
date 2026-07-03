# Test Scenarios (50+)

This document contains **54 detailed test scenarios** covering all 12 modules of the **ShopEase** e-commerce application. The scenarios represent a mix of positive, negative, boundary value, and edge cases.

---

## Module 1: User Registration
* **TS-REG-01 (Positive):** Verify that a user can successfully register with valid details (unique username, valid email, and strong password).
* **TS-REG-02 (Negative):** Verify that registration fails when mandatory fields (username, email, or password) are left blank.
* **TS-REG-03 (Negative):** Verify that a user cannot register with an already existing/registered email address.
* **TS-REG-04 (Negative):** Verify that registration fails when the password does not meet complexity requirements (e.g., less than 8 characters, no special character).
* **TS-REG-05 (Negative):** Verify that registration fails when "Password" and "Confirm Password" fields do not match.
* **TS-REG-06 (Edge Case):** Verify SQL injection inputs in registration fields (e.g., entering `' OR '1'='1` in the username) are handled safely and rejected.

---

## Module 2: Login/Logout
* **TS-LOG-07 (Positive):** Verify that a user can successfully log in using registered email/username and correct password.
* **TS-LOG-08 (Negative):** Verify that login fails with an incorrect password for a registered username.
* **TS-LOG-09 (Negative):** Verify that login fails with an unregistered email/username.
* **TS-LOG-10 (Negative/Security):** Verify account lockout policy (account is temporarily disabled for 15 minutes after 5 consecutive failed login attempts).
* **TS-LOG-11 (Positive):** Verify that logging out successfully terminates the user session and redirects them to the Home page.
* **TS-LOG-12 (Security/Session):** Verify that clicking the browser "Back" button after logging out does not display authenticated pages.

---

## Module 3: Forgot Password
* **TS-FGP-13 (Positive):** Verify that a password recovery email is sent when a registered email is entered.
* **TS-FGP-14 (Negative):** Verify that the system displays a validation error or handles gracefully when an unregistered email is entered.
* **TS-FGP-15 (Edge Case):** Verify that the password reset token/link expires after the designated 30-minute threshold.
* **TS-FGP-16 (Security):** Verify that reusing a password reset link that has already been used displays an "Expired or invalid token" error.

---

## Module 4: Product Search & Navigation
* **TS-SCH-17 (Positive):** Verify that searching with an exact product name displays the correct matching product.
* **TS-SCH-18 (Positive):** Verify search by categories and sub-categories (e.g., Electronics, Apparel).
* **TS-SCH-19 (Negative):** Verify the message displayed when searching for non-existent products or random alphanumeric strings.
* **TS-SCH-20 (Boundary):** Verify search inputs at maximum character limits (e.g., 255 characters) are handled gracefully without application crashes.
* **TS-SCH-21 (Positive):** Verify that users can filter search results by price range, star rating, and availability status.

---

## Module 5: Product Details
* **TS-DET-22 (Positive):** Verify that clicking a product displays its detailed page with name, description, high-quality images, pricing, specs, and reviews.
* **TS-DET-23 (Negative):** Verify that trying to access a non-existent or inactive Product ID URL directly (e.g., `/product/99999`) redirects to a 404 error page.
* **TS-DET-24 (Positive):** Verify product stock indicators dynamically update (e.g., shows "In Stock", "Only 2 left", or "Out of Stock").

---

## Module 6: Add to Cart
* **TS-CRT-25 (Positive):** Verify adding a single item to the cart updates the cart item count header.
* **TS-CRT-26 (Positive):** Verify that a user can update product quantities in the cart and the subtotal updates accordingly.
* **TS-CRT-27 (Boundary):** Verify adding product quantity up to the maximum available inventory limit succeeds.
* **TS-CRT-28 (Boundary):** Verify that trying to add more quantity than available in inventory displays an "Insufficient Stock" error.
* **TS-CRT-29 (Negative):** Verify that users cannot add negative quantities or zero quantities to the cart.
* **TS-CRT-30 (Positive):** Verify that guest users' carts merge with their registered accounts upon logging in.

---

## Module 7: Wishlist
* **TS-WSH-31 (Positive):** Verify that a registered user can add an item to the wishlist and the wishlist count increments.
* **TS-WSH-32 (Positive):** Verify that items in the wishlist can be moved directly to the shopping cart.
* **TS-WSH-33 (Negative):** Verify that guest users are prompted to log in/register when attempting to add a product to the wishlist.

---

## Module 8: Checkout
* **TS-CHK-34 (Positive):** Verify that a user can successfully enter shipping and billing addresses during checkout.
* **TS-CHK-35 (Negative):** Verify checkout progress is blocked if mandatory shipping details (ZIP code, Phone number, Address Line 1) are missing.
* **TS-CHK-36 (Boundary):** Verify shipping calculations for different geographical zones, taxes, and optional discount codes.
* **TS-CHK-37 (Negative):** Verify entering an expired or invalid coupon code displays a clear error and does not deduct the price.

---

## Module 9: Payment Gateway
* **TS-PAY-38 (Positive):** Verify successful transaction using a valid mock credit card (Visa/Mastercard).
* **TS-PAY-39 (Negative):** Verify that transaction is declined when entering an invalid credit card number, expired card, or wrong CVV.
* **TS-PAY-40 (Negative/Security):** Verify system behavior when connection times out during payment processing (ensure duplicate charges do not occur).
* **TS-PAY-41 (Edge Case):** Verify transaction processing with international currencies and correct currency conversions.

---

## Module 10: Order Tracking
* **TS-TRK-42 (Positive):** Verify that a user can view their order status (Pending -> Shipped -> Delivered) using the Order ID.
* **TS-TRK-43 (Negative):** Verify error message when searching for an invalid or non-existent Order ID.
* **TS-TRK-44 (Positive):** Verify that customers receive automated order confirmation emails immediately after successful checkout.

---

## Module 11: User Profile Management
* **TS-PRF-45 (Positive):** Verify that users can edit their profile information (name, phone number, saved addresses).
* **TS-PRF-46 (Negative):** Verify validations on phone numbers (e.g., rejecting alphabets or short lengths) and zip codes.
* **TS-PRF-47 (Positive):** Verify that users can view their past order history, status, and download invoices.

---

## Module 12: Admin Product Management
* **TS-ADM-48 (Positive/Auth):** Verify that only users with the "Admin" role can access the administration dashboard.
* **TS-ADM-49 (Negative/Security):** Verify that standard users receive a "403 Forbidden" page when attempting to access `/admin` directly.
* **TS-ADM-50 (Positive):** Verify that admins can create a new product with valid metadata and images.
* **TS-ADM-51 (Positive):** Verify that admins can update pricing and stock levels of existing products.
* **TS-ADM-52 (Positive):** Verify that deleting a product removes it from the catalog immediately.
* **TS-ADM-53 (Boundary):** Verify that setting inventory count to zero makes the product display "Out of Stock" on the customer storefront.
* **TS-ADM-54 (Negative):** Verify that creating a product with negative prices or negative stock quantities is blocked by validation filters.
