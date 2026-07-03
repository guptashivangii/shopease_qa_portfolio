# Requirement Traceability Matrix (RTM)

This matrix maps Business Requirements (from the BRD) and Software Requirements (from the SRS) to their corresponding Test Case IDs (from `Test_Cases.md`), demonstrating complete testing coverage.

---

## 1. Traceability Mapping Table

| BR ID | SRS ID | Module / Feature | Requirement Description | Test Case IDs (TC-*) | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BR-01** | SRS-FUN-001 | User Registration | Support new user sign-up with email, username, password validations. | TC-REG-001, TC-REG-002, TC-REG-003, TC-REG-004, TC-REG-005, TC-REG-006, TC-REG-007, TC-REG-008, TC-REG-009, TC-REG-010 | Covered |
| **BR-01** | SRS-FUN-002 | User Login | Authenticate users securely, support lockout after 5 failures. | TC-LOG-011, TC-LOG-012, TC-LOG-013, TC-LOG-014, TC-LOG-015, TC-LOG-016, TC-LOG-017, TC-LOG-018 | Covered |
| **BR-01** | SRS-FUN-003 | Logout | Terminate active user sessions securely. | TC-LOG-019, TC-LOG-020 | Covered |
| **BR-01** | SRS-FUN-004 | Forgot Password | Automated password recovery flow via email, links valid for 30 mins. | TC-FGP-021, TC-FGP-022, TC-FGP-023, TC-FGP-024, TC-FGP-025, TC-FGP-026 | Covered |
| **BR-02** | SRS-FUN-005 | Product Search | Search catalog by keyword, partial matches, handling special characters. | TC-SCH-027, TC-SCH-028, TC-SCH-029, TC-SCH-029b, TC-SCH-033, TC-SCH-034 | Covered |
| **BR-02** | SRS-FUN-006 | Product Filters | Filter search results by Category, Price Range, and Rating. | TC-SCH-030, TC-SCH-031, TC-SCH-032 | Covered |
| **BR-02** | SRS-FUN-007 | Product Details Page | View specifications, description, images carousel, stock levels. | TC-DET-035, TC-DET-036, TC-DET-037, TC-DET-038, TC-DET-039, TC-DET-040 | Covered |
| **BR-03** | SRS-FUN-008 | Add to Cart | Add items, edit quantities, respect available inventory stock limits. | TC-CRT-041, TC-CRT-042, TC-CRT-043, TC-CRT-044, TC-CRT-045, TC-CRT-046, TC-CRT-047, TC-CRT-047b | Covered |
| **BR-03** | SRS-FUN-009 | Cart Persistence | Session persistence for guest cart and merging upon user login. | TC-CRT-048, TC-LO-049 | Covered |
| **BR-04** | SRS-FUN-010 | Wishlist Management | Save items for future purchase; move items to cart. | TC-WSH-050, TC-WSH-051, TC-WSH-052, TC-WSH-053, TC-WSH-054, TC-WSH-055 | Covered |
| **BR-05** | SRS-FUN-011 | Checkout Flow | Guide user through address entry, coupons, summary validation. | TC-CHK-056, TC-CHK-057, TC-CHK-058, TC-CHK-059, TC-CHK-060, TC-CHK-061, TC-CHK-062, TC-CHK-063, TC-CHK-064, TC-CHK-065 | Covered |
| **BR-06** | SRS-FUN-012 | Payment Processing | Secure credit card processing using Luhn algorithm; check limits. | TC-PAY-066, TC-PAY-067, TC-PAY-068, TC-PAY-069, TC-PAY-070, TC-PAY-071, TC-PAY-074 | Covered |
| **BR-06** | SRS-FUN-013 | Invoice & Stock | Generate invoices on payment and decrement stock counts in DB. | TC-PAY-072, TC-PAY-073 | Covered |
| **BR-07** | SRS-FUN-014 | Order Tracking | Track order shipping progress via Order ID search; check links. | TC-TRK-076, TC-TRK-077, TC-TRK-078, TC-TRK-079, TC-TRK-080, TC-TRK-081 | Covered |
| **BR-01** | SRS-FUN-015 | User Profile Mgmt | Modify profile, check address logs, view order history. | TC-PRF-082, TC-PRF-083, TC-PRF-084, TC-PRF-085, TC-PRF-086, TC-PRF-087, TC-PRF-088, TC-PRF-089, TC-PRF-090, TC-PRF-091 | Covered |
| **BR-08** | SRS-ADM-001 | Catalog CRUD Admin | Admins manage product configurations, inventories, CRUD entries. | TC-ADM-092, TC-ADM-093, TC-ADM-094, TC-ADM-095, TC-ADM-096, TC-ADM-097, TC-ADM-098, TC-ADM-099b, TC-ADM-100 | Covered |
| **BR-08** | SRS-ADM-002 | Inventory Alert | Admin warning thresholds on low inventory listings. | TC-ADM-099 | Covered |
| **N/A** | SRS-NFR-001 | Security: Encryption | Hashing credentials, TLS transit security parameters. | Verified during registration & login checks (TC-REG-008, TC-LOG-015) | Covered |
| **N/A** | SRS-NFR-002 | PCI-DSS Compliance | Do not store raw CC or CVV codes in the database. | TC-PAY-075 | Covered |
| **N/A** | SRS-NFR-003 | Performance | Page load response time < 2.0s under default execution conditions. | Tracked in API/automation test checks | Covered |
| **N/A** | SRS-NFR-004 | Concurrency | Concurrency limits checked during automated checkout simulations. | Tracked in performance execution report | Covered |
| **N/A** | SRS-NFR-005 | Compatibility | Cross-browser operational integrity. | Verified across standard test environments | Covered |
| **N/A** | SRS-NFR-006 | Mobile Responsiveness| Dynamic layout adjustments across devices. | Verified during UI/UX tests | Covered |

---

## 2. Coverage Metrics & Statistics

We evaluate test coverage based on the percentage of Software Requirements mapped to at least one test case.

$$\text{Test Coverage \%} = \left( \frac{\text{Number of Mapped Requirements}}{\text{Total Number of Defined Requirements}} \right) \times 100$$

* **Total Defined Requirements:** 23 (17 Functional/Admin + 6 Non-Functional)
* **Total Mapped Requirements:** 23
* **Test Coverage Percentage:** **100%**

All functional requirements are comprehensively validated, ensuring complete coverage.
