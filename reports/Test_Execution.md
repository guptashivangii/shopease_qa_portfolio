# Test Execution & QA Metrics Report

This document presents the test execution statistics, defect metrics, defect density, defect leakage rates, and a daily status report (DSR) for the **ShopEase Storefront (v1.0)** release cycle.

---

## 1. Test Execution Sheet (Summary by Module)

The manual test suite of **102 test cases** was executed during the main staging test cycle.

| Module Name | Total Cases | Executed | Passed | Failed | Blocked | Pass % |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **User Registration** | 10 | 10 | 9 | 1 | 0 | 90.0% |
| **Login/Logout** | 10 | 10 | 9 | 1 | 0 | 90.0% |
| **Forgot Password** | 6 | 6 | 5 | 1 | 0 | 83.3% |
| **Product Search & Filters**| 9 | 9 | 9 | 0 | 0 | 100.0% |
| **Product Details** | 6 | 6 | 6 | 0 | 0 | 100.0% |
| **Add to Cart** | 10 | 10 | 9 | 1 | 0 | 90.0% |
| **Wishlist** | 6 | 6 | 5 | 1 | 0 | 83.3% |
| **Checkout** | 10 | 10 | 8 | 2 | 0 | 80.0% |
| **Payment Gateway** | 11 | 11 | 9 | 2 | 0 | 81.8% |
| **Order Tracking** | 6 | 6 | 5 | 1 | 0 | 83.3% |
| **User Profile Management** | 11 | 11 | 9 | 2 | 0 | 81.8% |
| **Admin Product Management**| 7 | 7 | 6 | 1 | 0 | 85.7% |
| **Non-Functional / Security**| 10 | 10 | 7 | 3 | 0 | 70.0% |
| **TOTAL** | **102** | **102** | **91** | **11** | **0** | **89.2%** |

---

## 2. Pass/Fail Statistics (Visual & Numerical)

* **Total Test Cases:** 102
* **Total Executed:** 102 (100% Execution Rate)
* **Total Passed:** 91 (89.2%)
* **Total Failed:** 11 (10.8%)
* **Total Blocked:** 0 (0.0%)

```text
Staging Execution Summary:
[█████████████████████████████████████████████████░░░░░░] 89.2% Passed (91/102)
```

> [!NOTE]
> The 11 failing test cases correspond to the active/resolved bugs logged in the [Defect Log](file:///C:/Users/shiva/.gemini/antigravity/scratch/shopease_qa_portfolio/jira/Defect_Log.md) (e.g. SE-BUG-001, SE-BUG-003, SE-BUG-011, etc.).

---

## 3. Defect Density Report

Defect density measures the number of defects found relative to the size of the software module or codebase, helping identify high-risk components.

$$\text{Defect Density} = \frac{\text{Total Defects Found}}{\text{Size of the Application (KLOC - Thousands of Lines of Code)}}$$

### Parameters
* **Codebase Size (ShopEase v1.0):** 8.5 KLOC (approx. 8,500 lines of functional web app and backend API code).
* **Total Defects Found in QA Cycle:** 25

### Calculation
$$\text{Defect Density} = \frac{25}{8.5} \approx \mathbf{2.94\text{ defects / KLOC}}$$

### Defect Density by Module

| Module Name | Total Defects | Module Size (Est. KLOC) | Defect Density (Defects / KLOC) | Risk Level |
| :--- | :---: | :---: | :---: | :--- |
| **Authentication & Registration**| 5 | 1.8 | 2.78 | Medium |
| **Checkout & Payments** | 7 | 2.0 | 3.50 | High |
| **Catalog & Search** | 5 | 2.2 | 2.27 | Medium |
| **User Profile & Admin** | 5 | 1.5 | 3.33 | High |
| **Database & API Core** | 3 | 1.0 | 3.00 | High |

---

## 4. Defect Leakage Report

Defect leakage measures the efficacy of the QA testing process by calculating the percentage of defects that slipped past QA testing and were identified in production by end users.

$$\text{Defect Leakage \%} = \left( \frac{\text{Defects Found in Production}}{\text{Defects Found in QA} + \text{Defects Found in Production}} \right) \times 100$$

### Parameters (Staging vs. Beta Release)
* **Defects Identified by QA in Staging:** 25
* **Defects Leaked and Reported in Production (Beta):** 2 (Minor UI/UX bugs: a missing tooltip and a minor layout misalignment in Firefox Mobile).

### Calculation
$$\text{Defect Leakage \%} = \left( \frac{2}{25 + 2} \right) \times 100 = \left( \frac{2}{27} \right) \times 100 \approx \mathbf{7.4\%}$$

### QA Benchmark
A leakage rate of **7.4%** is well below the target industry threshold of **10%**, demonstrating high test coverage and effective staging validation.

---

## 5. Daily Status Report (DSR)

**Date:** June 23, 2026  
**Project:** ShopEase Storefront  
**Phase:** Functional Regression & API Testing  

### 5.1 Work Completed Today
1. Executed all 102 manual test cases for the v1.0 release package.
2. Logged 25 defects on the Jira simulation sheet.
3. Conducted API tests using Postman, verifying 100% of the core checkout and authorization endpoints.
4. Conducted database validations to ensure that credit card CVVs and numbers are not stored in cleartext.

### 5.2 Key Metrics Summary
* **Test Cases Planned:** 102
* **Test Cases Executed:** 102
* **Passed:** 91
* **Failed:** 11
* **Open Defects:** 4 (SE-BUG-003, SE-BUG-011, SE-BUG-019, SE-BUG-022)
* **Resolved/Closed Defects:** 21

### 5.3 Blockers & Risks
* **Blocker:** None.
* **Risk:** High latency spikes during payment gateway checkout database loads (SE-BUG-003). Development team is currently working on an indexation and connection pooling hotfix.

### 5.4 Next Steps for Tomorrow
1. Re-verify the fixes for the 4 remaining open bugs.
2. Execute the automated Selenium regression suite to verify registration and login paths.
3. Sign off on the final Release Recommendation Report once SE-BUG-003 is resolved.
