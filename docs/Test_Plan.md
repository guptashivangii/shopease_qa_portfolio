# Master Test Plan

## Project: ShopEase E-Commerce Web Application
**Document Version:** 1.0  
**Author:** Shivangi Gupta  
**Date:** June 23, 2026  

---

## 1. Scope & Objectives

### 1.1 Objectives
The main objective of testing is to verify that the ShopEase web application functions exactly as specified in the SRS. Testing aims to identify critical defects prior to product release, evaluate response times under expected loads, verify security controls, and guarantee user-friendly operations across multiple browsers and screen resolutions.

### 1.2 Scope of Testing
Testing will focus on all user-facing front-end components and backend integrations (API services, relational database structures, payment simulations).

#### 1.2.1 In-Scope for Testing
* **Functional Testing:** Registration, login, product browsing, cart actions, checkout, admin CRUD operations.
* **API Testing:** Request/Response payloads, headers, security tokens, HTTP status codes.
* **Database Testing:** Verification of CRUD state, foreign key integrity, constraint checks, inventory updates.
* **UI/UX Testing:** Font styles, alignments, responsiveness across devices, input forms validation error feedback.
* **Compatibility Testing:** Google Chrome, Safari, Firefox, Edge, iOS Safari, Android Chrome.
* **Security Testing:** Session termination on logout, password hashing checks, SQL Injection prevention, XSS prevention.

#### 1.2.2 Out-of-Scope for Testing
* Integration with actual production merchant bank accounts (real transactions).
* Load testing exceeding 10,000 concurrent virtual users.
* Physical network latency and hardware-level failure testing.

---

## 2. Testing Types Covered

| Testing Type | Methodology | Description |
| :--- | :--- | :--- |
| **Smoke Testing** | Manual / Automated | Executed upon every new build deployment to ensure critical components (Login, Registration, Checkout) are operational. |
| **Functional Testing** | Manual / Automated | Black-box verification of every SRS-FUN requirement. |
| **Regression Testing** | Automated (Selenium) | Routine execution of the automated test suite on modified builds to check that existing functionalities are not broken. |
| **API Testing** | Automated (Postman / requests) | Testing individual REST endpoints to confirm correct responses, payloads, and status codes. |
| **Database Testing** | Manual (SQL Queries) | Directly querying the backend database to check data storage, state consistency, and integrity constraints. |
| **UI/UX & Compatibility** | Manual | Verifying mobile responsiveness, layouts, and cross-browser styling. |
| **Security Testing** | Manual | Checking authentication boundaries, authorization controls, and standard vulnerabilities. |

---

## 3. Entry and Exit Criteria

### 3.1 Entry Criteria
1. The Software Requirements Specification (SRS) is finalized and approved.
2. The Test Plan, Test Cases, and Automation Scripts are reviewed and baselined.
3. The Target environment (QA Environment) is configured and running.
4. The deployment package is built and deployed successfully.
5. Smoke tests pass with 100% success.

### 3.2 Exit Criteria
1. 100% of planned test cases have been executed.
2. At least 95% of test cases have a status of "PASSED".
3. There are zero open Blockers, Critical, or High severity defects.
4. All found defects are logged in the bug tracker and linked to respective test cases.
5. The Requirement Traceability Matrix (RTM) shows 100% coverage of functional requirements.

---

## 4. Risk Assessment & Mitigations

| Risk ID | Description | Severity | Probability | Mitigation Strategy |
| :--- | :--- | :--- | :--- | :--- |
| **R-01** | Third-party Mock Payment API might be down or slow, blocking checkout. | High | Medium | Implement mock API services inside the code to allow testing when the external payment simulator is down. |
| **R-02** | Late changes to requirements in the Sprint. | Medium | High | Maintain active communication between QA, BA, and Product Owner; dynamically adjust scope; execute targeted regression runs. |
| **R-03** | Automation scripts break due to frequent UI changes in early stages. | Medium | Medium | Use robust Page Object Model (POM) dynamic selectors (IDs, custom QA-specific data attributes) instead of fragile absolute XPaths. |
| **R-04** | Short timeline for execution of 100+ cases. | High | Low | Prioritize execution based on Risk (Checkout and Payment first) and leverage automated test scripts. |

---

## 5. Resource Planning

### 5.1 Human Resources
* **1 QA Lead:** Oversees strategy, test design review, defect triage, and writes Test Summary Reports.
* **2 QA Analysts (Manual):** Write test cases, execute scenarios, log defects, verify fixes.
* **1 QA Automation Engineer:** Implements and maintains the Selenium test suite.

### 5.2 Software/Hardware Resources
* **QA Environment:** ShopEase QA Sandbox URL.
* **Database Client:** DBeaver or SQLite CLI.
* **API Client:** Postman.
* **Code Editor:** VS Code / Python / Selenium / pytest.
* **Agile Management:** Jira Software (simulated).

---

## 6. Test Schedule

| Phase | Duration | Deliverable |
| :--- | :--- | :--- |
| **Phase 1: Test Design** | 3 Days | Test Scenarios, Test Cases, RTM |
| **Phase 2: Environment Setup** | 1 Day | Postman, DB Schema, Automation Boilerplate |
| **Phase 3: Test Execution (Run 1)** | 4 Days | Defect logging, Manual and API execution |
| **Phase 4: Defect Verification & Regression** | 2 Days | Re-testing, Selenium Suite Run |
| **Phase 5: Reporting & Closure** | 1 Day | Walkthrough, Test Summary Report, Closure Signoff |
