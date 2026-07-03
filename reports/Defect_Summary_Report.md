# Defect Summary Report

**Project:** ShopEase Storefront  
**Release Version:** v1.0-GA  
**Date:** June 23, 2026  

---

## 1. Defect Metrics Breakdown

During the ShopEase storefront development and testing cycle, **25 defects** were logged. This report provides a visual and statistical analysis of these defects.

### 1.1 Defects by Severity

| Severity Level | Defect Count | Percentage | Description |
| :--- | :---: | :---: | :--- |
| **Blocker** | 1 | 4% | Prevents testing or releases critical failure. |
| **Critical** | 4 | 16% | Security loopholes, data loss, database crashes. |
| **Major** | 11 | 44% | Core functional failures without quick workarounds. |
| **Minor** | 9 | 36% | Cosmetic issues, minor validations, non-blocking UI. |
| **Total** | **25** | **100%** | |

### 1.2 Defects by Priority

* **P0 (Critical/Immediate):** 3 (12%)
* **P1 (High/Urgent):** 11 (44%)
* **P2 (Medium/Normal):** 9 (36%)
* **P3 (Low/Deferred):** 2 (8%)

---

## 2. Defect Distribution by Module

The heat map of defects highlights modules requiring additional quality checks in future releases:

| Module Name | Blocker/Critical | Major | Minor | Total | Defect % |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **User Accounts & Login** | 1 | 3 | 1 | 5 | 20% |
| **Catalog & Search** | 1 | 1 | 3 | 5 | 20% |
| **Checkout & Payments** | 1 | 3 | 3 | 7 | 28% |
| **Admin Portal** | 1 | 2 | 2 | 5 | 20% |
| **Database & API Core** | 1 | 2 | 0 | 3 | 12% |
| **TOTAL** | **5** | **11** | **9** | **25** | **100%** |

---

## 3. Defect Status Distribution

* **New:** 0
* **Open:** 3 (Active)
* **In Progress:** 0
* **Resolved (Fixed & Verified):** 12
* **Closed (Merged to Release):** 10

---

## 4. Key Security & Functional Vulnerabilities Resolved

### 4.1 SQL Injection on Search Reviews (SE-BUG-025)
* **Impact:** High-severity database compromise.
* **Resolution:** Parameterized query statements implemented in Python database layer, completely separating SQL command interpretation from user query inputs.

### 4.2 Plain Text Passwords in Database (SE-BUG-002)
* **Impact:** Potential data breach exposing user credentials.
* **Resolution:** Integrated the `bcrypt` library to hash passwords using standard salt factors before database writes.

### 4.3 Credit Card CVV Accepts Alpha Inputs (SE-BUG-001)
* **Impact:** Checkout bypass allowing customers to place fake orders.
* **Resolution:** Frontend HTML input changed to numeric type with matching validation. Backend API checks constraints using regex filters.
