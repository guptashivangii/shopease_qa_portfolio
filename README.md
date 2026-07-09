# ShopEase – Software QA Portfolio

Welcome to the **ShopEase QA Project**! 

This repository showcases my approach to testing an e-commerce application from requirements analysis through manual testing, API testing, database validation, and Selenium automation using Python.

I created this project to demonstrate the testing workflow followed in a real software development environment and to strengthen my practical QA skills.
---

## Application Under Test (AUT) Overview: ShopEase

The application under test is an e-commerce website that allows users to register, browse products, manage a cart, place orders, and administer inventory. It provides enough functionality to demonstrate functional, API, database, and automation testing.

---

## Project Structure

The project is structured logically into several key modules, demonstrating competence across manual testing, API testing, database verification, automation testing (using Python & Selenium), agile test management (Jira simulation), and test metrics analysis:

```text
shopease_qa_portfolio/
│
├── README.md                           
│
├── docs/                               
│   ├── BRD.md                          
│   ├── SRS.md                          
│   └── Test_Plan.md                    
│
├── test_design/                       
│   ├── Test_Scenarios.md              
│   ├── Test_Cases.md                  
│   └── RTM.md                          
│
├── jira/                               
│   ├── Jira_Simulation.md              
│   └── Defect_Log.md                  
│
├── backend/                           
│   ├── API_Testing.md                  
│   └── Database_Testing.sql            
│
├── automation/                         
│   ├── pages/                        
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── registration_page.py
│   │   ├── search_page.py
│   │   └── cart_page.py
│   └── tests/                          
│       ├── conftest.py
│       └── test_suite.py
│
├── reports/                            
    ├── Test_Execution.md              
    ├── Test_Summary_Report.md          
    └── Defect_Summary_Report.md        
```
## Why I built this project

I wanted a project that covered the complete QA lifecycle instead of isolated examples. My objective was to practice documenting requirements, designing test cases, reporting defects, validating APIs and databases, and building a maintainable Selenium framework using the Page Object Model.
