# Milestone 4 Project – Full Stack Frameworks with Django – FitHub Fitness Subscription Application

---

## Links

- [Link to Live Website](https://fithub-rp-90631f751ed4.herokuapp.com/)
- [GitHub Project Repository](https://github.com/rpires71/milestone-4)

---

## Table of Contents

- [Milestone Project 4](README.md#milestone-project-4)
- [FitHub Fitness Subscription Application](README.md#fithub-fitness-subscription-application)
  - [Project Overview](README.md#project-overview)
  - [Project Goals](README.md#project-goals)
  - [Purpose of the Website](README.md#purpose-of-the-website)
  - [Target Audiences](README.md#target-audiences)
  - [Key Features and Skills Demonstrated](#key-features-and-skills-demonstrated)
  - [UX Strategy](#ux-strategy)
    - [Research and Planning](#research-and-planning)
    - [Design Principles](#design-principles)
    - [Testing and Feedback](#testing-and-feedback)
  - [Features](#features)
  - [Future Features](#future-features)
  - [Technologies Used](#technologies-used)
  - [Wireframes](#wireframes)
  - [FitHub Fitness Subscription Application Wireframes](#fithub-fitness-subscription-application-wireframes)
  - [FitHub — User Stories](#fithub--user-stories)
    - [User Story 1: Account Registration (Visitor)](#user-story-1-account-registration-visitor)
    - [User Story 2: Secure Authentication (Visitor / Member)](#user-story-2-secure-authentication-visitor--member)
    - [User Story 3: Browse Fitness Plans (Visitor / Member)](#user-story-3-browse-fitness-plans-visitor--member)
    - [User Story 4: View Fitness Plan Details and Access-Controlled Content (Member)](#user-story-4-view-fitness-plan-details-and-access-controlled-content-member)
    - [User Story 5: Subscribe to a Membership Plan (Member)](#user-story-5-subscribe-to-a-membership-plan-member)
    - [User Story 6: Manage or Cancel a Subscription (Subscriber)](#user-story-6-manage-or-cancel-a-subscription-subscriber)
    - [User Story 7: Add Products to the Shopping Cart (Member)](#user-story-7-add-products-to-the-shopping-cart-member)
    - [User Story 8: Update or Remove Shopping Cart Items (Member)](#user-story-8-update-or-remove-shopping-cart-items-member)
    - [User Story 9: Secure Checkout and Payment Processing (Member)](#user-story-9-secure-checkout-and-payment-processing-member)
    - [User Story 10: View Order Confirmation (Member)](#user-story-10-view-order-confirmation-member)
    - [User Story 11: View Order History (Member)](#user-story-11-view-order-history-member)
    - [User Story 12: Create, Update and Delete Product Reviews (Member)](#user-story-12-create-update-and-delete-product-reviews-member)
    - [User Story 13: Create, Edit and Delete Community Posts (Subscriber)](#user-story-13-create-edit-and-delete-community-posts-subscriber)
    - [User Story 14: View the Community Feed (Subscriber)](#user-story-14-view-the-community-feed-subscriber)
    - [User Story 15: Manage My Profile Information (Member)](#user-story-15-manage-my-profile-information-member)
    - [User Story 16: View a Personalised Dashboard (Member)](#user-story-16-view-a-personalised-dashboard-member)
    - [User Story 17: Delete My Account (Member)](#user-story-17-delete-my-account-member)
    - [User Story 18: Create, Edit and Archive Membership Plans (Admin)](#user-story-18-create-edit-and-archive-membership-plans-admin)
    - [User Story 19: Manage Shop Products (Admin)](#user-story-19-manage-shop-products-admin)
    - [User Story 20: View Orders and Subscribers (Admin)](#user-story-20-view-orders-and-subscribers-admin)
  - [FitHub Colour Palette Justification](#fithub-colour-palette-justification)
  - [Typography Justification for FitHub Website](#typography-justification-for-fithub-website)
  - [Accessibility Implementation, User Flow and Navigation Strategies](#accessibility-implementation-user-flow-and-navigation-strategies)
  - [Database Design for FitHub](#database-design-for-fithub)
  - [Django Framework Setup and Configuration](#django-framework-setup-and-configuration)
  - [Database Models Implementation](#database-models-implementation)
  - [Django Admin Configuration and Sample Data](#django-admin-configuration-and-sample-data)
  - [Test Plan](#test-plan)
    - [Testing Overview](#testing-overview)
    - [1. Functionality and Content Accuracy Testing](#1-functionality-and-content-accuracy-testing)
    - [2. Security and Access Control Testing](#2-security-and-access-control-testing)
    - [3. Payment and Integration Testing](#3-payment-and-integration-testing)
    - [4. Usability and Typography Testing](#4-usability-and-typography-testing)
    - [5. Responsiveness Testing](#5-responsiveness-testing)
    - [6. Accessibility Testing](#6-accessibility-testing)
    - [7. Performance Testing](#7-performance-testing)
    - [8. Regression Testing](#8-regression-testing)
    - [9. Python/Django Automated Testing](#9-pythondjango-automated-testing)
    - [10. Code Validation and Static Analysis](#10-code-validation-and-static-analysis)
    - [11. Defect Log](#11-defect-log)
- [Heroku Deployment](#heroku-deployment)
  - [Introduction](#introduction)
  - [Live Application](#live-application)
  - [Deployment Configuration](#deployment-configuration)
  - [Deployment Process](#deployment-process)
  - [Project Files for Deployment](#project-files-for-deployment)
  - [Static Files Handling](#static-files-handling)
  - [Database](#database)
  - [Stripe Configuration](#stripe-configuration)
  - [Stripe Webhook Configuration](#stripe-webhook-configuration)
  - [Email Configuration](#email-configuration)
  - [Deployment Checklist](#deployment-checklist)
  - [Deployment Verification](#deployment-verification)
  - [Monitoring and Logs](#monitoring-and-logs)
  - [Deployment Performance Optimisation](#deployment-performance-optimisation)
  - [Security Configuration](#security-configuration)
  - [Deployment Commands Reference](#deployment-commands-reference)
  - [Troubleshooting](#troubleshooting)
  - [Continuous Deployment](#continuous-deployment)
  - [Production Environment Validation](#production-environment-validation)
  - [Conclusion](#conclusion)
- [Django Admin Interface](#django-admin-interface)
- [Reflection](#reflection)
- [Credits](#credits)
- [References](README.md#references)

---

# Milestone Project 4

Development Milestone Project 4 – **Full Stack Frameworks with Django**

[⬆ Back to Table of Contents](#table-of-contents)

---

# FitHub Fitness Subscription Application

[⬆ Back to Table of Contents](#table-of-contents)

---

## Project Overview

[⬆ Back to Table of Contents](#table-of-contents)

As part of the **Level 5 Diploma in Web Application Development** (**Code Institute**, 2025), and for **Full Stack Frameworks with Django – Milestone Project 4**, I developed **FitHub**, a **full-stack, database-driven web application** designed to simulate a real-world subscription-based fitness community platform.

Through an intuitive online interface, users are able to **join a fitness community, select personalised exercise and nutrition plans, purchase branded merchandise, and manage their subscriptions**. The platform has been designed to provide a consistent and user-friendly experience across desktop, tablet, and mobile devices through the implementation of **responsive design, accessibility, and usability principles**.

Following modern **user-centred design standards**, the application supports a clear and logical user journey through structured navigation, a strong **visual hierarchy**, and the use of **semantic HTML**. Features such as subscription-based registration, e-commerce transactions, and community engagement further enhance the overall user experience.

From a technical perspective, the project uses **Python** and the **Django framework** to manage full-stack application logic, alongside **HTML5, CSS3, Bootstrap 5, JavaScript, and Django template-based rendering** for the front-end presentation layer. Comprehensive **CRUD (Create, Read, Update, Delete)** functionality is fully implemented across multiple specialised Django applications, including **accounts, plans, shop, community, and subscriptions**.

The system uses a **PostgreSQL relational database** to securely store, retrieve, update, and manage user profiles, subscriptions, products, fitness plans, and community content. To maintain data integrity and security, the project incorporates **permission-based access control, authentication, authorisation, error handling, and both client-side and server-side validation**.

The application integrates **Stripe payment processing** to support subscription billing and one-off purchases, including branded merchandise and fitness plans. In addition, **Stripe webhook handlers** are used to manage asynchronous payment events and ensure accurate subscription and order processing.

Secure user registration and account management are handled through **django-allauth**, allowing different permission levels for administrators, subscribers, and standard users.

The project follows modern professional development and deployment practices, including:

- Deployment to the **Heroku cloud hosting platform**
- Use of a **PostgreSQL production database**
- Management of dependencies through **requirements.txt**
- Separation of **development and production settings**
- Use of **environment variables** for sensitive configuration data
- A comprehensive testing strategy incorporating both **manual and automated testing**
- Application of **Test-Driven Development (TDD)** principles where appropriate

As part of the project submission, extensive testing was carried out to verify the application's functionality, responsiveness, usability, e-commerce workflows, payment processing, and data handling procedures.

Overall, **FitHub** demonstrates my ability to design and develop a **publishable, production-grade full-stack web application** using modern development frameworks and industry best practices. The project combines robust back-end development, relational database management, real-world payment integration, community-driven functionality, and user-focused design principles to deliver a scalable, secure, and practical fitness subscription platform.

---

## Project Goals
 
[⬆ Back to Table of contents](#table-of-contents)
 
By utilising an intuitive and secure platform, users will be able to **participate in an active fitness community, access personalised nutrition and training programmes, purchase premium merchandise, manage their subscriptions, and provide feedback regarding their positive experiences**, which represents the primary objective of the **FitHub** project. The application will be designed and developed as a full-stack, user-centred web solution.

The requirements outlined in the Code Institute Full Stack Frameworks with Django – Milestone Project 4 specification (Code Institute, 2025) are comprehensively fulfilled through the implementation of database-driven functionality, full-stack framework integration, responsive user interface design, accessible navigation systems, real-world payment processing, and extensive testing procedures, all of which contribute towards the successful achievement of the project objectives.

### 1. Dynamic Full-Stack Functionality

To enable users to create their profiles, search for and purchase products and plans, comment on and contribute to community posts, and manage subscriptions, the application incorporates **CRUD (Create, Read, Update, Delete)** functionality across the five Django specialist applications: **accounts, plans, shop, community, and subscriptions**.

By utilising template-based views, dynamic content is rendered, demonstrating that all server-side operations are processed using **Python and Django**. To ensure persistent, secure, and consistent user sessions, data is stored and managed securely using a **relational PostgreSQL database**. A seamless user experience is supported, and data integrity is maintained through **server-side and client-side validation** mechanisms.

Asynchronous payment events, subscription renewals, cancellations, and access-control operations are managed using **webhook handlers** to maintain accurate billing records, while one-time purchases (merchandise and exercise/nutrition plans) and recurring subscription payments are processed through **Stripe payment integration**. Both technologies are fully integrated within the application.

### 2. Responsive and Accessible User Experience

Regardless of device type or screen size, accessibility and usability are ensured through the project's design, delivering consistency and responsiveness across desktop, tablet, and mobile devices.

In accordance with the **Web Content Accessibility Guidelines (WCAG) 2.1 Level AA**, accessibility considerations have been incorporated, including semantic HTML markup, clear navigation hierarchies, readable typography, appropriate colour contrast ratios, ARIA labels, alternative text for images, and meaningful form validation feedback to support inclusive user interaction (W3C, 2023).

Professional visual consistency and responsive grid-based layouts are maintained across all pages and components through the implementation of the CSS framework **Bootstrap 5**.

### 3. User Interaction and Feedback

User registration, plan purchases, product reviews, community posts, subscription management, and payment transactions represent the primary interactions provided by the system, all of which deliver clear and immediate feedback (Nielsen, 2020).

Server-side and client-side validation mechanisms ensure that user input data is accurate, complete, and correctly formatted prior to being stored within the system (MDN Web Docs, 2024). Throughout critical workflows — including subscription checkout, cancellation procedures, and community interactions — users are guided through the process using user-friendly **flash messages** and **modal confirmations**, which highlight required corrections and confirm successful actions (W3C, 2023).

To keep users informed of processing status and prevent accidental duplicate submissions, progress indicators and loading states are implemented during long-running operations, such as Stripe Checkout payment processing (Stripe, 2025).

### 4. Information Architecture and Navigation

To ensure that users can efficiently navigate between the key sections — **Home**, **Dashboard**, **Shop**, **Plans**, **Community**, and **Account Settings** — a logical information architecture is implemented through a clear page hierarchy and consistent navigation structure.

The use of semantic HTML enhances accessibility, maintainability, and search engine optimisation (SEO), while supporting best practices in modern web application development (Mozilla Developer Network, 2024). Conditional navigation is implemented to ensure that only authenticated users can access subscriber-exclusive content, while non-subscribers are presented with a teaser page designed to encourage subscription conversions.

Permission-based access control ensures that users can only view and modify their own data, while administrative functionality — including the creation of plans and products — is restricted exclusively to staff members. To enforce these permissions consistently throughout the application, **decorator-based view protection** (@login_required, @staff_member_required, @subscription_required) is implemented.

### 5. Secure Data Handling and Configuration

With the use of **environment variables** and a .env file to ensure security and flexibility across development and deployment environments, sensitive configuration data — including secret keys, Stripe API credentials, and environment-specific settings — are securely managed.

Secure authentication and authorisation mechanisms for user registration, login, password reset, and session management are provided by **django-allauth**. To prevent unauthorised access to profile data, community content, and subscription information, all sensitive views require authenticated user access.

User input validation across all forms and external API failures (e.g., Stripe errors) are handled gracefully through the application’s implementation of appropriate **error handling and data validation mechanisms**, protecting user data and maintaining system stability.

To prevent N+1 query issues and ensure responsive page loading times, database queries are optimised using **select_related() and prefetch_related()**. Throughout the codebase, compliance with **PEP 8 code style conventions** and adherence to **DRY (Don't Repeat Yourself) principles** are maintained.

### 6. Payment Processing and Subscription Management

Support for secure payment processing is implemented through the integration of Stripe within the application using two revenue models:
 
- **One-time purchases:** Directly through Stripe Checkout, users can buy individual products and plans.

- **Subscription-based access:** Users can subscribe to monthly or annual plans to access subscriber-only content (community, exclusive plans, members-only merchandise).

Without requiring the user to refresh the page **webhook handlers** (`checkout.session.completed`, `invoice.paid`, `customer.subscription.deleted`, `subscription.updated`) asynchronously process payment events and update subscription statuses in real-time.

During development, **Stripe test cards** are utilised to verify all payment workflows — including successful transactions, declined cards, and 3D Secure authentication — with comprehensive documentation of test results provided within the project README.

### 7. Testing and Quality Assurance

A **Test-Driven Development (TDD)** approach is employed throughout this project, with failing unit tests written prior to implementation. Through a clear Git commit history demonstrating that tests were created before features were implemented, this approach ensures rigorous code coverage and reflects disciplined software development practices.
  
**Automated unit tests** cover all major functionality:

- Model methods and relationships
- View permissions and access control
- Form validation
- Stripe webhook handlers (using mocked Stripe payloads)
- User authentication and profile creation

**Manual testing** validates end-to-end user journeys:

- User registration -> profile creation -> subscription -> community access
- Product browsing -> checkout -> order confirmation
- Subscription cancellation and renewal workflows
- Browser compatibility (Chrome, Firefox, Safari, Edge) across mobile, tablet, and desktop

**Code validation** ensures compliance with modern development standards:

- **W3C HTML Validator:** Zero errors
- **Jigsaw CSS Validator:** Zero errors
- **JSHint:** No major JavaScript issues
- **PEP 8:** Python code style compliance

### 8. Version Control and Deployment

Throughout the development of this project, **Git and GitHub** version control are utilised to document development progress in a transparent and professional manner, track modifications, and manage source code versioning. Clear and descriptive commit messages following a structured format (`feat:`, `fix:`, `test:`, `docs:`, etc.) are implemented for each new feature and bug fix.

Understanding of modern deployment workflows for production-grade full-stack applications is demonstrated through the deployment of the final version of the application using **Heroku**, a cloud-based hosting platform with **PostgreSQL** database support, ensuring public accessibility (Code Institute, 2025).

Without requiring code modifications, production (PostgreSQL, 2025) and development (SQLite, 2025) environments are executed using **environment-specific configuration** within the same codebase. All sensitive configuration variables are managed securely through Heroku Config Vars, and **DEBUG mode** is disabled in the production environment.

### 9. Documentation and Attribution 
 
Comprehensive project documentation is provided within the **`README.md`** file, including:
 
- **Project rationale** and business justification
- **User stories** and target audience analysis
- **Entity Relationship Diagram (ERD)** documenting the database schema
- **Wireframes** for key user journeys
- **Feature descriptions** supported by screenshots
- **Installation and deployment instructions** for local development and Heroku deployment
- **Testing procedures** and documented results
- **Credits and attribution** for all external libraries, tutorials, and resources

### Outcome 
 
Through the successful achievement of these objectives, **FitHub** demonstrates advanced proficiency in **full-stack web application development using modern frameworks**. The project incorporates the effective implementation of Django, database architecture, secure payment integration, asynchronous webhook processing, user authentication systems, and community-driven functionality to deliver a fully operational subscription-based fitness platform.
 
The completed application reflects both **professional presentation and technical competence**, demonstrating a comprehensive understanding of:

- **User-centred design** and accessibility
- **Secure data management** and payment processing
- **Test-driven development** and software quality assurance
- **Real-world web application development practices** at Level 5
- **Business logic implementation**, including dual revenue models, permissions, and access control.

Aligned with the standards expected within **Level 5 Web Application Development**, the project demonstrates production deployment readiness and advanced capability in the development of scalable, secure, and user-focused web applications.

---

## Purpose of the Website
 
[⬆ Back to Table of contents](#table-of-contents)

My **Full Stack Frameworks with Django – Milestone Project 4**, which forms a core component of the **Level 5 Diploma in Web Application Development**, is based on the development of **FitHub**.
 
A fully functional subscription-based fitness community platform is the result of the project’s demonstration of the practical application of **full-stack web development**, **modern payment processing**, **database-driven functionality**, **test-driven development**, and **user-centred design**. Through an intuitive and structured web interface, the system enables users to manage subscriptions, share success stories, purchase branded merchandise, nutrition and personalised exercise plans, join a fitness community, and create accounts.
 
Handling both one-time purchases and recurring subscription billing through asynchronous webhook handlers, the application integrates **real-world payment processing** via **Stripe**. Users are able to register, subscribe to membership tiers, access subscriber-exclusive community content, purchase products and plans, and manage their fitness profiles and subscriptions, reflecting a real-world fitness startup environment within the system design. To ensure efficient control over platform operations and business logic, administrators are able to create and manage plans, products, and content through a protected administration interface.

To ensure data integrity, security, and a reliable user experience, the application has been developed using **Django**, **Python**, **HTML5**, **CSS3**, **JavaScript**, **Bootstrap 5**, and **PostgreSQL**, incorporating **template-based rendering**, **comprehensive CRUD functionality**, **form validation**, **permission-based access control**, and **payment webhook handlers**. To guarantee accessibility and usability across desktop, tablet, and mobile devices, responsive design principles and **semantic HTML** are implemented. Through the utilisation of ARIA labels, alternative text, colour contrast ratios, and inclusive navigation structures, **WCAG 2.1 Level AA** accessibility standards are satisfied.

**Professional full-stack development standards** are adhered to through the implementation of:

- **Secure authentication and authorisation** mechanisms using **django-allauth** to support user registration, login functionality, and permission-based access control

- **Test-Driven Development (TDD)** practices supported by a comprehensive automated test suite, demonstrating development discipline and software quality assurance

- **Environment-based configuration management**, including the secure storage of sensitive information (API keys and secret keys) through the use of environment variables

- **Structured application architecture** implemented across five specialised Django applications: **accounts**, **plans**, **shop**, **community**, and **subscriptions**

- **Real-world payment integration** via Stripe, including webhook handlers for asynchronous transaction and subscription management

- **Database query optimisation** using `select_related()` and `prefetch_related()` to prevent N+1 query issues and improve application performance

- **Professional code standards** adhering to PEP 8 style guidelines and DRY (Don't Repeat Yourself) principles, version control is maintained using **Git and GitHub**, with clear, descriptive commits documenting the development process and demonstrating progressive feature implementation. The final application is deployed to **Heroku** with a **PostgreSQL** database, ensuring public accessibility, scalability, and compliance with modern cloud deployment practices.

The ability to translate real-world business requirements — including a dual revenue model (subscriptions and e-commerce), community engagement functionality, and secure payment processing — into a scalable, database-driven solution is demonstrated through the completed **FitHub** application, a polished, professional, and accessible web platform. In alignment with industry expectations for Level 5 web application development, the project reflects both **advanced technical proficiency** and **professional presentation**, showcasing readiness for production deployment and real-world application environments.

---

## Target Audiences
 
[⬆ Back to Table of contents](#table-of-contents)

**FitHub** has been specifically developed to meet the requirements of several interconnected user groups with a shared interest in fitness, health, and wellbeing. The target audience will experience a user interface that prioritises **accessibility**, **clarity**, **community engagement**, and **operational efficiency** (W3C, 2023; Interaction Design Foundation, 2023), supported by customised functionality.

### 1. Fitness Enthusiasts and Gym-goers

With the provision of a simple and intuitive interface, the target audience will be able to access a supportive community, explore personalised nutrition and exercise plans, and purchase branded fitness products through a platform designed to help fitness enthusiasts engage with its features efficiently and effectively. For individuals seeking a reliable and convenient method of progressing their fitness journey, the platform also provides support from experienced coaches and like-minded community members.

### 2. Health-Conscious Individuals and Wellness Seekers

From beginners establishing healthy habits to advanced athletes seeking to achieve performance excellence, this website is designed to accommodate these target audiences. With a responsive design that ensures users can view plans, join the community, and manage subscriptions efficiently across mobile devices, tablets, and desktop systems, the platform supports users who may prioritise flexibility and on-the-go access.

When committing to personalised fitness and nutrition guidance, the platform reduces friction and enhances user confidence by streamlining the registration, subscription, and plan-purchase processes. Users can discover content relevant to their specific fitness goals (weight loss, muscle gain, endurance, flexibility) through a platform that provides clear informational content, structured subject material, and accessible navigation.

### 3. Fitness Coaches and Content Creators

**FitHub** provides a secure and centralised environment for creating, managing, and monetising personalised exercise and nutrition plans, which are functions specifically targeted towards fitness professionals and coaches. Authorised staff members can efficiently create new plans, upload product listings, monitor community engagement, and track subscription metrics, supporting business operations and revenue management through the use of a protected administrative interface.

By combining digital product sales with community-driven engagement and recurring subscription revenue, coaches can develop a sustainable business model, while the functionality reflects real-world fitness coaching and online education workflows.

### 4. Community Members and Peer Support Groups

Through an inclusive and welcoming environment, the subscriber-only community section enables users to provide peer support, celebrate achievements, and share their fitness progress. By building social connections with users pursuing similar fitness goals and commenting on others’ achievements, members can share their experiences.

Through this community-driven approach, a sense of belonging and mutual accountability beyond transactional product purchases is established, enhancing user retention, motivation, and long-term platform engagement.

### 5. Business Owners and Fitness Platform Entrepreneurs 
 
A scalable and commercially viable business model is demonstrated by **FitHub** for entrepreneurs and business leaders seeking to launch fitness subscription platforms, combining multiple revenue streams — including subscriptions, product sales, and plan purchases — with secure payment integration and community engagement functionality. Best practices relating to subscription management, customer retention strategies, and community-platform development are showcased throughout the application.
 
Valuable reference material for the development of comparable platforms is provided through the transparent and well-documented codebase, together with the deployment infrastructure, illustrating how a competitive market-ready solution can be achieved through the combination of technical sophistication and user-centred design.

### 6. Educators and Technical Assessors
 
Effective implementation of **full-stack web development principles** is demonstrated throughout the project, including:
 
- Separation of concerns through a multi-app Django architecture
- Stripe integration for real-world payment processing (subscriptions and e-commerce)
- Comprehensive automated testing through a Test-Driven Development (TDD) methodology
- Permission-based access control with secure user authentication
- Performance-focused database design and optimisation
- WCAG 2.1 Level AA compliant responsive and accessible design

For educators, technical assessors, and professional reviewers seeking insight into modern production-grade full-stack web applications, the project serves as a valuable reference resource. The manner in which **advanced technical functionality**, **business logic implementation**, **accessibility compliance**, **payment-processing systems**, and **professional presentation standards** are combined demonstrates how a robust real-world web solution suitable for commercial deployment can be developed (Code Institute, 2025).

---

## Key Features and Skills Demonstrated
 
[⬆ Back to Table of contents](#table-of-contents)

The successful development of **FitHub**, an interactive, community-driven full-stack web application, demonstrates a high level of technical proficiency, advanced software engineering practices, and professional design principles. Through the application of modern web technologies, full-stack framework implementation, real-world payment integration, test-driven development methodologies, and recognised accessibility standards, a secure, dependable, and user-friendly subscription-based fitness community platform has been delivered.

### Database-Driven Functionality and Full-Stack Processing

To facilitate real-world subscription and e-commerce functionality, the storage and management of user profiles, fitness plans, products, orders, community posts, and subscription information are supported through the implementation of a **relational PostgreSQL database** distributed across five specialised Django applications. Comprehensive data management is achieved through the incorporation of full **CRUD (Create, Read, Update, Delete)** functionality across all core features, including plans, products, community posts, orders, and subscriptions (Code Institute, 2025).

Secure and efficient processing of plan browsing, product purchases, community interactions, subscription administration, and form submissions is enabled through server-side logic developed using **Python and the Django web framework**. To enhance data retrieval performance and support application scalability, **database optimisation techniques**, including `select_related()` and `prefetch_related()`, are utilised to mitigate N+1 query issues and maintain responsive system performance (Django Software Foundation, 2024).

### Real-World Payment Processing and Subscription Management

Support for two distinct revenue models is provided through the integration of **Stripe payment processing** within the application:

- **One-time purchases:** Secure card transactions and payment method tokenisation are facilitated through product and plan purchases using the Stripe Checkout API.
- **Subscription billing:** Access to recurring monthly and annual subscription services is managed through automated renewals, cancellation handling, and dunning workflows.

Real-time updates to subscription status and access permissions are achieved through **webhook handlers** that asynchronously process Stripe events (`checkout.session.completed`, `invoice.paid`, `customer.subscription.deleted`, `subscription.updated`) without requiring manual user intervention. To maintain reliable payment processing and prevent duplicate event execution, **idempotency checks** are implemented through a `StripeEvent` model, ensuring that webhook events are processed only once (Stripe Developer Documentation, 2025).

The practical implementation of production-grade payment infrastructure and subscription-based business logic suitable for real-world deployment is demonstrated through these features.

This section demonstrates the practical implementation of production-grade payment infrastructure and subscription-based business logic suitable for deployment within a real-world environment.

### Test-Driven Development and Code Quality

Throughout the development lifecycle, a **Test-Driven Development (TDD)** methodology is consistently employed, whereby failing unit tests are created prior to the implementation of application features. Evidence of this approach is reflected within the project's Git commit history, where test-related commits precede corresponding feature-development commits (for example, `test: add failing tests for shop views` followed by `feat: implement shop CRUD`).

The scope of **comprehensive automated testing** includes:

- Model methods and relationships across all five Django applications
- View-level permission validation and access-control mechanisms
- Form validation procedures and data-integrity checks
- Stripe webhook processing logic using mocked Stripe payloads
- User authentication workflows and profile-generation functionality

Adherence to established **code quality standards** is maintained through:

- **PEP 8 compliance** across the Python codebase
- Application of **DRY (Don't Repeat Yourself) principles** to reduce code duplication
- The use of **descriptive variable and function naming conventions** to improve readability and maintainability
- **Structured exception handling** using `try/except` blocks for external API integrations and error management

### Multi-Application Architecture and Separation of Concerns

Advanced architectural design is demonstrated throughout the project through the implementation of five specialised Django applications, each responsible for a distinct area of functionality:

- **accounts:** Management of user authentication, user profiles, and fitness objectives
- **plans:** Creation, browsing, and purchasing of exercise and nutrition plans
- **shop:** Administration of the product catalogue, order processing, and product reviews
- **community:** Subscriber-exclusive success-story sharing and peer-to-peer engagement
- **subscriptions:** Management of subscriptions, Stripe customer records, and webhook event processing

Code reusability, independent testing, and scalable feature development are facilitated through the adoption of this modular architecture. To preserve referential integrity and minimise data duplication, **model relationships** (`OneToOne`, `ForeignKey`, and `ManyToMany`) are structured appropriately in accordance with relational database design principles (Django Software Foundation, 2024).

### Permission-Based Access Control and Security

Robust **permission-based access control mechanisms** are implemented throughout the application to ensure that access to functionality and data is restricted according to user roles and subscription status:

- Public content, including the home page, shop, and plans sections, can be viewed by anonymous users; however, access to community features and purchasing functionality is restricted to registered and subscribed users.
- Authenticated users are permitted to create profiles, purchase plans and products, and manage their personal information.
- Access to the subscriber-exclusive community area is granted only to users with an active subscription.
- Protected administrative views enable staff members to create, update, and manage plans and products.
- Modification or viewing of data belonging to other users is prohibited for non-administrative accounts.

Consistent enforcement of access permissions across application views is achieved through the use of **decorators** (`@login_required`, `@staff_member_required`, `@subscription_required`), thereby preventing unauthorised access and inappropriate data manipulation. Secure user authentication, account registration, and session management are provided through **django-allauth** (Code Institute, 2025).

Protection of sensitive configuration data, including Stripe API credentials, secret keys, and database connection details, is achieved through the use of **environment variables**, ensuring that confidential information is excluded from version control repositories.

### Responsive and Accessible Interface Design

Consistent usability across desktop, tablet, and mobile devices is achieved through the implementation of **responsive web design techniques**, incorporating the **Bootstrap 5 CSS framework**, **CSS Grid**, **Flexbox**, and **media queries** (Bootstrap Documentation, 2024; Mozilla Developer Network, 2024).

Compliance with **Web Content Accessibility Guidelines (WCAG) 2.1 Level AA** is supported through the implementation of the following accessibility features:

- **Semantic HTML5** elements (`<nav>`, `<main>`, `<section>`, `<article>`, etc.) are utilised to communicate document structure effectively.
- **ARIA labels and attributes** are incorporated to enhance compatibility with assistive technologies.
- **Alternative text (alt text)** is provided for all images to describe their content and intended purpose.
- **Colour contrast ratios** are maintained in accordance with WCAG AA requirements (minimum 4.5:1 for text).
- A logical **heading hierarchy** (`<h1>` through `<h6>`) is employed to support content organisation and navigation.
- **Form labels** are explicitly associated with input elements to improve screen-reader accessibility.

An inclusive and accessible user experience is promoted through these design considerations, ensuring that the platform remains usable for individuals with visual, motor, cognitive, and auditory impairments (W3C, 2023).

### Dynamic User Interaction, Validation, and Feedback

Interactive functionality throughout the application is delivered through the implementation of the following mechanisms:

- **Template-based rendering** utilising Django's template engine to generate dynamic HTML content populated with user-specific information.
- **Server-side validation** applied across all forms (registration, profile editing, product reviews, and community posts) to ensure data accuracy and integrity prior to database storage.
- **Client-side validation** implemented through HTML5 form attributes and JavaScript to provide immediate feedback during user input.
- **Flash messages** used to communicate the outcome of user actions, including success, warning, and error notifications.
- **Progress indicators and loading states** incorporated into long-running processes, such as Stripe Checkout, to reduce the likelihood of accidental duplicate submissions.
- **Modal confirmation dialogs** utilised for potentially destructive actions, including subscription cancellations and post deletions.

Throughout key workflows, users are provided with clear and immediate feedback, promoting transparency and enhancing the overall user experience during registration, purchasing, community participation, and subscription management activities (Mozilla Developer Network, 2024).

### User-Centred Design and Visual Consistency

The development of the interface has been guided by **user-centred design principles**, with particular emphasis placed on clarity, intuitive navigation, accessibility, and visual appeal. To support user objectives and enhance overall usability, the following design considerations have been incorporated:

- A clear **information hierarchy** directs users towards primary actions, including subscribing, making purchases, and exploring the community section.
- **Consistent typography, colour schemes, and page layouts** are utilised to establish visual consistency throughout the platform.
- **Conditional navigation** dynamically displays or restricts features according to user authentication and subscription status.
- **Intuitive user journeys** reduce the number of steps required to complete essential tasks (register → subscribe → access community).
- **Visual feedback mechanisms**, including button states, hover effects, and loading animations, provide confirmation of user interactions.

By prioritising user experience throughout the design process, friction is minimised and efficient task completion is encouraged across all areas of the application (Interaction Design Foundation, 2023).

### Secure Configuration, Environment Management, and Deployment

Management of sensitive configuration information is achieved through the use of **environment variables** and a `.env` file, providing:

- **Secure isolation** between development and production environments
- **Flexible application configuration** across multiple deployment contexts without requiring code modifications
- **Protection of confidential information**, including API keys, database credentials, and secret keys, from exposure within version control systems

Deployment of the completed application is undertaken using **Heroku**, a cloud-based hosting platform that provides:

- **Automatic scaling capabilities** to accommodate fluctuations in user traffic
- **Managed PostgreSQL database support** with integrated backup functionality
- **Centralised environment variable management** through Heroku Config Vars
- **SSL/TLS encryption** to secure data transmitted between clients and the application
- **Disabled DEBUG mode** within the production environment to minimise the risk of information disclosure

Through the adoption of these deployment and configuration management practices, alignment with modern full-stack application hosting standards is demonstrated, while also evidencing readiness for deployment within a production environment (Code Institute, 2025; Heroku Developer Centre, 2024).

### Version Control and Professional Development Workflow

Throughout the project development lifecycle, **Git and GitHub** were employed to support version control, project tracking, and professional software development practices. Their use facilitated:

- Version management through clear and descriptive commit messages
- Progress monitoring via a detailed and traceable development history
- Documentation of feature development, bug resolutions, and project documentation updates
- Collaboration and peer-review workflows where applicable
- Separation of development and production environments through dedicated branching strategies

By adopting this approach, iterative development, project transparency, and industry-standard software engineering practices are effectively supported (GitHub Guides, 2024; Code Institute, 2025).

**Target commit frequency:** Between 85 and 105 meaningful commits distributed across a 15-week development period, demonstrating disciplined working practices, consistent incremental progress, and sustained engagement throughout the project lifecycle.

### Comprehensive Documentation and Professional Code Standards

Comprehensive project documentation is provided through the **`README.md`** file, which includes:

- An overview of the project and its business rationale
- User stories and analysis of the intended target audience
- An Entity Relationship Diagram (ERD) illustrating the database structure
- Wireframes and supporting design rationale
- Detailed feature descriptions accompanied by screenshots
- Installation guidance and local development setup instructions
- Complete deployment procedures covering Heroku, PostgreSQL, and Stripe configuration
- Testing methodologies and documented results
- Credits and attribution for external resources, libraries, and supporting materials

To promote maintainability and adherence to professional development standards, the codebase follows **modular and structured development conventions**, including:

- The use of **descriptive variable and function names** to improve code clarity and readability
- **Inline documentation and comments** to clarify complex functionality and implementation logic
- A **logical file and directory structure** that organises related components according to their purpose
- Effective **separation of concerns**, ensuring static assets, templates, and Python application logic remain appropriately segregated
- Adherence to established **Django conventions** for model creation, view organisation, and URL configuration

Collectively, these practices support long-term maintainability, simplify the onboarding process for future developers, and demonstrate alignment with recognised professional software development standards (Code Institute, 2025; PEP 8 Style Guide, 2023).

### Advanced Features Demonstrating Professional Competence

A range of additional features have been incorporated to demonstrate professional-level development practices and advanced technical competence, including:

- **Robust error-handling mechanisms** featuring graceful degradation and user-friendly error pages (404, 403, and 500)
- **Comprehensive form validation** utilising both server-side and client-side verification to strengthen data integrity and protection
- **Email integration services** supporting user registration confirmations and password-reset workflows through **django-allauth**
- **Customised administrative interfaces** that provide staff members with an efficient and streamlined management environment
- **Database query optimisation techniques** designed to eliminate N+1 query issues and maintain responsive page performance
- **Security-enhancement measures** incorporating CSRF protection, SQL injection mitigation, and secure session-management practices

Collectively, these features demonstrate a comprehensive understanding of production-grade web application development while reflecting contemporary industry standards and recognised best practices.

**Overall**, a high level of proficiency in full-stack web application development is demonstrated by **FitHub** through the effective application of modern frameworks, real-world payment integration, scalable database architecture, test-driven development methodologies, user-centred design principles, security best practices, and professional deployment strategies. Readiness for deployment within a real-world environment is evidenced throughout the project, while the technical expertise, design capability, and professional development practices exhibited align with the expectations associated with Level 6 of the UK Higher Education Framework.

---

## UX Strategy
 
[⬆ Back to Table of Contents](#table-of-contents)
 
A **user-centred design methodology** underpins the UX strategy for **FitHub**, ensuring that the application effectively addresses the practical requirements of fitness enthusiasts, coaches, community participants, and administrators while maintaining accessibility, intuitiveness, engagement, and operational efficiency (Interaction Design Foundation, 2023).
 
Three core phases form the foundation of the strategy:
 
- Research and Planning
- Design Principles
- Testing and Feedback

Throughout the development process, particular emphasis is placed on **accessibility**, **clarity**, **responsiveness**, **community participation**, **data integrity**, and **ease of use**. These priorities align with the principles outlined within the **Web Content Accessibility Guidelines (WCAG) 2.1 Level AA** and recognised contemporary usability standards (W3C, 2023).

### Research and Planning
 
[⬆ Back to Table of Contents](#table-of-contents)
 
The primary focus of this phase is the identification and analysis of the key user groups associated with the fitness community platform, including:
 
- Fitness enthusiasts and gym-goers
- Health-conscious individuals and wellness seekers
- Fitness coaches and content creators
- Community members and peer-support groups
- Business owners and fitness entrepreneurs
- Educators and technical assessors

An understanding of user requirements, expectations, and objectives is developed through the creation of **user personas** and **usage scenarios**, which reflect real-world interactions commonly associated with fitness platforms, including:
 
- Browsing exercise and nutrition plans according to fitness goals and difficulty levels
- Evaluating subscription options and making informed purchasing decisions
- Registering accounts and creating personalised fitness profiles
- Completing payment transactions for plans and merchandise
- Accessing the subscriber-exclusive community and sharing success stories
- Engaging with peer-generated content through comments and support
- Managing subscription status and membership cancellations
- Creating, updating, and administering plans and products (coaches and administrators)

Key areas of research include:
 
- User expectations when discovering and purchasing fitness plans online
- The information required before committing to a subscription service
- The role of community functionality in promoting engagement and user retention
- Methods used by coaches to manage multiple plans and monitor subscriber activity
- Payment processes that increase user confidence and minimise checkout abandonment
- The contribution of inclusive and accessible design to supporting users from diverse backgrounds and with varying abilities

To ensure relevance and usability across all user groups, features and content are prioritised according to user requirements. As a result, plan descriptions, pricing information, reviews, community functionality, checkout workflows, and administrative dashboards are presented clearly and structured for ease of understanding (Code Institute, 2025).

### Design Principles
 
[⬆ Back to Table of Contents](#table-of-contents)
 
#### Accessibility

Accessibility throughout the application is supported through the use of **Semantic HTML5**, logical heading structures, and inclusive design practices. Clear form labels, placeholder text, and validation messages are incorporated to assist screen-reader users and those relying on keyboard-only navigation. Interactive components utilise ARIA labels and roles to improve compatibility with assistive technologies. Compliance with WCAG AA colour-contrast requirements (4.5:1 for text) is maintained, while readable typography contributes to an inclusive user experience across plan browsing, checkout workflows, and community interactions (W3C, 2023).

#### Responsiveness

Consistent usability across desktop, tablet, and mobile devices is achieved through a mobile-first design strategy implemented using the **Bootstrap 5 CSS framework**, **CSS Grid**, **Flexbox**, and **media queries** (Bootstrap Documentation, 2024; Mozilla Developer Network, 2024). Plans, products, community content, checkout forms, and navigation components adapt seamlessly to varying screen sizes and device orientations.

#### Navigation

Intuitive movement between major application areas, including **Home**, **Dashboard**, **Plans**, **Shop**, **Community**, and **Account Settings**, is facilitated through a clear and consistent navigation structure. Public content remains accessible to anonymous users, while subscriber-exclusive functionality is revealed through conditional navigation controls. User journeys are structured to minimise friction between registration, subscription, and community participation activities (Interaction Design Foundation, 2023).

#### Visual Hierarchy

User attention is directed towards key actions, such as subscribing, purchasing plans, completing transactions, participating within the community, and managing subscriptions, through the strategic application of typography, spacing, colour, and layout consistency. White space is utilised effectively to reduce cognitive load, improve readability, and highlight important information (Mozilla Developer Network, 2024).

#### Information Architecture

A logical organisational structure is applied to plans and products by grouping content according to category, difficulty level, and pricing. Community content is presented chronologically and supplemented with filtering capabilities. Information is prioritised according to user needs, ensuring that primary actions, such as subscribing and browsing plans, remain prominent, while secondary actions, including account management and support resources, remain easily accessible without creating visual clutter.

#### Community Engagement

Peer support and user motivation are encouraged through the design of the community section, which incorporates:

- Prominent presentation of success stories and achievements
- Comment-based discussions that encourage user interaction
- Visual activity indicators, including post and comment counts
- Notifications and content feeds designed to promote ongoing participation
- Subscriber-exclusive access, reinforcing the value of the membership offering

These features collectively contribute to the development of an active and engaged user community.

#### Interactivity

Meaningful user interaction is supported through plan browsing, product filtering, checkout processes, subscription management, community participation, and administrative functionality. Clear calls to action guide users through critical workflows, including registration, profile creation, subscription activation, and community access. Loading indicators and progress states are incorporated into long-running operations, such as Stripe Checkout, to maintain transparency and reduce accidental duplicate submissions.

#### Trust and Credibility

User confidence is strengthened through the inclusion of product reviews, five-star rating systems, transparent pricing structures, and detailed plan descriptions. Where applicable, coach credentials provide additional credibility. Secure checkout workflows, SSL encryption indicators, and clear payment-processing information further reassure users during financial transactions. Community success stories contribute valuable social proof and reinforce trust in the platform.

#### Performance

Responsive application performance is achieved through efficient server-side processing, database-query optimisation using `select_related()` and `prefetch_related()`, and the use of compressed static assets. Community feeds, plan browsing, and transaction processing benefit from fast response times, while progressive page loading ensures that above-the-fold content is prioritised without unnecessary delays.

#### Error Handling and Validation

Data accuracy and completeness are maintained through comprehensive server-side and client-side validation procedures covering registration details, profile information, payment data, and community content. User-friendly validation messages provide clear guidance on corrective actions, while confirmation notifications reinforce successful task completion. Graceful handling of external service failures, including Stripe API issues, ensures that users receive meaningful feedback and appropriate next-step guidance (Code Institute, 2025).

#### Feedback and Confirmation

Immediate and contextual feedback is delivered through **flash messages**, informing users of the outcome of their actions. Examples include:

- "Successfully subscribed! Welcome to the community."
- "Payment failed. Please try a different card or contact support."
- "Your post has been shared with the community."
- "Subscription cancelled. You have access until [date]."

To minimise accidental data loss, confirmation modal dialogues are implemented for destructive actions, including subscription cancellations and post deletions.

### Testing and Feedback
 
[⬆ Back to Table of Contents](#table-of-contents)
 
Consistent functionality, responsiveness, and user engagement are verified through manual usability testing conducted across **desktop**, **tablet**, and **mobile** devices. Particular attention is given to the following areas:
 
- Plan browsing and filtering workflows
- Subscription checkout and payment processes
- Community participation, including posting and commenting
- Profile administration and preference management
- Administrative creation and management of plans and products
- Permission-controlled access to subscriber-exclusive and public content

To validate application functionality and user experience, the following testing methodologies are employed:
 
- **User journey testing**, replicating real-world workflows such as registration → subscription → community access → plan purchase
- **Form validation testing**, assessing the handling of missing, invalid, or incomplete data across registration, profile editing, plan creation, product review, and checkout forms
- **CRUD functionality testing**, verifying the creation, retrieval, modification, and deletion of plans, products, posts, comments, and subscriptions
- **Permission and access-control testing**, ensuring subscriber-only content remains inaccessible to unauthenticated users and administrative functionality is restricted to authorised staff members
- **Payment workflow testing** using Stripe test cards (successful transactions, declined payments, and 3D Secure authentication) to validate checkout processes and webhook functionality
- **Cross-browser testing** across Chrome, Firefox, Safari, and Edge environments (Mozilla Developer Network, 2024)
- **HTML and CSS validation** using W3C validation tools to verify standards compliance and semantic markup implementation (W3C, 2023)
- **Keyboard accessibility testing**, confirming that all interactive elements can be operated using keyboard controls alone (Tab, Enter, Escape)
- **Screen-reader testing** using NVDA and JAWS to ensure content is announced correctly and navigation structures remain logical and accessible (WebAIM, 2023)

Assessment of performance and accessibility is undertaken through the use of:

- **Google Lighthouse**, evaluating performance, accessibility, search engine optimisation (SEO), and adherence to best practices
- **Browser developer tools**, supporting responsive-design verification, console error monitoring, and network-performance analysis
- **WAVE (Web Accessibility Evaluation Tool)**, identifying accessibility concerns and validating ARIA implementation
- **HTML and CSS validators**, ensuring code quality and compliance with recognised web standards

Given that fitness enthusiasts frequently interact with the platform whilst exercising or attending the gym, particular emphasis is placed on mobile usability. To enhance the user experience on smaller screens and touch-enabled devices, subscription management, checkout workflows, and community-content visibility are optimised for mobile interaction.

Accessibility evaluation focuses on the following key areas:

- **Colour-contrast verification** (4.5:1 for standard body text and 3:1 for larger text)
- **Font-size assessment**, ensuring readability through a minimum body-text size of 14px
- **Form labels and validation messages**, clearly associated with their corresponding input elements
- **Visible focus indicators** to support keyboard-based navigation
- **ARIA labels** applied to icon-only controls and interactive components
- **Heading structures** that provide a logical and meaningful document hierarchy

Insights obtained during testing activities are utilised to:

- Refine user journeys and minimise friction within critical workflows, including subscriptions and community engagement
- Improve the clarity of plan descriptions, pricing structures, and subscription benefits
- Enhance community features and moderation capabilities
- Optimise checkout processes to reduce cart abandonment rates
- Strengthen validation feedback and error-message clarity
- Improve accessibility for users with disabilities
- Enhance performance across slower devices and network connections

Potential areas for future A/B testing include:

- Subscription-pricing structures and feature allocation
- Community-feed layouts and engagement measurements
- Plan presentation methods and filtering functionality
- Call-to-action button wording and placement
- Email-notification frequency and content strategy

Continuous feedback from beta users, including early subscribers and fitness coaches, is incorporated into an iterative development process. This ongoing feedback cycle informs feature prioritisation and platform enhancements, ensuring that the application continues to evolve in response to user expectations and changing market requirements.

**Overall**, a comprehensive and user-centred design methodology is reflected throughout the UX strategy for **FitHub**, supporting the development of a sophisticated multi-user platform that effectively balances commercial objectives, including subscription services and product sales, with meaningful user engagement and community development. By prioritising accessibility, inclusivity, clarity, and operational efficiency across a diverse range of user groups and usage scenarios, the strategy supports both individual fitness achievements and collaborative community experiences.

---

## Features
 
[⬆ Back to Table of Contents](#table-of-contents)
 
Developed as a full-stack, database-driven web application, **FitHub** replicates the functionality of a real-world subscription-based fitness community platform. Through a structured and interactive user interface that aligns with contemporary web application standards, the system provides functionality that enables users to **create accounts, explore personalised exercise and nutrition plans, purchase branded fitness merchandise, subscribe to community-access features, share success stories with fellow members, and manage their subscriptions** (Code Institute, 2025).
 
The application places particular emphasis on **server-side processing and relational database integration** rather than relying on third-party fitness APIs or prebuilt subscription-management services. Secure and efficient management of user profiles, plan catalogues, product inventories, community-generated content, subscription billing, and payment transactions is achieved through the implementation of custom business logic and database-driven functionality.
 
All user information, including **fitness profiles**, **subscription records**, **purchase history**, and **community contributions**, is processed through validated data-entry mechanisms and stored within a **relational PostgreSQL database**. This approach ensures data persistence, maintains data integrity, and supports secure access-control procedures across the platform.

### Core Features
 
#### User Authentication and Profile Management
 
Secure account registration, user authentication, and session management are provided through the integration of **django-allauth**. Upon successful registration, a dedicated **UserProfile** is automatically generated for each user, storing fitness-specific information that supports personalisation and user engagement.
 
Profile data includes:
 
- **Fitness objectives** (weight loss, muscle gain, endurance, flexibility, and general fitness)
- **Experience categories** (beginner, intermediate, and advanced)
- **Physical measurements** (weight and height) used to support personalised plan recommendations
 
At any stage, users are able to update and manage their profile information through pre-populated forms designed to streamline data entry and enhance the overall user experience. Access to profile information is protected through **secure authentication mechanisms**, ensuring that users can view and modify only their own data, while permission-based decorators enforce access restrictions and prevent unauthorised interaction with protected resources.

#### Browse and Filter Plans
 
Discovery of **Exercise Plans** and **Nutrition Plans** is facilitated through the **Plans** section, allowing users to explore content aligned with their individual fitness objectives and experience levels. To support efficient navigation and plan selection, the following browsing capabilities are provided:
 
- **Plan catalogues** presenting the title, difficulty rating, duration, pricing information, and a concise overview of each plan
- **Category-based filtering** enabling plans to be refined by type (exercise or nutrition) and difficulty level
- **Comprehensive plan pages** containing detailed descriptions, trainer qualifications, anticipated outcomes, and customer feedback
- **Subscriber-only indicators**, including lock icons and prominent calls to action encouraging subscription upgrades
- **Responsive grid-based layouts** that automatically adapt to desktop, tablet, and mobile viewing environments

Flexible purchasing options are supported through a dual-access model, whereby plans are priced individually (£9.99–£49.99) while also being available as part of an active subscription, thereby supporting multiple revenue streams within the platform.

#### E-Commerce Shop and Product Management
 
Access to branded fitness merchandise, including clothing, supplements, equipment, and accessories, is provided through the **Shop** section of the platform. To support product discovery, purchasing, and post-purchase management, the following functionality is available:
 
- **Product catalogues** displaying images, descriptions, pricing information, and current stock availability
- **Advanced product filtering** based on category, price range, and popularity
- **Five-star review functionality** enabling users to submit ratings and detailed product feedback
- **Average rating indicators** displayed on product cards to assist users in making informed purchasing decisions
- **Shopping basket functionality** integrated with **secure Stripe Checkout** to facilitate one-time transactions
- **Order-confirmation pages** providing order references and estimated delivery schedules
- **Purchase-history records** allowing users to review previous orders and conveniently reorder products

Administrative management of products is performed through a protected interface, enabling authorised staff members to maintain inventory levels, update pricing structures, and efficiently manage the product catalogue.

#### Subscription Management
 
Access to subscriber-exclusive functionality within **FitHub** is provided through a **dual-tier subscription model**, offering users a choice between the following membership options:
 
- **Monthly subscription** (£9.99 per month) with automated recurring billing
- **Annual subscription** (£99.99 per year) charged as a single payment, providing a saving of approximately 17%

To support subscription administration and payment management, the platform incorporates the following features:
 
- **Subscription plan pages** presenting membership tiers, included features, and pricing information
- **Secure Stripe Checkout integration** utilising Stripe's Subscriptions API to process recurring payments
- **Subscription management dashboards** displaying the active membership tier, upcoming billing dates, and available cancellation options
- **Automated webhook processing** responsible for managing payment renewals, failed-payment scenarios, and subscription-status synchronisation
- **Flexible cancellation functionality** enabling users to terminate subscriptions at any time while retaining access until the end of the current billing cycle
- **Automatic renewal notifications** issued in advance of scheduled subscription charges

Implementation of the Stripe subscription infrastructure demonstrates the practical application of real-world recurring-payment systems, including the management of common edge cases such as failed transactions, expired payment methods, and customer-initiated cancellations.

#### Subscriber-Only Community
 
Exclusive access to the **Community** section is granted to paying subscribers, creating an environment that promotes peer support, accountability, and ongoing motivation. To encourage meaningful interaction and member engagement, the community incorporates the following functionality:
 
- **Success-story submissions** enabling subscribers to share fitness milestones, progress photographs, and personal experiences
- **Chronologically ordered feeds** presenting the most recent community posts first
- **Discussion threads** facilitating peer-to-peer conversations, encouragement, and knowledge sharing
- **Post-creation forms** incorporating title and content fields, input validation, and confirmation feedback upon successful submission
- **Post editing and deletion capabilities** restricted to the original author, ensuring users can manage only their own content
- **Comment-management controls** allowing users to remove their own comments through author-specific permissions
- **Community preview pages** for non-subscribers, highlighting selected activity and encouraging membership conversion
- **Responsive layouts** optimised to support seamless community interaction across desktop, tablet, and mobile devices

By fostering a sense of belonging, shared achievement, and mutual accountability, the community functionality enhances subscription value while contributing to long-term user engagement and retention.

#### Payment Processing and Order Management
 
Support for secure financial transactions within **FitHub** is delivered through the integration of **Stripe payment processing**, which is implemented across two distinct payment workflows:
 
##### One-Time Purchases (Shop)

The following functionality supports the processing of individual product transactions:

- **Stripe Checkout Sessions** utilised for secure product purchases
- **Card tokenisation and PCI-compliant payment processing** to protect sensitive payment information
- **Automatic order generation** following successful payment authorisation
- **Failed-payment management** providing clear error notifications and opportunities to retry transactions
- **Order-confirmation emails** containing purchase receipts and transaction details

##### Recurring Subscriptions

Subscription-based billing is facilitated through Stripe's recurring-payment infrastructure and includes:

- **Stripe Subscriptions API** supporting monthly and annual membership billing
- **Webhook event processing** (`checkout.session.completed`, `invoice.paid`, `customer.subscription.deleted`, `subscription.updated`) to manage asynchronous payment events
- **Idempotency controls** implemented to prevent duplicate webhook execution
- **Real-time subscription synchronisation** ensuring membership-status updates occur without requiring page refreshes
- **Automated handling of payment failures**, dunning processes, and customer-initiated cancellations
- **Stripe test-card compatibility** supporting development, quality assurance, and payment-workflow testing

To maintain transparency and enhance the user experience, comprehensive **payment feedback mechanisms** are incorporated throughout the checkout process, including:

- Clearly structured checkout workflows with transparent pricing and associated charges
- Success notifications confirming completed orders and active subscriptions
- Failure alerts providing actionable guidance, including payment retries and support options
- Loading states applied to checkout controls to minimise accidental duplicate submissions during transaction processing

#### Administrative Interfaces
 
Access to protected management functionality is provided exclusively to **staff members**, including coaches and administrators, through a dedicated set of administrative views designed to support platform management and operational activities.
 
The available administrative features include:
 
- **Exercise Plan creation interfaces**, enabling coaches to define new plans by specifying titles, descriptions, difficulty levels, durations, and pricing structures
- **Nutrition Plan management forms** incorporating similar functionality, tailored specifically to nutrition-focused content
- **Product administration tools** allowing the creation and management of shop inventory, including images, descriptions, pricing information, and stock levels
- **Order-management views** providing access to customer information, purchase records, and revenue-monitoring data
- **Community-content moderation functionality** (planned for future implementation), enabling the review of user-generated content and the removal of inappropriate material where necessary
- **Analytics dashboards** (future enhancement) designed to present subscription statistics, revenue performance, and user-engagement metrics

To ensure that administrative functionality remains secure and accessible only to authorised personnel, permission-based controls are enforced through the use of the `@staff_member_required` decorator.

#### Data Validation and Error Handling
 
Reliable data processing and application stability are maintained through the implementation of comprehensive validation and error-management mechanisms across all areas of user interaction.
 
The platform incorporates the following validation and error-handling features:
 
- **Form-validation procedures** applied to user registration (including email-uniqueness checks and password-strength requirements), profile updates, plan creation, product reviews, and community-content submissions
- **Server-side validation mechanisms** ensuring data accuracy and integrity before information is committed to the database
- **Client-side validation controls** utilising HTML5 constraints and JavaScript checks to provide immediate feedback during data entry
- **User-friendly validation messages** offering clear explanations of input errors alongside actionable guidance for resolution
- **Graceful API error management** addressing Stripe-related failures, timeout conditions, and network-connectivity issues
- **Custom error pages** (404, 403, and 500) designed to assist users in recovering from unexpected situations and navigating back to relevant content

By combining multiple layers of validation and error handling, the application promotes dependable data management, improves system reliability, and minimises user frustration throughout key workflows.

#### Responsive Design and Accessibility
 
Accessibility and responsive usability are fundamental design priorities throughout the application, ensuring a consistent and inclusive experience across a wide range of devices and user requirements.
 
The platform incorporates the following accessibility and responsive-design features:
 
- A **mobile-first development approach** implemented using the Bootstrap 5 CSS framework to provide a seamless user experience across multiple device types
- Compliance with **WCAG 2.1 Level AA accessibility standards**, including:
  - **Semantic HTML5 elements** (`<nav>`, `<main>`, `<section>`, `<article>`) to communicate document structure effectively
  - **ARIA labels and attributes** applied to form controls and icon-based interactive elements
  - **Alternative text (alt text)** provided for all images
  - **Colour-contrast ratios** meeting accessibility requirements (minimum 4.5:1 for standard text)
  - A logical **heading hierarchy** (`<h1>` through `<h6>`) supporting content organisation and navigation
  - Comprehensive **keyboard-navigation support** using controls such as Tab, Enter, and Escape
  - Compatibility with **screen-reader technologies** to improve accessibility for visually impaired users

- **Responsive grid-based layouts** designed to adapt effectively to mobile (320px), tablet (768px), and desktop (1024px+) viewport dimensions
- A **touch-optimised interface** incorporating appropriately sized buttons and interactive controls for mobile-device users
- **Progress indicators and loading states** displayed during long-running processes, such as Stripe Checkout transactions, to keep users informed of processing status
- **Flash-message notifications** providing immediate, contextual feedback in response to user actions and system events

Through the implementation of these accessibility and responsive-design practices, the platform promotes inclusivity, enhances usability, and ensures a consistent user experience regardless of device type, input method, or accessibility requirement.

#### Performance Optimisation
 
Application performance is enhanced through the implementation of a range of optimisation techniques designed to improve responsiveness, reduce resource consumption, and support scalability.
 
Key performance-enhancement measures include:
 
- **Database-query optimisation** through the use of `select_related()` and `prefetch_related()`, reducing unnecessary database requests and mitigating N+1 query issues
- **Compressed static resources**, including CSS and JavaScript assets, to minimise page-load times and reduce bandwidth usage
- **Progressive content delivery**, ensuring that essential information is displayed first while supplementary content is loaded subsequently
- **Efficient server-side rendering** using Django templates to limit unnecessary processing and improve response times
- **Caching mechanisms** applied to frequently accessed content, such as plan catalogues and product information, to reduce database load and accelerate content retrieval

Collectively, these optimisation strategies contribute to faster page rendering, improved scalability, and a more responsive user experience across the platform.

---

## Future Features
 
[⬆ Back to Table of Contents](#table-of-contents)
 
Several enhancements have been identified as part of the future development roadmap for **FitHub**, with the aim of strengthening personalisation, increasing user engagement, improving retention rates, and expanding operational functionality. These planned developments are intended to further enhance the platform whilst maintaining a secure, scalable, and data-driven environment.

### Enhanced Personalisation
 
Through a secure user dashboard, registered users will have the ability to **save favourite plans**, **create personalised workout schedules**, and **monitor progress metrics**, including weight, workout frequency, and personal performance records. To improve content discovery and support purchasing decisions, a planned **personalised recommendation engine** will evaluate factors such as fitness objectives, experience level, and previous purchase history, enabling the delivery of relevant plan and product recommendations while enhancing user engagement and conversion opportunities.

### Expanded Community Features
 
Community participation and social interaction will be further strengthened through the introduction of the following enhancements:
 
- **Follow functionality**, enabling users to subscribe to updates from preferred community members and receive notifications when new content is published
- **Likes and reaction mechanisms** applied to posts and comments, encouraging engagement and providing social recognition
- **Community-profile pages** displaying member achievements, activity badges (e.g., "100 Days Active"), and follower statistics
- **Community-based challenges**, such as a "30-Day Transformation Challenge", incorporating leaderboards, achievement tracking, and reward systems
- **Content-moderation tools** providing administrators with the ability to identify, flag, and remove inappropriate content, thereby promoting a positive and inclusive community environment
- **Direct messaging functionality** (planned for future consideration), facilitating peer-to-peer communication, support networks, and accountability partnerships

Collectively, these enhancements are intended to increase user engagement, strengthen community relationships, and encourage long-term participation within the platform.

### Advanced Subscription Tiers
 
Market reach and subscription flexibility will be expanded through the introduction of additional membership options designed to appeal to a broader range of users and organisations:
 
- A **Premium membership tier** (£19.99 per month) offering benefits such as one-to-one coaching consultations, priority customer support, and access to exclusive content
- **Group and family subscription plans** allowing multiple users to access the platform under a shared membership at discounted rates
- **Corporate wellness packages** tailored for organisations seeking to promote employee health, wellbeing, and fitness engagement

By diversifying the subscription offering, these additional tiers will support new revenue opportunities while addressing the varying needs of individual users, families, fitness groups, and corporate clients.

### Integration with Wearables and Fitness Tracking
 
Support for popular fitness platforms and wearable technologies is planned for future releases, enabling enhanced activity tracking and deeper integration between user fitness data and platform functionality.
 
Proposed integrations include:
 
- **Strava connectivity**, allowing running and cycling activities to be synchronised automatically with community profiles and activity feeds
- **MyFitnessPal integration**, enabling nutritional tracking data to be combined with personalised meal plans and dietary recommendations
- **Apple Health and Google Fit synchronisation**, providing access to activity metrics such as step counts, heart-rate data, and calorie expenditure
- **Achievement-based activity badges** awarded when predefined fitness milestones are reached (e.g., "500 km Cycled" or "100 Workouts Completed")

Through the incorporation of these integrations, user engagement will be strengthened while providing richer, data-driven insights to support personalised coaching, progress monitoring, and long-term fitness development.

### Enhanced Content Management
 
Advanced content-management functionality will be made available to coaches, providing greater control over the creation, delivery, and evaluation of fitness-related content.
 
Planned features include:
 
- **Video-upload and streaming capabilities**, enabling the delivery of instructional content demonstrating correct exercise techniques and movement patterns
- **Downloadable PDF resources**, providing offline access to detailed workout programmes and nutrition guides
- **Integrated live coaching sessions** through video-conferencing platforms such as Zoom and Google Meet, supporting group training and real-time interaction
- **Content-scheduling tools**, allowing coaches to plan content releases, automate publication schedules, and manage structured content calendars
- **Analytics dashboards**, offering insights into plan popularity, completion statistics, user engagement, and participant feedback

The introduction of these capabilities will enhance content delivery, improve user engagement, and provide coaches with valuable performance metrics to support data-informed decision-making and programme optimisation.

### User-Generated Content and Reviews
 
Community participation and content creation will be further enhanced through the introduction of user-generated media, testimonials, and verified feedback mechanisms.
 
Planned features include:
 
- **Progress-photo galleries**, enabling users to showcase fitness achievements, physical transformations, and personal milestones
- **Video testimonials** submitted by community members and coaches to share experiences, success stories, and motivational content
- **Dedicated blog functionality** supporting the publication of in-depth fitness guidance, training advice, and nutritional information
- **Verified review systems** that authenticate feedback through purchase-history validation, ensuring the credibility and reliability of user reviews

These enhancements will strengthen community engagement, increase content authenticity, and provide valuable social proof that supports informed decision-making and user confidence across the platform.

### Payment and Billing Enhancements
 
Additional payment and billing functionality is planned to improve purchasing flexibility, support promotional activities, and accommodate a wider range of user and organisational requirements.
 
Proposed enhancements include:
 
- **Expanded payment options**, extending beyond Stripe to include alternative payment methods such as PayPal, Apple Pay, and Google Pay
- **Gift-subscription functionality**, enabling users to purchase memberships on behalf of friends, family members, or colleagues
- **Referral programmes** that reward users with discounts or incentives for successfully introducing new members to the platform
- **Coupon and promotional-code systems** supporting marketing campaigns, seasonal offers, and targeted discount initiatives
- **Automated invoice generation** to facilitate financial administration and record-keeping for corporate wellness programmes

By broadening payment and billing capabilities, these enhancements will improve user convenience, support customer acquisition strategies, and provide greater flexibility for both individual subscribers and organisational clients.

### Performance and Infrastructure Improvements

To enhance scalability, performance, and future platform expansion, the following infrastructure and optimisation improvements are planned:

- **Progressive Web App (PWA) functionality**, allowing users to install FitHub directly on their devices and continue accessing essential features when offline
- **Image-optimisation techniques**, incorporating lazy loading and responsive image delivery to reduce bandwidth usage and improve page-loading efficiency
- **Content Delivery Network (CDN) implementation**, enabling static assets to be distributed globally and delivered more efficiently to users across different regions
- **Database-scaling solutions**, designed to accommodate increasing user numbers, larger datasets, and higher transaction volumes
- **API versioning strategies**, supporting the future development of native iOS and Android mobile applications while maintaining compatibility with existing platform services

Collectively, these enhancements will strengthen platform reliability, improve application performance, and provide a robust foundation for future growth and technological expansion.

### Accessibility Enhancements

To further strengthen inclusivity and support a wider range of accessibility requirements, several enhancements are planned for future implementation:

- **High-contrast display modes**, providing improved visual accessibility for users with low vision or visual impairments
- **Text-to-speech functionality**, enabling community content and plan descriptions to be consumed through audio output
- **Dyslexia-friendly typography options**, designed to improve readability and support users with reading difficulties
- **Closed-caption support** for future video-based content, ensuring accessibility for users who are deaf or hard of hearing
- **Enhanced ARIA implementation** and additional semantic HTML refinements, maximising compatibility with screen readers and other assistive technologies

The introduction of these accessibility-focused features will promote a more inclusive user experience while ensuring that the platform remains accessible to individuals with diverse needs, preferences, and assistive technology requirements.

### Machine Learning and Analytics

Advanced data-analysis and machine-learning capabilities are planned to provide deeper business insights, improve personalisation, and support long-term user engagement.

Proposed features include:

- **Predictive analytics models** designed to identify subscribers at risk of cancellation, enabling proactive retention strategies and targeted intervention
- **Recommendation engines** utilising collaborative-filtering techniques to suggest relevant plans and products based on the preferences and behaviours of similar users
- **Natural language processing (NLP)** capabilities applied to community posts and product reviews to perform sentiment analysis and identify user trends
- **Customer-churn prediction models** integrated with engagement and retention campaigns to support data-driven marketing initiatives

By incorporating machine-learning and analytical technologies, the platform will be able to deliver more personalised user experiences, improve decision-making, and enhance customer retention through intelligent, data-driven insights.

### Internationalisation and Localisation

To support global expansion and improve accessibility for international audiences, a range of internationalisation and localisation features are planned for future implementation.

Proposed enhancements include:

- **Multi-language functionality**, supporting languages such as Spanish, French, German, and Portuguese to increase accessibility and extend the platform's international reach
- **Localised pricing models**, allowing subscription and product costs to be aligned with regional economic conditions and purchasing power
- **Time-zone-aware scheduling systems**, facilitating the coordination of coaching sessions, community events, and fitness challenges across geographically distributed user groups
- **Multi-currency payment support**, enabling transactions to be completed using local currencies and providing a more seamless purchasing experience

Through the implementation of these features, the platform will be better equipped to serve a diverse global audience while improving user convenience, accessibility, and market adaptability.

### Social Integration

User engagement, content sharing, and account accessibility will be enhanced through the introduction of social-media integration features designed to strengthen community participation and expand platform visibility.

Planned functionality includes:

- **Social authentication options**, enabling users to register and sign in using existing Google, Facebook, or Instagram accounts, thereby simplifying the account-access process
- **Social-sharing capabilities**, allowing members to publish fitness achievements, milestones, and progress updates directly to external social-media platforms
- **Instagram integration**, facilitating the synchronisation of fitness-related content with connected Instagram accounts
- **Influencer collaboration programmes**, featuring recognised fitness coaches, trainers, and content creators to increase platform engagement and provide additional value to users

By incorporating these social-integration features, the platform will encourage community growth, improve user acquisition opportunities, and strengthen engagement through increased social connectivity and content visibility.

**Overall**, a robust, production-ready platform has been established through the current implementation of **FitHub**, delivering secure user management, subscription-based billing, e-commerce functionality, and community-driven engagement within a unified web application. Through the introduction of planned future enhancements, the platform's capabilities in personalisation, user engagement, content delivery, and international accessibility will be further expanded, strengthening its position as a competitive solution within the rapidly growing online fitness and wellness sector.

## Technologies Used
 
[⬆ Back to Table of Contents](#table-of-contents)
 
A variety of technologies, tools, and development resources have been utilised throughout the creation of this project to support both the design and implementation phases. This section provides an overview of the primary technologies employed, including hardware platforms, development environments, software frameworks, database technologies, and payment-processing solutions that contributed to the successful delivery of the application.

---

### Hardware & Operating System
 
#### Dell Latitude 5401
 
Development of this project was undertaken using a **Dell Latitude 5401** x64-based laptop equipped with an **Intel® Core™ i7-9850H processor** (2.60GHz, 6 cores, 12 threads) and **16GB of RAM**. The hardware configuration provides a reliable and high-performance development environment, supporting efficient multitasking, reduced build times, and the smooth operation of development applications, local servers, and browser-based testing tools.
 
#### Windows 11 Pro
 
A stable and modern development platform was provided through the use of **Windows 11 Pro**, Microsoft's latest professional operating system. Enhanced security features, performance improvements, and developer-focused functionality contribute to an environment well suited to web application development. Support for advanced hardware integration, broad software compatibility, and regular system updates ensures dependable operation throughout the development lifecycle. Compatibility with industry-standard IDEs, web browsers, testing frameworks, and validation tools further facilitates the efficient development, testing, and maintenance of the application.
 
---

### Development Environment
 
#### Visual Studio Code
 
A productive and efficient development workflow was supported through the use of **Visual Studio Code (VS Code)**, a lightweight yet feature-rich source-code editor widely adopted within modern software development environments. Intelligent code completion, syntax highlighting, and comprehensive language support for HTML5, CSS3, JavaScript, and Python contributed to enhanced coding efficiency, improved code quality, and a reduction in development errors.
 
Integrated **Git version-control functionality** enabled source-code changes to be managed directly within the editor, simplifying commit management and repository synchronisation. Additional development capabilities were provided through a range of extensions, including **Live Server**, which facilitated real-time browser previews during development, and **Python extensions**, which offered advanced debugging, linting, and Django-development support. Workspace settings, interface preferences, and keyboard shortcuts were customised to create a development environment tailored to project requirements and individual workflow preferences.
 
#### Git & GitHub
 
Version control throughout the project was managed using **Git**, a distributed source-code management system designed to track changes and maintain a complete development history. Repository hosting and cloud-based source-code management were provided through **GitHub**, enabling secure storage, version tracking, and efficient project organisation.
 
Development activities were supported through GitHub's branching and merging workflows, allowing new functionality to be implemented and tested without affecting the primary codebase. Additional project-management features, including issue tracking and task organisation tools, were used to document defects, proposed enhancements, and feature requests throughout the development process.
 
The combined use of Git and GitHub played a critical role in maintaining a structured, reliable, and professional development workflow, with descriptive commit messages providing a clear record of implemented features, bug fixes, and project improvements.

---

### Frontend Technologies
 
#### HTML5
 
The structural foundation of the application is provided by **HTML5**, which utilises semantic elements such as `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, and `<footer>` to improve accessibility, enhance content organisation, and support search engine optimisation. The use of meaningful markup assists screen-reader technologies in interpreting page structure while enabling search engines to better understand and index site content.
 
In addition to its semantic capabilities, HTML5 offers a range of advanced form controls and attributes that improve usability and data validation. Input types including `email`, `number`, `date`, and `tel` provide built-in validation mechanisms and device-specific input interfaces, such as optimised mobile keyboards. Together, these features contribute to a more accessible, intuitive, and user-friendly experience.
 
#### CSS3
 
Visual presentation and responsive layout behaviour throughout the application are achieved through the use of **CSS3**. Responsive design functionality is supported by **media queries**, enabling layouts to adapt effectively across desktop, tablet, and mobile devices. Additional styling features, including **gradients**, **box shadows**, **transitions**, and **animations**, contribute to a polished and visually engaging user interface.
 
To establish a distinctive visual identity and maintain consistency across the application, custom CSS styling is used alongside Bootstrap's predefined components and layout structure. CSS3 also facilitates accessibility improvements through the management of typography, colour schemes, spacing, and contrast ratios, supporting compliance with **WCAG 2.1 Level AA** accessibility requirements.
 
#### Bootstrap 5
 
Responsive and mobile-first development is accelerated through the implementation of **Bootstrap 5**, a widely adopted open-source front-end framework. Its flexible grid system, extensive collection of reusable components, and utility classes enable rapid interface development while maintaining a professional and consistent appearance across the application.
 
A broad range of built-in components, including navigation bars, buttons, cards, forms, modals, and dropdown menus, are utilised to provide a cohesive user experience and reduce reliance on extensive custom CSS. Bootstrap also incorporates accessibility-focused features, supporting semantic HTML structures, ARIA implementation, and colour-contrast requirements to improve usability for users with disabilities.
 
#### JavaScript
 
Interactive client-side functionality throughout the application is powered by **JavaScript**, enhancing user engagement and supporting dynamic content behaviour. A variety of interactive features are implemented using JavaScript, including:
 
- **Client-side form validation**, verifying email formats, password-strength requirements, and mandatory fields before submission
- **Progress indicators and loading states**, reducing the likelihood of duplicate form submissions during processing
- **Modal confirmation dialogues** for critical actions such as subscription cancellations and post deletions
- **Dynamic content updates** without requiring full-page refreshes
- **Flash-message management**, enabling notifications to be displayed and dismissed interactively
- **Responsive navigation functionality**, supporting mobile-friendly menu interactions and adaptive navigation behaviour

Collectively, these technologies contribute to a responsive, accessible, and engaging front-end experience while supporting modern web-development standards and best practices.

---

### Backend Technologies
 
#### Python 3.11
 
The core backend functionality of **FitHub** is powered by **Python 3.11**, a modern high-level interpreted programming language recognised for its readability, versatility, and extensive ecosystem of frameworks and libraries. Application business logic, server-side processing, and database interactions are managed through Python, making it a fundamental component of the platform's architecture.
 
Efficient software development is supported by Python's clear syntax and comprehensive standard library, while its emphasis on readability contributes to long-term maintainability. The language's object-oriented capabilities and support for structured programming principles facilitate the development of modular, reusable, and well-organised application components.
 
Robust exception-handling features, extensive documentation, and a large developer community provide valuable support when troubleshooting issues and implementing new functionality. Furthermore, Python's cross-platform compatibility enables development to take place on Windows-based systems while allowing seamless deployment to Linux-based hosting environments, such as Heroku, without requiring modifications to the codebase.
 
#### Django 4.2
 
Serving as the primary web framework for the project, **Django 4.2** provides a comprehensive Python-based framework built around the **Model–View–Template (MVT)** architectural pattern. By promoting the **DRY (Don't Repeat Yourself)** principle, Django supports rapid development while encouraging clean, maintainable, and scalable application design.
 
The framework offers a wide range of integrated features that significantly accelerate development, including:
 
- **Object-Relational Mapping (ORM):** Enables database interactions to be performed through Python code rather than raw SQL, improving maintainability, readability, and security.
- **Authentication Framework:** Simplifies user registration, login, logout, and password-management processes through a built-in authentication system.
- **Administrative Interface:** Provides an automatically generated management dashboard for maintaining database records and administering plans, products, and other platform content.
- **Template Engine:** Separates presentation from application logic, allowing dynamic content to be rendered efficiently while maintaining a clear code structure.
- **Forms Framework:** Streamlines form creation, validation, error handling, and CSRF protection.
- **URL Routing System:** Maps URL patterns to application views in a structured and maintainable manner.
- **Middleware Architecture:** Processes requests and responses globally while supporting functionality such as session management, security controls, and static-file handling.
- **Security Mechanisms:** Includes built-in protection against SQL injection, Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), and clickjacking attacks.
- **Database Migration Framework:** Tracks, manages, and applies database schema modifications through version-controlled migrations.
 
#### django-allauth
 
Secure user authentication and account management are facilitated through **django-allauth**, a comprehensive Django package that provides registration, login, password management, and account-verification functionality without the need for custom authentication implementations.
 
Key features provided by django-allauth include:
 
- Email-based user registration and authentication
- Social-authentication support (planned for future implementation)
- Password-reset and password-change workflows
- Email-verification functionality
- Secure session management
- User-profile extension and account customisation

By integrating django-allauth, the application benefits from a secure, well-maintained authentication framework that reduces development complexity while supporting industry-standard account-management practices.

---

### Payment Processing
 
#### Stripe API
 
Secure payment processing within **FitHub** is delivered through the integration of **Stripe**, a widely adopted payment platform that supports both one-time transactions and recurring subscription billing. The application utilises multiple Stripe services to manage payments securely, reliably, and efficiently.
 
##### Stripe Checkout
 
One-time purchases, including products and individually purchased plans, are processed through **Stripe Checkout**, which provides a pre-built and secure payment experience. By leveraging the Stripe Checkout Session API, sensitive card information is handled directly by Stripe, eliminating the need for custom payment-processing implementations and reducing PCI-compliance requirements.
 
##### Stripe Subscriptions API
 
Management of recurring membership payments is facilitated through the **Stripe Subscriptions API**, supporting both monthly and annual subscription plans. Key subscription-management capabilities include:
 
- Automated renewal processing on scheduled subscription dates
- Subscription-status monitoring, including `active`, `past_due`, and `cancelled` states
- Dunning workflows designed to manage failed-payment scenarios
- Flexible cancellation options through `cancel_at_period_end`, allowing continued access until the end of the current billing cycle
- Webhook-driven processing to support asynchronous subscription updates and status synchronisation
 
##### Stripe Webhooks
 
Real-time payment and subscription management is achieved through the implementation of **Stripe Webhooks**, which process critical payment events as they occur. The application handles several key webhook events, including:
 
- `checkout.session.completed` — Processes successful completion of one-time purchases
- `invoice.paid` — Updates subscription records following successful renewal payments
- `customer.subscription.deleted` — Manages customer-initiated subscription cancellations
- `subscription.updated` — Synchronises subscription-status changes, including `past_due` and `trialing` states
 
To ensure reliable event processing and prevent duplicate transaction handling, **idempotency controls** are implemented through a dedicated `StripeEvent` model. This mechanism records processed webhook events and safeguards against repeated execution of the same payment event, thereby improving transaction integrity and overall system reliability.

---

### Database Technologies
 
#### PostgreSQL
 
The production database for **FitHub** is powered by **PostgreSQL**, a robust open-source relational database management system widely recognised for its reliability, stability, and extensive enterprise-grade capabilities. Within the deployment environment, PostgreSQL replaces SQLite, which is utilised during local development and testing.
 
Several features make PostgreSQL particularly well suited to modern web applications, including:
 
- **ACID-compliant transaction processing**, ensuring data reliability and integrity through Atomicity, Consistency, Isolation, and Durability principles
- **Advanced indexing mechanisms**, improving query efficiency and accelerating data retrieval, searching, and filtering operations
- **Foreign-key constraint support**, maintaining referential integrity between related database entities
- **Connection-pooling capabilities**, enhancing application performance through efficient management of database connections
- **Automated backup and recovery functionality**, provided through Heroku's managed PostgreSQL service
- **Extensible architecture**, supporting advanced features such as full-text search, custom data types, and user-defined functions for future application growth

Communication between Django and PostgreSQL is facilitated through the **psycopg2** database adapter, which enables Django's Object-Relational Mapping (ORM) framework to convert Python-based database operations into PostgreSQL-compatible SQL queries. Database configuration within the Heroku environment is further simplified through the use of the **dj-database-url** package, which automatically parses and applies the `DATABASE_URL` environment variable.
 
#### SQLite3
 
Local development and testing activities are supported through **SQLite3**, a lightweight file-based relational database management system that requires no dedicated server installation or configuration. Its simplicity and ease of deployment make it particularly suitable for development environments where rapid setup and portability are desirable.
 
By default, Django is configured to utilise SQLite during development unless an alternative database engine is explicitly specified. This allows developers to focus on application development while maintaining a streamlined and efficient local testing environment.

---

### Hosting & Deployment
 
#### Heroku
 
Application deployment and hosting are provided through **Heroku**, a cloud-based **Platform-as-a-Service (PaaS)** solution that simplifies the deployment, management, and scaling of web applications without requiring direct administration of server infrastructure. The platform was selected due to its streamlined deployment workflow, native PostgreSQL support, and seamless integration with Git-based version-control processes.
 
A range of features provided by Heroku support the operation and maintenance of the application, including:
 
- **Git-based deployment workflows**, enabling application updates to be deployed directly from the repository using commands such as `git push heroku main`
- **Dyno-based execution environments**, where lightweight containers provide isolated runtime instances for application processes. Within FitHub, a web dyno hosts the Gunicorn WSGI server responsible for handling incoming HTTP requests
- **Automatic scaling capabilities**, allowing application resources to be adjusted in response to changing traffic levels and workload demands
- **Managed PostgreSQL services**, providing fully maintained database infrastructure with integrated monitoring, backup, and recovery functionality
- **Config Vars**, enabling sensitive configuration values such as `SECRET_KEY`, database credentials, and API tokens to be stored securely outside the version-controlled codebase
- **Static-file management integration**, allowing supporting technologies such as WhiteNoise to efficiently deliver CSS, JavaScript, and image assets
- **Automatic SSL/TLS certificate management**, ensuring secure HTTPS communication through encrypted data transmission
- **Logging and monitoring tools**, offering real-time visibility into application performance, operational status, and runtime behaviour through command-line utilities and web-based dashboards
 
#### WhiteNoise
 
Efficient delivery of static assets is facilitated through **WhiteNoise**, a middleware solution designed to simplify the serving of CSS, JavaScript, image, and other static resources within Heroku-hosted environments. By integrating directly with the Django application, WhiteNoise eliminates the requirement for a dedicated content-delivery network (CDN) when serving static files.
 
Additional performance benefits are achieved through built-in compression and caching mechanisms, which reduce bandwidth consumption and improve page-load times. This lightweight approach provides a reliable and efficient method of managing static resources while maintaining a simplified deployment architecture.

---

### Code Quality & Testing Tools
 
#### Flake8
 
Code quality and standards compliance are supported through the use of **Flake8**, a Python linting utility designed to identify programming errors, stylistic inconsistencies, and potential defects within source code. By combining the capabilities of PyFlakes, pycodestyle, and McCabe, Flake8 provides comprehensive analysis while enforcing adherence to **PEP 8** coding conventions.
 
Within the project, Flake8 is utilised to:
 
- Validate compliance with PEP 8 coding standards
- Detect unused imports and variables
- Identify undefined variables and references
- Verify indentation consistency and line-length requirements
- Highlight potential logical and structural issues within the codebase

Linting behaviour is customised through a dedicated `.flake8` configuration file, which specifies a maximum line length of 88 characters to align with Black formatting conventions while excluding Django migration files from analysis.
 
#### Black
 
Consistent code formatting throughout the application is maintained through **Black**, an automated Python code formatter that applies a standardised coding style across all source files. By removing the need for manual formatting decisions, Black promotes consistency, readability, and maintainability throughout the codebase.
 
Key characteristics of Black include:
 
- **Deterministic formatting**, ensuring identical input consistently produces identical output
- **Minimal configuration options**, encouraging adoption of widely recognised formatting standards
- **Standardised line-length management**, using a default limit of 88 characters
- **Quotation-mark normalisation**, promoting consistency across source files
- **Automatic trailing-comma insertion**, resulting in cleaner and more manageable version-control diffs

Integration with Visual Studio Code extensions enables automatic formatting whenever files are saved, ensuring formatting consistency throughout the development process.
 
#### Pylint
 
Comprehensive static code analysis is provided through **Pylint**, a Python quality-assurance tool that evaluates source code for programming errors, coding-standard compliance, maintainability concerns, and refactoring opportunities. In addition to generating detailed analysis reports, Pylint produces an overall code-quality score measured on a ten-point scale.
 
Enhanced support for Django-specific development is achieved through the integration of the **pylint-django** plugin, which improves analysis accuracy by recognising Django's dynamic behaviours and reducing false-positive warnings.
 
Pylint is used to assess:
 
- Programming errors, including undefined variables and incorrect imports
- Code-quality concerns, such as overly complex methods and excessive parameter usage
- Refactoring opportunities aimed at improving maintainability and efficiency
- Compliance with coding conventions, naming standards, and documentation practices
 
#### isort
 
Management of Python import statements is automated through **isort**, a utility that organises and sorts imports in accordance with PEP 8 recommendations. Imports are categorised into logical groups, including standard-library modules, third-party packages, and locally developed application modules, before being arranged alphabetically.
 
Configuration settings defined within `.isort.cfg` ensure compatibility with Black and Flake8 by applying the following rules:
 
- `profile = black` to maintain alignment with Black formatting standards
- `known_django = django` to correctly identify Django-related packages
- `known_first_party = accounts, plans, shop, community, subscriptions` to categorise locally developed applications
- `line_length = 88` to maintain consistency across code-quality tools
- `skip = migrations` to exclude automatically generated migration files from import sorting

The combined use of Flake8, Black, Pylint, and isort contributes to a consistent, maintainable, and professional codebase while supporting modern Python development standards and best practices.

---

### Testing Frameworks
 
#### Django TestCase
 
Application testing is supported through **Django TestCase**, the testing framework provided as part of the Django ecosystem. Built upon Python's `unittest` framework, it extends core testing functionality with Django-specific utilities designed to simplify the validation of web applications and database-driven systems.
 
Within the project, Django TestCase is utilised to:
 
- Perform unit testing of models, views, and forms
- Validate database queries and Object-Relational Mapping (ORM) operations
- Verify view functionality and permission-based access controls
- Assess form validation and data-processing behaviour

To maintain test reliability and data integrity, each test is executed within a dedicated and isolated test database, ensuring that testing activities do not impact production or development data.
 
#### pytest & pytest-django
 
Additional testing flexibility is provided through **pytest**, a widely adopted Python testing framework recognised for its readability, extensibility, and streamlined syntax. Django-specific functionality is further enhanced through **pytest-django**, which introduces specialised fixtures and utilities tailored to Django applications.
 
Within the project, pytest is used to provide:
 
- A more concise and expressive testing syntax compared with Python's `unittest` framework
- **Parametrised testing**, allowing multiple input scenarios to be evaluated efficiently within a single test definition
- Advanced fixture management for test setup, configuration, and teardown operations
- Enhanced assertion reporting and more informative error messages to simplify debugging and fault diagnosis

The combined use of Django TestCase, pytest, and pytest-django provides a comprehensive testing environment that supports reliable quality assurance, efficient test execution, and maintainable automated testing practices throughout the development lifecycle.

---

### Design & Wireframing Tools
 
#### Balsamiq Wireframes
 
The planning and user-interface design stages of the project were supported through the use of **Balsamiq Wireframes**, a web-based wireframing application designed to facilitate the rapid creation of website layouts and interface prototypes. Prior to development, Balsamiq was used to visualise the structure, navigation flow, and overall layout of the **FitHub** platform.
 
A range of features within Balsamiq contributed to the design process, including:
 
- A **drag-and-drop design environment** enabling rapid creation of interface mock-ups
- A collection of **pre-built user-interface components**, including forms, buttons, and navigation elements
- **Low-fidelity prototyping capabilities** that prioritise information architecture, layout structure, and user journeys over visual styling
- **Export functionality** supporting the sharing of designs with stakeholders and project reviewers
- **Version-management features** allowing iterative refinement and comparison of design revisions

Wireframes were produced for all major areas of the application, including the homepage, user-registration page, dashboard, plan-listing pages, e-commerce shop, community feed, checkout workflow, and account-management section.
 
#### Draw.io
 
Database modelling and system design documentation were supported through **Draw.io**, a free online diagramming platform used to create the **Entity Relationship Diagram (ERD)** for the FitHub database architecture. The tool provides a flexible environment for producing technical diagrams and visual representations of system structures.
 
Draw.io was utilised for:
 
- **Entity Relationship Diagram (ERD) creation** to model database entities and relationships
- **Flowchart development** for documenting processes and workflows
- **System-architecture diagramming** to visualise application components and interactions
- **Exporting diagrams** in formats such as PNG, PDF, and SVG for inclusion within project documentation

The completed ERD provides a clear representation of the application's database structure, illustrating the relationships between key models, including **User**, **UserProfile**, **ExercisePlan**, **NutritionPlan**, **Product**, **Order**, **OrderItem**, **Review**, **Post**, **Comment**, **Subscription**, and **StripeEvent**, together with their associated relational links.

---

### API Documentation & Validation Tools
 
#### W3C Validator Tools
 
Compliance with recognised web-development standards is verified through the use of **W3C Validator tools**, which assess HTML and CSS code against specifications published by the **World Wide Web Consortium (W3C)**. These validation utilities play an important role in maintaining code quality and ensuring adherence to industry best practices throughout the development process.
 
The W3C validation tools are used to:
 
- Verify **HTML5 markup** for syntax errors and structural issues
- Validate **CSS3 stylesheets** against established standards
- Support the implementation of accessible and semantic HTML structures
- Improve compatibility across different web browsers
- Contribute to enhanced **Search Engine Optimisation (SEO)** through standards-compliant markup

Regular validation is performed throughout development to identify issues at an early stage, helping to maintain a high standard of code quality and consistency across the application.
 
#### JSHint
 
Quality assurance for client-side scripting is supported through **JSHint**, a static code-analysis tool designed to identify potential problems and coding inconsistencies within JavaScript source files.
 
JSHint is used to detect issues such as:
 
- Undefined variables and references
- Unused variables and redundant code
- Missing semicolons and syntax inconsistencies
- Type-coercion concerns that may lead to unexpected behaviour
- Potentially problematic coding patterns and logic structures

Project-specific validation requirements are managed through a dedicated `.jshintrc` configuration file, allowing analysis rules to be tailored to the application's development standards and coding practices.
 
#### Stripe Dashboard & Testing Tools
 
Payment-management and transaction-monitoring activities are facilitated through the **Stripe Dashboard**, which provides a centralised administrative interface for overseeing payment operations and subscription services.
 
The Stripe Dashboard supports:
 
- Monitoring both test and live payment transactions
- Managing subscription customers and billing information
- Reviewing payment events, logs, and transaction histories
- Testing and validating webhook integrations through Stripe's development tools

Local webhook testing during development is enabled through the **Stripe CLI**, which allows Stripe events to be forwarded directly to the local development environment. This functionality supports efficient testing of webhook handlers without requiring deployment to a live hosting platform.
 
```bash
stripe listen --forward-to localhost:8000/webhooks/stripe/
```

The command above forwards Stripe test events to the local development server, enabling webhook-processing functionality to be tested, validated, and debugged in a controlled development environment.

---

### Communication & Collaboration
 
#### Code Institute Discord
 
Communication, collaboration, and peer support throughout the project were facilitated through the **Code Institute Discord** platform, which serves as the primary online community environment for students, mentors, and support staff. The platform provides a centralised space for knowledge sharing, discussion, and project-related assistance.
 
Key benefits of using Code Institute Discord include:
 
- Ongoing interaction with the wider learning community
- Access to guidance and support from mentors and fellow learners
- Opportunities to share development progress, challenges, and solutions
- Availability of learning materials, documentation, and technical resources
- Dedicated channels organised around project development and technical support topics

Features such as threaded conversations, direct messaging, and file sharing promote collaborative learning, constructive feedback, and effective problem-solving throughout the development process.
 
#### Google Meet
 
Virtual communication and remote collaboration were supported through **Google Meet**, providing a reliable platform for live discussions, mentoring sessions, and project reviews.
 
Google Meet was used to facilitate:
 
- Real-time participation in tutorials, workshops, and mentor consultations
- Screen-sharing sessions for code reviews, debugging activities, and project demonstrations
- Immediate feedback and guidance from mentors and peers
- Stable video-conferencing functionality through an intuitive and user-friendly interface

The combination of Code Institute Discord and Google Meet provided an effective communication framework that supported collaboration, knowledge exchange, and continuous learning throughout the project lifecycle.

---

### Additional Utilities
 
#### Notepad++
 
Rapid code editing and lightweight script development were supported through the use of **Notepad++**, a versatile text editor well suited to quick modifications and file management tasks. Its lightweight architecture provides an efficient alternative to full-featured integrated development environments (IDEs) when performing smaller development activities.
 
Key functionality includes:
 
- **Syntax highlighting** for HTML, CSS, JavaScript, and Python source files
- A **tabbed document interface** for managing multiple files simultaneously
- **Advanced search-and-replace capabilities** with regular-expression support
- **Auto-completion and macro-recording features** to improve productivity and automate repetitive tasks
- A lightweight and responsive environment for quick code reviews and amendments
 
#### Diffchecker
 
Comparison and change-tracking activities were facilitated through **Diffchecker**, a web-based utility designed to identify differences between text, code, and file versions. The tool provides side-by-side comparisons, making it easier to review modifications and verify updates before integration.
 
Diffchecker was used to:
 
- Compare different versions of HTML, CSS, JavaScript, and Python files
- Identify changes, inconsistencies, and potential coding errors
- Reduce the risk of accidental file overwrites
- Verify amendments and refinements before committing changes to GitHub
 
#### Image Colour Picker
 
Colour selection and palette management were supported through **Image Colour Picker**, a utility that extracts precise colour values from images and provides corresponding HSL, RGB, and hexadecimal (HEX) codes.
 
The tool was used to:
 
- Capture accurate colour values from design references and visual assets
- Maintain consistency across branding elements and colour schemes
- Assist in selecting effective and visually balanced colour combinations
- Streamline the design process by simplifying colour identification and application
 
#### GIMP
 
Graphic design and image-processing tasks were completed using **GIMP (GNU Image Manipulation Program)**, a powerful open-source image-editing application capable of supporting a wide range of creative and optimisation activities.
 
GIMP was utilised for:
 
- Creating, editing, and enhancing graphical assets
- Optimising images for web delivery by reducing file sizes whilst preserving visual quality
- Preparing project resources such as logos, icons, banners, and thumbnails
- Performing advanced image manipulation through the use of layers, masks, filters, and other professional editing tools

Collectively, these supporting utilities enhanced productivity, streamlined development and design workflows, and contributed to the creation of a consistent and professionally presented application.

---

### Web Browsers
 
#### Microsoft Edge, Mozilla Firefox, and Google Chrome
 
Testing, debugging, and quality-assurance activities throughout the project were conducted using **Microsoft Edge**, **Mozilla Firefox**, and **Google Chrome**, three widely adopted modern web browsers that provide comprehensive development and testing capabilities.
 
These browsers offer a range of tools and features that support the development process, including:
 
- **Responsive-design testing tools**, enabling websites to be previewed and evaluated across various screen sizes, device types, and viewport resolutions
- **Integrated developer tools**, providing advanced debugging functionality such as live editing of HTML, CSS, and JavaScript, network analysis, accessibility auditing, and performance monitoring
- **Accessibility-assessment features**, supporting the evaluation of colour contrast, heading structures, ARIA implementation, and overall accessibility compliance
- **Performance-analysis capabilities**, including Lighthouse audits for assessing performance, accessibility, search-engine optimisation, and adherence to best practices
- **Cross-browser compatibility testing**, ensuring that application functionality, styling, and user experience remain consistent across different browsers and operating systems

By utilising multiple browsers throughout development, the application can be thoroughly tested, refined, and optimised for a diverse range of users. This approach helps ensure reliable functionality, consistent presentation, and a high-quality user experience across desktop, tablet, and mobile platforms.

---

### Environment Management
 
#### python-dotenv
 
Secure configuration management within the application is supported through **python-dotenv**, a Python library that loads environment variables from a `.env` file into the `os.environ` namespace. This approach enables sensitive settings to be stored separately from the source code, improving security and reducing the risk of exposing confidential information.
 
Key configuration values managed through python-dotenv include:
 
- `SECRET_KEY` — Django's cryptographic secret key
- `DATABASE_URL` — Database connection configuration string
- `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` — Stripe API authentication credentials
- `DEBUG` — Environment setting controlling development and production behaviour

To prevent sensitive configuration data from being exposed through version-control systems, the `.env` file is excluded from repository commits through inclusion within the `.gitignore` file.
 
#### dj-database-url
 
Database configuration is simplified through the use of **dj-database-url**, a Python utility designed to parse and interpret database connection strings automatically. The package is particularly valuable within cloud-hosted environments, where database credentials are commonly provided through environment variables.
 
Within the project, dj-database-url is used to interpret Heroku's `DATABASE_URL` configuration variable and automatically configure Django's database settings accordingly. This approach enables seamless transitions between **SQLite** during local development and **PostgreSQL** within the production environment, eliminating the need for manual configuration changes or modifications to the application codebase.
 
By combining python-dotenv and dj-database-url, the project benefits from a secure, flexible, and environment-independent configuration-management strategy that supports both local development and cloud-based deployment workflows.

---

### Deployment & Production
 
#### Gunicorn
 
Application execution within the production environment is managed through **Gunicorn** (Green Unicorn), a Python-based **Web Server Gateway Interface (WSGI)** server responsible for serving the Django application and processing incoming HTTP requests. Acting as the intermediary between the web server and the Django framework, Gunicorn ensures that client requests are received, handled, and routed efficiently to the appropriate application components.
 
Within the Heroku deployment environment, Gunicorn is configured through a `Procfile`, which defines the command required to launch the application:
 
```bash
web: gunicorn fitHub.wsgi
```

This configuration instructs Heroku to start a Gunicorn web process that loads the Django WSGI application and listens for incoming web traffic. By utilising Gunicorn, the application benefits from a reliable and production-ready server capable of handling concurrent requests efficiently.
 
#### requirements.txt
 
Dependency management and deployment consistency are maintained through the use of a **requirements.txt** file, which contains a complete list of Python packages and version specifications required by the application. By defining exact dependency versions, the file ensures that development, testing, and production environments remain consistent and reproducible.
 
The requirements file enables automated installation of all project dependencies during deployment, reducing configuration errors and simplifying environment setup.
 
Examples of key dependencies used within **FitHub** include:
 
- `Django==4.2.0`
- `psycopg2-binary` (PostgreSQL database adapter)
- `dj-database-url`
- `python-dotenv`
- `stripe`
- `django-allauth`
- `gunicorn`
- `whitenoise`

Through the combined use of Gunicorn and requirements.txt, the application benefits from a stable deployment process, consistent environment configuration, and reliable production operation across cloud-hosted infrastructure.

---

## Version Control Standards
 
### Git Conventions
 
A structured and consistent version-control strategy is maintained through the use of **Git**, with descriptive commit-message conventions applied throughout the development lifecycle. These conventions provide clear documentation of project changes, making development history easier to understand, review, and maintain.
 
The project follows the following commit-message categories:
 
```text
feat: add new feature
fix: resolve a bug
test: add or update tests
docs: documentation changes
style: formatting and PEP 8 compliance
refactor: code restructuring
perf: performance enhancement
chore: maintenance tasks
```

By categorising commits according to their purpose, changes can be identified quickly and tracked more effectively throughout the project's history.
 
Examples of commit messages used within the project include:
 
- `feat: add Stripe webhook handler for subscription renewals`
- `test: add unit tests for Product review model`
- `fix: resolve N+1 query issue in shop list view`
- `docs: update README with deployment instructions`

The adoption of clear and meaningful commit descriptions provides a transparent record of development activities, supports maintainability, and enables contributors to understand the evolution of the project with minimal effort.

---

### Summary
 
A broad range of modern technologies, development frameworks, and industry-recognised practices have been integrated throughout the FitHub project to support the creation of a scalable, secure, and user-focused fitness subscription platform. Core technologies such as **Django** for backend development, **Bootstrap** for responsive user-interface design, **Stripe** for secure payment processing, and **PostgreSQL** for relational data management collectively provide the foundation for a robust and professional web application.
 
High standards of software quality, accessibility, and maintainability are further supported through the combined use of development tools, including **Visual Studio Code**, **Git**, and **GitHub**, alongside code-quality solutions such as **Flake8**, **Black**, and **Pylint**. In addition, comprehensive testing is facilitated through frameworks including **Django TestCase** and **pytest**, while design and planning activities are supported by tools such as **Balsamiq Wireframes** and **Draw.io**.
 
The effective integration of these technologies demonstrates the practical implementation of contemporary full-stack web-development methodologies, encompassing responsive design, secure authentication, payment processing, database management, automated testing, accessibility compliance, and professional deployment practices. As a result, FitHub reflects the technical competence, development standards, and professional expectations associated with **Level 5 of the UK Higher Education Framework**.

---

## Wireframes
 
[⬆ Back to Table of Contents](#table-of-contents)
 
The structural planning of **FitHub**, a subscription-based fitness community platform, commenced with the creation of **wireframes** before any visual styling or detailed interface design activities were undertaken. Rather than focusing on typography, colour schemes, imagery, or branding elements, wireframes provide a simplified visual representation of the application that concentrates on layout structure, content organisation, and user-navigation pathways.
 
Serving as the **architectural foundation** of the platform, the wireframes illustrate the positioning and relationships of key interface components, including navigation systems, plan-discovery pages, subscription-management workflows, e-commerce checkout processes, community-content feeds, and administrative management areas. Their low-fidelity, grayscale presentation helps maintain attention on usability, information hierarchy, and overall **user experience (UX)** considerations without the influence of visual design elements.
 
During the **pre-development planning stage**, the wireframing process provided an effective method of evaluating and refining design decisions before implementation commenced. This approach ensured that core functional requirements, such as exercise and nutrition plan discovery, subscription administration, online purchasing, community engagement features, and administrative controls, were clearly defined, reviewed, and validated prior to development.
 
The production of wireframes for this **Milestone 4 full-stack project** reflects established industry practice and demonstrates a structured, **user-centred design methodology**. Throughout the development lifecycle, these wireframes served as the conceptual framework for the application, informing both front-end interface construction and the integration of back-end functionality.

### Design Rationale and Planning
 
A structured approach to **information architecture, user-flow design, and layout consistency** is demonstrated through the wireframes, which were used to map key user interactions and establish clear navigation pathways across the platform. By modelling these interactions during the early planning stages, development activities could be organised into logical phases, enabling requirements to be prioritised effectively and user needs to be addressed systematically.
 
The complexity of **FitHub** required the design of several distinct user journeys, each supporting different user roles and platform objectives.
 
#### Customer Journey (Public User to Subscriber)
 
This journey focuses on guiding prospective users from initial platform discovery through to active subscription and community participation:
 
- Public-facing homepage and landing-page experience for unauthenticated visitors
- User registration and authentication workflows
- Fitness-profile creation and goal-configuration processes
- Exercise and nutrition plan discovery, including filtering by difficulty level and fitness objective
- Subscription-tier comparison, selection, and checkout procedures
- Access to subscriber-exclusive community features
 
#### E-Commerce Journey (Product Discovery to Purchase)
 
This workflow supports users throughout the purchasing process, from product exploration to order completion:
 
- Product-catalogue browsing and filtering functionality
- Detailed product pages incorporating reviews and supporting information
- Secure checkout workflows and payment-confirmation processes
- Order-history management and invoice-access functionality
 
#### Community Engagement Journey (Subscriber-Exclusive)
 
Designed to encourage interaction and long-term engagement, this user journey focuses on community participation and content sharing:
 
- Community feeds presenting member success stories and progress updates
- Individual post pages supporting discussions through comments
- Interfaces for creating and publishing community content
- Peer-support interactions, including commenting and community engagement activities
 
#### Administrative Dashboard (Staff and Coach Access)
 
This workflow supports platform management and operational oversight through dedicated administrative functionality:
 
- Interfaces for creating and managing exercise plans, nutrition plans, and products
- Subscriber, customer, and order-management facilities
- Revenue-monitoring and analytics functionality
- Community-content moderation and administrative controls
 
By defining these user journeys during the wireframing stage, essential functionality such as plan discovery, subscription management, online purchasing, and community participation could be positioned logically within the interface and designed to support intuitive navigation. The inclusion of wireframes within the project demonstrates the importance of **iterative planning, usability-focused design, and structured refinement**, emphasising the design process itself rather than focusing solely on the completed visual implementation.

### UX Awareness and Multi-User Context
 
All wireframe decisions were guided by a strong focus on **user experience (UX)**, ensuring that the needs of multiple user groups with differing objectives, behaviours, and usage contexts were carefully considered throughout the design process.
 
To support these diverse requirements, several key user journeys were mapped and refined during the wireframing stage.
 
#### 1. New User Discovery and Subscription Journey
 
This workflow was designed to guide prospective users from their initial interaction with the platform through to subscription enrolment and checkout completion. The wireframes establish a clear information hierarchy that highlights subscription opportunities while presenting exercise plans, nutrition plans, and membership benefits in an accessible and structured manner. Registration forms were intentionally simplified, minimising the number of required fields to reduce user effort and improve conversion rates.
 
#### 2. Subscriber Community Engagement Journey
 
Community-focused wireframes were developed to encourage ongoing participation, interaction, and user retention. Particular emphasis was placed on chronological content presentation, clearly structured discussion threads, and the visibility of engagement indicators. By prominently displaying member success stories, comments, and community activity, the design encourages repeat visits and fosters a supportive environment centred on peer interaction and motivation.
 
#### 3. E-Commerce Product Discovery Journey
 
The e-commerce workflow was structured to facilitate efficient product exploration and purchasing. Wireframes incorporate clearly visible filtering mechanisms based on category, pricing, and popularity, alongside product reviews and streamlined shopping-cart functionality. Consistency between the shop and plan-discovery sections was maintained to provide a cohesive and familiar browsing experience throughout the platform.
 
#### 4. Administrative Content Management Journey
 
Administrative wireframes were designed with operational efficiency as a primary objective. Dashboard layouts prioritise access to key performance indicators, while streamlined interfaces support the creation and management of plans, products, subscriptions, and other platform content. Clear navigation pathways between administrative functions help reduce complexity and improve workflow efficiency for coaches and staff members.
 
Particular attention was given to optimising high-priority user journeys, especially **subscription registration and checkout workflows**. By evaluating navigation flows, information placement, and task completion processes during the planning stage, potential usability challenges could be identified and addressed before development commenced. This approach helped minimise user friction, reduce cognitive load, and support efficient task completion.
 
The wireframing process also enabled consideration of alternative scenarios and edge cases that may arise during real-world usage, including:
 
- Presenting non-subscribers with an informative teaser page rather than a restrictive 403 access-denied response
- Supporting users who manage multiple subscriptions, purchases, or order histories
- Accommodating coaches responsible for creating and maintaining multiple fitness plans
- Allowing subscribers to filter community content based on activity type, topic, or areas of interest

By modelling these scenarios during the design phase, the platform's usability, flexibility, and overall user experience could be enhanced before implementation, resulting in a more intuitive and user-centred application architecture.

### Information Architecture & Navigation
 
A clear and structured navigation framework was established through the wireframing process to support the differing requirements of public visitors, registered users, subscribers, and administrative users. By mapping navigation pathways during the planning stage, the application's information architecture could be organised to promote intuitive navigation and minimise user confusion.
 
#### Primary Navigation Structure
 
The wireframes defined the following core navigation areas:
 
- **Home** — Public-facing landing page and entry point to the platform
- **Dashboard** — Central hub providing authenticated users with access to personalised content and account information
- **Plans** — Dedicated area for discovering, browsing, and purchasing exercise and nutrition plans
- **Shop** — E-commerce section containing fitness-related products and merchandise
- **Community** — Subscriber-exclusive area providing access to community discussions and success stories
- **Account Settings** — Profile-management and account-configuration functionality
 
Role-based and conditional navigation behaviours were incorporated into the wireframes to ensure that relevant functionality is presented according to the user's authentication and subscription status. For example, unauthenticated visitors are presented with **Log In** and **Sign Up** calls to action, authenticated users gain access to personalised dashboard features, and active subscribers are provided with community-access functionality. Visualising these navigation states during the wireframing phase helped ensure clarity, consistency, and an intuitive user experience.
 
#### Secondary Navigation Patterns
 
In addition to primary navigation, several supporting navigation mechanisms were incorporated into the wireframes to improve usability and content discoverability:
 
- **Breadcrumb navigation** to assist users when navigating plan-detail and content pages
- **Filtering and sorting controls** to refine results within listings and catalogue views
- **Pagination systems** to improve navigation through larger collections of content and community posts
- **Tabbed interfaces** to support subscription-tier comparison and related content organisation
 
By defining both primary and secondary navigation structures during the planning process, the wireframes established a logical information architecture that supports efficient task completion, improved content discovery, and a consistent user experience across the platform.

### Responsive Design Considerations
 
Responsive design requirements were incorporated during the wireframing stage to ensure that essential functionality remained accessible and usable across a variety of screen sizes and device types. Separate wireframes were developed for both desktop and mobile environments, allowing layout adaptations and interaction patterns to be evaluated before implementation began.
 
#### Mobile Viewports
 
Wireframes designed for mobile devices focused on usability within constrained screen dimensions and incorporated the following considerations:
 
- **Single-column, stacked layouts** to maximise readability and simplify navigation on smaller screens
- **Touch-friendly interactive elements** with appropriately sized buttons and controls
- **Condensed navigation systems**, including hamburger-menu functionality to conserve screen space
- **Optimised typography and spacing** to improve readability and reduce visual clutter
- **Mobile-focused form design**, incorporating larger input fields and context-appropriate virtual keyboards to improve data entry efficiency
 
#### Desktop Viewports
 
Desktop wireframes were designed to take advantage of larger screen areas, supporting more complex layouts and enhanced content visibility through:
 
- **Multi-column page structures** incorporating sidebars where appropriate
- **Persistent navigation menus** displayed directly within the page header
- **Grid-based layouts** for presenting products, plans, and other catalogue-based content
- **Expanded filtering, comparison, and browsing controls** to support more detailed content exploration
 
By producing dedicated wireframes for both mobile and desktop environments, responsive-design requirements were considered as a core aspect of the planning process rather than being introduced later during development. This approach helped ensure a consistent user experience across devices while reducing the need for significant layout revisions during implementation.


### Form Design & User Input
 
Particular emphasis was placed on form usability during the wireframing process, with careful consideration given to input-field organisation, validation requirements, and the presentation of user feedback. By evaluating form interactions during the planning stage, the design could be refined to promote usability, reduce input errors, and support efficient task completion.
 
#### Registration and Login Forms
 
User-authentication wireframes were designed to streamline the account-creation and login experience through:
 
- **Minimal mandatory input fields**, including email address, password, and fitness-goal selection
- **Clearly labelled form controls** supported by descriptive placeholder text
- **Password-strength indicators** to encourage secure credential creation
- **Inline validation feedback**, with error messages positioned directly beneath relevant input fields for improved clarity
 
#### Plan and Product Creation Interfaces (Administrative Users)
 
Administrative forms were structured to support efficient content management while reducing complexity for staff members and coaches. Key design considerations included:
 
- **Multi-section form layouts** grouping related fields into logical categories
- **Contextual help text and examples** to assist with the completion of more complex inputs
- **Image-upload previews** allowing uploaded content to be reviewed before submission
- **Clearly defined action controls**, including Save, Cancel, and Delete options
 
#### Subscription Checkout Workflow
 
Wireframes for the subscription and payment process were designed to improve transparency and user confidence throughout the purchasing journey. Features incorporated into the checkout flow included:
 
- **Progress indicators** displaying the user's position within multi-step processes (e.g., Step 1 of 3)
- **Security indicators and SSL assurances** reinforcing trust during payment activities
- **Transparent pricing information**, including clear breakdowns of costs and applicable fees
- **Order-review stages** allowing users to verify details before final confirmation and payment submission
 
By incorporating these considerations into the wireframes, form interactions were designed to be intuitive, accessible, and aligned with established professional standards commonly found within modern e-commerce and subscription-based platforms.

### Accessibility & Clarity
 
Accessibility considerations were incorporated into the wireframing process from the outset, ensuring that the planned implementation would align with **WCAG 2.1 Level AA** requirements. Rather than being introduced during later development stages, accessibility features were considered as a fundamental component of the platform's conceptual design.
 
The wireframes incorporated a range of accessibility-focused considerations, including:
 
- **Clearly defined heading structures**, illustrating a logical content hierarchy from H1 through to H6
- **Explicitly associated form labels**, ensuring input fields could be identified and understood easily by users and assistive technologies
- **Alternative-text placeholders** indicating where descriptive image content would be provided
- **Visual contrast planning**, represented through distinct grayscale differentiation to support future compliance with colour-contrast requirements
- **Keyboard-accessible navigation pathways**, with tab-order considerations reflected within the layout design
- **Visible focus indicators and interactive-state representations**, ensuring important interface elements remained identifiable during keyboard navigation
 
By documenting these accessibility requirements within the wireframes, the project established a strong foundation for inclusive design. This approach ensured that usability, accessibility, and clarity were embedded within the planning process rather than being treated as secondary considerations during implementation.

### Iterative Refinement & Stakeholder Alignment
 
The wireframing process provided an effective mechanism for validating design concepts and refining interface decisions before development commenced. Through a structured and iterative approach, layouts could be evaluated, revised, and aligned with both user requirements and business objectives at an early stage of the project lifecycle.
 
The refinement process consisted of four key stages:
 
1. **Conceptual layout exploration** — Initial low-fidelity sketches were produced to investigate alternative navigation structures, content arrangements, and information hierarchies.
2. **Requirements validation** — Wireframes were reviewed against project objectives to ensure alignment with key business requirements, including subscription-based access control, community functionality, and the dual-revenue model supporting both subscriptions and product sales.
3. **Design refinement** — Feedback gathered during review activities informed revisions to layouts, navigation pathways, and critical user workflows, resulting in progressively more detailed wireframes.
4. **Implementation preparation** — Refined wireframes served as a reference framework during development, guiding both interface construction and feature implementation.

This iterative methodology helped identify potential usability and design challenges before development resources were committed. Examples of issues explored and resolved during the wireframing stage included:

- Determining whether subscription tiers should be presented on a single comparison page or distributed across separate tabbed interfaces, with both approaches evaluated through alternative wireframe designs
- Assessing the most effective method of organising community content by comparing chronological content ordering with trending or popularity-based presentation models
- Evaluating the visual prominence of subscription and checkout calls to action through the testing of different information hierarchies and interface layouts

By enabling early experimentation and validation, the wireframing process reduced design uncertainty, improved decision-making, and ensured that both user expectations and business requirements were effectively reflected within the final application design.

### Professional Development Practice
 
The wireframing process reflects recognised software-development best practices by emphasising planning, validation, and user-focused decision-making before implementation begins. Rather than concentrating immediately on visual styling or code development, wireframes were used to establish requirements, evaluate user interactions, and guide design decisions throughout the project lifecycle.
 
Several professional practices are demonstrated through the use of wireframes:
 
- **User-centred design principles**, prioritising user goals, behaviours, and navigation requirements before visual design and technical implementation
- **Iterative design and planning**, using wireframes as collaborative tools to review, discuss, and refine requirements throughout the project
- **Structured requirements analysis**, ensuring that expected functionality and user interactions are clearly defined prior to development
- **Risk-reduction strategies**, enabling potential usability concerns and design challenges to be identified during the planning phase, when modifications can be implemented more efficiently and at lower cost
- **Professional stakeholder communication**, utilising visual representations to convey design intentions, interface structures, and workflow concepts to developers, reviewers, and other stakeholders

The adoption of this methodology demonstrates an understanding of the distinction between **design** and **implementation**, where design focuses on planning, evaluation, and informed decision-making, while implementation concerns the development, coding, and visual realisation of those decisions. As such, the approach aligns with recognised **Level 5 professional development standards**, reflecting a structured, methodical, and user-focused software-development process.

### Wireframe Coverage
 
To ensure comprehensive planning and effective validation of user journeys, wireframes were produced for all major sections of the **FitHub** platform. These wireframes covered public-facing pages, authenticated user functionality, subscription workflows, e-commerce processes, community features, and administrative interfaces, providing a complete visual blueprint for the application's structure and functionality.
 
#### Public and Authentication Pages
 
Wireframes were developed for the platform's public-access and authentication-related functionality, including:
 
- Homepage and primary landing-page experience
- User-registration workflow
- User-login interface
- Password-reset process
 
#### User Dashboard and Profile Management
 
Dedicated wireframes were created to support personalised user-account functionality, including:
 
- User dashboard serving as the primary authenticated-user hub
- Profile-view and profile-edit interfaces
- Account-settings and account-management pages
 
#### Plans Section
 
The exercise and nutrition plan workflows were modelled through wireframes covering:
 
- Plan-listing pages incorporating filtering and browsing functionality
- Individual plan-detail pages
- Plan-purchase and checkout processes
 
#### Shop Section
 
The e-commerce component of the platform was supported through wireframes illustrating:
 
- Product-listing pages with filtering and sorting controls
- Product-detail pages featuring reviews and supporting information
- Shopping-cart functionality
- Checkout and payment workflows
- Order-confirmation pages
- Order-history management interfaces
 
#### Community Section (Subscriber-Only)
 
Subscriber-exclusive community functionality was represented through wireframes covering:
 
- Community-feed pages displaying member content
- Individual post-detail views
- Post-creation interfaces
- Comment-thread and discussion functionality
 
#### Subscription Management
 
Subscription-related user journeys were planned through dedicated wireframes for:
 
- Subscription-tier comparison pages
- Subscription-checkout workflows
- Subscription-confirmation pages
- Billing and subscription-management interfaces
 
#### Administrative Interfaces
 
Wireframes were also produced for staff and coach management functionality, including:
 
- Administrative dashboard views
- Plan-creation and plan-management interfaces
- Product-creation and product-management functionality
- Subscriber-management and administration tools
 
By developing wireframes for each of these core areas, the project ensured that all major workflows, user interactions, and business requirements were visualised, reviewed, and validated before implementation. This comprehensive approach reduced development risk, improved usability planning, and provided a structured foundation for both front-end and back-end development activities.

### Summary
 
The wireframes created for **FitHub** acted as a vital link between project requirements and technical implementation, providing a structured framework through which user experience, functionality, and information architecture could be evaluated and refined before development commenced. By establishing a clear visual representation of the platform at an early stage, design decisions could be validated and aligned with both user needs and business objectives.
 
Throughout the planning process, the wireframes reinforced a commitment to delivering an **accessible, intuitive, and user-focused fitness subscription platform** that reflects the expectations of modern e-commerce systems and online community applications. Their development demonstrates the application of recognised **full-stack software-development practices**, consistent with the professional standards expected at **Level 5 of the UK Higher Education Framework**.
 
By modelling a variety of user journeys—including those of public visitors, registered users, subscribers, coaches, and administrators—the wireframes ensured that the platform's complexity could be managed through logical navigation structures, clear interface design, and well-organised information architecture. This structured and user-centred methodology reduced development risk, improved planning accuracy, and helped ensure that the final implementation would effectively support the needs of all user groups.

---

## FitHub Fitness Subscription Application Wireframes

[⬆ Back to Table of contents](#table-of-contents)

The wireframes presented here correspond to the fourteen pages planned for inclusion in this FitHub Fitness Subscription Application website. Each page is shown in three versions: desktop, tablet, and mobile.

---

### Homepage

FitHub has been designed to provide a clear, motivating, and user-friendly entry point into a complete fitness subscription platform. This homepage introduces visitors to the purpose and vision of FitHub, establishing its role as a modern, all-in-one solution that brings expert fitness plans, quality merchandise, and a supportive member community together in a single place.

The primary aim of the website is to help visitors quickly understand the value FitHub offers and to guide them confidently toward the right first action — whether that is browsing membership plans, exploring the shop, or joining the community. By leading with a clear hero message, three concise value propositions (Plans, Shop, Community), and curated previews of featured plans and products, the homepage communicates the platform's purpose immediately, without the visitor needing to consult any supporting documentation.

The project focuses on delivering modern web functionality, secure data handling, e-commerce capability, and a fully responsive design, while maintaining an encouraging and professional tone. The layout adapts deliberately across breakpoints — the hero image moves below the headline on smaller screens for readability, and the "Community" navigation item appears only to authenticated users — and accessibility is built in throughout, with a clear heading hierarchy, semantic structure, alt text, high-contrast typography, and visible focus states. Through clarity, usability, social proof, and a consistent call-to-action system, visitors quickly grasp what FitHub provides and why it has been developed as a practical, real-world fitness platform.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1024" height="1536" alt="homepage wireframe v2" src="https://github.com/user-attachments/assets/99a262ab-70c6-405c-9dac-978b281ca681" />

</details>

---

### Registration

FitHub's registration has been designed as a clear, reassuring, two-step journey that turns a new visitor into a member with as little friction as possible. Rather than presenting a single intimidating form, the process is split into two focused steps — account creation, then an optional fitness profile — so that each stage asks only for what it needs and the visitor always knows how far they have progressed.

Step 1 establishes the member's login credentials, capturing their email address and password with real-time, accessible validation: password requirements are checked and confirmed as the user types, the show/hide toggle aids accuracy, and the matching-password check provides immediate feedback. Trust is built deliberately at this stage through clear messaging that the data is encrypted, GDPR compliant, and free of spam. Step 2 then personalises the experience by inviting the member to share their main fitness goal, experience level, and optional height and weight, which allows FitHub to recommend the most relevant plans and products — while making clear this information is optional and can be updated at any time from Account Settings.

The flow focuses on modern web functionality, secure credential handling, and a fully responsive design that adapts deliberately across breakpoints, with the progress indicator ("Step 1 of 2 — 50% complete") keeping users oriented throughout. Accessibility is built in at every step: a clear heading hierarchy, labels associated with all inputs, real-time validation announced via aria-live regions, visible focus states, minimum 44px touch targets, decorative icons hidden from assistive technology, and status conveyed by more than colour alone. Through clarity, transparency, and trust-focused design, visitors can create an account quickly and confidently, understanding exactly why each piece of information is requested.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="registration wireframe v2" src="https://github.com/user-attachments/assets/dacbc014-7aef-4bfe-bf1b-cc9c30430030" />

</details>

---

### Login

FitHub's login page has been designed to be simple, secure, and fast, returning members to their account with minimal effort while reassuring them that their data is protected. A clear "Welcome Back" header and a single, focused form keep the page uncluttered, so members can sign in confidently and get straight to their fitness plans, progress tracking, and community.

The login form captures the member's email (or username) and password, with helper text, a show/hide password toggle to aid accuracy, and an optional "Remember me on this device" choice that keeps them signed in for 30 days. A "Forgot your password?" link supports easy recovery, and secondary actions guide visitors without an account toward registration. Trust is reinforced throughout via supporting messaging — SSL encryption, bank-level security, and a no-spam promise — while a concise "Why log in?" panel explains the value of signing in (personalised plans, progress tracking, community access, and member benefits), ensuring the purpose is immediately evident.

The page focuses on secure authentication, defensive design, and a fully responsive layout that adapts deliberately across breakpoints, with the trust panel repositioning and the "Why log in?" explainer collapsing into an accordion on smaller screens. Error handling is explicit and accessible: invalid credentials produce a clear, non-revealing message announced via an aria-live region so users are notified without disrupting their flow. Accessibility is built in throughout, with a clear heading hierarchy, labels associated with all inputs, decorative icons hidden from assistive technology, visible focus states, minimum 44px touch targets, and status conveyed by more than colour alone. Through clarity, security, and trust-focused design, returning members can sign in quickly and with confidence.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="login wireframe v2" src="https://github.com/user-attachments/assets/05e53146-31a5-46a1-bcb4-d55785d7026b" />

</details>

---

### Dashboard

The dashboard is the member's personal hub — the first place they land after logging in — designed to surface everything relevant to their fitness journey at a glance and guide them straight to their next action. A personalised welcome ("Welcome back, Roberto") and a progress snapshot establish context immediately, so the page's purpose is evident from the moment it loads and the member feels recognised and motivated.

The layout is organised into clear, scannable zones. A quick-overview strip summarises key metrics — workouts completed this week, weekly progress, and daily calorie and protein intake against goals — each with a visual progress indicator and a text alternative. Beneath this, a set of main content cards gives the member direct access to the things they manage most: their current plan and its progress, recent and upcoming workouts, their subscription status and renewal date with management actions, and a nutrition tracker. A final motivation-and-social section celebrates achievements and surfaces a community leaderboard, encouraging consistency and engagement. Throughout, the dashboard shows only the member's own data and never asks for information the application already holds, in line with good UX practice.

The page focuses on presenting personalised, real-time data within a fully responsive grid that adapts deliberately across breakpoints — the multi-column card layout reflowing into stacked cards and a bottom navigation bar on mobile — while keeping the most important information reachable at every size. Accessibility is built in throughout: a clear heading hierarchy, cards with labelled headings and descriptions, text alternatives for charts and progress bars, visible focus states, minimum 44px touch targets, full keyboard navigation, and status conveyed by more than colour alone. Through clarity, personalisation, and a motivating tone, the dashboard helps members understand their progress and decide what to do next with confidence.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="dashboard wireframe v3" src="https://github.com/user-attachments/assets/c47844f4-8f3d-4f59-8d2c-00092084f5fe" />

</details>

---

### Plans Listing

The plans listing page is where members and visitors discover FitHub's fitness plans and find the one that matches their goals and ability. A clear page header sets the purpose, and the page is built around helping users narrow a large catalogue down to relevant options quickly, so they can compare and choose with confidence.

The page combines a comprehensive filter sidebar with a responsive grid of plan cards. Filters allow users to refine by difficulty level, fitness goal, duration and features (such as video included, no equipment, or home-gym friendly), with a live result count beside each option and a clear "results found" total, while a sort control lets users order plans by relevance, popularity or price. Each plan card surfaces the key information needed for comparison at a glance — plan name, goal, star rating and review count, duration and time commitment, difficulty and feature badges, and price — alongside clear actions to view details or add the plan. The most popular plans are surfaced first and badged, and pagination keeps the catalogue performant and navigable.

The page focuses on efficient data filtering and a fully responsive layout that adapts deliberately across breakpoints — the desktop filter sidebar collapsing into an expandable filter panel/drawer on tablet and mobile, and the grid reflowing from three columns to one. Accessibility is built in throughout: a clear heading hierarchy, filters with associated labels and counts, keyboard-navigable cards, visible focus states, minimum 44px touch targets, and status indicators (difficulty badges) conveyed by text as well as colour. Trust is reinforced with supporting messaging on security, the money-back guarantee, and flexible cancellation. Through smart filtering, scannable cards, and clear comparison, users can find the right plan for their goals with minimal effort.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="plans_listing wireframe v4" src="https://github.com/user-attachments/assets/025c1112-73c0-454a-a64e-22df89cd4490" />

</details>

---

### Plan Detail

The plan detail page gives a member or visitor everything they need to evaluate a single fitness plan and decide whether it is right for them. A clear breadcrumb and page header establish context, and the page is structured so the most decision-critical information — what the plan is, what it costs, and how to get it — is immediately visible, while supporting detail is available for those who want it.

The page leads with an image carousel showing the plan from multiple angles alongside a prominent information card that summarises the goal, difficulty, rating and review count, and key facts such as duration, session length, equipment requirements and lesson count. Pricing is presented clearly with the saving on the annual option highlighted, and primary actions are always to hand. Beneath this, tabbed navigation organises the deeper content — an overview of what the member will learn, what's included and how the programme is structured; a curriculum; reviews; and FAQs — so the page remains scannable rather than overwhelming. Trust and confidence are reinforced through an instructor profile with credentials, aggregated member ratings and testimonials, and a "similar plans" section that supports comparison and continued browsing.

The page focuses on clear information hierarchy and a fully responsive layout that adapts deliberately across breakpoints — the sticky information and pricing card keeping the calls to action visible while scrolling on desktop, the content tabs becoming collapsible accordions on smaller screens to reduce scrolling, and a sticky bottom CTA bar ensuring the primary action is always reachable on mobile. Accessibility is built in throughout: a clear heading hierarchy, alt text for all images, an accessible accordion pattern for the FAQs, visible focus states, minimum 44px touch targets, and pricing options conveyed by text as well as colour. Through clear pricing, organised content, and strong social proof, the page helps users make a confident, well-informed decision.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="plans_detail wireframe v3" src="https://github.com/user-attachments/assets/73955235-7b3d-46c6-aee4-703ee398c0e4" />

</details>

---

### Shop Listing

The shop listing page is FitHub's storefront for physical merchandise — equipment, supplements and accessories — designed to help members find and purchase the right products quickly. A clear header and breadcrumb set the context, and the page is built around efficient browsing of a large catalogue, so users can filter a wide range of products down to relevant options and add them to their cart with minimal effort.

The page pairs a comprehensive filter sidebar with a responsive product grid. Users can refine by category, brand, price range, rating and stock status, each filter showing a live count, with a clear results total and a sort control for ordering by relevance, popularity or price. Each product card surfaces the information needed to make a purchase decision at a glance — product image, name, brand, star rating and review count, price, and real stock status (in stock, low stock, pre-order) — along with a quick-add quantity control and a view-details action, so members can add items to the cart directly from the grid without leaving the page. Pagination keeps the catalogue performant and navigable ("Showing 12 of 127 products").

The page focuses on efficient data filtering, accurate stock information, and a fully responsive layout that adapts deliberately across breakpoints — the desktop filter sidebar collapsing into an expandable filter panel on tablet and mobile, and the grid reflowing from three columns to two to one. Accessibility is built in throughout: a clear heading hierarchy, filters with associated labels and counts, keyboard-navigable cards, visible focus states, minimum 44px touch targets, and stock status conveyed by text as well as colour. Trust is reinforced with a persistent benefits bar covering secure checkout, free shipping, easy returns and the size of the member community. Through smart filtering, scannable cards, and quick add-to-cart, users can shop efficiently and with confidence.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="shop_listing wirefrme" src="https://github.com/user-attachments/assets/46809c29-a9e3-46a8-b70e-de324054d699" />

</details>

---

### Product Detail

The product detail page gives a member everything they need to evaluate and buy a single shop product with confidence. A clear breadcrumb and a rich media gallery establish the product immediately, and the page is structured so the key purchase decision — what the product is, its options, its price and stock, and how to buy it — is front and centre, with supporting detail available for those who want it.

The page leads with a high-resolution product gallery (with zoom, 360° view and video) alongside a prominent, sticky purchase card. That card summarises the product name, brand, rating and review count, real stock status with quantity remaining, and price, and lets the member configure their purchase through variant selection (colour swatches and weight options) and a quantity control before adding to the basket. Beneath this, tabbed navigation organises the deeper content — an overview of product highlights, what's in the box and certifications/warranty; specifications; reviews; and FAQs — keeping the page scannable. Confidence and value are reinforced through a detailed customer reviews breakdown with verified-purchase badges, a "frequently bought together" bundle, and a "customers also viewed" section that supports comparison and continued shopping.

The page focuses on clear information hierarchy, accurate stock information, and a fully responsive layout that adapts deliberately across breakpoints — the sticky purchase card keeping the calls to action visible while scrolling on desktop, the content tabs becoming collapsible accordions on smaller screens, and a sticky bottom add-to-cart bar ensuring the primary action is always reachable on mobile. Accessibility is built in throughout: alt text for all images, a keyboard-navigable gallery and controls, ARIA labels on interactive elements, visible focus states, minimum 44px touch targets, and variant and stock states conveyed by text as well as colour. Through rich media, clear options, accurate stock, and strong social proof, the page helps users make a confident, well-informed purchase.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="product_detail wirefrme" src="https://github.com/user-attachments/assets/087bb261-78c8-4200-8058-0a45e84fb7f4" />

</details>

---

### Shopping Cart

The shopping cart gives members a clear, trustworthy review of the products they intend to buy before committing to checkout. A clear header and breadcrumb set the context, and the page is designed so users can confirm their items, adjust what they're buying, and see exactly what they'll pay — with no surprises before payment.

The cart is organised into a cart-items list and an order summary. Each item is shown with its image, name, variant details (colour, size), price, an editable quantity control, stock status, and a line total, along with clear actions to remove the item or save it for later — the latter reducing accidental loss and cart abandonment. The order summary presents the subtotal, delivery and total, with the free-delivery threshold applied and pricing shown VAT-inclusive, and a promo-code field allows discounts to be applied. The summary and primary calls to action are kept prominent so the cost and the path to checkout are always clear. Stock visibility ("Only 2 left") and trust signals reinforce confidence at the point of decision.

The page focuses on accurate, real-time totals and a fully responsive layout that adapts deliberately across breakpoints — the order summary sitting sticky alongside the items on desktop, collapsing into an accordion on tablet, and becoming a sticky bottom bar with the total and checkout action on mobile. Four key states are designed for explicitly — empty cart, loading, error, and out-of-stock/quantity-capped — so the page behaves gracefully in real use rather than only on the happy path. Accessibility is built in throughout: a clear heading hierarchy, a live region announcing cart and total updates, descriptive labels on all interactive controls (including icon-only buttons via aria-labels), visible focus states, minimum 44px touch targets, and stock status conveyed by text as well as colour. Through clarity, accurate pricing, and trust-focused design, members can review their cart and proceed to checkout with confidence.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="shopping_cart wireframe v2" src="https://github.com/user-attachments/assets/6263009e-eb3a-4a86-8c54-ffef662bc088" />

</details>

---

### Checkout

The checkout page is where a member completes their purchase securely, and it is the most trust-critical page in the e-commerce flow. A clear breadcrumb and header set the context, and the page is designed to collect everything needed to fulfil and pay for the order — contact, delivery and payment details — in a single, well-structured flow that keeps the member oriented and confident at every step.

The page is organised into clear sections: a contact section (with the email pre-filled for logged-in members, so they are not asked for information the application already holds), a delivery details section with validated address fields and an option to save the address to the member's profile, and a payment section. Card details are captured using Stripe Elements, so the card field is hosted by Stripe and card data never touches the application's server — a genuine security benefit that is communicated to the user. A persistent order summary keeps the items and total visible throughout, and the primary call to action states the exact amount to be paid. The order itself is created via a Stripe webhook on successful payment, so the order is recorded reliably even if the member closes the browser immediately after paying.

The page focuses on secure payment, defensive design, and a fully responsive layout that adapts deliberately across breakpoints — the order summary sitting sticky alongside the form on desktop, collapsing into an accordion on tablet and mobile, and the pay action and total fixed in a sticky bottom bar on smaller screens. Several states are designed for explicitly — empty-cart guard, a processing overlay that prevents double submission, inline Stripe payment errors, and field-level validation errors — so the page handles real payment scenarios gracefully. Accessibility is built in throughout: fieldset/legend grouping for each section, labels and required indicators on all fields, an aria-live region for payment errors, focus moving to the first invalid field on submission, icon-only buttons carrying aria-labels, visible focus states, sufficient colour contrast, and minimum 44px touch targets. Through secure card handling, reliable order creation, and clear feedback, members can pay with confidence. (Note: this checkout handles one-time shop products; recurring subscriptions are processed through a separate Stripe Checkout flow.)

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="checkout wireframe v2" src="https://github.com/user-attachments/assets/7850123a-fdf4-4068-b468-38d1fa048287" />

</details>

---

### Order Confirmation

The order confirmation page reassures the member that their purchase succeeded and tells them what happens next, closing the e-commerce journey on a clear, confidence-building note. A prominent success message and the order reference are shown immediately, so the member has instant proof of their order and a number to reference for any future query.

The page presents the order in full: a read-only order summary listing the items, quantities, pricing and total (VAT-inclusive, with the free-delivery rule applied), the delivery address, and a "what happens next" timeline covering the confirmation email, packing and dispatch, and an estimated delivery date. The delivery estimate is calculated dynamically (order date plus processing and shipping time) so it is always accurate rather than hard-coded. Clear primary actions let the member view the order in their account or continue shopping, and a support section reduces post-purchase anxiety. Importantly, the page is reached after the Stripe redirect but is populated from the order created by the webhook, and a brief "confirming your order" state handles the case where the page loads before the webhook has finished — so the confirmation is reliable even under the asynchronous reality of payment processing.

The page focuses on clear feedback, robust handling of asynchronous processes, and a fully responsive layout that adapts deliberately across breakpoints, with the order details and timeline reflowing into stacked, collapsible sections on smaller screens while keeping the success message and key information visible. Several states are designed for explicitly — confirming/webhook-pending, order not found (with an ownership guard so a member can only view their own order), email-not-sent with a resend fallback, a guest-order variant, and email-sent-successfully. Accessibility is built in throughout: focus moves to the success heading on load, the order number is selectable text, updates are announced via an aria-live region, the delivery date is available on all breakpoints, and the design meets WCAG 2.1 AA. Through clear confirmation, a helpful next-steps timeline, and reliable order handling, the member leaves the journey informed and reassured.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="order_confirmation wireframe v2" src="https://github.com/user-attachments/assets/7f12874f-d99d-41b3-baa1-baeecf5ef6b6" />

</details>

---

### User Profile

The user profile, or "My Account", is the member's central hub for managing their account, viewing their activity, and controlling their membership and preferences. A clear header and breadcrumb set the context, and the page is organised so that the many different aspects of a member's relationship with FitHub — their details, subscription, orders, saved items and community activity — are grouped into focused sections rather than presented as one long, overwhelming form.

The page combines a persistent profile summary card (avatar, name, membership status and join date) with a tab-driven content area covering Overview, Account Details, Subscription, Orders, Saved Items and Community. The Overview tab gives an at-a-glance summary of the member's activity, fitness goal and active plan, while the other tabs provide focused management of each area. Account details use an edit-in-place pattern, allowing the member to update their information with validation and clear save/cancel actions — demonstrating update functionality directly in the interface. Subscription management is delegated to the Stripe Customer Portal, so billing changes and cancellations are handled securely without rebuilding payment infrastructure, with the application storing the Stripe customer ID and keeping plan status in sync via webhooks. Account actions, including a clearly separated and confirmed "delete account" option, are available throughout.

The page focuses on clear information architecture, full control over the member's own data, and a fully responsive layout that adapts deliberately across breakpoints — the section navigation moving from a sidebar on desktop, to a tab strip on tablet, to a dropdown on mobile. Several states are designed for explicitly — view mode, edit-in-place, validation error, update success, empty states for orders and saved items, and a type-to-confirm delete-account flow that respects the irreversibility of the action and the member's data-protection rights. Accessibility is built in throughout: an ARIA tab pattern, focus moving to the first field in edit mode, alt text on all images, descriptive labels, destructive actions behind confirmation, success and error announced via an aria-live region, minimum 44px touch targets, and WCAG 2.1 AA compliance. The page shows only the member's own, access-controlled data. Through clear organisation, in-place editing, and secure account management, members stay in full control of their FitHub account.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="user_profile wireframe v2" src="https://github.com/user-attachments/assets/4579b4ad-05c6-4f65-a884-3c4fafe55abd" />

</details>

---

### Order History

The order history page lets members view and manage their past orders as read-only historical records. A clear header and breadcrumb set the context, and the page is built around a list-and-detail model: a scannable list of all the member's orders, each opening into a full detail view, so members can find a past purchase quickly and review it in full.

The order list presents each order with its key information — order number, date, items, status and total — and supports filtering, sorting and searching so it remains usable as a member's history grows, with pagination keeping large histories performant. Order status is shown using a clear, consistent lifecycle (Processing, Dispatched, Delivered, Cancelled, Refunded) conveyed by text and icon rather than colour alone, and refund status is driven by Stripe webhooks so it stays accurate. Selecting an order opens its detail view, which reuses the structure of the confirmation page — items, delivery address, order summary and a status timeline — and provides useful actions such as reorder, invoice download and access to support. Throughout, an ownership guard ensures a member can only view their own orders. As with the rest of the account area, recurring subscription billing and invoices are managed in the Stripe Customer Portal rather than here.

The page focuses on clear presentation of historical data and a fully responsive layout that adapts deliberately across breakpoints — the desktop order table transforming into stacked cards on tablet and mobile, and the detail view reflowing into collapsible sections. Several states are designed for explicitly — loading, empty (no orders yet), no-results (from filters), many-orders (paginated), and order-not-found (with the ownership guard). Accessibility is built in throughout: a real data table with column headers on desktop, status badges carrying text and icons, descriptive link text ("View order FH-10428"), labelled filter controls, pagination marking the current page, an aria-live region for filter updates, visible focus states, minimum 44px touch targets, and WCAG 2.1 AA compliance. Through clear organisation, accurate status, and reliable access control, members can track and revisit their purchases with confidence.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="order_history wireframe v5" src="https://github.com/user-attachments/assets/02fff654-780c-4041-b738-8087685c94fa" />

</details>

---

### Admin Plan Creation

The admin plan creation and management page is the staff-only interface for managing FitHub's membership plans, deliberately built as a custom front-end rather than relying on the Django admin. It allows authorised staff to create, edit and archive plans through the application's own styled interface, keeping the management experience consistent with the rest of the site and demonstrating full owner-side control of catalogue content.

The page is structured around a plan-management list and a shared create/edit form. The list shows existing plans with their tier, price, billing interval and status (Published, Draft or Archived), each with edit and delete actions. The same form serves both creation and editing — empty for a new plan, pre-populated when editing — capturing the plan name, description, price and billing interval, tier, features and an image, with a published/draft status control. All input is validated server-side (required fields, price as a positive number, image type and size), and removal is handled as an archive/soft-delete behind a type-to-confirm step, so existing subscriptions and historical records are preserved rather than broken. Crucially, plans map to Stripe Products and Prices: creating a plan creates the corresponding Stripe objects via the API, and because Stripe Prices are immutable, editing a price creates a new Price and archives the previous one — with plan status kept in sync through Stripe webhooks.

The page focuses on secure, role-based access, robust data integrity, and a fully responsive layout that adapts deliberately across breakpoints, with the management table transforming into cards and the form reflowing into collapsible sections on smaller screens. Access control is enforced at two layers — the route is protected so non-staff users receive a 403, and the management controls are not rendered for non-staff in the interface — directly supporting the requirement that the data store is not accessible without going through appropriate permissions. Several states are designed for explicitly — loading, empty (no plans yet), permission-denied (403), validation error and save success. Accessibility is built in throughout: labelled fields with required indicators, fieldset/legend grouping, errors announced via an aria-live region with focus moving to the first invalid field, a focus-trapped confirmation dialog, descriptive action labels, minimum 44px touch targets, and WCAG 2.1 AA compliance. Through a custom interface, defensive validation, role-based permissions and Stripe synchronisation, staff can manage the plan catalogue safely and reliably.

<details>
<summary><strong>View wireframes (Desktop / Tablet / Mobile)</strong></summary>

<img width="1536" height="1024" alt="admin_plan_creation wireframe v2" src="https://github.com/user-attachments/assets/040556fa-3ac0-4e74-8e9d-e3c090ce7006" />

</details>

---

## FitHub — User Stories

[⬆ Back to Table of contents](#table-of-contents)

FitHub is a fitness subscription web application built with Django that allows users to enrol in fitness plans, purchase merchandise through an integrated e-commerce system, and interact with other members within a subscriber-only community platform.

- Each user story follows the standard format: *"As a [role], I want to [goal] so that [benefit]"* and is assigned a **MoSCo priority** (**Must**, **Should**, or **Could**) to indicate its relative importance within the project.

- **Acceptance Criteria (ACs)** are defined as measurable and testable conditions that determine whether a user story has been successfully implemented. These criteria also serve as the basis for both manual and automated testing activities.

- Progress is monitored using checkboxes throughout the document.

- A comprehensive mapping of user stories to the **Gateway Qualifications Unit 4: Full Stack Frameworks with Django** assessment criteria is provided at the end of this document.

### User Roles

- **Visitor** — An anonymous user who accesses the platform without being authenticated.

- **Member** — A registered user who has created an account and successfully logged into the application.

- **Subscriber** — A member with an active paid subscription, granting access to premium features and content.

- **Staff / Administrator** — An authorised user with elevated permissions responsible for managing platform content, subscriptions, products, and operational activities.

### User Story 1: Account Registration (Visitor)

#### As a visitor, I want to **create an account** so that **I can access member-only features, subscribe to fitness plans, and purchase products.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Registration Form Accessible to Visitors

- [ ] Given that a user is not authenticated, when they navigate to the registration page, then a clearly labelled account registration form is displayed.

##### AC2 – Restricted Access for Authenticated Users

- [ ] Given that a user is already logged in, when they attempt to access the registration page, then they are redirected to an appropriate page (such as their dashboard) instead of being shown the registration form.

##### AC3 – Validation of Mandatory Fields

- [ ] Given that a visitor submits the registration form with incomplete or invalid information, when the form is processed, then submission is prevented and clear field-specific validation messages are displayed.

##### AC4 – Password Strength and Confirmation Requirements

- [ ] Given that a visitor enters a password during registration, when the form is submitted, then the password must meet the defined security requirements and match the confirmation field before the account can be created.

##### AC5 – Prevention of Duplicate Registrations

- [ ] Given that an email address is already associated with an existing account, when a visitor attempts to register using that email address, then the registration request is rejected and an appropriate notification is displayed.

##### AC6 – Registration Success Confirmation

- [ ] Given that valid registration details are submitted, when the account is successfully created, then the system displays a confirmation message and, where applicable, sends an account verification email.

##### AC7 – Secure Storage of User Credentials

- [ ] Given that a new account has been created, when user credentials are stored, then passwords are securely hashed and no sensitive credentials, secret keys, or authentication data are exposed within the source code or repository.

##### AC8 – Accessibility and Responsive Design Compliance

- [ ] Given that a visitor accesses the registration form using a desktop, tablet, mobile device, or assistive technology, when interacting with the form, then all controls are keyboard accessible, screen-reader compatible, responsive, and supported by meaningful labels and accessible error messaging.

---

### User Story 2: Secure Authentication (Visitor / Member)

#### As a visitor, I want to **sign in and sign out securely** so that **I can access my account while ensuring my personal information remains protected.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Login Form Available to Unauthenticated Users

- [ ] Given that a user is not logged in, when they navigate to the login page, then a clearly labelled authentication form is displayed.

##### AC2 – Restricted Access to Authentication Pages

- [ ] Given that a user is already authenticated, when they attempt to access the login or registration pages, then they are redirected to an appropriate location rather than being shown the authentication forms.

##### AC3 – Successful User Authentication

- [ ] Given that a member enters valid login credentials, when the authentication form is submitted, then access is granted and the user is redirected to their dashboard or the originally requested page.

##### AC4 – Feedback for Invalid Credentials

- [ ] Given that a member enters incorrect login details, when the authentication attempt fails, then the system displays a clear and generic error message without indicating whether the email address or password was incorrect.

##### AC5 – Secure Logout Functionality

- [ ] Given that a user is authenticated, when they select the logout option, then their session is terminated, access to protected resources is revoked, and a logout confirmation message is displayed.

##### AC6 – Authentication Required for Protected Content

- [ ] Given that a visitor attempts to access a restricted page directly via its URL, when they are not authenticated, then they are redirected to the login page and prevented from viewing protected content.

##### AC7 – Accessible and Responsive Authentication Experience

- [ ] Given that a user accesses the authentication system from a desktop, tablet, mobile device, or assistive technology, when logging in or out, then the process is fully responsive, keyboard accessible, screen-reader compatible, and provides clear user feedback throughout.

---

### User Story 3: Browse Fitness Plans (Visitor / Member)

#### As a visitor or member, I want to **view and explore the available fitness plans** so that **I can identify the option that best aligns with my fitness goals before committing to a subscription.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Published Plans Retrieved from the Database

- [ ] Given that fitness plans are available, when a user accesses the Plans page, then all published plans are retrieved from the database and displayed in a clear and organised card-based layout.

##### AC2 – Essential Plan Information Displayed

- [ ] Given that plans are displayed on the Plans page, when a user views an individual plan card, then the card includes, at a minimum, the plan name, difficulty level or tier, subscription price, and billing frequency.

##### AC3 – Filtering and Sorting Functionality

- [ ] Given that multiple fitness plans are available, when a user applies filters (such as plan type or difficulty level) or changes the sorting criteria, then the displayed results update accordingly to reflect the selected options.

##### AC4 – Subscriber-Only Content Clearly Identified

- [ ] Given that a plan contains premium or subscriber-exclusive content, when it is viewed by a non-subscriber, then a clear access restriction indicator is displayed using both text and an accompanying icon rather than relying solely on colour.

##### AC5 – Empty State Management

- [ ] Given that no plans match the selected filters, or no plans are currently published, when the Plans page is displayed, then a clear and user-friendly message is presented instead of an empty or incomplete interface.

##### AC6 – Responsive Layout Across Devices

- [ ] Given that a user accesses the Plans page from a desktop, tablet, or mobile device, when the page is rendered, then the layout adapts appropriately to the available screen size without requiring horizontal scrolling.

##### AC7 – Accessibility Compliance

- [ ] Given that a user navigates the Plans page using assistive technologies, when interacting with plan cards and controls, then semantic HTML structure is used, images include meaningful alternative text, and all interactive elements remain fully keyboard accessible.

##### AC8 – Graceful Error Handling

- [ ] Given that plan information cannot be retrieved from the database, when the Plans page attempts to load, then a clear and user-friendly error message is displayed instead of exposing a system or server error.

---

### User Story 4: View Fitness Plan Details and Access-Controlled Content (Member)

#### As a member, I want to **view detailed information about a fitness plan** so that **I can make an informed decision before subscribing or accessing premium content.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Comprehensive Plan Details Displayed

- [ ] Given that a user selects a fitness plan, when the plan detail page loads, then a comprehensive overview is displayed, including the plan description, difficulty level, key features, and an appropriate call-to-action for subscribing or accessing content.

##### AC2 – Content Restriction for Non-Subscribers

- [ ] Given that a member does not have an active subscription, when they view a subscriber-exclusive fitness plan, then a preview or teaser of the content is displayed together with a clear subscription call-to-action instead of the full protected content.

##### AC3 – Full Access for Eligible Subscribers

- [ ] Given that a member has an active subscription that includes the selected fitness plan, when they access the plan detail page, then the complete plan content is made available.

##### AC4 – Server-Side Access Control Enforcement

- [ ] Given that protected plan content is requested, when access permissions are evaluated, then authorisation is enforced on the server side to prevent non-subscribers from accessing restricted content through URL manipulation, browser tools, or modified requests.

##### AC5 – Context-Aware Calls to Action

- [ ] Given that a user is viewing a fitness plan, when the page is displayed, then the primary call-to-action clearly reflects their current subscription status, such as subscribing to the plan or accessing available content.

##### AC6 – Accessibility and Responsive Design Compliance

- [ ] Given that a user accesses the plan detail page using any device or assistive technology, when interacting with the page, then the content remains readable, headings follow a logical hierarchy, and all controls are fully keyboard accessible and screen-reader compatible.

##### AC7 – Graceful Handling of Missing or Invalid Plans

- [ ] Given that a user requests a fitness plan that does not exist, when the request is processed, then a user-friendly "Plan Not Found" message is displayed together with a navigation option that allows the user to return to the Plans page.

---

### User Story 5: Subscribe to a Membership Plan (Member)

#### As a member, I want to **subscribe to a membership plan** so that **I can gain access to premium fitness content, exclusive resources, and the subscriber community.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Secure Subscription Checkout for Authenticated Members

- [ ] Given that a member is logged into the platform, when they choose a subscription plan and billing option (monthly or annual), then they are redirected to a secure Stripe checkout process for the selected subscription.

##### AC2 – Secure Payment Processing via Stripe

- [ ] Given that a member enters payment information during checkout, when the transaction is processed, then Stripe securely handles the payment and no payment card information is stored, processed, or exposed by the application.

##### AC3 – Subscription Confirmation Through Webhooks

- [ ] Given that a subscription payment has been successfully completed, when Stripe sends the relevant webhook event (for example, `customer.subscription.created`), then the subscription record is created or updated within the database, ensuring reliable processing even if the user closes their browser before the checkout flow completes.

##### AC4 – Clear Subscription Success Feedback

- [ ] Given that a subscription has been successfully activated, when the member is redirected back to the application, then a confirmation message is displayed containing the selected plan, subscription cost, billing interval, and renewal date.

##### AC5 – Helpful Payment Failure Handling

- [ ] Given that a payment is declined or cannot be completed, when the transaction fails, then the system displays a clear and informative error message and allows the member to retry the payment process without losing their progress.

##### AC6 – Immediate Subscription Status Updates

- [ ] Given that a subscription becomes active, when the member next interacts with the application, then their subscription status is reflected consistently throughout the platform, including their profile, dashboard, content access permissions, and community features.

##### AC7 – Prevention of Duplicate Active Subscriptions

- [ ] Given that a member already has an active subscription, when they attempt to subscribe to another plan, then the system prevents the creation of duplicate subscriptions and directs the member to manage their existing subscription where appropriate.

##### AC8 – Accessible and Responsive Subscription Experience

- [ ] Given that a member completes the subscription process on a desktop, tablet, mobile device, or through assistive technologies, when progressing through the checkout journey, then all functionality remains responsive, keyboard accessible, screen-reader compatible, and provides clear feedback at every stage.

---

### User Story 6: Manage or Cancel a Subscription (Subscriber)

#### As a subscriber, I want to **manage or cancel my subscription** so that **I can maintain control over my membership, billing preferences, and subscription status.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Subscription Management Option Available

- [ ] Given that a user has an active subscription, when they access their profile or subscription management area, then a clearly visible **Manage Subscription** option is displayed.

##### AC2 – Integration with the Stripe Customer Portal

- [ ] Given that a subscriber chooses to manage their membership, when they select the **Manage Subscription** option, then they are securely redirected to the Stripe Customer Portal where they can update payment details, change subscription plans, or cancel their subscription.

##### AC3 – Subscription Changes Synchronised via Webhooks

- [ ] Given that a subscriber modifies or cancels their subscription through Stripe, when the relevant webhook event (for example, `customer.subscription.updated` or `customer.subscription.deleted`) is received, then the subscription status is accurately synchronised with the application's database.

##### AC4 – Ownership-Based Access Control

- [ ] Given that a subscriber accesses subscription management features, when subscription information is displayed, then they can only view and manage subscriptions associated with their own account.

##### AC5 – Continued Access Until the End of the Billing Period

- [ ] Given that a subscriber cancels an active subscription, when the cancellation is processed, then access to subscriber-only content and features remains available until the end of the current paid billing cycle, after which access is automatically removed.

##### AC6 – Subscription Status Reflected Across the Platform

- [ ] Given that a subscription is updated, downgraded, upgraded, or cancelled, when the subscriber next interacts with the application, then the updated membership status is displayed consistently within their profile, dashboard, and access-controlled areas.

##### AC7 – Clear Confirmation and User Feedback

- [ ] Given that a subscription management action has been completed successfully, when the process finishes, then the subscriber is presented with a clear confirmation message describing the outcome of the action performed.

##### AC8 – Accessible and Responsive Subscription Management

- [ ] Given that a subscriber manages their membership using a desktop, tablet, mobile device, or assistive technology, when interacting with subscription management features, then all controls remain responsive, keyboard accessible, screen-reader compatible, and clearly labelled.

---

### User Story 7: Add Products to the Shopping Cart (Member)

#### As a member, I want to **add products to my shopping cart** so that **I can purchase fitness-related merchandise and equipment.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Add Products from Listing and Detail Pages

- [ ] Given that a member is viewing a product from either the shop catalogue or an individual product page, when they select a quantity and choose **Add to Cart**, then the selected item is added to their shopping cart.

##### AC2 – Cart Contents Persist Throughout the Session

- [ ] Given that a member has added one or more items to their cart, when they continue browsing the application, then the cart contents remain available and unchanged throughout their active session.

##### AC3 – Stock Availability Validation

- [ ] Given that a member attempts to add a quantity greater than the available stock level, when the request is processed, then the system limits the quantity to the maximum available amount and displays an informative message explaining the restriction.

##### AC4 – Real-Time Cart Indicator Updates

- [ ] Given that a product has been successfully added to the shopping cart, when the action is completed, then the cart quantity indicator displayed within the navigation bar updates immediately to reflect the change.

##### AC5 – Clear User Feedback Following Cart Updates

- [ ] Given that an item has been added to the cart, when the operation succeeds, then the member receives a clear confirmation message indicating that the product has been successfully added.

##### AC6 – Separation of Product Purchases and Subscriptions

- [ ] Given that a member adds items to their cart, when the cart is updated, then only one-time purchasable products are included, while recurring subscription plans continue to be processed through the dedicated subscription workflow.

##### AC7 – Accessible and Responsive Cart Functionality

- [ ] Given that a member interacts with shopping cart functionality using a desktop, tablet, mobile device, or assistive technology, when adding products to the cart, then all controls remain responsive, keyboard accessible, screen-reader compatible, and clearly labelled.

---

### User Story 8: Update or Remove Shopping Cart Items (Member)

#### As a member, I want to **modify item quantities or remove products from my shopping cart** so that **my order accurately reflects the items I intend to purchase.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Quantity Updates with Real-Time Price Recalculation

- [ ] Given that a member changes the quantity of an item within their shopping cart, when the update is applied, then the corresponding line total and overall order total are recalculated immediately, and the change is announced to assistive technologies using an appropriate live region.

##### AC2 – Remove Products from the Shopping Cart

- [ ] Given that a member chooses to remove an item from their cart, when the action is confirmed, then the product is removed and all pricing totals are recalculated accordingly.

##### AC3 – Save Items for Later Purchase

- [ ] Given that a member selects the **Save for Later** option, when the action is processed, then the item is removed from the active cart and stored separately so that it can be restored at a later date.

##### AC4 – Stock Availability Enforcement

- [ ] Given that a member attempts to increase a product quantity beyond the available stock level, when the update is submitted, then the system prevents the change and displays the maximum quantity currently available.

##### AC5 – Empty Cart State Handling

- [ ] Given that no products remain in the shopping cart, when the cart page is displayed, then a clear and user-friendly empty-cart message is shown together with a prominent link directing the member back to the shop.

##### AC6 – Accurate Order Calculations

- [ ] Given that the contents of the shopping cart are modified, when totals are recalculated, then the subtotal, delivery charges, discounts (where applicable), and final order total are calculated correctly, including any free-delivery threshold rules.

##### AC7 – Accessible and Responsive Cart Management

- [ ] Given that a member manages their cart using a desktop, tablet, mobile device, or assistive technology, when interacting with quantity controls and action buttons, then all controls remain responsive, keyboard accessible, screen-reader compatible, and include descriptive labels.

---

### User Story 9: Secure Checkout and Payment Processing (Member)

#### As a member, I want to **complete the checkout process and pay securely** so that **I can purchase products with confidence and receive a reliable order confirmation.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Delivery Information Validation

- [ ] Given that a member proceeds to the checkout page, when delivery information is entered and submitted, then all required fields are validated on the server side before payment processing can begin.

##### AC2 – Secure Payment Collection Through Stripe

- [ ] Given that a member enters payment details during checkout, when card information is provided, then the payment field is delivered through **Stripe Elements**, ensuring that card data is processed securely by Stripe and never reaches the application server.

##### AC3 – Prevention of Duplicate Payment Submissions

- [ ] Given that a member submits a payment request, when the transaction is being processed, then a loading or processing state is displayed and further submissions are temporarily disabled to prevent duplicate charges.

##### AC4 – Order Confirmation Through Webhooks

- [ ] Given that a payment has been successfully authorised, when the `payment_intent.succeeded` webhook event is received from Stripe, then the corresponding order is created or confirmed within the application's database, ensuring reliability even if the user closes their browser before redirection completes.

##### AC5 – Successful Checkout Confirmation

- [ ] Given that payment has been processed successfully, when the checkout process is completed, then the member is presented with a clear confirmation message and redirected to an order confirmation page.

##### AC6 – Payment Failure Recovery

- [ ] Given that a payment attempt is declined or encounters an error, when the transaction fails, then a clear inline error message is displayed and the member is able to correct the issue and retry without losing their cart contents.

##### AC7 – Accurate Pricing and Order Totals

- [ ] Given that an order is submitted, when pricing information is calculated, then all totals, including VAT-inclusive pricing, delivery charges, discounts, and free-delivery threshold rules, accurately match the values previously displayed within the shopping cart.

##### AC8 – Protection Against Empty Cart Checkouts

- [ ] Given that a member attempts to access the checkout page without any items in their shopping cart, when the request is processed, then they are redirected to the shop rather than being presented with an invalid £0.00 checkout process.

##### AC9 – Accessible and Responsive Checkout Experience

- [ ] Given that a member completes the checkout process using a desktop, tablet, mobile device, or assistive technology, when interacting with the checkout form, then the interface remains responsive, keyboard accessible, screen-reader compatible, and provides clear feedback for validation errors and payment outcomes.

---

### User Story 10: View Order Confirmation (Member)

#### As a member, I want to **view a confirmation of my completed order** so that **I have clear evidence that my purchase was processed successfully.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Order Confirmation Displayed Following Successful Payment

- [ ] Given that a member's payment has been successfully processed, when the transaction is completed, then an order confirmation page is displayed.

##### AC2 – Display of Essential Order Information

- [ ] Given that an order confirmation page is shown, when the member reviews the confirmation, then it includes the order reference number, purchased items, order total, delivery information, and confirmation that an order email has been sent.

##### AC3 – Confirmation Data Sourced from the Verified Order Record

- [ ] Given that the order confirmation page is loaded, when order information is displayed, then the data originates from the order record created or confirmed by the Stripe webhook rather than being generated solely from redirect parameters.

##### AC4 – Support for Asynchronous Order Confirmation

- [ ] Given that the order confirmation page loads before the webhook has finished processing the order, when the page is displayed, then a temporary **"Confirming Your Order"** status is shown and automatically transitions to the completed confirmation view once processing has finished.

##### AC5 – Ownership and Authorisation Controls

- [ ] Given that a member attempts to access an order confirmation page, when the request is processed, then only orders associated with their account are accessible, and any attempt to view another user's order results in an appropriate not-found or permission-denied response.

##### AC6 – Confirmation Email Guidance and Support

- [ ] Given that an order has been successfully confirmed, when the confirmation page is displayed, then the member is informed that a confirmation email has been sent and provided with appropriate guidance if the email has not been received (for example, checking spam folders or requesting a resend).

##### AC7 – Accessible and Responsive Confirmation Experience

- [ ] Given that a member accesses the order confirmation page using a desktop, tablet, mobile device, or assistive technology, when viewing the confirmation details, then the order number remains selectable text, headings follow a logical hierarchy, and the layout adapts appropriately to different screen sizes while remaining fully accessible.

---

### User Story 11: View Order History (Member)

#### As a member, I want to **access and review my previous orders** so that **I can monitor, track, and reference my past purchases.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Order History Accessible to Authenticated Members

- [ ] Given that a member is logged in, when they navigate to the **Order History** section, then a list of their previous orders is displayed.

##### AC2 – User-Specific Order Visibility

- [ ] Given that the order history page is loaded, when order records are retrieved, then only orders associated with the authenticated member's account are shown.

##### AC3 – Structured Presentation of Order Information

- [ ] Given that one or more orders exist, when the order history is displayed, then each order includes key information such as the order reference number, purchase date, item quantity, order status, and total amount paid.

##### AC4 – Clear and Accessible Status Indicators

- [ ] Given that order records are displayed, when a status is shown (for example, Processing, Dispatched, Delivered, Cancelled, or Refunded), then it is communicated using both descriptive text and an accompanying icon rather than relying solely on colour.

##### AC5 – Filtering, Sorting, and Pagination Support

- [ ] Given that a member has a large number of orders, when browsing their order history, then they can filter, sort, and paginate the results to maintain usability and efficient navigation.

##### AC6 – Secure Access to Order Details

- [ ] Given that a member selects an order from their history, when the order detail page is displayed, then they can view the complete order information, and access to orders belonging to other members is prevented through server-side ownership validation.

##### AC7 – Empty-State Handling

- [ ] Given that a member has not yet placed any orders, when the order history page is accessed, then a clear empty-state message is displayed together with a prominent link directing them to the shop.

##### AC8 – Accessible and Responsive Design

- [ ] Given that a member views their order history using a desktop, tablet, mobile device, or assistive technology, when interacting with the page, then the content is presented in an accessible format (such as a table with headers on larger screens and card-based layouts on smaller screens) and remains fully keyboard navigable.

---

### User Story 12: Create, Update and Delete Product Reviews (Member)

#### As a member, I want to **create, edit, and remove product reviews** so that **I can share my experiences with other users and ensure my feedback remains accurate and up to date.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Review Submission Available to Eligible Members

- [ ] Given that a logged-in member is viewing a product page, when they choose to leave feedback, then a review form containing a rating field and comment area is available.

##### AC2 – Review Creation with Input Validation

- [ ] Given that a member submits a review, when the form is processed, then all input is validated (for example, a mandatory rating and character limits), and valid reviews are saved and associated with both the member and the relevant product.

##### AC3 – Immediate Review and Rating Updates

- [ ] Given that a review has been successfully submitted, when the product page refreshes or reloads, then the review is displayed and the product's average rating is recalculated and updated accordingly.

##### AC4 – Edit Existing Reviews

- [ ] Given that a member has previously submitted a review, when they choose to modify it, then the updated content is validated and saved successfully.

##### AC5 – Delete Reviews with Confirmation

- [ ] Given that a member chooses to remove one of their reviews, when the deletion request is confirmed, then the review is permanently removed and the product's average rating is recalculated to reflect the change.

##### AC6 – Ownership-Based Permissions

- [ ] Given that a member attempts to edit or delete a review, when the request is processed, then they can only modify reviews that they have created and are prevented from changing reviews submitted by other members.

##### AC7 – Secure Handling of Review Content

- [ ] Given that review content is submitted, stored, and displayed, when the data is processed, then it is sanitised and escaped appropriately to prevent malicious scripts or unauthorised code execution.

##### AC8 – Accessible and Responsive Review Features

- [ ] Given that a member interacts with the review system using a desktop, tablet, mobile device, or assistive technology, when creating, editing, or deleting reviews, then all forms and review content remain responsive, keyboard accessible, screen-reader compatible, and clearly labelled.

---

### User Story 13: Create, Edit and Delete Community Posts (Subscriber)

#### As a subscriber, I want to **create, update, and remove community posts** so that **I can actively participate in discussions and engage with other members of the fitness community.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Community Posting Restricted to Active Subscribers

- [ ] Given that a user does not have an active subscription, when they attempt to create a community post, then access is denied through server-side permission checks and a clear subscription prompt is displayed.

##### AC2 – Community Post Creation with Validation

- [ ] Given that an active subscriber submits a new community post, when the form is processed, then all input is validated and, if successful, the post is saved and linked to the subscriber's account.

##### AC3 – Immediate Display of New Posts

- [ ] Given that a community post has been created successfully, when the action is completed, then the post appears within the community feed without requiring additional user interaction.

##### AC4 – Edit Existing Community Posts

- [ ] Given that a subscriber has authored a community post, when they choose to edit it, then the updated content is validated and saved successfully.

##### AC5 – Delete Community Posts with Confirmation

- [ ] Given that a subscriber chooses to remove one of their community posts, when the deletion request is confirmed, then the post is permanently removed from the community feed.

##### AC6 – Ownership-Based Authorisation

- [ ] Given that a subscriber attempts to edit or delete a community post, when the request is processed, then they are only permitted to modify posts that they have authored and are prevented from changing content created by other users.

##### AC7 – Secure Handling of Community Content

- [ ] Given that post content is submitted, stored, and displayed within the application, when the data is processed, then it is appropriately sanitised and escaped to protect against malicious scripts and unauthorised code execution.

##### AC8 – Accessible and Responsive Community Features

- [ ] Given that a subscriber accesses the community area using a desktop, tablet, mobile device, or assistive technology, when interacting with the post creation form or community feed, then all controls remain responsive, keyboard accessible, screen-reader compatible, and clearly labelled.

---

### User Story 14: View the Community Feed (Subscriber)

#### As a subscriber, I want to **access and browse the community feed** so that **I can stay informed about updates, discussions, and experiences shared by other members.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Community Feed Available to Active Subscribers

- [ ] Given that a user has an active subscription, when they navigate to the community area, then community posts are retrieved from the database and displayed within the feed.

##### AC2 – Access Control for Non-Subscribers

- [ ] Given that a user does not have an active subscription, when they attempt to access the community feed, then they are presented with a preview or teaser page together with a subscription call-to-action, while access to the full feed is restricted through server-side permission checks.

##### AC3 – Clear and Consistent Post Presentation

- [ ] Given that posts are displayed within the community feed, when the page loads, then each post includes the author's name, publication date, and content in a clear, readable, and consistent format.

##### AC4 – Pagination for Scalability and Performance

- [ ] Given that a large number of community posts exist, when the feed is displayed, then pagination is applied to ensure efficient performance and a positive user experience.

##### AC5 – Empty-State Handling

- [ ] Given that no community posts have been created, when a subscriber accesses the feed, then a friendly message is displayed encouraging members to create the first post and begin community engagement.

##### AC6 – Accessible and Responsive Community Experience

- [ ] Given that a subscriber views the community feed using a desktop, tablet, mobile device, or assistive technology, when interacting with the page, then posts are presented using semantic HTML structure, the layout adapts appropriately to different screen sizes, and all content remains keyboard accessible and screen-reader compatible.

---

### User Story 15: Manage My Profile Information (Member)

#### As a member, I want to **update and maintain my profile details** so that **my personal information, fitness preferences, and account settings remain accurate and up to date.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Profile Displays Member-Specific Information

- [ ] Given that a member accesses their profile page, when the page loads, then their personal information, including name, email address, fitness goals, profile image, and subscription status, is displayed accurately.

##### AC2 – Profile Information Can Be Updated

- [ ] Given that a member edits their profile information, when the updated details are submitted, then all changes are validated and successfully saved to the database.

##### AC3 – Email Address Uniqueness Validation

- [ ] Given that a member attempts to change their email address, when the submitted email is already associated with another account, then the update is rejected and a clear validation message is displayed.

##### AC4 – Profile Image Upload and Validation

- [ ] Given that a member uploads a profile image, when the file is submitted, then the file type and size are validated, the image is stored using the configured media or cloud storage solution, and the updated image is displayed within the member's profile.

##### AC5 – Ownership-Based Access Control

- [ ] Given that a member accesses profile management functionality, when profile data is retrieved or updated, then they can only view and modify information associated with their own account and are prevented from accessing another user's data.

##### AC6 – Clear Success and Error Feedback

- [ ] Given that a profile update succeeds or fails, when the operation is completed, then the member receives a clear confirmation or error message, which is announced to assistive technologies through an appropriate live region.

##### AC7 – Intelligent Form Pre-Population

- [ ] Given that a member is authenticated and accesses a profile form, when existing information is available, then the application automatically pre-populates relevant fields (such as email address and personal details) to reduce unnecessary data entry.

##### AC8 – Accessible and Responsive Profile Management

- [ ] Given that a member updates their profile using a desktop, tablet, mobile device, or assistive technology, when interacting with profile forms, then all fields are clearly labelled, focus is managed appropriately during edit operations, and the interface remains responsive, keyboard accessible, and screen-reader compatible.

---

### User Story 16: View a Personalised Dashboard (Member)

#### As a member, I want to **access a personalised dashboard** so that **I can quickly view important account information and navigate to the features most relevant to me.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Dashboard Available to Authenticated Members

- [ ] Given that a member has successfully logged in, when they access their account area, then a personalised dashboard is available and displays an overview of their account.

##### AC2 – Relevant Personalised Summary Information

- [ ] Given that the dashboard is loaded, when account data is retrieved, then the dashboard displays relevant information such as subscription status, recent orders, saved items, and the member's fitness goals.

##### AC3 – Member-Specific Data Only

- [ ] Given that a member accesses their dashboard, when account information is displayed, then only data associated with the authenticated member's account is shown.

##### AC4 – Upgrade Prompt for Non-Subscribers

- [ ] Given that a member does not have an active subscription, when they view the dashboard, then a clear upgrade or subscription call-to-action is displayed in place of subscriber-only content or functionality.

##### AC5 – Quick Access to Key Features

- [ ] Given that the dashboard is displayed, when a member reviews the available options, then clear navigation shortcuts are provided to important areas of the application, including fitness plans, the shop, the community area, and profile management.

##### AC6 – Accessible and Responsive Dashboard Experience

- [ ] Given that a member accesses the dashboard using a desktop, tablet, mobile device, or assistive technology, when interacting with dashboard content, then information is organised using a logical heading structure, the layout adapts appropriately to different screen sizes, and all interactive elements remain keyboard accessible and screen-reader compatible.

---

### User Story 17: Delete My Account (Member)

#### As a member, I want to **permanently delete my account** so that **I can remove my personal information and discontinue use of the service when it is no longer required.** *(Could Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Account Deletion Option Available

- [ ] Given that a member accesses their account settings or profile area, when the page is displayed, then a clearly identifiable **Delete Account** option is available.

##### AC2 – Confirmation of Destructive Actions

- [ ] Given that a member chooses to delete their account, when the deletion process is initiated, then explicit confirmation is required (for example, through a type-to-confirm mechanism) before the action can proceed.

##### AC3 – Active Subscription Handling

- [ ] Given that a member has an active subscription, when their account is deleted, then any associated Stripe subscription is cancelled as part of the account deletion process.

##### AC4 – Compliance with Data Protection Requirements

- [ ] Given that an account deletion request is completed, when the member's data is processed, then personal information is removed or anonymised in accordance with applicable data protection and right-to-erasure requirements, whilst retaining any records necessary to preserve order integrity and legal obligations.

##### AC5 – Ownership-Based Authorisation

- [ ] Given that a member requests account deletion, when the request is processed, then they may only delete their own account and cannot perform deletion actions on behalf of another user.

##### AC6 – Confirmation, Logout and Redirection

- [ ] Given that account deletion has been completed successfully, when the process finishes, then the member is logged out, presented with a confirmation message, and redirected to an appropriate public-facing page.

##### AC7 – Accessible and Responsive Deletion Workflow

- [ ] Given that a member deletes their account using a desktop, tablet, mobile device, or assistive technology, when progressing through the confirmation process, then all controls remain keyboard accessible, focus is managed appropriately, and the workflow is clearly labelled and responsive.

---

### User Story 18: Create, Edit and Archive Membership Plans (Admin)

#### As an administrator, I want to **create, update, and archive membership plans** so that **I can manage the platform's subscription offerings through a dedicated front-end interface without relying on the Django administration panel.** *(Must Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Staff-Only Access with Defence-in-Depth Controls

- [ ] Given that a non-staff user attempts to access the membership plan management area directly via a URL, when the request is processed, then a **403 Forbidden** response is returned, and management controls are hidden from non-staff users throughout the user interface.

##### AC2 – Dedicated Front-End Management Interface

- [ ] Given that an administrator manages membership plans, when performing management actions, then all functionality is available through the application's custom front-end interface rather than the built-in Django administration system.

##### AC3 – Create New Membership Plans

- [ ] Given that an administrator completes the plan creation form with valid information, when the form is submitted, then a new membership plan is saved successfully and displayed within the management interface and, when published, becomes visible on the customer-facing Plans page.

##### AC4 – Shared Create and Edit Workflow

- [ ] Given that an administrator chooses to edit an existing membership plan, when the edit page is opened, then the same form used for creation is displayed with the plan's existing data pre-populated, and any valid changes are saved successfully.

##### AC5 – Comprehensive Server-Side Validation

- [ ] Given that an administrator submits a membership plan form, when the data is processed, then all input is validated on the server side, including required fields, positive pricing values, image type restrictions, and file-size limits, with clear inline validation messages displayed for invalid submissions.

##### AC6 – Archive Plans Instead of Permanent Deletion

- [ ] Given that an administrator removes a membership plan, when the action is confirmed, then the plan is archived (soft deleted) rather than permanently removed, ensuring that existing subscriptions and historical records remain intact whilst preventing new users from subscribing to the archived plan.

##### AC7 – Synchronisation with Stripe Products and Prices

- [ ] Given that an administrator creates or updates a membership plan, when the change is processed, then the corresponding Stripe Product and Price records are synchronised accordingly. Where a pricing change occurs, a new Stripe Price is created and the previous Price is archived because Stripe Prices are immutable.

##### AC8 – Immediate Reflection of Administrative Changes

- [ ] Given that an administrator creates, updates, or archives a membership plan, when the request is completed successfully, then the changes are reflected within the management interface and customer-facing pages on the next application request.

##### AC9 – Clear Success and Failure Feedback

- [ ] Given that an administrative action succeeds or fails, when processing is complete, then the administrator receives clear confirmation or error feedback, and no partial updates are applied if an operation fails.

##### AC10 – Accessible and Responsive Management Interface

- [ ] Given that an administrator manages membership plans using a desktop, tablet, mobile device, or assistive technology, when interacting with the interface, then forms use appropriate labels, fieldsets, and validation messaging, errors are announced to assistive technologies, and the layout adapts responsively across different screen sizes (for example, transforming from tables to card-based layouts).

---

### User Story 19: Manage Shop Products (Admin)

#### As an administrator, I want to **create, update, and manage shop products** so that **customers are presented with accurate, up-to-date merchandise listings at all times.** *(Should Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Restricted Access for Staff Users

- [ ] Given that a non-staff user attempts to access the product management area, when the request is processed, then access is denied with a **403 Forbidden** response, and all management controls remain hidden from non-staff users throughout the application interface.

##### AC2 – Product Catalogue Management View

- [ ] Given that an administrator opens the product management section, when the page loads, then all existing products are displayed in a structured list showing key information, including product name, category, price, stock level, and availability status.

##### AC3 – Create New Products

- [ ] Given that an administrator completes the product creation form with valid information, when the form is submitted, then the product is saved successfully and becomes visible within the management interface and, where applicable, the customer-facing shop.

##### AC4 – Edit Existing Products

- [ ] Given that an administrator updates product information, when valid changes are submitted, then the amended product details are stored in the database and reflected across the customer-facing shop on the next request.

##### AC5 – Archive or Hide Products

- [ ] Given that an administrator chooses to remove a product from sale, when the action is confirmed, then the product is hidden or archived rather than permanently deleted, ensuring historical orders remain intact whilst preventing new purchases.

##### AC6 – Validation and Image Management

- [ ] Given that an administrator submits product information, when the data is processed, then all required fields are validated, pricing values are verified, and any uploaded product images are checked for permitted file types and size restrictions.

##### AC7 – Immediate Reflection of Product Changes

- [ ] Given that a product is created, edited, archived, or hidden, when the operation is completed successfully, then the updated information is reflected within the customer-facing shop on the next application request.

##### AC8 – Accessible and Responsive Administration Interface

- [ ] Given that an administrator manages products using a desktop, tablet, mobile device, or assistive technology, when interacting with the interface, then all controls remain keyboard accessible, clearly labelled, and responsive across different screen sizes.

---

### User Story 20: View Orders and Subscribers (Admin)

#### As an administrator, I want to **view and monitor customer orders and subscriber accounts** so that **I can provide effective customer support and oversee business activity.** *(Could Have)*

[⬆ Back to Table of Contents](#table-of-contents)

#### Acceptance Criteria

##### AC1 – Restricted Access for Staff Users

- [ ] Given that a non-staff user attempts to access order or subscriber management areas, when the request is processed, then access is denied with a **403 Forbidden** response.

##### AC2 – Order Management Overview

- [ ] Given that an administrator accesses the orders section, when the page loads, then a structured list of orders is displayed, including key information such as order number, customer name, order date, current status, and total value.

##### AC3 – Subscriber Management Overview

- [ ] Given that an administrator accesses the subscriber management section, when subscriber data is retrieved, then both active and inactive subscribers are displayed along with their membership plan and subscription status.

##### AC4 – Search and Filtering Capabilities

- [ ] Given that an administrator performs a search or applies filters, when criteria such as customer name, subscription status, or order status are selected, then only matching records are displayed.

##### AC5 – Empty-State Handling

- [ ] Given that no records match the selected search or filter criteria, when the results are returned, then a clear and informative message is displayed instead of an empty or broken interface.

##### AC6 – Secure and Proportionate Data Display

- [ ] Given that customer information is presented to an administrator, when records are displayed, then only data required to complete the task is shown and processed in accordance with applicable data protection requirements.

##### AC7 – Performance and Scalability

- [ ] Given that large numbers of orders or subscriber records exist, when an administrator views the data, then the interface remains responsive through mechanisms such as pagination, filtering, and efficient data retrieval.

##### AC8 – Accessible and Responsive Interface

- [ ] Given that an administrator accesses order or subscriber information using a desktop, tablet, mobile device, or assistive technology, when interacting with the interface, then data is presented accessibly, remains keyboard navigable, and adapts appropriately to different screen sizes.

---

## FitHub Colour Palette Justification

[⬆ Back to Table of Contents](#table-of-contents)

### Selected Colour Palette

| Colour Name | Hex Code | Purpose |
|-------------|----------|---------|
| Energy Red | `#C81E2D` | Primary brand colour used for key call-to-action buttons, active states, and prominent interface accents |
| Ink Black | `#1A1A1A` | Applied to headings, body text, footer backgrounds, and secondary action buttons |
| Slate Grey | `#6B7280` | Used for supporting text, icons, form borders, and subtle interface elements |
| Mist Grey | `#F4F5F7` | Provides background colour for pages, content sections, and dividers |
| Pure White | `#FFFFFF` | Used for cards, forms, modal windows, and content containers |
| Success Green | `#2E7D32` | Indicates successful actions, stock availability, and confirmation messages |

#### Functional Status Colours

The following colours are used consistently throughout the application to communicate system status. To support accessibility, colour is always accompanied by descriptive text and an icon rather than being used as the sole means of conveying information.

| Status | Hex Code | Application |
|---------|----------|-------------|
| Success | `#2E7D32` | Confirmations, completed actions, in-stock indicators, and delivered orders |
| Warning | `#B45309` | Low-stock alerts and cautionary notifications |
| Information | `#1D4ED8` | Processing states, dispatched orders, and informational messages |
| Neutral Accent | `#6D28D9` | Refunded orders and other special status indicators |

A darker variation of the primary brand colour (`#A3151F`) is used for hover and active states, providing clear visual feedback during user interactions.

### Overview and Design Rationale

The FitHub colour palette has been carefully selected to reflect the energy, motivation, and confidence associated with a modern fitness platform. As the application enables users to subscribe to training plans, purchase merchandise, and manage their accounts, the colour scheme balances motivational visual elements with a professional and highly usable interface.

The palette combines a single high-impact brand colour with a structured set of neutral tones, ensuring that important actions remain prominent while maintaining clarity throughout the user journey. This restrained approach prevents visual clutter, improves usability, and allows fitness content and product imagery to remain the primary focus.

The design philosophy centres on one strong accent colour, a confident dark neutral, and a collection of light supporting tones, complemented by a concise set of functional status colours. This approach creates a contemporary interface while supporting accessibility, consistency, and strong visual hierarchy.

### Colour Selection Justification

#### Energetic Brand Colour for User Engagement

Energy Red (`#C81E2D`) serves as the primary brand colour and is intentionally reserved for the application's most important actions, including:

- **Subscribe**
- **Add to Basket**
- **Complete Order**
- Active navigation states
- Key interface highlights

Red is strongly associated with energy, determination, and action, making it particularly appropriate within a fitness-focused environment. Restricting its use to primary actions ensures that it remains visually meaningful and encourages user engagement without becoming overwhelming.

#### Strength and Professionalism Through Ink Black

Ink Black (`#1A1A1A`) is used extensively for headings, body content, footer areas, and secondary action buttons. By choosing a near-black tone rather than pure black (`#000000`), the interface achieves a premium and professional appearance whilst reducing visual harshness and improving long-form readability.

This is particularly beneficial for plan descriptions, product information, and account management pages where users may spend extended periods reading content.

#### Neutral Foundations for Clarity

Mist Grey (`#F4F5F7`) and Pure White (`#FFFFFF`) establish a clean and distraction-free foundation throughout the application.

These colours:

- Reduce visual fatigue
- Improve content separation
- Enhance readability
- Support strong contrast ratios
- Allow product imagery and fitness plans to stand out

The resulting interface feels spacious, organised, and easy to navigate.

#### Positive Reinforcement Through Success Green

Success Green (`#2E7D32`) is used for:

- Success notifications
- Subscription confirmations
- Order confirmations
- In-stock indicators

Green is widely associated with progress, achievement, health, and positive outcomes. These associations align naturally with both fitness goals and successful transactional experiences.

#### Accessible Functional Status Indicators

A carefully defined set of functional colours communicates system status consistently throughout the platform:

- **Green** — Success
- **Amber** — Warning
- **Blue** — Information
- **Purple** — Special or neutral states

To comply with accessibility best practices, colour is never used as the sole indicator of meaning. Every status is reinforced through accompanying text and iconography, ensuring information remains understandable for users with visual impairments or colour-vision deficiencies.

### Consistent Branding and Visual Hierarchy

The palette establishes a clear visual hierarchy across all areas of the application, including:

- Navigation
- Membership plans
- Product listings
- Shopping cart and checkout
- User accounts and dashboards
- Community features

The combination of a single accent colour and structured neutral tones directs user attention towards key actions whilst maintaining balance and consistency.

Implemented through CSS custom properties (variables), the palette supports scalability and ensures a cohesive visual identity across desktop, tablet, and mobile devices.

### Applied Colour Theory Principles

#### 1. Accent-Led Balance (60–30–10 Rule)

The design follows the widely recognised 60–30–10 principle:

- **60%** Light neutral colours
- **30%** Dark structural colours
- **10%** Accent colour

This distribution creates visual stability while ensuring important actions remain highly visible.

#### 2. High-Contrast Focal Points

The use of a single saturated accent colour against a predominantly neutral background creates strong focal points that naturally draw attention to interactive elements such as subscription and checkout actions.

This prevents competing accents from diluting the effectiveness of primary calls to action.

#### 3. Psychological Associations

The palette has been selected with consideration for colour psychology:

- **Red** encourages energy, action, and motivation.
- **Green** reinforces success, growth, and achievement.
- **Dark neutrals** communicate professionalism, trust, and reliability.

Together, these colours create an environment that is both motivating and credible.

#### 4. Accessibility and Readability

The palette has been designed to support **WCAG 2.1 AA** accessibility standards, including:

- Minimum contrast ratio of **4.5:1** for body text
- Minimum contrast ratio of **3:1** for large text and interface components
- Dark text on light backgrounds for improved readability
- Status indicators supported by text and icons

All final colour pairings should be validated using a recognised contrast-checking tool prior to deployment.

#### 5. Brand Consistency and Recognition

Colours are applied consistently throughout the application, including:

- Navigation components
- Forms and validation messages
- Product and plan cards
- Modal windows
- Status indicators
- Checkout flows

The use of CSS variables ensures a maintainable, scalable, and recognisable visual identity across all devices and screen sizes.

### Strategic Use of Colour

- **Emphasis:** Energy Red (`#C81E2D`) highlights primary actions such as subscribing, purchasing products, and completing transactions.
- **Hierarchy:** Ink Black (`#1A1A1A`) provides structure and readability, whilst the brand red is reserved exclusively for primary interactions.
- **Consistency:** The palette is applied uniformly across membership plans, shop functionality, cart workflows, checkout processes, and account management areas.
- **Status Communication:** Functional colours provide clear and consistent feedback, always supported by text and icons.
- **Contrast:** Mist Grey (`#F4F5F7`) and Pure White (`#FFFFFF`) create effective separation between content, controls, and background areas.

### Summary

FitHub utilises an energetic yet controlled colour palette to deliver a motivating, trustworthy, and accessible user experience. By combining a distinctive high-energy brand red with a structured neutral foundation and a carefully selected set of functional status colours, the platform achieves a modern and professional appearance whilst maintaining excellent usability.

This deliberate application of colour supports user confidence throughout subscription, shopping, and account-management journeys, reinforces accessibility principles, and establishes a consistent and recognisable brand identity across the entire application.

---

## Typography Justification for FitHub Website

[⬆ Back to Table of Contents](#table-of-contents)

### Overview

The typography selected for FitHub has been chosen to communicate a modern, confident, and motivating brand identity whilst maintaining excellent readability, accessibility, and usability. The platform is designed for users pursuing a wide range of fitness goals, from beginners taking their first steps towards a healthier lifestyle to experienced fitness enthusiasts seeking structured training plans.

As FitHub supports essential user journeys such as membership subscriptions, merchandise purchases, community engagement, and account management, the typography strategy prioritises clarity, hierarchy, and consistency across all devices and screen sizes.

The selected typeface pairing — **Poppins** for headings and **Inter** for body content — combines a contemporary and energetic visual style with exceptional on-screen legibility. This combination reinforces the platform's fitness-focused identity whilst ensuring that information remains accessible and easy to consume.

### Typography Objectives

The chosen typography system has been designed to achieve the following objectives:

- Deliver a highly readable and accessible user experience for all audiences.
- Reinforce a modern, energetic, and motivational fitness brand.
- Establish trust and professionalism during transactional interactions such as subscriptions, purchases, and account management.
- Maintain clarity and consistency across desktop, tablet, and mobile devices.
- Support a wide variety of content types, including fitness plans, product information, forms, dashboards, and account pages.
- Align with recognised user experience (UX) and accessibility best practices.

This approach ensures that typography contributes positively to both the visual identity and usability of the application.

### Primary Typeface — Poppins (Headings)

The geometric sans-serif typeface **Poppins** is used for:

- Page headings
- Section titles
- Navigation items
- Card headings
- Call-to-action buttons
- Key interface labels

#### Justification

Poppins features clean geometric shapes, balanced proportions, and strong visual presence, making it particularly effective for establishing hierarchy and guiding user attention.

Its bold and confident appearance allows users to quickly identify important information, including:

- Page titles
- Membership plan names
- Product names
- Section headings
- Primary actions such as **Subscribe**, **Add to Basket**, and **Complete Order**

The slightly rounded characteristics of Poppins create an approachable and energetic feel that aligns well with a fitness-focused platform. At the same time, its professional appearance ensures it remains suitable for commercial and transactional content.

Its widespread browser support and excellent rendering performance further contribute to a consistent user experience across different devices and operating systems.

### Secondary Typeface — Inter (Body Content)

The humanist sans-serif typeface **Inter** is used for:

- Body text
- Plan descriptions
- Product descriptions
- Form labels
- Helper text
- Error and confirmation messages
- Account information
- Supporting content throughout the application

#### Justification

Inter was specifically designed for digital interfaces and screen-based reading, making it an excellent choice for FitHub's primary content areas.

Key characteristics include:

- Open and highly distinguishable letterforms
- Generous spacing between characters
- Tall x-height for improved readability
- Excellent clarity at smaller font sizes

These attributes ensure that users can comfortably read longer content sections such as:

- Fitness plan descriptions
- Product specifications
- Checkout summaries
- Community discussions
- Profile information

The neutral and highly legible design of Inter helps users absorb information efficiently and complete important tasks with confidence, particularly during registration, subscription management, and checkout workflows.

### Typography Implementation Strategy

To maximise consistency, maintainability, and performance, the application uses only two primary typefaces throughout the interface:

| Typeface | Purpose |
|-----------|---------|
| **Poppins** | Headings, navigation, prominent labels, and call-to-action buttons |
| **Inter** | Body text, paragraphs, descriptions, forms, and supporting content |

Limiting the design system to two complementary typefaces reduces visual complexity, strengthens brand consistency, and minimises cognitive load for users.

This restrained approach also improves performance by reducing the number of font files that must be downloaded and rendered by the browser.

### Typography Specifications

#### Font Sizes

- **Minimum body text size:** `16px`
- Larger font sizes are used for headings according to the visual hierarchy.
- Text scales responsively across breakpoints to maintain readability.

#### Scalable Units

Typography is implemented using **rem units**, based on a root font size of `16px`.

This approach ensures that:

- Browser zoom functions correctly.
- User accessibility preferences are respected.
- Text scales consistently across devices.
- The interface remains responsive and accessible.

#### Font Weights

| Weight | Usage |
|----------|---------|
| `400` | Body text and general content |
| `500–600` | Sub-headings, emphasis, and supporting labels |
| `600–700` | Headings, navigation, and call-to-action buttons |

#### Fallback Font Stack

```css
font-family: 'Poppins', 'Inter', Arial, sans-serif;
````

Providing fallback fonts ensures content remains readable even if custom web fonts fail to load.

### Visual Hierarchy and User Experience

Typography plays a critical role in establishing a clear visual hierarchy throughout FitHub.

#### Hierarchy

Poppins creates strong visual anchors through:

* Page titles
* Section headings
* Product names
* Membership plan names
* Primary actions

Inter supports this hierarchy by presenting supporting information in a highly readable format.

#### Scannability

The combination of distinct heading and body fonts allows users to quickly scan pages and locate relevant information without unnecessary effort.

This is particularly important for:

* Plan comparison pages
* Product listings
* Dashboard summaries
* Checkout workflows
* Community content

#### Consistency

The same typography system is applied consistently across:

* Navigation
* Plans
* Product pages
* Cart and checkout
* User profiles
* Community features
* Administrative interfaces

This consistency strengthens familiarity and reduces cognitive effort when moving between different areas of the application.

### Accessibility Considerations

Typography has been selected with accessibility as a core requirement.

#### Readability

* Minimum body text size of `16px`
* Clear distinction between heading levels
* Adequate line spacing and character spacing
* High colour contrast between text and background

#### WCAG 2.1 AA Alignment

The typography strategy supports compliance with WCAG 2.1 AA guidelines through:

* Readable font sizes
* Logical heading hierarchy
* Scalable text
* Support for browser zoom functionality
* Clear distinction between interactive and non-interactive content

#### Device Independence

Both typefaces render effectively across:

* Desktop computers
* Laptops
* Tablets
* Smartphones
* Assistive technologies

This ensures a consistent reading experience regardless of device or screen size.

### Strategic Use of Typography

The typography system supports several key design objectives:

* **Emphasis:** Poppins highlights important actions and navigational elements.
* **Hierarchy:** Clear differentiation between headings, sub-headings, and supporting content.
* **Readability:** Inter provides excellent legibility for extended reading.
* **Consistency:** A unified typography system strengthens brand identity.
* **Accessibility:** Scalable sizing and clear hierarchy support users with varying needs.

### Summary

FitHub employs a carefully selected typography system that balances motivation, professionalism, and accessibility. By combining the bold, contemporary character of **Poppins** with the exceptional readability of **Inter**, the platform creates a strong visual hierarchy whilst maintaining clarity across all user journeys.

This typography strategy supports effective communication throughout subscription management, shopping experiences, community engagement, and account administration. The result is a modern, responsive, and accessible interface that reinforces the FitHub brand while delivering an excellent user experience across all devices.

---

## Accessibility Implementation, User Flow and Navigation Strategies

**FitHub**

[⬆ Back to Table of Contents](#table-of-contents)

### Accessibility Implementation

Accessibility was embedded into FitHub from the earliest stages of design and development, forming a fundamental requirement rather than a post-development enhancement. The platform has been designed to ensure that all users — including individuals with visual, auditory, cognitive, and motor impairments — can independently browse fitness plans and merchandise, register and subscribe, complete purchases, engage with the community, and manage their accounts.

All accessibility decisions were informed by the **Web Content Accessibility Guidelines (WCAG) 2.1**, ensuring alignment with internationally recognised standards and inclusive design best practices (W3C, 2018).

### Core Accessibility Features

#### Semantic HTML Structure

FitHub uses semantic HTML elements consistently, including:

* `<header>`
* `<nav>`
* `<main>`
* `<section>`
* `<article>`
* `<footer>`

**Purpose within FitHub**

These elements provide clearly defined page regions, helping users navigate plans, products, carts, checkout processes, account areas, and community content in a logical and predictable manner.

**Justification**

Semantic markup improves screen-reader interpretation, strengthens document structure, and enhances compatibility with assistive technologies (W3C, 2018; MDN, 2023).

#### Keyboard Accessibility

All interactive components can be operated entirely via keyboard navigation, including:

* Navigation menus
* Filters and sorting controls
* Plan and product cards
* Quantity selectors
* Add-to-cart actions
* Subscription controls
* Account tabs
* Form fields and buttons

Visible focus indicators are provided throughout the application.

**Purpose within FitHub**

Users can browse plans, subscribe, shop, complete purchases, and manage their accounts without relying on a mouse or touch device.

**Justification**

This supports users with motor impairments and satisfies WCAG 2.1 Success Criterion 2.1.1 (Keyboard Accessible) (W3C, 2018).

#### Colour Contrast Compliance

Text, icons, and interactive components are designed to achieve:

* Minimum contrast ratio of **4.5:1** for standard text.
* Minimum contrast ratio of **3:1** for large text and user-interface components.

All colour combinations are validated using recognised contrast-analysis tools.

**Purpose within FitHub**

Ensures that plan descriptions, product details, prices, buttons, status indicators, and form controls remain legible for users with low vision or colour-perception differences.

**Justification**

Supports WCAG 2.1 Success Criterion 1.4.3 (Contrast Minimum) (WebAIM, 2024).

#### Status Information Beyond Colour Alone

Order statuses and stock indicators are communicated using a combination of:

* Colour
* Icons
* Descriptive text

Examples include:

* Processing
* Dispatched
* Delivered
* Cancelled
* Refunded
* In Stock
* Low Stock

**Purpose within FitHub**

Ensures that important information remains understandable even when colour cannot be perceived.

**Justification**

Complies with WCAG 2.1 Success Criterion 1.4.1 (Use of Colour) (W3C, 2018).

#### Responsive Typography

Typography is implemented using scalable `rem` units based on a root font size of `16px`.

**Purpose within FitHub**

Provides consistent readability for:

* Fitness plans
* Product descriptions
* Community content
* Account information
* Checkout and order details

across desktop, tablet, and mobile devices.

**Justification**

Supports browser zoom functionality and user-defined accessibility preferences, improving accessibility for users with visual or cognitive impairments (W3C, 2018; Nielsen Norman Group, 2020).

#### ARIA Support

Where native HTML semantics do not provide sufficient context, ARIA attributes are implemented, including:

* `aria-label`
* `aria-describedby`
* `aria-live`
* `role`

**Purpose within FitHub**

Examples include:

* Live announcements for cart updates and recalculated totals.
* Notification of payment and validation errors.
* Descriptive labels for icon-only actions such as remove-item, save-for-later, and cart controls.
* Proper ARIA tab implementation within the account area.
* Order-confirmation and processing states announced using `role="status"`.

**Justification**

Improves accessibility for screen-reader users and enhances the usability of dynamic, interactive components (WAI-ARIA, 2017).

#### Alternative Text and Descriptive Actions

All non-decorative images include meaningful alternative text.

Examples of descriptive actions include:

* *View Order FH-10428*
* *Subscribe to Premium Plan*
* *Continue to Checkout*

rather than generic labels such as *Click Here* or *View*.

**Purpose within FitHub**

Provides contextual information to users relying on assistive technologies and improves navigation clarity.

**Justification**

Supports WCAG 2.1 Success Criteria:

* 1.1.1 Non-text Content
* 2.4.4 Link Purpose

(W3C, 2018).

#### Accessible Forms and Validation

Forms throughout the application include:

* Associated labels
* Required-field indicators
* Inline validation feedback
* Contextual guidance through `aria-describedby`

When validation fails:

* Focus moves to the first invalid field.
* Errors are announced through live regions.
* Clear instructions explain how the issue can be corrected.

**Purpose within FitHub**

Supports users during:

* Registration
* Login
* Subscription management
* Checkout
* Delivery information entry
* Administrative content management

**Justification**

Accessible validation improves task completion rates and reduces form abandonment, particularly for users with cognitive, visual, or motor impairments (Nielsen Norman Group, 2020).

#### Focus Management

Focus behaviour is intentionally managed throughout the application.

Examples include:

* Moving focus to the confirmation heading after a successful purchase.
* Using focus-trapped dialogs for destructive actions such as account deletion and plan archiving.
* Returning focus to the triggering element when a modal or dialog closes.

**Purpose within FitHub**

Maintains user orientation during significant transitions and protects users from accidental completion of irreversible actions.

**Justification**

Supports WCAG 2.1 focus-management best practice and improves the overall experience for keyboard and screen-reader users (W3C, 2018).

### User Flow and Navigation Strategy

FitHub's navigation architecture has been designed to support clear, intuitive, and goal-oriented user journeys. Navigation structures, calls-to-action, and content organisation work together to guide users efficiently through the platform's primary objectives.

The platform enables users to:

1. **Discover and compare** fitness plans and merchandise.
2. **Register and subscribe** to membership plans.
3. **Purchase** fitness products securely.
4. **Manage** subscriptions, orders, and account information.
5. **Participate** in the subscriber community.


### Primary User Journeys

#### Plan Discovery and Subscription

* Users arrive on the **Home Page** and discover available plans.
* The **Plans Listing** page allows filtering and sorting of available memberships.
* Selecting a plan opens the **Plan Detail** page.
* Users proceed through the **Stripe Checkout** subscription workflow.
* Subscription status is synchronised through Stripe webhooks.

#### Shopping and Merchandise Purchases

* Users browse products through the **Shop Listing** page.

* Selecting a product opens the **Product Detail** page.

* Products are added to the cart.

* Users proceed through:

  **Product Detail → Cart → Checkout → Order Confirmation**

* Payments are processed using Stripe Elements.

* Orders are confirmed using the `payment_intent.succeeded` webhook.

#### Account Management

The **My Account** hub provides centralised access to:

* Profile management
* Subscription information
* Order history
* Saved items
* Community activity

Subscription management is delegated to the **Stripe Customer Portal**, ensuring secure handling of billing information.

#### Community Engagement

Subscriber-only content is protected through server-side access control.

Users without an active subscription are guided towards the subscription journey through contextual upgrade prompts and content previews rather than being granted access to protected resources.

### Navigation Enhancements

To further improve usability and accessibility, FitHub incorporates the following navigation strategies:

#### Skip Links

A **Skip to Content** link allows keyboard and screen-reader users to bypass repetitive navigation and move directly to the page's primary content.

#### Consistent Component Patterns

Cards, buttons, forms, tables, states, and navigation elements follow consistent design patterns throughout the application.

This consistency:

* Reduces cognitive load.
* Improves learnability.
* Creates a predictable user experience.

#### Mobile-First Responsive Design

Layouts are designed using a mobile-first approach, incorporating:

* Responsive grids
* Sticky calls-to-action
* Mobile action bars
* Touch-friendly controls

#### Clear Information Hierarchy

Primary actions receive greater visual emphasis than secondary actions.

Examples include:

* **Subscribe**
* **Add to Basket**
* **Complete Order**

This hierarchy guides users naturally towards key conversion goals.

#### Authentication Routing

Login and registration pages are accessible only to anonymous users.

Authenticated users attempting to access these pages are redirected appropriately, reducing confusion and preventing unnecessary actions.

#### Ownership and Permission Controls

Sensitive pages are protected through ownership and role-based access checks.

Examples include:

* Members can access only their own orders and account information.
* Subscribers can access only subscriber-exclusive content.
* Staff-only areas are inaccessible to standard users.

#### Graceful Error Recovery

When users encounter invalid URLs, unavailable resources, or permission restrictions, the application provides clear recovery routes rather than exposing technical error pages.

This helps maintain user confidence and reduces abandonment.

### Summary of Accessibility and Navigation Features

| Feature                          | Purpose                                           | Standard / Justification         |
| -------------------------------- | ------------------------------------------------- | -------------------------------- |
| Semantic HTML                    | Improves navigation for assistive technologies    | W3C (2018); MDN (2023)           |
| Keyboard Accessibility           | Enables complete non-mouse interaction            | WCAG 2.1 SC 2.1.1                |
| Colour Contrast                  | Enhances readability and visual clarity           | WCAG 2.1 SC 1.4.3; WebAIM (2024) |
| Status Beyond Colour             | Prevents reliance on colour alone                 | WCAG 2.1 SC 1.4.1                |
| Responsive Typography            | Supports readability across devices               | Nielsen Norman Group (2020)      |
| ARIA Support                     | Improves accessibility of dynamic content         | WAI-ARIA (2017)                  |
| Alt Text and Descriptive Actions | Provides context for all users                    | WCAG 2.1 SC 1.1.1; SC 2.4.4      |
| Accessible Forms                 | Improves data entry and validation                | Nielsen Norman Group (2020)      |
| Focus Management                 | Maintains orientation during interactions         | WCAG 2.1 Best Practice           |
| Structured User Flow             | Supports efficient navigation and task completion | User-Centred Design Principles   |

### Summary

Accessibility, navigation, and user experience considerations have been integrated throughout FitHub's design and development process. By combining semantic structure, keyboard accessibility, responsive layouts, ARIA enhancements, strong visual hierarchy, and clearly defined user journeys, the platform aims to provide an inclusive and intuitive experience for all users.

These decisions support accessibility compliance, improve usability, reduce cognitive load, and create a consistent experience across subscription management, shopping, account administration, and community engagement workflows.

*Note: The references cited throughout this section are widely recognised accessibility and usability sources, including W3C/WAI, MDN, WebAIM, and Nielsen Norman Group. These references should be aligned with the project's final reference list and verified before submission. Any AI-assisted drafting should be acknowledged in accordance with the academic integrity requirements of the awarding organisation.*

---

## Database Design for FitHub

[⬆ Back to Table of Contents](#table-of-contents)

### Overview

FitHub is built on a **relational database architecture** comprising **12 models**, including Django's built-in `User` model. These models are distributed across six custom Django applications, each representing a distinct and closely related area of the platform's functionality.

The database structure consists of:

- **accounts** app: 1 model (`Profile`)
- **plans** app: 3 models (`Plan`, `PlanFeature`, `Subscription`)
- **shop** app: 3 models (`ProductCategory`, `Product`, `ProductImage`)
- **orders** app: 2 models (`Order`, `OrderLineItem`)
- **reviews** app: 1 model (`Review`)
- **community** app: 1 model (`Post`)
- **Django built-in authentication**: `User`

### Commerce Architecture

FitHub employs two distinct commercial workflows:

- **Membership plans** are managed as recurring subscriptions and processed through **Stripe Checkout** and the **Stripe Customer Portal**.
- **Shop products** are purchased as one-time transactions through the shopping cart and checkout process using **Stripe Payment Intents** and **Stripe Elements**.

This separation is reflected directly within the database schema. Membership plans are associated with the `Subscription` model, whereas merchandise purchases are represented through the `Order` and `OrderLineItem` models. By modelling subscriptions and product purchases independently, the database accurately reflects the different business processes and payment workflows used throughout the platform.

#### Database System

- **Development:** SQLite3
- **Production:** PostgreSQL

### Entity Relationship Diagram (ERD)

<img width="1550" height="1035" alt="fithub_erd" src="https://github.com/user-attachments/assets/33ed6286-a685-40a2-93e9-6aeddd117122" />

### Models / Tables (12 total)

1. **User** (Django built-in)
2. **Profile** (one-to-one with `User`)
3. **Plan** (membership plan catalogue)
4. **PlanFeature** (individual "what's included" items for a plan)
5. **Subscription** (a user's membership, linked to Stripe)
6. **ProductCategory** (shop product organisation)
7. **Product** (individual shop merchandise)
8. **ProductImage** (gallery images for a product)
9. **Order** (a completed one-time purchase)
10. **OrderLineItem** (individual product line within an order)
11. **Review** (a user's review of a product)
12. **Post** (a community feed post)

### Relationships Identified

- **User -> Profile** (one-to-one)
- **User -> Subscription** (one-to-many — a user may have a current and past subscriptions; one active at a time)
- **Plan -> Subscription** (one-to-many)
- **Plan -> PlanFeature** (one-to-many)
- **ProductCategory -> Product** (one-to-many)
- **Product -> ProductImage** (one-to-many)
- **User -> Order** (one-to-many)
- **Order -> OrderLineItem** (one-to-many)
- **Product -> OrderLineItem** (one-to-many)
- **User -> Review** (one-to-many) and **Product -> Review** (one-to-many), with a unique constraint on (`user`, `product`) to prevent duplicate reviews
- **User -> Post** (one-to-many)

The database design follows established **relational modelling principles** commonly used in subscription-based and e-commerce applications.

The development of the entity relationships—including **one-to-many subscription and order models**, **multiple related product images and plan features**, and **user-owned reviews and community posts**—was informed by recognised relational database design practices, Entity Relationship Diagram (ERD) modelling methodologies, and guidance provided within the official Django documentation (Django Software Foundation, 2024).

This approach helps ensure that the database remains well-structured, scalable, and maintainable, while supporting efficient data integrity, relationship management, and future system expansion.

### Database Normal Forms and Their Importance

Efficient and logical data organisation is a fundamental principle of relational database design. To achieve this, database **normalisation** applies a recognised set of rules, known as **normal forms**, which structure tables and their relationships in a way that minimises data redundancy and prevents anomalies during data insertion, modification, and deletion.

The normalisation process follows a progressive series of stages, including **First Normal Form (1NF)**, **Second Normal Form (2NF)**, and **Third Normal Form (3NF)**. As a database advances through these forms, its structure becomes increasingly consistent, maintainable, and resilient to issues caused by duplicated, incomplete, or poorly organised data.

Within transactional systems such as subscription-based and e-commerce applications, where data integrity and reliability are critical, the application of normalisation principles is particularly important. A well-normalised database supports accurate reporting, efficient data management, future scalability, and overall system performance while maintaining strong referential integrity.

To satisfy the requirements of **Third Normal Form (3NF)**, the entities within the FitHub database were separated into distinct tables, with each table representing a single, clearly defined business concept. All non-key attributes depend exclusively on the primary key of their respective table, ensuring that data is stored only once and in the appropriate location.

Redundancy was minimised through the use of well-defined relationships connected by foreign keys, while transitive dependencies were eliminated to reduce the risk of update anomalies and maintain a consistent, reliable data structure throughout the application.

### Fully Compliant Third Normal Form (3NF) Database Design

The FitHub database schema was developed in accordance with established **relational database normalisation principles** to promote data integrity, reduce redundancy, and support efficient querying, maintainability, and future scalability. The completed schema conforms fully to **Third Normal Form (3NF)**.

#### First Normal Form (1NF)

##### Requirements

* Each table must contain a unique primary key.
* All attributes must be atomic, storing only a single value.
* Repeating groups and multi-valued fields must be eliminated.

##### Implementation within FitHub

* Every entity uses a single-field surrogate primary key (`id`).
* Each attribute stores one discrete and indivisible value.
* Repeating data structures are represented through related tables rather than embedded lists or multi-valued fields:

  * Plan features are stored as individual `PlanFeature` records rather than within a list attribute.
  * Product gallery images are represented by separate `ProductImage` records.
  * Order contents are stored as individual `OrderLineItem` records linked to an order.

This design ensures a consistent data structure, simplifies data manipulation, and completely avoids the use of multi-valued attributes.

#### Second Normal Form (2NF)

##### Requirements

* The database must already satisfy First Normal Form (1NF).
* Non-key attributes must not depend on only part of a composite primary key.

##### Implementation within FitHub

* All entities use surrogate primary keys rather than composite primary keys.
* Consequently, every non-key attribute depends entirely on the table's primary key by definition.

This approach promotes clear entity responsibility, simplifies relationship management, and prevents unnecessary dependencies between unrelated attributes.

#### Third Normal Form (3NF)

##### Requirements

* The database must already satisfy Second Normal Form (2NF).
* Transitive dependencies must be removed so that non-key attributes depend only on the primary key.

##### Implementation within FitHub

All non-key attributes within the FitHub schema depend exclusively on the primary key of their respective table. No non-key attribute relies on another non-key attribute, ensuring that transitive dependencies are eliminated throughout the database structure.

Relationships between entities are maintained through foreign keys, allowing data to remain normalised while preserving referential integrity across the application.

#### Deliberate and Justified Snapshot Data

A notable and intentional exception to dynamic data derivation exists within the order-processing system.

The `OrderLineItem.price` field and the monetary summary values stored within the `Order` model capture the product price **at the time of purchase** rather than referencing the current value of `Product.price`.

This design decision ensures historical accuracy and auditability. For example, if the price of a product changes after an order has been placed, the original order must continue to reflect the amount that the customer actually paid at the time of the transaction.

Storing historical pricing information in this manner is a recognised best practice in transactional and e-commerce systems. It preserves financial accuracy, supports reporting requirements, and prevents historical records from being altered by future product-price updates. Therefore, this approach represents a deliberate and justified architectural decision rather than a breach of normalisation principles.

## Database Table Purposes and Design Justification

Each entity within the FitHub database represents a distinct real-world concept relevant to the application's domain. By separating these concepts into individual tables, the database maintains clear boundaries of responsibility and adheres to established relational design principles.

This structured approach enhances **data integrity**, improves **maintainability**, and supports future **scalability** by reducing redundancy and ensuring that data is stored in the most appropriate location. Furthermore, the separation of concerns aligns with the requirements of **Third Normal Form (3NF)**, helping to eliminate unnecessary dependencies and promote a consistent, well-organised database architecture.

### Table-by-table verification

#### User (Django Built-in)

* All attributes (`username`, `email`, `password`, permissions, and account flags) relate directly to the user identified by the primary key (`id`).
* No attributes are derived from other non-key fields.
* No transitive dependencies exist within the entity.

**Purpose:**
The Django built-in `User` model stores the core authentication, authorisation, and identity information required for all system users, including members and administrative staff.

**Justification:**
Utilising Django's standard `User` model separates authentication and access-control concerns from application-specific business data. This approach promotes security, maintainability, and extensibility by ensuring that credentials, permissions, and user roles remain independent of fitness plans, subscriptions, orders, reviews, and community interactions.

In addition, the model provides robust support for role-based access control, enabling clear separation between standard members and privileged staff users while leveraging Django's established authentication framework and security best practices.

#### Profile (`accounts`)

* All attributes (`fitness_goal`, `experience_level`, `height_cm`, `weight_kg`, `profile_image`, `stripe_customer_id`, and audit timestamps) describe the profile entity identified by its primary key.
* The `user_id` field is implemented as a one-to-one foreign key and functions as a candidate key, ensuring that each user can have only one associated profile.
* No authentication-related attributes are duplicated from the Django `User` model.
* The entity follows a clean and fully compliant **Third Normal Form (3NF)** extension pattern.

**Purpose:**
The `Profile` model stores member-specific information that extends the core user account, including fitness goals, experience level, optional physical measurements, profile imagery, and the Stripe customer reference associated with the member.

**Justification:**
A one-to-one relationship with Django's built-in `User` model provides a structured extension mechanism without altering the core authentication framework. This separation of concerns prevents the `User` entity from becoming overloaded with application-specific attributes while supporting future growth and maintainability.

The design also promotes normalisation by ensuring that authentication and identity data remain isolated from fitness and subscription-related information. Furthermore, storing the `stripe_customer_id` within the profile creates a direct association between the member and their Stripe customer record, enabling subscription management and billing integration without duplicating sensitive payment information within the local database.

This approach improves extensibility, maintains data integrity, and supports a scalable architecture that aligns with established relational database design principles.

#### Plan (`plans`)

* All attributes (`name`, `slug`, `description`, `tier`, `price`, `billing_interval`, `image`, `status`, Stripe identifiers, and audit timestamps) describe the membership plan entity.
* Plan features are stored separately within the related `PlanFeature` entity, ensuring the design remains fully normalised.
* No transitive dependencies exist within the model.
* The entity conforms to **Third Normal Form (3NF)**.

**Purpose:**
The `Plan` model represents a membership offering within the FitHub catalogue. It stores essential information including the plan name, description, difficulty tier, subscription price, billing interval, publication status (`published`, `draft`, or `archived`), and the corresponding Stripe Product and Price references.

**Justification:**
Membership plans are administered through a custom staff-facing management interface and are synchronised with Stripe's subscription infrastructure. Storing the `stripe_product_id` and `stripe_price_id` creates a direct relationship between each plan and its associated Stripe resources, ensuring consistency between the application database and the payment platform.

The design also accommodates Stripe's pricing model, where Price objects are immutable. Consequently, when a plan's subscription fee changes, a new Stripe Price is created and linked to the plan while the previous Price is archived rather than modified. This approach preserves billing history and maintains the integrity of existing subscriptions.

In addition, the `status` attribute supports a soft-delete strategy through plan archiving. Rather than permanently removing records, plans can be marked as archived, preventing new subscriptions while preserving existing memberships, historical transactions, and reporting data. This approach improves data integrity, supports referential consistency, and aligns with established best practices for subscription-based systems.

#### PlanFeature (`plans`)

* All attributes (`text` and `display_order`) describe a single feature associated with a membership plan.
* The `plan_id` attribute is implemented as a foreign key linking each feature to its parent `Plan`.
* No plan-specific attributes are duplicated within this entity.
* The model conforms to **Third Normal Form (3NF)** and contains no transitive dependencies.

**Purpose:**
The `PlanFeature` model stores individual feature entries that describe the benefits, services, or content included within a membership plan. Each feature is represented as a separate record, enabling flexible presentation of the "What's Included" section throughout the application.

**Justification:**
Representing plan features as related records rather than storing them within a single multi-valued field supports compliance with **First Normal Form (1NF)** by ensuring that each attribute remains atomic and that repeating groups are eliminated.

This design mirrors the administrative workflow, allowing staff to add, edit, remove, and reorder features independently without modifying the parent plan record. The inclusion of a `display_order` attribute enables consistent presentation of features while maintaining separation of concerns between the plan itself and its associated benefits.

By normalising plan features into a dedicated entity, the database structure becomes more maintainable, scalable, and flexible, particularly if plans require a varying number of features over time.

> **Alternative Design Consideration:**
> For a simplified implementation, plan features could be stored as a single text field within the `Plan` model. However, modelling features as a related entity provides a more normalised solution, offers greater flexibility for future development, and better aligns with established relational database design principles.

#### Subscription (`plans`)

* All attributes (`stripe_subscription_id`, `status`, `current_period_end`, and audit timestamps) describe an individual subscription record.
* The `user_id` and `plan_id` fields are implemented as foreign keys linking the subscription to a specific member and membership plan.
* No user-specific or plan-specific attributes are duplicated within this entity.
* The model contains no transitive dependencies and conforms to **Third Normal Form (3NF)**.

**Purpose:**
The `Subscription` model represents a member's active or historical membership relationship with a particular fitness plan. It stores the associated Stripe subscription reference, subscription status, renewal information, and lifecycle dates required to manage recurring memberships.

**Justification:**
Acting as the associative entity between `User` and `Plan`, the `Subscription` model records membership activity without duplicating data already stored within the related entities. This approach maintains normalisation, reduces redundancy, and preserves a clear separation of responsibilities within the database schema.

The model also supports real-world subscription workflows by storing the current membership status (for example, active, cancelled, past due, or expired) together with the subscription renewal or period-end date. These values are synchronised with Stripe through webhook events, ensuring that the application's representation of a member's subscription remains accurate and up to date.

By maintaining a dedicated subscription entity, FitHub can reliably manage membership access, enforce content-gating rules, support subscription lifecycle management, and provide an authoritative record of each member's relationship with their chosen plan. This design improves maintainability, supports scalability, and aligns with established relational database modelling practices for subscription-based platforms.

#### ProductCategory (`shop`)

* All attributes (`name` and `slug`) describe the product category entity.
* No attributes are derived from other fields.
* The entity contains no transitive dependencies and complies with **Third Normal Form (3NF)**.

**Purpose:**
The `ProductCategory` model provides a structured classification system for shop products, grouping items into logical categories such as equipment, supplements, clothing, or accessories.

**Justification:**
Separating product categories into a dedicated entity promotes normalisation by eliminating the need to repeatedly store category information within individual product records. This reduces data redundancy and improves consistency across the catalogue.

The relationship between `ProductCategory` and `Product` supports efficient filtering, searching, sorting, and navigation throughout the shop interface, while enabling categories to be created, modified, or archived independently of the products assigned to them.

By managing categories as a standalone entity, the database remains more maintainable, scalable, and flexible, supporting future expansion of the product catalogue without introducing unnecessary duplication or update anomalies.

#### Product (`shop`)

* All attributes (`name`, `slug`, `description`, `brand`, `price`, `stock`, `image`, `is_available`, and audit timestamps) describe the product entity.
* The `category_id` attribute is implemented as a foreign key linking each product to a single `ProductCategory`.
* Additional gallery images are normalised into the related `ProductImage` entity.
* No transitive dependencies exist within the model.
* The entity conforms to **Third Normal Form (3NF)**.

**Purpose:**
The `Product` model stores individual merchandise items available within the FitHub shop. It contains key information including the product name, description, brand, price, stock quantity, availability status, and primary product image.

**Justification:**
Each product is associated with a single category through a foreign-key relationship, ensuring category information is stored only once and preventing unnecessary duplication of data. This design supports normalisation, improves maintainability, and enables efficient filtering and categorisation throughout the shop interface.

Stock management is facilitated through the `stock` attribute, which supports inventory validation across the shopping workflow, including product pages, the cart, and the checkout process. This ensures customers cannot purchase quantities exceeding the available inventory and helps maintain accurate stock records.

The `is_available` attribute provides a mechanism for controlling product visibility without requiring permanent deletion. Products can be hidden from the customer-facing catalogue while remaining in the database, preserving relationships with historical orders and maintaining referential integrity.

Separating product data from related images and category information results in a scalable and maintainable structure that supports future catalogue growth while remaining fully compliant with established relational database design principles.

#### ProductImage (`shop`)

* All attributes (`image`, `alt_text`, and `display_order`) describe a single product image.
* The `product_id` attribute is implemented as a foreign key linking each image to a specific `Product`.
* Each record represents one gallery image associated with a product.
* The entity complies with **Third Normal Form (3NF)**.

**Purpose:**
The `ProductImage` model stores supplementary gallery images associated with individual products, enabling multiple images to be displayed for a single merchandise item.

**Justification:**
Modelling product images as separate related records rather than storing multiple images within a single field supports **First Normal Form (1NF)** by ensuring that all attributes remain atomic and free from repeating groups.

This structure allows products to have a flexible number of associated images while maintaining a clean and scalable database design. The `display_order` attribute provides control over the sequence in which images appear within the product gallery, improving the user experience and presentation of merchandise.

The inclusion of `alt_text` supports accessibility requirements by providing meaningful alternative descriptions for users who rely on assistive technologies such as screen readers. This aligns with WCAG guidance and ensures that non-visual users can understand the content and purpose of product imagery.

By separating gallery images into their own entity, the database remains extensible, maintainable, and fully normalised, while supporting richer product presentation throughout the shop interface.

*Note: For a simplified implementation, a single image field could be stored directly within the `Product` model. However, the dedicated `ProductImage` entity provides the more scalable and fully normalised solution.*

#### Order (`orders`)

* All attributes (`order_number`, customer and delivery details, monetary totals, `status`, `stripe_payment_intent_id`, and `created_at`) describe a single order transaction.
* The `user_id` attribute is implemented as a nullable foreign key to `User`, supporting both registered-member and guest purchases.
* Individual purchased items are normalised into the related `OrderLineItem` entity.
* Monetary totals are intentionally stored as historical snapshots to preserve transaction accuracy.
* The entity conforms to **Third Normal Form (3NF)**, with justified denormalisation applied only where required for audit and reporting purposes.

**Purpose:**
The `Order` model represents a completed one-time purchase within the FitHub shop. It stores customer information, delivery details, order totals, fulfilment status, and the associated Stripe payment reference required to process and track transactions.

**Justification:**
As the central transactional entity within the e-commerce component of the application, the `Order` model acts as the parent record for all purchased items while maintaining links to the customer account where applicable. The nullable `user_id` relationship provides flexibility by supporting both authenticated purchases and guest checkout workflows without compromising data integrity.

Orders are created and confirmed through Stripe webhook events, specifically `payment_intent.succeeded`, ensuring that successful transactions are recorded reliably even if the customer closes their browser before the payment flow completes. This webhook-driven approach provides a more robust and authoritative source of truth than relying solely on client-side redirects.

The `status` attribute supports the complete order lifecycle, including states such as **Processing**, **Dispatched**, **Delivered**, **Cancelled**, and **Refunded**. Status changes are synchronised through internal business processes and relevant Stripe webhook events, ensuring that order progress remains accurate and up to date throughout fulfilment and post-purchase activities.

Order totals, delivery charges, and related monetary values are intentionally stored at the point of purchase rather than recalculated from current product data. This deliberate snapshotting preserves historical accuracy, ensuring that past orders continue to reflect the exact prices, discounts, taxes, and charges that applied when the transaction occurred. This is a recognised design pattern in transactional systems and does not constitute a normalisation violation.

By separating order-level information from individual line items, the database maintains a scalable, maintainable, and fully relational structure that supports reporting, fulfilment, customer service, and long-term audit requirements.

#### OrderLineItem (`orders`)

* All attributes (`quantity` and `price`) describe a single purchased item within an order.
* The `order_id` and `product_id` attributes are implemented as foreign keys linking the record to its parent order and associated product.
* The `price` attribute is intentionally stored as a snapshot of the product price at the time of purchase.
* The entity conforms to **Third Normal Form (3NF)**, with justified transactional snapshotting applied for historical accuracy.

**Purpose:**
The `OrderLineItem` model represents an individual product purchased as part of an order. It records the specific product, quantity ordered, and the price paid for that item at the time the transaction was completed.

**Justification:**
Separating purchased items into a dedicated `OrderLineItem` entity supports **First Normal Form (1NF)** by eliminating repeating groups and avoiding the need to store multiple products within a single order record. This design allows each order to contain any number of products while maintaining a fully relational structure.

The relationship between `Order` and `OrderLineItem` creates a scalable one-to-many model, where a single order can contain multiple line items, each linked to a different product. This approach improves maintainability, simplifies reporting, and supports accurate order management throughout the application.

The `price` field is intentionally stored as a historical snapshot rather than being dynamically retrieved from the current `Product.price`. This ensures that completed orders continue to reflect the exact amount paid by the customer, even if product prices change in the future. Preserving transactional values in this way is a recognised and widely adopted practice in e-commerce systems, supporting financial accuracy, auditing requirements, customer service enquiries, and historical reporting.

By isolating item-level purchase data from order-level information, the database maintains a clean, normalised structure while providing the flexibility and reliability required for real-world transactional processing.

#### Review (`reviews`)

* All attributes (`rating`, `comment`, and audit timestamps) describe an individual product review.
* The `user_id` and `product_id` attributes are implemented as foreign keys linking the review to both the author and the reviewed product.
* A unique constraint on (`user`, `product`) ensures that each member can submit only one review per product.
* The entity conforms to **Third Normal Form (3NF)**, with no duplicated user or product information.

**Purpose:**
The `Review` model stores a member's rating and written feedback for a specific product, allowing customers to share their experiences and contribute to the overall evaluation of merchandise available within the FitHub shop.

**Justification:**
By linking reviews to both `User` and `Product` through foreign-key relationships, the database avoids duplicating customer or product information while maintaining clear ownership and traceability of each review. This relational approach supports data integrity and ensures that reviews remain associated with the correct author and product throughout their lifecycle.

The unique constraint on (`user`, `product`) enforces a business rule that limits each member to a single review per product. This helps maintain fairness and prevents review inflation while still allowing members to update their feedback over time through the application's edit functionality.

The model supports full user-level **CRUD** operations, enabling members to create, read, update, and delete their own reviews while preventing them from modifying reviews submitted by other users. Ownership controls are enforced through application-level permissions, ensuring that review management remains secure and user-specific.

In addition to storing customer feedback, the `Review` model provides the foundation for aggregated product ratings displayed throughout the shop. Individual ratings can be combined to calculate average review scores, helping customers make informed purchasing decisions and enhancing trust in the platform.

This design maintains a fully normalised structure while supporting user engagement, product evaluation, and the broader e-commerce functionality of the application.

#### Post (`community`)

* All attributes (`content` and audit timestamps) describe a single community post.
* The `author_id` attribute is implemented as a foreign key linking each post to its creator.
* No transitive dependencies exist within the entity.
* The model conforms to **Third Normal Form (3NF)**.

**Purpose:**
The `Post` model stores user-generated content published within the FitHub community feed, enabling subscribers to share experiences, ask questions, provide motivation, and engage with other members.

**Justification:**
Each post is associated with a specific user through the `author_id` foreign-key relationship, ensuring clear ownership while preventing the duplication of user-related data. This relational structure supports data integrity, maintains accountability, and enables efficient retrieval of posts created by individual members.

Community participation is restricted to active subscribers, aligning with the platform's content-gating strategy and providing additional value to paid membership plans. Access controls are enforced at the application level to ensure that only authorised users can create and manage community content.

The model supports full user-level **CRUD** functionality, allowing subscribers to create, read, update, and delete their own posts. Ownership rules ensure that members can modify only content they have authored, preventing unauthorised changes to posts created by others and maintaining the integrity of community discussions.

By separating community content into a dedicated entity, the database remains fully normalised while supporting scalable social interaction features. This design provides a clear foundation for future enhancements such as comments, reactions, reporting mechanisms, moderation workflows, and community engagement analytics.

The `Post` model therefore plays a key role in supporting member interaction, subscriber engagement, and long-term community growth while maintaining a secure and maintainable relational database structure.

### Final Conclusion

The FitHub database schema has been designed in accordance with established relational database principles, with related data separated into distinct entities and multi-valued attributes eliminated through the use of appropriate relationships. By avoiding unnecessary duplication and ensuring that each table represents a single business concept, the final design conforms to **Third Normal Form (3NF)**.

Throughout the schema, every non-key attribute is fully dependent on the primary key of its respective table, with no partial or transitive dependencies present. The only exception to this principle is the intentional storage of transactional monetary values within orders and order line items. These values are retained as historical snapshots to preserve audit accuracy and ensure that completed purchases continue to reflect the exact prices, charges, and totals that applied at the time of the transaction.

Each entity fulfils a clearly defined responsibility within the application domain. Authentication data, member profiles, subscription management, fitness plans, shop products, order processing, customer reviews, and community content are all maintained within dedicated tables and organised across logically grouped Django applications. This separation of concerns promotes maintainability, improves scalability, and supports long-term system growth while preserving data integrity.

The resulting schema provides a robust foundation for both the subscription and e-commerce functionality of FitHub. By combining sound normalisation practices with carefully justified transactional design decisions, the database supports efficient querying, reliable reporting, secure data management, and future extensibility. Furthermore, the structure closely reflects the application's real-world business processes and user stories, ensuring strong alignment between the data model and the functional requirements of the system.

The final design therefore delivers a scalable, maintainable, and fully normalised relational database architecture capable of supporting the ongoing development and operation of the FitHub platform.

---

## Django Framework Setup and Configuration

[⬆ Back to Table of Contents](#table-of-contents)

### Overview

FitHub is developed using **Django 4.2.23**, a high-level Python web framework that supports the rapid development of secure, scalable, and maintainable web applications. Django follows the **Model-View-Template (MVT)** architectural pattern and provides a comprehensive set of built-in features, including authentication, database management through an ORM (Object-Relational Mapping), session handling, and an administrative interface.

The framework was selected because it aligns closely with the requirements of the project, supporting subscription management, e-commerce functionality, user-generated content, and role-based access control within a single, integrated platform.

### Development Environment Setup

#### Prerequisites

Before configuring the project, the following software and tools were installed and verified.

##### System Requirements

* **Python:** Version **3.12.10**
* **pip:** Python package manager (included with Python 3.12)
* **Git:** Version control and source-code management
* **Visual Studio Code:** Primary development environment
* **GitHub:** Remote repository hosting and version control

##### Development Platform

* **Operating System:** Windows 11
* **Development Environment:** PowerShell within Visual Studio Code
* **Repository:** GitHub (`milestone-4`)

### Step 1: Creating the Virtual Environment

To isolate project dependencies from the system-wide Python installation, a dedicated virtual environment was created. This approach prevents package conflicts and ensures that all project dependencies remain consistent across development and deployment environments.

#### Creating and Activating the Virtual Environment

```bash
# Navigate to the project directory
cd C:\Users\rober\OneDrive\Documents\vscode-projects\milestone-4

# Create the virtual environment using Python 3.12
py -3.12 -m venv venv

# Activate the environment
venv\Scripts\activate

# Verify activation
python --version
```

**Output:**

```text
Python 3.12.10
```

A successful activation displays the `(venv)` prefix in the terminal prompt.

### Step 2: Installing Django

After activating the virtual environment, the package manager was upgraded before installing Django.

```bash
python -m pip install --upgrade pip
pip install Django==4.2.23
```

#### Verification

```bash
python -m django --version
```

**Output:**

```text
4.2.23
```

### Step 3: Creating the Django Project

The Django project was created within the existing repository directory using the following command:

```bash
django-admin startproject fithub .
```

The trailing dot (`.`) is essential because it creates the project within the current directory rather than generating an additional nested project folder.

#### Resulting Structure

```text
milestone-4/
│
├── manage.py
├── fithub/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── venv/
├── .gitignore
└── README.md
```

#### Purpose of the Core Files

| File          | Purpose                                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `manage.py`   | Django command-line utility used to run the development server, migrations, and administrative tasks                      |
| `settings.py` | Central project configuration including installed applications, middleware, database settings, and security configuration |
| `urls.py`     | Root URL router responsible for directing requests throughout the application                                             |
| `wsgi.py`     | Entry point for WSGI-compatible production servers                                                                        |
| `asgi.py`     | Entry point for ASGI-compatible deployment environments                                                                   |

### Step 4: Creating the FitHub Applications

To support separation of concerns and maintain a modular architecture, the project was divided into six dedicated Django applications.

```bash
python manage.py startapp accounts
python manage.py startapp plans
python manage.py startapp shop
python manage.py startapp orders
python manage.py startapp reviews
python manage.py startapp community
```

#### Application Responsibilities

| Application | Purpose                                                        |
| ----------- | -------------------------------------------------------------- |
| `accounts`  | User profiles, dashboard functionality, and account management |
| `plans`     | Membership plans, plan features, and subscription management   |
| `shop`      | Product catalogue, categories, and product media               |
| `orders`    | Cart, checkout, and order processing                           |
| `reviews`   | Product reviews and ratings                                    |
| `community` | Subscriber-only community posts and interactions               |

### Step 5: Registering Applications

After creation, each application was registered in `INSTALLED_APPS` within `settings.py`.

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'accounts',
    'plans',
    'shop',
    'orders',
    'reviews',
    'community',
]
```

This configuration allows Django to recognise and manage each application throughout the project lifecycle.

### Step 6: Initial Database Migration

Before creating custom models, Django's built-in migrations were applied to generate the core authentication and session-management tables.

```bash
python manage.py migrate
```

These migrations create the foundational Django tables, including:

* Authentication (`auth`)
* Administration (`admin`)
* Content Types (`contenttypes`)
* User Sessions (`sessions`)

The migration process also creates the development database (`db.sqlite3`) used during initial development.

### Step 7: Creating a Superuser Account

A superuser account provides full administrative access to the Django administration interface and supports management tasks during development and testing.

```bash
python manage.py createsuperuser
```

The command prompts for:

```text
Username
Email Address
Password
Password Confirmation
```

### Step 8: Testing the Development Environment

The project configuration was validated by running the Django development server.

```bash
python manage.py runserver
```

Django successfully started using:

```text
Django version 4.2.23
Python version 3.12.10
```

The application was then accessed through:

```text
http://127.0.0.1:8000/
```

where the default Django welcome page confirmed that the framework had been installed and configured correctly.

### Step 9: Version Control Integration

The project repository was connected to GitHub before development commenced.

#### Git Repository Configuration

```bash
git init
git remote add origin https://github.com/rpires71/milestone-4.git
```

#### Initial Commit

```bash
git add .
git commit -m "Create Django project structure"
git push -u origin main
```

This established version control from the beginning of development and provided a secure remote backup of the project.

### Step 10: Dependency Management

To ensure reproducibility across development and deployment environments, installed package versions are documented within a `requirements.txt` file.

```bash
pip freeze > requirements.txt
```

Dependencies can then be recreated on another machine using:

```bash
pip install -r requirements.txt
```

### Summary

The FitHub development environment was successfully configured using **Python 3.12.10**, **Django 4.2.23**, **Visual Studio Code**, **Git**, and **GitHub**. A dedicated virtual environment was created, the Django project was initialised, six modular applications were established, and the project was placed under version control before development commenced.

This structured setup provides a maintainable foundation for implementing FitHub's subscription management, e-commerce functionality, community features, and administrative tools while following recognised Django development best practices.

---

## Database Models Implementation

[⬆ Back to Table of Contents](#table-of-contents)

### Overview

Following the database design and Entity Relationship Diagram (ERD) presented in the **Database Design** section, FitHub implements **10 custom database models** alongside Django's built-in `User` model. These models are developed using Django's **Object-Relational Mapping (ORM)** framework, which converts the relational database schema into Python classes responsible for managing data relationships, validation rules, and business logic.

The models are organised across six dedicated Django applications — `accounts`, `plans`, `shop`, `orders`, `reviews`, and `community` — in accordance with Django's modular architecture. This separation of concerns improves maintainability, scalability, code organisation, and future extensibility.

> **Implementation Note:** Membership plan features are implemented as a separate related model (`PlanFeature`) using a one-to-many relationship. Product imagery is managed through a single `image` field within the `Product` model rather than a dedicated gallery model, simplifying development while maintaining a normalised database structure.

### Model Architecture

#### Application Structure

| Application | Models | Purpose |
|------------|---------|---------|
| **accounts** | Profile (1) | Member profile management and extended user information |
| **plans** | Plan, PlanFeature, Subscription (3) | Membership plans and subscription lifecycle management |
| **shop** | ProductCategory, Product (2) | Product catalogue and categorisation |
| **orders** | Order, OrderLineItem (2) | Shopping cart, checkout, and order processing |
| **reviews** | Review (1) | Product ratings and reviews |
| **community** | Post (1) | Subscriber community interactions |
| **Django Built-in** | User (1) | Authentication and user account management |

**Total Models:** 11 (10 custom models plus Django's built-in `User` model)

**Commerce Architecture:**

FitHub distinguishes between recurring subscription services and one-time merchandise purchases.

- **Membership Plans** are managed through Stripe Checkout and the Stripe Customer Portal and are represented by the `Plan` and `Subscription` models.
- **Shop Products** are purchased through the cart and checkout workflow using Stripe PaymentIntents and are represented by the `Product`, `Order`, and `OrderLineItem` models.

This separation reflects real-world business processes while maintaining a clear, scalable, and maintainable database structure.

### Model Definitions

#### Accounts Application

##### File: `accounts/models.py`

###### **Profile Model**

The `Profile` model extends Django's built-in `User` model through a one-to-one relationship, enabling member-specific information to be stored independently from Django's authentication framework.

**Purpose:**

- Store member fitness goals and training experience levels
- Record optional physical measurements
- Maintain profile image information
- Store the Stripe customer reference used for subscription management

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `user` | OneToOneField(User) | CASCADE | Links the profile to an authenticated user |
| `fitness_goal` | CharField(20) | choices, blank=True | Primary fitness objective |
| `experience_level` | CharField(20) | choices, blank=True | Training experience level |
| `height_cm` | PositiveIntegerField | null=True, blank=True | Optional height measurement |
| `weight_kg` | DecimalField(5,2) | null=True, blank=True | Optional weight measurement |
| `profile_image` | ImageField | null=True, blank=True | Profile photograph |
| `stripe_customer_id` | CharField(255) | blank=True | Stripe customer identifier |
| `created_at` | DateTimeField | auto_now_add=True | Record creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |

**Relationships:**
- **One-to-One:** `User <-> Profile`

Each authenticated user owns a single profile record.


#### Plans Application

##### File: `plans/models.py`

###### **Plan Model**

The `Plan` model represents a membership package available within the FitHub subscription catalogue.

**Purpose:**

- Define membership tiers and pricing structures
- Store billing interval information
- Maintain Stripe Product and Price references
- Support draft, published, and archived states

**Fields:**
 
| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `name` | CharField(100) | - | Plan name (e.g. "Premium") |
| `slug` | SlugField | unique=True | URL-friendly identifier |
| `description` | TextField | blank=True | Plan description |
| `tier` | CharField(20) | choices | Difficulty/level |
| `price` | DecimalField(6,2) | - | Price in GBP |
| `billing_interval` | CharField(10) | choices (monthly/annual) | Billing frequency |
| `image` | ImageField | null=True, blank=True | Optional plan image |
| `status` | CharField(10) | choices (published/draft/archived) | Visibility/lifecycle |
| `stripe_product_id` | CharField(255) | blank=True | Stripe Product reference |
| `stripe_price_id` | CharField(255) | blank=True | Stripe Price reference |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |
 
**Relationships:**
- **One-to-Many:** Plan -> PlanFeature (a plan has many features)
- **One-to-Many:** Plan -> Subscription (a plan has many subscriptions)

###### **PlanFeature Model**

The `PlanFeature` model stores individual feature descriptions associated with a membership plan.

**Purpose:**

- Store each feature independently
- Support ordered display within the interface
- Maintain First Normal Form (1NF) compliance

**Fields:**
 
| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `plan` | ForeignKey(Plan) | CASCADE | Parent plan |
| `text` | CharField(255) | - | Feature description |
| `display_order` | PositiveIntegerField | default=0 | Ordering value |

**Relationships:**
- **Many-to-One:** PlanFeature -> Plan

###### **Subscription Model**

The `Subscription` model represents a member's active or historical subscription.

**Purpose**

- Record the relationship between a user and a plan
- Store Stripe subscription identifiers
- Track subscription status and renewal dates

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `user` | ForeignKey(User) | CASCADE | Subscribing member |
| `plan` | ForeignKey(Plan) | PROTECT | Subscribed plan |
| `stripe_subscription_id` | CharField(255) | blank=True | Stripe subscription reference |
| `status` | CharField(20) | choices | active / cancelled / past_due |
| `current_period_end` | DateTimeField | null=True, blank=True | Renewal/expiry date |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |

**Relationships:**
- **Many-to-One:** Subscription -> User (a member may have current and past subscriptions)
- **Many-to-One:** Subscription -> Plan

**On Delete Behaviours:**
- **User (CASCADE):** subscriptions deleted when the member is deleted
- **Plan (PROTECT):** a plan with subscriptions cannot be hard-deleted (archive instead)

#### Shop Application

##### File: `shop/models.py`

###### **ProductCategory Model**

The `ProductCategory` model groups products into logical classifications such as equipment, accessories, and supplements.

**Purpose:**

- Improve product organisation
- Support filtering and navigation
- Eliminate duplication of category information

**Fields:**
 
| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `name` | CharField(100) | - | Category name |
| `slug` | SlugField | unique=True | URL-friendly identifier |

**Relationships:**
- **One-to-Many:** `ProductCategory -> Product`

###### **Product Model**

The `Product` model represents merchandise available for purchase through the FitHub shop.

**Purpose:**

- Store product information and pricing
- Manage stock levels
- Control product availability
- Maintain product imagery

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `category` | ForeignKey(ProductCategory) | SET_NULL, null=True | Product category |
| `name` | CharField(200) | - | Product name |
| `slug` | SlugField | unique=True | URL-friendly identifier |
| `description` | TextField | - | Product description |
| `brand` | CharField(100) | blank=True | Brand name |
| `price` | DecimalField(6,2) | - | Price in GBP |
| `stock` | PositiveIntegerField | default=0 | Available stock |
| `image` | ImageField | null=True, blank=True | Product image |
| `is_available` | BooleanField | default=True | Whether shown for sale |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |

**Relationships:**
- **Many-to-One:** `Product -> ProductCategory`
- **One-to-Many:** `Product -> OrderLineItem`
- **One-to-Many:** `Product -> Review`

**On Delete Behaviours:**
- **Category (SET_NULL):** products preserved if a category is deleted.

#### Orders Application

##### File: `orders/models.py`

###### **Order Model**

The `Order` model represents a completed one-time purchase generated through the checkout process and confirmed through Stripe webhooks.

**Fields:**
 
| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `order_number` | CharField(32) | unique=True | Unique order reference |
| `user` | ForeignKey(User) | SET_NULL, null=True | Customer (nullable for guests) |
| `full_name` | CharField(100) | - | Customer name |
| `email` | EmailField | - | Customer email |
| `phone` | CharField(20) | blank=True | Contact number |
| `address_line1` | CharField(120) | - | Delivery address |
| `address_line2` | CharField(120) | blank=True | Delivery address (cont.) |
| `town_city` | CharField(60) | - | Town/city |
| `postcode` | CharField(20) | - | Postcode |
| `country` | CharField(60) | - | Country |
| `subtotal` | DecimalField(8,2) | default=0 | Items subtotal (snapshot) |
| `delivery_cost` | DecimalField(6,2) | default=0 | Delivery cost (snapshot) |
| `total` | DecimalField(8,2) | default=0 | Order total (snapshot) |
| `status` | CharField(20) | choices | processing → refunded |
| `stripe_payment_intent_id` | CharField(255) | blank=True | Stripe payment reference |
| `created_at` | DateTimeField | auto_now_add=True | Order timestamp |

**Purpose:**

- Store customer and delivery information
- Record order totals
- Maintain payment references
- Track order status throughout its lifecycle

**Relationships:**
- **Many-to-One:** `Order -> User`
- **One-to-Many:** `Order -> OrderLineItem`

**On Delete Behaviours:**
- **User (SET_NULL):** orders preserved if a user is deleted (historical record)

###### **OrderLineItem Model**

The `OrderLineItem` model represents an individual product purchased within an order.

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `order` | ForeignKey(Order) | CASCADE | Parent order |
| `product` | ForeignKey(Product) | PROTECT | Purchased product |
| `quantity` | PositiveIntegerField | default=1 | Quantity ordered |
| `price` | DecimalField(6,2) | - | Unit price at purchase (snapshot) |

**Purpose:**

- Store purchased quantities
- Preserve historical product pricing
- Support multi-product orders

**Relationships:**
- **Many-to-One:** `OrderLineItem -> Order`
- **Many-to-One:** `OrderLineItem -> Product`

**On Delete Behaviours:**
- **Order (CASCADE):** line items deleted with their order
- **Product (PROTECT):** a product referenced by orders cannot be hard-deleted

#### Reviews Application

##### File: `reviews/models.py`

###### **Review Model**

The `Review` model stores member ratings and written feedback for products.

**Purpose:**

- Support product review functionality
- Generate product ratings
- Enable member-managed CRUD operations

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `product` | ForeignKey(Product) | CASCADE | Reviewed product |
| `user` | ForeignKey(User) | CASCADE | Author |
| `rating` | PositiveSmallIntegerField | validators 1–5 | Star rating |
| `comment` | TextField | blank=True | Written review |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |

**Constraints:**
- One review per user per product (`unique_together`)

**Relationships:**
- **Many-to-One:** `Review -> Product`
- **Many-to-One:** `Review -> User`

#### Community Application

##### File: `community/models.py`

###### **Post Model**

The `Post` model stores subscriber-generated content within the community section.

**Purpose:**

- Support subscriber interaction
- Facilitate community discussions
- Provide authorised users with CRUD functionality

**Fields:**

| Field Name | Type | Constraints | Purpose |
|------------|------|-------------|---------|
| `author` | ForeignKey(User) | CASCADE | Post author |
| `content` | TextField | - | Post body |
| `created_at` | DateTimeField | auto_now_add=True | Creation timestamp |
| `updated_at` | DateTimeField | auto_now=True | Last modification timestamp |

**Relationships:**
- **Many-to-One:** `Post -> User`

Each post is linked directly to its author, ensuring ownership and permission controls can be enforced.

### Database Relationships Summary

##### One-to-One Relationships

| Parent Model | Child Model | Implementation | Purpose |
|--------------|-------------|----------------|---------|
| User | Profile | OneToOneField, CASCADE | Extend user with member data |

##### One-to-Many Relationships (Foreign Keys)

| Parent Model | Child Model | On Delete | Purpose |
|--------------|-------------|-----------|---------|
| User | Subscription | CASCADE | Member owns their subscriptions |
| Plan | Subscription | PROTECT | Cannot hard-delete a subscribed plan |
| Plan | PlanFeature | CASCADE | Plan owns its features |
| ProductCategory | Product | SET_NULL | Preserve products if category removed |
| User | Order | SET_NULL | Preserve order history |
| Order | OrderLineItem | CASCADE | Order owns its line items |
| Product | OrderLineItem | PROTECT | Preserve purchased-product integrity |
| Product | Review | CASCADE | Product owns its reviews |
| User | Review | CASCADE | Member owns their reviews |
| User | Post | CASCADE | Member owns their posts |

### Implementation Process

#### Step 1 – Create the Models

Models are implemented within their respective applications:

```bash
accounts/models.py    # Profile
plans/models.py       # Plan, PlanFeature, Subscription
shop/models.py        # ProductCategory, Product
orders/models.py      # Order, OrderLineItem
reviews/models.py     # Review
community/models.py   # Post
```

#### Step 2 – Generate Migration Files

```bash
python manage.py makemigrations
```

#### Step 3 – Apply Database Migrations

```bash
python manage.py migrate
```

#### Step 4 – Verify Functionality

Each model should be registered within its corresponding `admin.py` file and verified through the Django administration interface to ensure records can be created, viewed, updated, and deleted successfully.

### Summary

FitHub implements a modular database architecture consisting of **10 custom models** alongside Django's built-in `User` model. By distributing responsibility across dedicated applications and enforcing clearly defined relationships, the database remains scalable, maintainable, and aligned with the project's user stories, business requirements, and Third Normal Form (**3NF**) design principles.

---

## Testing

### Automated Testing

FitHub includes a comprehensive suite of automated tests that validate models, forms, views, permissions, session functionality, and integrations with external services through mocked APIs, including Stripe. All tests have been developed using Django's built-in `TestCase` framework.

To execute the complete automated test suite, run the following command:

```bash
python manage.py test
```

The testing suite currently covers seven Django applications:

* `accounts`
* `plans`
* `shop`
* `cart`
* `orders`
* `reviews`
* `community`

All automated tests are passing successfully, helping to ensure the reliability, stability, and correctness of the application's core functionality.

### Payment Testing

FitHub is configured to use **Stripe Test Mode**, ensuring that no real financial transactions are processed during development or testing.

To test the checkout and payment workflow, use the following Stripe test card credentials:

* **Card Number:** `4242 4242 4242 4242`
* **Expiry Date:** Any future date (e.g. `12/34`)
* **CVC:** Any three-digit value (e.g. `123`)
* **Postcode:** Any valid postcode (e.g. `PE12 7AA`)

These test credentials allow the complete payment process to be verified safely without charging a real payment card.

---

## Django Admin Configuration and Sample Data

[⬆ Back to Table of Contents](#table-of-contents)

### Django Admin Configuration

### Overview

Once the database models had been established, the Django administration panel was configured to enable staff users to efficiently manage application data throughout both the development lifecycle and ongoing system operation. Django's built-in admin framework provides a robust, production-ready management interface without the need to develop bespoke administrative views, helping to streamline development while delivering professional administrative capabilities (Vincent, 2020, Chapter 5).

A key architectural decision differentiates this project from solutions that rely solely on the Django admin interface. FitHub includes a **dedicated front-end management dashboard** for membership plans (`/plans/manage/`), accessible exclusively to staff members and supporting complete CRUD functionality. This implementation satisfies the expectations of an e-commerce project while providing a more user-focused management experience. Consequently, the Django admin is primarily utilised for development, data verification, and back-office administration, whereas routine management of membership plans is handled through the custom front-end interface. Each application has been configured with an admin interface appropriate to its role: comprehensive customisation is applied where the Django admin serves as the principal management environment (products, subscriptions, and community moderation), while simplified registrations are used for models whose records are maintained through application workflows or dedicated front-end interfaces (orders, profiles, and reviews).

### Admin Registration Process

#### Purpose of the Admin Interface

The Django admin interface fulfils several essential roles across both the development process and the live operation of the application.

**Development Phase:**

- Populate the database with sample records for development and testing
- Validate model structures and relationships
- Confirm database constraints and model validation rules
- Troubleshoot model functionality and application logic (e.g. verifying stock reductions after checkout and confirming orders generated by Stripe webhooks)

**Production Phase:**

- Maintain the product catalogue, including pricing, stock quantities and product availability
- Review and verify customer orders together with their associated line items
- Track member subscriptions and monitor their Stripe payment status
- Moderate community discussions and product review submissions
- Access and manage member profile information

**Rationale:** The Django admin provides immediate CRUD (Create, Read, Update and Delete) capabilities for every registered model without the need to develop bespoke views, forms or templates. This approach adheres to Django's "Don't Repeat Yourself" (DRY) philosophy while significantly reducing development effort (Vincent, 2020, Chapter 5).

### Admin Configuration by Application

#### Accounts Application

##### File: `accounts/admin.py`

The accounts application registers the member profile model using Django's default admin configuration.

**Registered Model:**

- `Profile` — Stores extended member profile details, including fitness goals, experience level, height and weight.

**Configuration Approach:**

The `Profile` model is registered using the standard `admin.site.register()` method, which provides the built-in CRUD functionality without additional customisation.

**Rationale:** A profile is generated automatically whenever a new user account is created, with members maintaining their own information through the front-end two-step registration process and account dashboard. Since administrative intervention is only occasionally required, the default Django admin configuration provides an appropriate solution. Consequently, the admin interface is used primarily for development validation, troubleshooting and support-related tasks (Vincent, 2020, Chapter 5).

#### Shop Application

##### File: `shop/admin.py`

The shop application provides the core administrative tools required to manage the e-commerce product catalogue through the Django admin interface.

**Registered Models:**

- `ProductCategory` — Organises products into categories such as Equipment, Supplements, Apparel and Accessories.
- `Product` — Represents individual products available for one-off purchases.

##### **ProductCategory Admin Configuration**

**List Display:**

- Category name
- Slug (URL identifier)

**Slug Prepopulation:**

- The slug field is automatically generated from the category name using `prepopulated_fields`, creating consistent, URL-friendly identifiers without requiring manual input.

**Rationale:** Automatically generating slugs minimises data-entry mistakes while ensuring category URLs remain aligned with their corresponding display names, improving consistency throughout the application (Vincent, 2020, Chapter 5).

##### **Product Admin Configuration**

**List Display:**

- Product name
- Category
- Price (GBP)
- Stock level
- Availability status

**Filtering Options:**

- Filter by category
- Filter by availability status

**Search Functionality:**

- Search by product name
- Search by brand
- Search by description

**Slug Prepopulation:**

- Product slugs are automatically created from the product name.

**Rationale:** Including stock levels alongside pricing and availability enables staff to assess inventory status instantly, supporting the project's stock management features, including quantity limits within the shopping cart and automatic stock reduction when an order is placed. These mechanisms can be quickly verified following test transactions. In addition, category and availability filters simplify catalogue administration and improve efficiency as the number of products increases (Vincent, 2020, Chapter 5).

#### Plans Application

##### File: `plans/admin.py`

The plans application provides the administrative tools required to manage the subscription component of the platform, including membership plans, their associated features and member subscriptions.

**Registered Models:**

- `Plan` — Membership plans linked to Stripe products.
- `PlanFeature` — Individual feature entries displayed within each membership plan (managed inline).
- `Subscription` — Member subscription records synchronised with Stripe.

##### **Plan Admin Configuration**

**List Display:**

- Plan name
- Tier (Beginner, Intermediate, Advanced)
- Price (GBP)
- Billing interval (Monthly, Annual)
- Status (Published, Draft, Archived)

**Filtering Options:**

- Filter by tier
- Filter by billing interval
- Filter by status

**Search Functionality:**

- Search by plan name
- Search by description

**Slug Prepopulation:**

- Plan slugs are automatically generated from the plan name.

**Inline Editing — PlanFeature:**

Rather than being registered as an independent admin model, `PlanFeature` is managed **inline** within the `Plan` admin page using a `TabularInline`. This allows feature entries, together with their display order, to be created, updated and removed directly from the parent plan's administration form.

**Rationale:** Since feature records are intrinsically linked to a specific membership plan, inline editing keeps related parent and child data within a single interface. This approach streamlines administration, reduces unnecessary navigation and helps prevent orphaned feature records (Vincent, 2020, Chapter 5). Although complete management of plans is also available through the custom staff front-end at `/plans/manage/`—including feature administration and soft-delete archiving—the Django admin remains available for development, testing and back-office management.

##### **Subscription Admin Configuration**

**List Display:**

- User (member username)
- Plan
- Status (Active, Cancelled, Past due)
- Current period end (renewal date)

**Filtering Options:**

- Filter by subscription status

**Rationale:** Subscription records are generated automatically through the Stripe Checkout workflow rather than manually by staff. As a result, the primary purpose of the admin interface is monitoring rather than record creation. Displaying the renewal date alongside the subscription status enables staff to quickly review active memberships, identify subscriptions nearing renewal and detect accounts that have entered a past-due state (Vincent, 2020, Chapter 5).

#### Orders Application

##### File: `orders/admin.py`

**Registered Models:**

- `Order` — Customer order records.
- `OrderLineItem` — Individual products associated with each order.

**Configuration Approach:**

Both models are registered using Django's standard `admin.site.register()` method, providing the default administrative CRUD interface.

**Rationale:** Order records are intentionally maintained as historical, read-only data. They are generated exclusively through application processes—either via the checkout workflow or the signature-validated Stripe webhook—and are never created manually by staff. Customers can access only their own purchase history through the front-end order history pages, which enforce ownership protection. Consequently, the Django admin is used primarily for verification and support purposes. Throughout development it played an important role in validating successful order creation, confirming line-item pricing, verifying stock reductions and ensuring webhook idempotency by checking that Stripe webhook events did not generate duplicate orders already created during checkout. As financial records should not normally be modified by administrators, no additional inline editing or quick-edit functionality was implemented (Vincent, 2020, Chapter 5).

#### Community Application

##### File: `community/admin.py`

**Registered Model:**

- `Post` — Community posts created by members.

##### **Post Admin Configuration**

**List Display:**

- Post title
- Author
- Creation timestamp

**Search Functionality:**

- Search by title
- Search by post content

**Filtering Options:**

- Filter by creation date

**Rationale:** The primary purpose of the admin interface is to support moderation of community-generated content rather than content creation. Staff can quickly locate posts requiring attention by searching titles and post content, while filtering by creation date makes it easier to review recent activity. Members retain responsibility for managing their own posts through the front-end, where owner-only permissions control editing and deletion, leaving the Django admin to fulfil an oversight and moderation role (Vincent, 2020, Chapter 5).

#### Reviews Application

##### File: `reviews/admin.py`

**Registered Model:**

- `Review` — Product reviews submitted with ratings.

**Configuration Approach:**

The `Review` model is registered using Django's standard `admin.site.register()` method, providing the default CRUD functionality without additional customisation.

**Rationale:** Product reviews are created and maintained by members through the front-end, where owner-only permissions govern editing and deletion. Consequently, the Django admin serves primarily as a moderation tool, enabling staff to review, investigate or remove inappropriate content when required. As no specialised administrative workflow is necessary, the standard admin registration provides a simple and effective solution (Vincent, 2020, Chapter 5).

#### Cart Application
 
##### File: `cart/admin.py`
 
**Registered Models:** None.
 
**Rationale:** The shopping basket is deliberately session-based and has no database models — basket contents live in the user's session until checkout converts them into an `Order` with `OrderLineItem` records. There is therefore nothing to register, and the empty `admin.py` reflects an architectural decision rather than an omission (Vincent, 2020, Chapter 4).

### Admin Interface Features Summary

#### Functionality Implemented

**Search Capabilities:**

- Search the product catalogue by product name, brand and description.
- Search membership plans using the plan name and description.
- Locate community posts by searching both titles and post content for moderation purposes.

**Filtering Options:**

- Filter by status (product availability, plan status and subscription status).
- Filter by related fields (product category and membership tier).
- Filter community posts according to their creation date.

**Slug Prepopulation:**

- URL-friendly slugs for products, product categories and membership plans are automatically generated from their respective names, removing the need for manual slug entry and reducing the likelihood of errors.

**Inline Editing:**

- `PlanFeature` records are managed inline within their parent plan using `TabularInline`, allowing all related information to be maintained within a single administrative workflow.

**Deliberate Simplicity:**

- Models containing transactional or user-managed data, including orders, profiles and reviews, rely on Django's default admin registration. This reflects the project's design philosophy that such records should be created and maintained through application logic and front-end functionality rather than direct staff intervention within the admin interface.

**Rationale:** Administrative customisation has been concentrated on areas where staff regularly perform management tasks, including catalogue administration, membership plans and community moderation. In contrast, models managed primarily by automated application processes or user interactions retain a simpler configuration, ensuring development effort is aligned with realistic operational requirements and day-to-day workflows (Vincent, 2020, Chapter 5).

### Accessing the Admin Interface

#### URL and Authentication

**Admin URL:** `http://127.0.0.1:8000/admin/` (development) or `https://fithub-rp-90631f751ed4.herokuapp.com/admin/` (production)

**Authentication Requirements:**

- Full administrative access requires a superuser account.
- Users with staff privileges are granted limited administrative access.
- Standard user accounts are prevented from accessing the Django admin interface.

The project also applies equivalent access restrictions to the custom front-end management system. The `/plans/manage/` interface is secured using a `staff_required` decorator, ensuring that any non-staff user attempting direct URL access receives an HTTP 403 (Forbidden) response.

**Creating Additional Admin Users:**

```bash
# Create a new superuser
python manage.py createsuperuser

# Follow prompts:
# Username: [enter username]
# Email: [enter email]
# Password: [enter password]
# Password (again): [confirm password]
```

**Security Considerations:**

- Access to the admin interface is secured through Django's built-in authentication framework.
- Password validation policies enforce minimum length and complexity requirements.
- In the production environment, `DEBUG=False` ensures that error messages do not reveal application configuration details.

**Production Configuration:**

- The Heroku deployment enforces HTTPS for all connections.
- Sensitive configuration values, including the Django secret key, Stripe API keys, webhook signing secret and email credentials, are stored as environment variables rather than within the project repository.

### Sample Data Population

### Overview

After configuring the Django admin interface, representative sample data was added to the application to support development, testing and demonstration of the FitHub fitness subscription and e-commerce platform. This dataset made it possible to validate model relationships, verify business processes such as stock management, checkout and Stripe webhooks, and test end-to-end user workflows while providing meaningful content for front-end development (Vincent, 2020, Chapter 5).

The sample records were designed to reflect a realistic fitness retail and membership environment. Authentic product names, recognised brands, appropriate pricing and representative membership tiers were used to create a demonstration platform that closely mirrors real-world operating conditions and user scenarios.

### Sample Data Strategy

#### Purpose of Sample Data

**Development Benefits:**

- Validate model relationships and database structure.
- Confirm database constraints and validation rules.
- Develop and refine database queries.
- Verify business logic, including stock quantity limits, automatic stock deduction and Stripe webhook order creation.

**Testing Benefits:**

- Build realistic testing scenarios.
- Validate form handling and error reporting.
- Test edge cases such as out-of-stock products, quantity restrictions and oversell prevention.
- Verify complete purchasing and subscription workflows using Stripe test payment cards.

**Demonstration Benefits:**

- Present the platform with realistic, fully populated content.
- Deliver an authentic user experience during demonstrations.
- Illustrate key data relationships, including categories -> products, plans -> features and orders -> line items.
- Enhance the overall quality of the project portfolio.

**Rationale:** A comprehensive sample dataset supports extensive development and testing while also providing professional demonstration content that closely reflects the expected production environment. This approach ensures both technical validation and an authentic presentation of the system's capabilities (Vincent, 2020, Chapter 5).

### Data Population Process

Unlike Milestone 3, where all records were created manually through the Django admin interface, this project adopted **three complementary population methods**, each selected to validate a different aspect of the system.

#### Method 1: Django Admin Interface (initial catalogue and plans)

The original product catalogue and membership plans were created manually through the Django admin interface. This method was selected to:

1. **Admin Interface Testing** — Confirm the usability and configuration of the Django admin.
2. **Validation Testing** — Verify form validation rules and administrative workflows.
3. **Relationship Verification** — Ensure foreign key relationships (product -> category and feature -> plan) function correctly.

#### Method 2: Data Migration (later catalogue additions)

Two additional products—**Yoga Mat** and **Skipping Rope**—were introduced using an **idempotent data migration** (`shop/migrations/0002_add_yoga_mat_skipping_rope.py`) rather than being entered manually. The migration:

- Implements `get_or_create`, making it **idempotent** and safe to execute multiple times without creating duplicate records.
- Locates categories using their names instead of primary keys, ensuring identical behaviour across both the local SQLite database and the production PostgreSQL database, where auto-incremented IDs differ.
- Executes automatically during deployment through the Heroku release phase (`release: python manage.py migrate`), keeping production data synchronised with the codebase without requiring manual intervention.

**Rationale:** Using a data migration ensures that new catalogue items are consistently deployed across every environment, including local development and production. Unlike manual data entry, this approach provides a repeatable, deployment-safe and environment-independent method of seeding application data (Vincent, 2020, Chapter 5).

#### Method 3: Custom Front-End Management (ongoing plan management)

Once the staff-only plan management interface (`/plans/manage/`) had been implemented, membership plans could be created, updated, published and archived entirely through the front-end, together with their associated feature lists. The interface applies server-side validation, including mandatory field checks and positive price validation, while protecting existing subscriptions by archiving plans instead of deleting them. This design complements the `on_delete=PROTECT` relationship used by subscriptions.

**Alternative Approaches Considered:**

- **Fixtures** — JSON or YAML datasets imported using Django's `loaddata` command (well suited to one-off data population but not inherently idempotent).
- **Management Commands** — Custom Django management commands for automated data generation.
- **Database Seeding Scripts** — Python scripts that populate the database through the Django ORM.

**Rationale:** Combining manual data entry, an idempotent migration and custom front-end CRUD functionality provided broader system coverage than relying on a single population technique. Together, these methods validated administrative workflows, deployment-safe data seeding and the bespoke plan management interface, resulting in more comprehensive testing of the application (Vincent, 2020, Chapter 5).

### Sample Data Specifications

#### Product Categories Configuration

**Quantity:** 4 categories

**Purpose:** Structure the product catalogue into the principal sections expected within a fitness e-commerce platform.

<img width="1546" height="351" alt="image" src="https://github.com/user-attachments/assets/9034ce19-1876-48dd-af6a-5346cfba57bb" />

**Categories and Distribution:**

- Equipment: 4 products (adjustable dumbbells, kettlebell, resistance bands, skipping rope)
- Supplements: 3 products (protein powder, creatine, electrolyte tablets)
- Apparel: 2 products (performance training t-shirt, compression leggings)
- Accessories: 3 products (water bottle, gym towel & bottle set, yoga mat)

**Rationale:** Four well-populated categories provide sufficient breadth to represent a typical online fitness retailer while ensuring each category contains enough products to demonstrate category browsing and filtering functionality effectively (Vincent, 2020, Chapter 4).

#### Products Configuration

**Quantity:** 12 products

**Purpose:** Present a representative fitness product catalogue featuring a range of brands, price points and product categories.

<img width="1533" height="628" alt="image" src="https://github.com/user-attachments/assets/0cef7402-4149-4581-b0d1-e52007c5701a" />


##### **Sample Products:**

**Equipment:**

1. Adjustable Dumbbell Set 24kg (£149.99) — PowerCore
2. Kettlebell 16kg (£39.99) — IronEdge
3. Resistance Bands Set (£24.99) — FlexFit
4. Skipping Rope (£12.99) — added through a data migration

**Supplements:**

5. Whey Protein Powder 1kg, Chocolate (£29.99) — PureFuel
6. Creatine Monohydrate 500g (£19.99) — PureFuel
7. Electrolyte Hydration Tablets (£12.99) — PureFuel

**Apparel:**

8. Compression Leggings (£34.99) — FitHub
9. Performance Training T-Shirt (£22.99) — FitHub

**Accessories:**

10. Stainless Steel Water Bottle 750ml (£16.99) — HydraGo
11. Gym Towel & Bottle Set (£18.99) — FitHub
12. Yoga Mat (£24.99) — added through a data migration

**Stock:** Every product was seeded with an initial inventory of 25 units. This quantity provides adequate stock to test the application's inventory management features, including basket quantity limits, automatic stock deduction during order creation and stock clamping to zero in oversell scenarios, without prematurely exhausting inventory during testing.

**Authenticity:**

- Realistic product names and descriptions supported by believable fictional brands, including PowerCore, IronEdge, FlexFit, PureFuel, HydraGo and the FitHub own-brand range.
- Prices ranging from £12.99 to £149.99 reflect realistic fitness retail values while supporting both low-value and premium purchase scenarios.
- Each product is paired with a corresponding product image delivered through the static image-map template filter.

**Rationale:** A diverse catalogue enables meaningful demonstrations while thoroughly exercising category filtering, price presentation, image rendering and stock management across a representative range of fitness products (Vincent, 2020, Chapter 4).

#### Membership Plans Configuration

**Quantity:** 4 plans

**Purpose:** Represent the subscription element of the platform using realistic pricing tiers and both supported billing intervals.

<img width="1544" height="501" alt="image" src="https://github.com/user-attachments/assets/81cd3759-ea78-493d-9e19-e8af634dea59" />

##### **Sample Plans:**

1. **Starter** — Beginner tier, £4.99/month — introductory package (beginner workouts, workout video library and community access)
2. **Premium** — Intermediate tier, £14.99/month — core subscription (unlimited workouts, premium content, personalised nutrition plans and priority support)
3. **Elite** — Advanced tier, £24.99/month — highest monthly tier (everything in Premium, one-to-one coaching, custom training plans and early feature access)
4. **Annual Pro** — Advanced tier, £119.00/year — annual subscription (everything in Elite, approximately two months free compared with monthly billing, annual fitness assessment and priority support)

**Plan Features:** Every membership plan includes between three and four `PlanFeature` records, each assigned a defined display order and presented on the public plan detail pages within the "What's included" section.

**Pricing Strategy:**

- A progressive pricing structure (£4.99 -> £14.99 -> £24.99) demonstrates a clear membership upgrade path.
- The annual subscription (£119.00, approximately ten times the equivalent monthly fee) illustrates the common "two months free" annual discount model while exercising the second billing interval.

**Rationale:** The sample plans demonstrate all three membership tiers, both billing intervals and the one-to-many relationship between plans and their associated features. At the same time, they present a commercially credible subscription structure suitable for a modern fitness platform (Vincent, 2020, Chapter 4).

### Data Quality Considerations

#### Validation Testing

During both sample data population and execution of the automated test suite, the following validation rules were verified:

**Field Validators:**

- Membership plan prices must be positive values, with server-side validation rejecting negative amounts and displaying an appropriate validation error.
- Product inventory cannot fall below zero, as stock deduction is clamped at zero in oversell scenarios.
- Monetary values enforce a decimal precision of two decimal places.

**Unique Constraints:**

- Product, category and membership plan slugs must remain unique. Slugs are generated automatically, while the custom plan management interface programmatically ensures uniqueness where required.
- Order numbers are guaranteed to be unique through UUID generation.

**Required Fields:**

- Mandatory fields are enforced throughout the application, for example requiring a plan name and description within the plan management form.
- Optional fields, including address line 2 and telephone number, correctly permit blank values.

**Choice Fields:**

- Plan tier, billing interval and publication status are limited to predefined option sets.
- Order status is restricted to valid workflow states (processing, dispatched, delivered, cancelled and refunded).
- Subscription status values are similarly constrained to the approved options.

**Rationale:** Validation performed during sample data entry, together with the project's 89 automated tests, confirmed that database constraints, model validators and server-side form validation rules operated as intended. This comprehensive testing ensured consistent data integrity and reliable application behaviour throughout the system (Vincent, 2020, Chapter 4).

### Sample Orders

#### Test Order Scenarios

Rather than being created manually, sample orders were produced through the complete checkout workflow using Stripe test payment cards. This ensured that each order exercised the genuine purchasing pipeline from payment processing through to order creation.

<img width="1542" height="703" alt="image" src="https://github.com/user-attachments/assets/75c7cfc1-a652-4d46-af6a-8fcac85cfb98" />

<img width="1544" height="796" alt="image" src="https://github.com/user-attachments/assets/5184f3ed-9589-4cca-9ec6-3c87c5568dd1" />


**Test Scenarios Covered:**

1. Standard checkout using a single product and the Stripe test card `4242 4242 4242 4242`.
2. Checkout involving a basket containing multiple products.
3. Basket quantities automatically restricted to available stock before checkout.
4. Checkout attempts with invalid form data, confirming validation errors are displayed and preventing order creation.
5. Order generation triggered by Stripe webhooks (`payment_intent.succeeded`) using both the Stripe CLI and the live webhook endpoint.

**Verification Points:**

- Order numbers are correctly generated using UUIDs.
- The `stripe_payment_intent_id` is stored with each order, enabling webhook idempotency so that repeated webhook events do not create duplicate orders.
- Product stock is reduced by the purchased quantity and prevented from dropping below zero through stock clamping.
- Order line items preserve a snapshot of the product price at the time of purchase.
- Customers can access only their own order history, with ownership protection returning a 404 response if another user's order number is requested.

**Rationale:** Creating sample orders through the authentic checkout and Stripe webhook workflows validated the complete purchasing process, including payment processing, order creation, inventory updates, webhook idempotency and access control. This approach provided significantly more meaningful testing than manually inserting order records into the database (Vincent, 2020, Chapter 4).

---

## Test Plan

[⬆ Back to Table of Contents](#table-of-contents)

### Testing Overview

[⬆ Back to Table of Contents](#table-of-contents)

### Testing Strategy

This project adopts an **automated-first, risk-driven testing strategy**. The project's suite of 89 automated Django tests serves as the foundation for regression testing, with every functional modification verified against the suite before being committed. Manual testing complements the automated tests by evaluating aspects that cannot be reliably automated, including visual layout, cross-browser compatibility, accessibility using assistive technologies and complete end-to-end payment workflows on the live deployment.

**Testing Priorities (highest risk first):**

1. **Payment processing integrity** (Stripe Checkout, subscriptions, webhooks and order generation)
2. **Stock and data integrity** (quantity limits, stock deduction and oversell prevention)
3. **Security and access control** (ownership protection, staff-only functionality and webhook signature validation)
4. **Core application functionality** (authentication, shopping basket, order history and membership plan management)
5. **User experience** (site navigation, forms and responsive behaviour)
6. **Code quality** (validation rules and adherence to Django best practices)
7. **Accessibility** (compliance with WCAG 2.1 guidelines)
8. **Performance** (page loading efficiency and database query optimisation)

**Rationale:** Within an e-commerce platform, the most significant risks relate to financial transactions and data integrity, such as payments being processed without corresponding orders, inventory being oversold or sensitive customer information being exposed. Consequently, testing resources have been prioritised according to the potential impact of each risk.

### Testing Environment

- **Development:** Windows 11, Python 3.12, Django 4.2.23
- **Database:** SQLite for development and PostgreSQL for the production deployment on Heroku
- **Deployment:** Heroku (`https://fithub-rp-90631f751ed4.herokuapp.com/`), Gunicorn and WhiteNoise
- **Payments:** Stripe Test Mode (Stripe Elements for one-off purchases and Stripe Checkout for subscriptions), together with Stripe CLI v1.4x for local webhook testing
- **Browsers:** Latest versions of Chrome, Edge and Firefox
- **Devices:** Desktop (1920×1080), Tablet (768×1024) and Mobile (375×667)

### Traceability

The **Notes** column within each manual test case references the corresponding user story (US*n*) and, where appropriate, the automated test or tests that validate the same functionality. This provides bidirectional traceability between project requirements, manual testing evidence and the automated regression suite.

---

#### 1. FUNCTIONALITY AND CONTENT ACCURACY TESTING

[⬆ Back to Table of Contents](#table-of-contents)

#### 1.1 User Authentication

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 001 | Register using valid account details | New account created; verification email issued; "Verify your email" page displayed | PASS | New account created; verification email issued; "Verify your email" page displayed |

<details>
<summary>📸 Evidence for 001 (click to expand)</summary>
<img width="1064" height="846" alt="image" src="https://github.com/user-attachments/assets/c7d91a4a-d15a-46c4-a73e-880f79316b77" />
<img width="1071" height="573" alt="image" src="https://github.com/user-attachments/assets/19a59801-2521-4f4a-97eb-57ba75ce9cf8" />
<img width="1389" height="673" alt="image" src="https://github.com/user-attachments/assets/3c3282e5-46d2-4a25-a930-053f91efc3af" />
<img width="1330" height="676" alt="image" src="https://github.com/user-attachments/assets/34031194-d152-44b1-8bdc-ab3f4ca39fb2" />
<img width="1334" height="749" alt="image" src="https://github.com/user-attachments/assets/bef897b5-260a-439c-89a6-97d7b32e4ac3" />
<img width="1346" height="763" alt="image" src="https://github.com/user-attachments/assets/ce101673-5b84-4088-909c-41485e37fc66" />
<img width="1363" height="920" alt="image" src="https://github.com/user-attachments/assets/11855c6c-3707-4758-9c50-334d00a05bff" />
<img width="1645" height="436" alt="image" src="https://github.com/user-attachments/assets/6cc8e62c-409a-4d80-b389-3c9ad8481246" />
<img width="1739" height="929" alt="image" src="https://github.com/user-attachments/assets/b2bdcca8-42cd-40fe-9984-c6087188cd51" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 002 | Attempt registration with an existing email address | Appropriate validation error displayed | PASS | Appropriate validation error displayed |

<details>
<summary>📸 Evidence for 002 (click to expand)</summary>
<img width="1057" height="874" alt="image" src="https://github.com/user-attachments/assets/8f1e9d10-8872-4a24-a225-5b7d95b59ec5" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 003 | Confirm account using the email verification link | Account verified successfully; user able to log in | PASS | Account verified successfully; user able to log in (verified in Test ID 001) |

<details>
<summary>📸 Evidence for 003 (click to expand)</summary>
<img width="1071" height="573" alt="image" src="https://github.com/user-attachments/assets/19a59801-2521-4f4a-97eb-57ba75ce9cf8" />
<img width="1389" height="673" alt="image" src="https://github.com/user-attachments/assets/3c3282e5-46d2-4a25-a930-053f91efc3af" />
<img width="1330" height="676" alt="image" src="https://github.com/user-attachments/assets/34031194-d152-44b1-8bdc-ab3f4ca39fb2" />
<img width="1334" height="749" alt="image" src="https://github.com/user-attachments/assets/bef897b5-260a-439c-89a6-97d7b32e4ac3" />
<img width="1346" height="763" alt="image" src="https://github.com/user-attachments/assets/ce101673-5b84-4088-909c-41485e37fc66" />
<img width="1363" height="920" alt="image" src="https://github.com/user-attachments/assets/11855c6c-3707-4758-9c50-334d00a05bff" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 004 | Initial login redirects to the Step 2 profile setup | Profile form displayed (fitness goal, experience level, height and weight) | PASS | Profile form displayed with all four fields on first login (verified during the 001/003 registration flow) — see 004.png |

<details>
<summary>📸 Evidence for 004 (click to expand)</summary>
<img width="1334" height="749" alt="image" src="https://github.com/user-attachments/assets/bef897b5-260a-439c-89a6-97d7b32e4ac3" />
<img width="1346" height="763" alt="image" src="https://github.com/user-attachments/assets/ce101673-5b84-4088-909c-41485e37fc66" />
<img width="1363" height="920" alt="image" src="https://github.com/user-attachments/assets/11855c6c-3707-4758-9c50-334d00a05bff" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 005 | Step 2 profile setup is skipped on future logins | User is redirected directly to the dashboard rather than the profile form | PASS | Step 2 profile setup is skipped on future logins and user is redirected directly to the dashboard rather than the profile form |

<details>
<summary>📸 Evidence for 005 (click to expand)</summary>
<img width="1261" height="914" alt="image" src="https://github.com/user-attachments/assets/8ecb0e11-758c-46ae-a1b1-0e73aac7b8c4" />
<img width="1228" height="920" alt="image" src="https://github.com/user-attachments/assets/42f8bad5-fda1-4c22-82bc-4da0c23b7203" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 006 | Log in with valid credentials | User authenticated and redirected to the dashboard | PASS | Log in with valid credentials and user authenticated and redirected to the dashboard |

<details>
<summary>📸 Evidence for 006 (click to expand)</summary>
<img width="1191" height="840" alt="image" src="https://github.com/user-attachments/assets/8d96b483-cab0-46ef-a15a-30b8b064da20" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 007 | Log in with an incorrect password | Error message displayed ("The username and/or password you specified are not correct.") | PASS | Fixed defect D1 — authentication errors were previously not displayed |

<details>
<summary>📸 Evidence for 007 (click to expand)</summary>
<img width="1228" height="741" alt="image" src="https://github.com/user-attachments/assets/260a0bb2-0884-4962-b391-961849f0349f" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 008 | Log out successfully | User signed out; confirmation message displayed; session terminated | PASS | Log out successfully. User signed out; confirmation message displayed; session terminated |

<details>
<summary>📸 Evidence for 008 (click to expand)</summary>
<img width="1254" height="572" alt="image" src="https://github.com/user-attachments/assets/1b6b8ea5-3033-4409-8bf6-8f98639bc157" />
<img width="1232" height="604" alt="image" src="https://github.com/user-attachments/assets/c6fbc221-65ea-46a1-99df-9b2ac3397af0" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 009 | Password reset process functions correctly | Password reset email received; password successfully reset using the email link | PASS | Password reset process functions correctly and password reset email received; password successfully reset using the email link. |

<details>
<summary>📸 Evidence for 009 (click to expand)</summary>
<img width="1239" height="540" alt="image" src="https://github.com/user-attachments/assets/88abaefc-7669-4074-8aac-79bdf44f203d" />
<img width="1258" height="597" alt="image" src="https://github.com/user-attachments/assets/95db8563-c8b9-42ca-b8bd-5c35d1773175" />
<img width="1813" height="196" alt="image" src="https://github.com/user-attachments/assets/17d5ea93-9284-4502-8f0c-7da25e0de507" />
<img width="976" height="487" alt="image" src="https://github.com/user-attachments/assets/cacb7175-c518-43c9-85af-e0313bade4b4" />
<img width="1318" height="499" alt="image" src="https://github.com/user-attachments/assets/e5229554-5d3d-4857-b9e5-6da164991237" />
<img width="1846" height="702" alt="image" src="https://github.com/user-attachments/assets/67bf24cf-ea90-4d49-85bf-4c62df107efe" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 010 | Dashboard displays accurate profile information | All profile data correctly presented across the account dashboard tabs | FAIL | Dashboard doesn't display all profile data correctly across the account dashboard tabs |

<details>
<summary>📸 Evidence for 010 (click to expand)</summary>
<img width="1252" height="775" alt="image" src="https://github.com/user-attachments/assets/c045702e-cb9a-4553-8a50-ec0d55f8be65" />
<img width="1008" height="750" alt="image" src="https://github.com/user-attachments/assets/bdf02136-10a2-41dc-bb4b-4bbb50574bc4" />
<img width="1203" height="737" alt="image" src="https://github.com/user-attachments/assets/44e03e02-f0b4-4356-a7fe-68e39c4b9230" />
<img width="1197" height="746" alt="image" src="https://github.com/user-attachments/assets/d282edb4-af1a-4606-a350-3e36e302f6d8" />
<img width="1183" height="752" alt="image" src="https://github.com/user-attachments/assets/a13b149a-89f4-4148-93c7-5501fc40b682" />
<img width="1228" height="831" alt="image" src="https://github.com/user-attachments/assets/06fd9cf1-e4e6-4d67-acb1-7e9400ff5005" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 010 (FIX)| Dashboard displays accurate profile information | All profile data correctly presented across the account dashboard tabs | PASS | Dashboard displays all profile data correctly across the account dashboard tabs |

<details>
<summary>📸 Evidence for 010 Fix (click to expand)</summary>
<img width="1202" height="746" alt="image" src="https://github.com/user-attachments/assets/0325249e-5421-44f0-a78f-fff9f1bbd44f" />
<img width="1203" height="757" alt="image" src="https://github.com/user-attachments/assets/56163aca-5906-411a-989d-64627ed88347" />
<img width="958" height="746" alt="image" src="https://github.com/user-attachments/assets/256a9088-1523-4f13-aba8-02fbcd6e4947" />
<img width="1192" height="746" alt="image" src="https://github.com/user-attachments/assets/34a4fc27-6e55-4b44-b817-6dae294e5e0b" />
<img width="1167" height="751" alt="image" src="https://github.com/user-attachments/assets/151803d3-7a3b-4b6c-b573-0a6863d807b7" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 011 | Update profile information | Changes saved successfully and immediately reflected on the dashboard | FAIL | Update profile information changes saved successfully and immediately reflected on the dashboard but EDIT PROFILE button doesn't redirect to Account Details - Fitness Profile interface  |

<details>
<summary>📸 Evidence for 011 (click to expand)</summary>
<img width="1190" height="833" alt="image" src="https://github.com/user-attachments/assets/a9ad8427-45ef-4c9a-9c52-749a508981f2" />
<img width="1610" height="522" alt="image" src="https://github.com/user-attachments/assets/5d61c37d-453c-47a6-beb4-924350d6078c" />
<img width="1214" height="834" alt="image" src="https://github.com/user-attachments/assets/48a820b4-c420-4e33-8d07-808f79660584" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 011 (FIX)| Update profile information | Changes saved successfully and immediately reflected on the dashboard | PASS | Update profile information - Changes saved successfully and immediately reflected on the dashboard   |

<details>
<summary>📸 Evidence for 011 Fix (click to expand)</summary>
<img width="1234" height="849" alt="image" src="https://github.com/user-attachments/assets/517ef473-5145-4dc9-a086-9f78f94946a4" />
<img width="1317" height="935" alt="image" src="https://github.com/user-attachments/assets/4c770a7d-0b09-47e6-a1ec-c2170681ecec" />
<img width="1554" height="563" alt="image" src="https://github.com/user-attachments/assets/cb46d981-ff09-47ef-8c9b-4ce3e5782430" />
</details>

#### 1.2 Membership Plans and Subscriptions

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 012 | Display published membership plans | Four published plans shown in a uniform grid with image, tier, price and billing interval | PASS | Display published membership plans - Four published plans shown in a uniform grid with image, tier, price and billing interval |

<details>
<summary>📸 Evidence for 012 (click to expand)</summary>
<img width="1111" height="820" alt="image" src="https://github.com/user-attachments/assets/6d5a0f7f-65f9-4650-9c39-0c6c0d9db4ed" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 013 | Hide draft and archived plans from members | Only published plans are visible on `/plans/` | PASS | Hide draft and archived plans from members and only published plans are visible on `/plans/`  |

<details>
<summary>📸 Evidence for 013 (click to expand)</summary>
<img width="1299" height="374" alt="image" src="https://github.com/user-attachments/assets/a7082251-bc51-4567-9ee4-3ee1a3dc7476" />
<img width="1076" height="784" alt="image" src="https://github.com/user-attachments/assets/94b17819-574a-4918-8818-10fe1461faff" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 014 | Plan detail page displays the correct features | "What's included" section lists only that plan's associated features | PASS | Plan detail page displays the correct features and "What's included" section lists only that plan's associated features in priority order |

<details>
<summary>📸 Evidence for 014 (click to expand)</summary>
<img width="1133" height="854" alt="image" src="https://github.com/user-attachments/assets/70305007-c049-4232-b250-4f50b638fe8d" />
<img width="1009" height="737" alt="image" src="https://github.com/user-attachments/assets/f387c5e9-49aa-48be-b6b0-3dea8effd006" />
<img width="673" height="855" alt="image" src="https://github.com/user-attachments/assets/110197c4-fc10-4a07-803d-d23afee56fdb" />
<img width="1020" height="762" alt="image" src="https://github.com/user-attachments/assets/509dc815-c1d2-4ead-a884-bb5dee3b9ecf" />
<img width="1148" height="843" alt="image" src="https://github.com/user-attachments/assets/ffe30b16-4f03-4e4f-9c7f-d1e7596a0608" />
<img width="1011" height="739" alt="image" src="https://github.com/user-attachments/assets/93e10549-05ec-461e-a2a8-72f4f804695d" />
<img width="1158" height="811" alt="image" src="https://github.com/user-attachments/assets/98883832-455a-41c5-80dd-15a5952b169e" />
<img width="1007" height="728" alt="image" src="https://github.com/user-attachments/assets/63ed2428-6664-4c5c-8622-ce37b7fa085e" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 015 | Access a draft plan directly via URL | Custom 404 page displayed | FAIL | Access a draft plan directly via URL but there is no custom 404 page displayed |

<details>
<summary>📸 Evidence for 015 (click to expand)</summary>
<img width="1296" height="326" alt="image" src="https://github.com/user-attachments/assets/de534ead-96f9-4f7b-a2d5-ef38bcff2555" />
<img width="654" height="180" alt="image" src="https://github.com/user-attachments/assets/a83c2742-9bf5-4d95-b49b-e2dc5e4b540f" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 015 (FIX) | Access a draft plan directly via URL | Custom 404 page displayed | PASS | Access a draft plan directly via URL but there is no custom 404 page displayed |

<details>
<summary>📸 Evidence for 015 Fix (click to expand)</summary>
<img width="1568" height="400" alt="image" src="https://github.com/user-attachments/assets/09bea93a-2572-49bb-881a-9ddbb879b71d" />
<img width="1175" height="572" alt="image" src="https://github.com/user-attachments/assets/93a10d36-bc8e-44dc-b346-6c57ef175bdc" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 016 | Subscription requires authentication | Unauthenticated users are prompted to log in | PASS | Subscription requires authentication and unauthenticated users are prompted to log in |

<details>
<summary>📸 Evidence for 016 (click to expand)</summary>
<img width="1045" height="759" alt="image" src="https://github.com/user-attachments/assets/aa4cb4df-3b04-49fc-a110-1fcf38503386" />
<img width="1009" height="754" alt="image" src="https://github.com/user-attachments/assets/1b342b10-668a-4427-ad38-cd115c398069" />
<img width="1017" height="561" alt="image" src="https://github.com/user-attachments/assets/13cc348f-d1ba-4d3a-8b17-fb41be4dd103" />
<img width="1016" height="725" alt="image" src="https://github.com/user-attachments/assets/36697061-7b3a-4bde-9899-c50a83fb53bf" />
<img width="1066" height="757" alt="image" src="https://github.com/user-attachments/assets/f9bcd3f6-b581-4589-b39e-19c241598aa7" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 017 | Subscribe redirects to Stripe Checkout | Stripe-hosted checkout opens with the correct membership plan and price | PASS | Subscribe redirects to Stripe Checkout and Stripe-hosted checkout opens with the correct membership plan and price |

<details>
<summary>📸 Evidence for 017 (click to expand)</summary>
<img width="1080" height="725" alt="image" src="https://github.com/user-attachments/assets/10b69c79-6ddc-4db3-aee3-073129e268a9" />
<img width="1032" height="936" alt="image" src="https://github.com/user-attachments/assets/f4b6d6e2-6e7c-4271-af66-a8c1f338caf0" />
<img width="1018" height="325" alt="image" src="https://github.com/user-attachments/assets/5abf5e53-591a-4241-90cd-2e552316ab31" />
<img width="1354" height="427" alt="image" src="https://github.com/user-attachments/assets/42acd036-1a4e-4607-ab2e-14987f4e94d3" />
<img width="1028" height="703" alt="image" src="https://github.com/user-attachments/assets/687ca816-c024-4dea-862c-bbfe657e3d8c" />
<img width="1001" height="698" alt="image" src="https://github.com/user-attachments/assets/9a3ee43c-8751-44ac-ab2d-5af91f8dc334" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 018 | Successful subscription recorded | Subscription appears on the dashboard with the correct plan and status | PASS | Successful subscription recorded and subscription appears on the dashboard with the correct plan and status |

<details>
<summary>📸 Evidence for 018 (click to expand)</summary>
<img width="1080" height="725" alt="image" src="https://github.com/user-attachments/assets/10b69c79-6ddc-4db3-aee3-073129e268a9" />
<img width="1032" height="936" alt="image" src="https://github.com/user-attachments/assets/f4b6d6e2-6e7c-4271-af66-a8c1f338caf0" />
<img width="1018" height="325" alt="image" src="https://github.com/user-attachments/assets/5abf5e53-591a-4241-90cd-2e552316ab31" />
<img width="1354" height="427" alt="image" src="https://github.com/user-attachments/assets/42acd036-1a4e-4607-ab2e-14987f4e94d3" />
<img width="1028" height="703" alt="image" src="https://github.com/user-attachments/assets/687ca816-c024-4dea-862c-bbfe657e3d8c" />
<img width="1001" height="698" alt="image" src="https://github.com/user-attachments/assets/9a3ee43c-8751-44ac-ab2d-5af91f8dc334" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 019 | Subscription success page remains idempotent | Refreshing the page does not generate a duplicate subscription | PASS | Subscription success page remains idempotent and refreshing the page does not generate a duplicate subscription |

<details>
<summary>📸 Evidence for 019 (click to expand)</summary>
<img width="1481" height="597" alt="image" src="https://github.com/user-attachments/assets/3eb45002-f660-4d18-b8fb-762326c30dbd" />
<img width="1656" height="278" alt="image" src="https://github.com/user-attachments/assets/fcb79eb1-9381-42c6-bea7-937af19a3d36" />
</details>

#### 1.3 Shop and Product Browsing

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 020 | Browse all available products | Twelve products displayed with images, names, prices and stock availability | PASS | Browsed all available products and twelve products displayed with images, names, prices and stock availability |

<details>
<summary>📸 Evidence for 020 (click to expand)</summary>
<img width="665" height="947" alt="image" src="https://github.com/user-attachments/assets/d69870bc-91cd-48e8-9377-df0d8b8a07fe" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 021 | Open a product detail page | Full product information displayed, including image, description, price, stock availability and related products | PASS | Opened all product detail pages and verified that full product information is displayed, including image, description, price, stock availability and related products |

<details>
<summary>📸 Evidence for 021 (click to expand)</summary>
<img width="886" height="941" alt="image" src="https://github.com/user-attachments/assets/f0928eb2-2582-4aed-8aaf-2c6e4b2020d2" />
<img width="1011" height="958" alt="image" src="https://github.com/user-attachments/assets/0113480b-8552-4da0-943d-ac3e17aaee9b" />
<img width="908" height="926" alt="image" src="https://github.com/user-attachments/assets/6d2a48b7-58a5-45f4-823f-97d3472626ae" />
<img width="893" height="936" alt="image" src="https://github.com/user-attachments/assets/b6869e6a-4b16-46ce-8b64-18916164e8e6" />
<img width="891" height="918" alt="image" src="https://github.com/user-attachments/assets/1889d279-3509-4382-95fe-85a95f3710ae" />
<img width="887" height="913" alt="image" src="https://github.com/user-attachments/assets/9909994c-cd0a-4de4-9d9d-bae52931fe76" />
<img width="890" height="912" alt="image" src="https://github.com/user-attachments/assets/a8b24c39-5f6b-414b-a47b-b2b41ef73414" />
<img width="895" height="910" alt="image" src="https://github.com/user-attachments/assets/2e5c4330-6980-447d-9724-cd1a6ddf699b" />
<img width="905" height="941" alt="image" src="https://github.com/user-attachments/assets/1b020f24-0f73-411b-b851-af836b70e72d" />
<img width="892" height="935" alt="image" src="https://github.com/user-attachments/assets/61c0e7cc-0ac0-469a-9fe5-7a4fdc8e5a00" />
<img width="904" height="923" alt="image" src="https://github.com/user-attachments/assets/70159789-4c9e-41bc-bffe-09a728f630a6" />
<img width="893" height="923" alt="image" src="https://github.com/user-attachments/assets/6c71d1d1-5dc8-485c-8c3d-2078f163a84e" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 022 | View an unavailable product directly | Custom 404 page returned | PASS | Viewed an unavailable product directly and custom 404 page returned` |

<details>
<summary>📸 Evidence for 022 (click to expand)</summary>
<img width="590" height="548" alt="image" src="https://github.com/user-attachments/assets/3e0d98d1-a20f-494d-a2bd-95410bfd46c1" />
<img width="1332" height="473" alt="image" src="https://github.com/user-attachments/assets/56c5ab1d-2102-4e0d-88fe-3960ab7bd157" />
<img width="673" height="950" alt="image" src="https://github.com/user-attachments/assets/bb36466d-980e-411b-86b5-1ccc4df06886" />
<img width="1430" height="619" alt="image" src="https://github.com/user-attachments/assets/57710322-4099-4190-9b9a-a362c76380ed" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 023 | Add an out-of-stock product to the basket | Product cannot be added; "Out of stock" message displayed | PASS | Add an out-of-stock product to the basket - Product cannot be added; "Out of stock" message displayed |

<details>
<summary>📸 Evidence for 023 (click to expand)</summary>
<img width="629" height="604" alt="image" src="https://github.com/user-attachments/assets/c0b44d78-374a-4c7a-8d46-bfecb0053384" />
<img width="1284" height="511" alt="image" src="https://github.com/user-attachments/assets/30e721a0-58cd-4250-bf1e-58627d267d61" />
<img width="657" height="888" alt="image" src="https://github.com/user-attachments/assets/4c826b60-5e18-404f-8998-66695ddab83d" />
<img width="246" height="359" alt="image" src="https://github.com/user-attachments/assets/d3ec0446-0ac3-48f1-bac3-a92b6833d43b" />
<img width="1000" height="950" alt="image" src="https://github.com/user-attachments/assets/4c25d1d8-2981-4e0d-ac96-b755206b92d4" />

</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 024 | Display related products | "Customers Also Viewed" section presents relevant products | PASS | Display related products - "Customers Also Viewed" section presents relevant products |

<details>
<summary>📸 Evidence for 024 (click to expand)</summary>
<img width="886" height="921" alt="image" src="https://github.com/user-attachments/assets/5962ae8e-0781-436b-97e2-79f5914d9a9d" />
<img width="892" height="930" alt="image" src="https://github.com/user-attachments/assets/0aa89895-be52-4b1e-a269-c00eea6ac077" />
<img width="886" height="923" alt="image" src="https://github.com/user-attachments/assets/4c24afef-ea62-49c0-9a8c-c49289aeab75" />
<img width="885" height="923" alt="image" src="https://github.com/user-attachments/assets/5dc3a1f6-f6df-4651-bc9d-3bf9b1ff8c70" />
<img width="914" height="916" alt="image" src="https://github.com/user-attachments/assets/a7c47927-6bcd-49ad-8bb5-560ea17b4877" />
<img width="900" height="912" alt="image" src="https://github.com/user-attachments/assets/f9d1855a-bb04-4eb7-86b2-5e0582d89b95" />
<img width="893" height="918" alt="image" src="https://github.com/user-attachments/assets/64734813-3858-4d79-a073-4c10ff3a0ed9" />
<img width="887" height="911" alt="image" src="https://github.com/user-attachments/assets/beff6190-6d7f-4d96-bcdd-e507e3ce4341" />
<img width="879" height="937" alt="image" src="https://github.com/user-attachments/assets/400ff44b-22bf-4068-a5ec-998f99534251" />
<img width="893" height="932" alt="image" src="https://github.com/user-attachments/assets/d742217b-6e9f-4029-98a0-b1a939a12dba" />
<img width="884" height="919" alt="image" src="https://github.com/user-attachments/assets/22f97daa-7d86-44db-a456-96eda4461b87" />
<img width="881" height="916" alt="image" src="https://github.com/user-attachments/assets/77095703-5876-46aa-a89f-5733312662d6" />
</details>

#### 1.4 Basket

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 025 | Add a selected quantity from the shop to the basket | Product added successfully; confirmation message includes a functional "View basket" link | PASS | Added a selected quantity from the shop to the basket and products added successfully; confirmation message includes a functional "View basket" link |

<details>
<summary>📸 Evidence for 025 (click to expand)</summary>
<img width="909" height="894" alt="image" src="https://github.com/user-attachments/assets/40c0f31a-f762-4ff6-809f-66177a600f16" />
<img width="923" height="617" alt="image" src="https://github.com/user-attachments/assets/b21076f9-a6d7-4d2c-8ee9-8cddfb11979c" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 026 | Display basket contents | Product images, quantities, line totals and overall basket total shown correctly | PASS | Displays basket contents and product images, quantities, line totals and overall basket total shown correctly |

<details>
<summary>📸 Evidence for 026 (click to expand)</summary>
<img width="911" height="762" alt="image" src="https://github.com/user-attachments/assets/4e32b2d0-c322-4f04-b937-60e21369827a" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 027 | Exceed available stock when adding a product | Quantity automatically limited to available stock with a warning message | PASS | Exceeded available stock when adding a product and quantity automatically limited to available stock with a warning message |

<details>
<summary>📸 Evidence for 027 (click to expand)</summary>
<img width="587" height="524" alt="image" src="https://github.com/user-attachments/assets/038aa3ba-acb5-4d04-866b-83af59058d38" />
<img width="1278" height="551" alt="image" src="https://github.com/user-attachments/assets/cd7b88cc-2390-42d6-8153-324b77726391" />
<img width="921" height="377" alt="image" src="https://github.com/user-attachments/assets/9b5b07de-481a-41db-9f12-7e4ec385a0ea" />

</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 028 | Increase basket quantity beyond stock availability | Quantity adjusted to the available stock level | PASS | Increased basket quantity beyond stock availability and quantity adjusted to the available stock level |

<details>
<summary>📸 Evidence for 028 (click to expand)</summary>
<img width="381" height="407" alt="image" src="https://github.com/user-attachments/assets/3117483e-365e-44a2-bf0a-5ea4430bcd24" />
<img width="1058" height="723" alt="image" src="https://github.com/user-attachments/assets/9e235326-5158-4bb0-b5e6-5a23edc8615d" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 029 | Change basket quantity to zero | Product removed and basket totals updated | PASS | Changed basket quantity to zero and products removed and basket totals updated |

<details>
<summary>📸 Evidence for 029 (click to expand)</summary>
<img width="1051" height="635" alt="image" src="https://github.com/user-attachments/assets/d7d6681b-fc00-48e4-9daf-b47147822274" />
<img width="1007" height="593" alt="image" src="https://github.com/user-attachments/assets/290bd181-9430-45f3-87d6-29548a7f9bfe" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 030 | Remove an item from the basket | Product removed successfully with confirmation feedback | PASS | Removed an item from the basket and product removed successfully with confirmation feedback  |

<details>
<summary>📸 Evidence for 030 (click to expand)</summary>
<img width="1004" height="596" alt="image" src="https://github.com/user-attachments/assets/c5965828-f3e0-428b-831a-a018a293f4e6" />
<img width="987" height="543" alt="image" src="https://github.com/user-attachments/assets/a7d899b3-7a21-4f6d-835d-f85f15022b2a" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 031 | Display an empty basket | "Your basket is empty" message displayed together with a link to browse products | PASS | Empty basket and "Your basket is empty" message displayed together with a link to browse products  |

<details>
<summary>📸 Evidence for 031 (click to expand)</summary>
<img width="1064" height="785" alt="image" src="https://github.com/user-attachments/assets/3949ec6c-4f06-4b06-841f-08f1790ee86c" />
<img width="1009" height="744" alt="image" src="https://github.com/user-attachments/assets/86a83fd9-38c3-422a-a921-15006884ff8d" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 032 | Enter an invalid basket quantity | Invalid input handled safely without crashing; default behaviour applied | PASS |  Verified manually via DevTools bypass and by four automated tests covering non-numeric and negative quantities on add and adjust (add defaults to 1; adjust treats invalid as 0 and removes the item) |

<details>
<summary>📸 Evidence for 032 (click to expand)</summary>
<img width="1120" height="547" alt="image" src="https://github.com/user-attachments/assets/f631959f-73e1-4a66-bcfd-ef872bd35302" />
<img width="1450" height="534" alt="image" src="https://github.com/user-attachments/assets/b880da4e-e59a-4da3-a4a2-6ae8fe72a8f4" />
<img width="1564" height="546" alt="image" src="https://github.com/user-attachments/assets/48de277d-2c06-4350-8d1a-b66955cc4c17" />
<img width="984" height="487" alt="image" src="https://github.com/user-attachments/assets/ce757a65-4c1a-4c4c-b7a0-f8c2668fb66d" />
</details>


#### 1.5 Checkout

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 033 | Attempt checkout with an empty basket | User redirected to the shop with an explanatory message | PASS | Attempted checkout with an empty basket and verified the user redirected to the shop with an explanatory message |

<details>
<summary>📸 Evidence for 033 (click to expand)</summary>
<img width="1027" height="753" alt="image" src="https://github.com/user-attachments/assets/b61bbb0a-ec22-4e26-ba0d-c83ca023914b" />
<img width="1372" height="838" alt="image" src="https://github.com/user-attachments/assets/490cd5c9-6cca-4b44-aefa-eb3c6125cfeb" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 034 | Display checkout order summary | Products, quantities, prices and totals accurately match the basket | PASS | Displayed checkout order summary with products, quantities, prices and totals accurately in the basket |

<details>
<summary>📸 Evidence for 034 (click to expand)</summary>
<img width="1008" height="938" alt="image" src="https://github.com/user-attachments/assets/8201cb73-0013-4aa7-b9b1-58cd1a625c61" />
<img width="999" height="848" alt="image" src="https://github.com/user-attachments/assets/ca4ea75d-8bec-4e8f-8582-82781d682c79" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 035 | Display delivery form correctly | All fields labelled; mandatory fields marked with *; phone number and Address Line 2 identified as optional | PASS | Displayed delivery form correctly with all fields labelled; mandatory fields marked with *; phone number and Address Line 2 identified as optional |

<details>
<summary>📸 Evidence for 035 (click to expand)</summary>
<img width="1003" height="858" alt="image" src="https://github.com/user-attachments/assets/8ae98ed6-4f4e-4f82-87d0-945f644b2cd0" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 036 | Submit an incomplete checkout form | Error summary displayed; invalid fields highlighted with field-level messages; no order created | PASS | Submitted an incomplete checkout form an an error summary is displayed; invalid fields highlighted with field-level messages; no order created |

<details>
<summary>📸 Evidence for 036 (click to expand)</summary>
<img width="991" height="864" alt="image" src="https://github.com/user-attachments/assets/9422b19e-b910-4f87-b84e-acc38f651639" />
<img width="978" height="850" alt="image" src="https://github.com/user-attachments/assets/30ce7fff-277a-4e91-9f0f-08b789b820b2" />
<img width="991" height="848" alt="image" src="https://github.com/user-attachments/assets/bf74fea9-ed24-4c17-8075-45dbef96d520" />
<img width="1017" height="852" alt="image" src="https://github.com/user-attachments/assets/8a557c8e-f517-48a4-ba9e-1f32f42e3ba6" />
<img width="1007" height="853" alt="image" src="https://github.com/user-attachments/assets/b2fce4dd-de82-444d-b8a2-77f278cca3b4" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 037 | Submit an invalid email address | Field displays "Enter a valid email address." validation message | PASS | Submitted an invalid email address and as a result the field displayed "Enter a valid email address." validation message |

<details>
<summary>📸 Evidence for 037 (click to expand)</summary>
<img width="1008" height="839" alt="image" src="https://github.com/user-attachments/assets/29703d43-4727-4cc7-b76b-750e8a4895a8" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 038 | Complete a successful checkout | Order and line items stored; user redirected to the confirmation page | PASS | Completed a successful checkout and order and line items stored; user redirected to the confirmation page |

<details>
<summary>📸 Evidence for 038 (click to expand)</summary>
<img width="1322" height="625" alt="image" src="https://github.com/user-attachments/assets/30ed4a3e-e22f-416a-9c75-9bd4e9d51168" />
<img width="687" height="926" alt="image" src="https://github.com/user-attachments/assets/79bfc563-d3b6-4a3d-a5a4-8a5911bffdff" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 039 | Verify stock deduction after purchase | Product stock reduced by the quantity ordered | PASS | Verified stock deduction after purchase - Product stock reduced by the quantity ordered |

<details>
<summary>📸 Evidence for 039 (click to expand)</summary>
<img width="1322" height="625" alt="image" src="https://github.com/user-attachments/assets/30ed4a3e-e22f-416a-9c75-9bd4e9d51168" />
<img width="687" height="926" alt="image" src="https://github.com/user-attachments/assets/79bfc563-d3b6-4a3d-a5a4-8a5911bffdff" />
<img width="1492" height="171" alt="image" src="https://github.com/user-attachments/assets/724801ed-068b-4d89-871f-fc2b95b93f76" />
<img width="834" height="749" alt="image" src="https://github.com/user-attachments/assets/73cac1e6-e181-4802-8b6a-3dbaf9405420" />
<img width="1313" height="402" alt="image" src="https://github.com/user-attachments/assets/5abfa87f-87a6-41fe-9ab4-0f3b3e4fd57b" />
<img width="1261" height="641" alt="image" src="https://github.com/user-attachments/assets/c319b4e7-02e7-4319-8848-48edc2a24957" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 040 | Prevent negative stock values | Stock level clamped at zero when oversell scenarios occur | PASS | Automated: `test_checkout_stock_never_negative` — reproduced manually via a stale basket (stock reduced in admin after items added) and stock clamped at zero |

<details>
<summary>📸 Evidence for 040 (click to expand)</summary>
<img width="1358" height="704" alt="image" src="https://github.com/user-attachments/assets/dd8e07d1-490f-410e-8cef-ee3fe783dad5" />
<img width="1160" height="695" alt="image" src="https://github.com/user-attachments/assets/5520e27a-78c7-4bef-9848-10c65a5a5556" />
<img width="1333" height="914" alt="image" src="https://github.com/user-attachments/assets/8e7d926a-8046-4b8c-9b2d-b7afb8e505a7" />
<img width="1355" height="926" alt="image" src="https://github.com/user-attachments/assets/3be7be9c-a581-4e14-ada5-0a91baf75f04" />
<img width="1345" height="363" alt="image" src="https://github.com/user-attachments/assets/01998677-9625-46d4-8c8d-d67686f7de1d" />
<img width="1579" height="155" alt="image" src="https://github.com/user-attachments/assets/2cdd3081-cfa3-48e1-a45a-6e65dae1a846" />
<img width="886" height="641" alt="image" src="https://github.com/user-attachments/assets/83721d1a-cd4c-41a4-b38c-045c7e2b3a1d" />
<img width="1164" height="608" alt="image" src="https://github.com/user-attachments/assets/f1c3f631-e732-43cf-b4e0-7c7e01262087" />

**NOTE:** One observation to keep in mind (not a defect for this test): in this scenario the customer is charged for more than the existing items — the clamp protects the stock counter, not the customer. Test 040 only asserts the clamping, which works, so PASS is legitimate.
</details>

#### 1.6 Order Confirmation and Order History

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 041 | Display successful order confirmation | Confirmation page shows checkmark icon, personalised message, order number and email address | PASS | Displayed successful order and confirmation page shows checkmark icon, personalised message, order number and email address |

<details>
<summary>📸 Evidence for 041 (click to expand)</summary>
<img width="1192" height="942" alt="image" src="https://github.com/user-attachments/assets/40802b0d-218a-4205-84a7-086191c681f7" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 042 | Display complete order summary | Ordered items, quantities, subtotal, FREE delivery and total displayed with images | PASS | Displayed complete order summary with ordered items, quantities, subtotal, FREE delivery and total displayed with images |

<details>
<summary>📸 Evidence for 042 (click to expand)</summary>
<img width="684" height="921" alt="image" src="https://github.com/user-attachments/assets/4ab7449a-526b-4e20-b1aa-6a1fb7bf7193" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 043 | Display delivery address | Delivery details entered during checkout shown correctly | PASS | Displayed delivery address and details entered during checkout shown correctly |

<details>
<summary>📸 Evidence for 043 (click to expand)</summary>
<img width="1002" height="588" alt="image" src="https://github.com/user-attachments/assets/96659667-8400-4b28-ab89-5a7a0a34edf3" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 044 | Calculate estimated delivery dates | Delivery estimate calculated dynamically as order date +3 to +5 days | PASS | Dynamic calculation rather than hard-coded values. Calculated estimated delivery dates and delivery estimate calculated dynamically as order date +3 to +5 days |

<details>
<summary>📸 Evidence for 044 (click to expand)</summary>
<img width="934" height="500" alt="image" src="https://github.com/user-attachments/assets/e6709d16-ca2c-4d24-a0ed-6c4e8b2e22da" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 045 | Open an order from "My Account" | Button opens the selected order for the logged-in owner only | PASS | Opened an order from "My Account" and button opens the selected order for the logged-in owner only |

<details>
<summary>📸 Evidence for 045 (click to expand)</summary>
<img width="1004" height="713" alt="image" src="https://github.com/user-attachments/assets/592684cc-4575-4fd8-b635-a1c2a5e86b27" />
<img width="1007" height="635" alt="image" src="https://github.com/user-attachments/assets/bae4ca9e-5c1e-44ff-96c8-1d6b9b4ef493" />
<img width="1005" height="871" alt="image" src="https://github.com/user-attachments/assets/aa22ecfe-8b4f-4405-928b-5a3ba8818347" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 046 | Send confirmation email | Customer receives an email containing complete order details | PASS | Confirmation email sent and customer receives an email containing complete order details |

<details>
<summary>📸 Evidence for 046 (click to expand)</summary>
<img width="1576" height="138" alt="image" src="https://github.com/user-attachments/assets/23d0b462-72c6-41bc-b0d7-8d90e117ed36" />
<img width="1603" height="718" alt="image" src="https://github.com/user-attachments/assets/8790f595-a50a-4dd6-b6b6-b437995c4c71" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 047 | Display order history | Order number, date, thumbnails, status badge, total and view link shown; pagination activates after 10 orders | PASS | Displayed order history with order number, date, thumbnails, status badge, total and view link shown; pagination activates after 10 orders |

<details>
<summary>📸 Evidence for 047 (click to expand)</summary>
<img width="995" height="903" alt="image" src="https://github.com/user-attachments/assets/87f41030-1ea8-4397-b839-9e41bbe03201" />
<img width="1016" height="678" alt="image" src="https://github.com/user-attachments/assets/cd932184-7f32-42e0-b8fd-71d27cc38c75" />
<img width="1026" height="801" alt="image" src="https://github.com/user-attachments/assets/e2ffdf93-b589-4542-8970-d4128c127a16" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 048 | Display order details | Complete order record shown, including images, delivery address, summary and status | PASS | Displayed order details and complete order record shown, including images, delivery address, summary and status |

<details>
<summary>📸 Evidence for 048 (click to expand)</summary>
<img width="1034" height="803" alt="image" src="https://github.com/user-attachments/assets/bad3d882-6bc8-468f-bd94-cb74790d842a" />
<img width="1098" height="760" alt="image" src="https://github.com/user-attachments/assets/5fd1c046-2a46-4787-abac-28b1ce2be240" />
<img width="472" height="686" alt="image" src="https://github.com/user-attachments/assets/b833eaed-bed0-4402-81a7-8719b8af40a0" />
<img width="437" height="437" alt="image" src="https://github.com/user-attachments/assets/f51a3a59-ba7a-4c58-9f9a-2ee8af37dd77" />
<img width="508" height="309" alt="image" src="https://github.com/user-attachments/assets/0702ddad-6fbd-4324-9e1d-c2a15fab4980" />
<img width="539" height="313" alt="image" src="https://github.com/user-attachments/assets/6ebe1f3a-19f8-4bcc-be01-9258b6c383b2" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 049 | Display empty order history | "You haven't placed any orders yet" message shown with a Browse the Shop link | PASS | Displayed empty order history and "You haven't placed any orders yet" message shown with a Browse the Shop link |

<details>
<summary>📸 Evidence for 049 (click to expand)</summary>
<img width="1029" height="778" alt="image" src="https://github.com/user-attachments/assets/bb1ba98d-d127-4e21-befb-23d7120c7a53" />
<img width="1019" height="950" alt="image" src="https://github.com/user-attachments/assets/5e7d7018-129e-4ae1-805d-937f2ad1dc65" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 050 | Access order history from the dashboard | Order numbers open the correct detail page; "View All Orders" opens the history page | PASS | Accessed order history from the dashboard and order numbers open the correct detail page; "View All Orders" opens the history page |

<details>
<summary>📸 Evidence for 050 (click to expand)</summary>
<img width="992" height="639" alt="image" src="https://github.com/user-attachments/assets/dd7d0618-b706-4763-8c15-a471396b8dba" />
<img width="1006" height="659" alt="image" src="https://github.com/user-attachments/assets/1572c08a-b43a-4582-9319-6ea269015407" />
<img width="998" height="648" alt="image" src="https://github.com/user-attachments/assets/2bbcb09a-8d34-45d9-9a32-419a6292ba9c" />
<img width="1017" height="905" alt="image" src="https://github.com/user-attachments/assets/35468553-9a74-422f-859b-d619164f3ce4" />
</details>

#### 1.7 Staff Plan Management (Front-End CRUD)

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 051 | Staff users see the "Manage" navigation link | Visible only to staff; hidden from members and visitors | PASS | Staff users see the "Manage" navigation link and visible only to staff; hidden from members and visitors |

<details>
<summary>📸 Evidence for 051 (click to expand)</summary>
<img width="344" height="194" alt="image" src="https://github.com/user-attachments/assets/da56f4b6-e595-4083-be62-5397867a1a7c" />
<img width="1322" height="371" alt="image" src="https://github.com/user-attachments/assets/dec78b44-886f-409a-bfed-6b6e2dcfe7dd" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 052 | Display all plan statuses | Published, Draft and Archived badges shown for every plan | PASS | Displayed all plan statuses - Published, Draft and Archived badges shown for every plan |

<details>
<summary>📸 Evidence for 052 (click to expand)</summary>
<img width="1310" height="275" alt="image" src="https://github.com/user-attachments/assets/38edae08-0b18-465d-a436-861add4c34bb" />
<img width="996" height="388" alt="image" src="https://github.com/user-attachments/assets/2a74edae-5f13-4bcc-a0c5-c02a8257454f" />
<img width="654" height="592" alt="image" src="https://github.com/user-attachments/assets/6953b81a-4deb-47c6-a264-6ae449739a86" />
<img width="655" height="601" alt="image" src="https://github.com/user-attachments/assets/4b5f93ef-cb15-420c-8e1d-130c8d23eef5" />
<img width="1400" height="348" alt="image" src="https://github.com/user-attachments/assets/7c715c72-27a0-4a0b-a9a6-103d0daaab9d" />
<img width="1001" height="697" alt="image" src="https://github.com/user-attachments/assets/31ff6399-0899-4792-a6b6-91aec66ede1c" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 053 | Create a new membership plan | Plan saved successfully; slug generated automatically; plan appears in the list | PASS | Automated: `test_staff_can_create_plan_with_features` — created "Foundation" plan via the staff form; slug auto-generated and plan listed |

<details>
<summary>📸 Evidence for 053 (click to expand)</summary>
<img width="1042" height="392" alt="image" src="https://github.com/user-attachments/assets/1e51eed7-fd92-4679-a601-9f5b7a447fff" />
<img width="1041" height="742" alt="image" src="https://github.com/user-attachments/assets/4a5a313c-643e-416c-b3ed-eac19307ed50" />
<img width="1006" height="482" alt="image" src="https://github.com/user-attachments/assets/ebf1c06f-c934-47a2-b067-03afa858a936" />
<img width="1288" height="309" alt="image" src="https://github.com/user-attachments/assets/52b4e142-6bd1-4cb3-b587-d9fa1731897e" />
<img width="1111" height="883" alt="image" src="https://github.com/user-attachments/assets/3d0ed8a3-ca20-440c-bc68-8f21da240291" />

</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 054 | Synchronise plan features | One `PlanFeature` created for each line and displayed correctly on the public plan page | PASS | Synchronised plan features via the edit form - reordered, removed and added lines in one save; public page matched exactly and blank lines were skipped |

<details>
<summary>📸 Evidence for 054 (click to expand)</summary>
<img width="1132" height="819" alt="image" src="https://github.com/user-attachments/assets/8cd42b3f-1252-4550-8631-2681f9bce64b" />
<img width="1057" height="421" alt="image" src="https://github.com/user-attachments/assets/bfa97d8e-dc03-456f-9761-b52a113d772d" />
<img width="1042" height="581" alt="image" src="https://github.com/user-attachments/assets/c93c7d7c-70bb-4894-87cf-497d7009a117" />
<img width="1026" height="381" alt="image" src="https://github.com/user-attachments/assets/ffbe1fbe-7462-4a01-b67f-ab65292f2d81" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 055 | Reject negative pricing | "Price must be a positive number." displayed; no record saved | PASS | Automated: `test_negative_price_rejected` — negative and zero prices both rejected with the field-level message; confirmed no plan record was created |

<details>
<summary>📸 Evidence for 055 (click to expand)</summary>
<img width="1019" height="525" alt="image" src="https://github.com/user-attachments/assets/ee60e8d5-34c7-45c9-9f46-7f4232fc426e" />
<img width="1023" height="739" alt="image" src="https://github.com/user-attachments/assets/cf0c61f6-ec0e-4bc9-ba80-26bf919a22dc" />
<img width="1022" height="827" alt="image" src="https://github.com/user-attachments/assets/2e16f08d-74dd-4975-aff9-de61f4a2830e" />
<img width="480" height="377" alt="image" src="https://github.com/user-attachments/assets/1e39cf4d-e2c0-4c01-a7af-df82743eb23b" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 056 | Reject blank required fields | Error summary and field-level validation displayed; no changes saved | PASS | Submitted the plan form with blank required fields - error summary and field-level messages displayed; confirmed no record was created or changed |

<details>
<summary>📸 Evidence for 056 (click to expand)</summary>
<img width="990" height="835" alt="image" src="https://github.com/user-attachments/assets/3b7f8b7a-ebc4-4d84-b382-947f6590edec" />
<img width="985" height="844" alt="image" src="https://github.com/user-attachments/assets/b4f2b53c-9d08-46b9-8d5f-9a013afafeed" />
<img width="987" height="653" alt="image" src="https://github.com/user-attachments/assets/a356ecd3-e782-466c-b96e-30756509c279" />
<img width="1030" height="402" alt="image" src="https://github.com/user-attachments/assets/12f0ccdd-505e-4f83-be24-e8ad50eda8e5" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 057 | Edit an existing plan | Changes saved successfully; associated features synchronised | PASS | Automated: `test_staff_can_edit_plan` — edited plan fields via the pre-filled staff form; changes saved and reflected in the manage list, public page and admin, with features synchronised |

<details>
<summary>📸 Evidence for 057 (click to expand)</summary>
<img width="1006" height="686" alt="image" src="https://github.com/user-attachments/assets/af7e8ee0-8090-4f54-bbff-ec2745aa0407" />
<img width="1029" height="494" alt="image" src="https://github.com/user-attachments/assets/a248eeda-7580-49dd-a581-99bf529db317" />
<img width="1302" height="342" alt="image" src="https://github.com/user-attachments/assets/366c6fd8-e61c-4740-a5da-b0718fc11c8f" />
<img width="684" height="583" alt="image" src="https://github.com/user-attachments/assets/3a659890-94b4-47f9-8753-ab8499b22aa2" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 058 | Confirm archive operation | Confirmation page explains the consequences before archiving | PASS | Archive action shows a confirmation page naming the plan and explaining consequences (removed from new sign-ups; existing subscriptions unaffected); cancelling leaves the plan unchanged and only confirming archives it |

<details>
<summary>📸 Evidence for 058 (click to expand)</summary>
<img width="1041" height="520" alt="image" src="https://github.com/user-attachments/assets/3ffb4863-d23d-4f86-829d-78773e9c0434" />
<img width="1067" height="503" alt="image" src="https://github.com/user-attachments/assets/3a938b88-a1d5-44d2-bc39-b28d26a89d09" />
<img width="1011" height="531" alt="image" src="https://github.com/user-attachments/assets/5793f139-150e-494b-9823-09cadcd61338" />
<img width="1286" height="348" alt="image" src="https://github.com/user-attachments/assets/bf954399-b0af-4ecc-976d-3cd0ae2a676f" />
<img width="647" height="606" alt="image" src="https://github.com/user-attachments/assets/43c01d15-79ad-4bb2-ae36-2c294c7a94bd" />
<img width="1010" height="745" alt="image" src="https://github.com/user-attachments/assets/192b2080-28c9-49f2-a73f-a5901a7084ea" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 059 | Archive using soft deletion | Plan marked as Archived, retained in the database and removed from public view | PASS | Automated: `test_archive_is_soft_delete`; protects subscriptions (`on_delete=PROTECT`) — archived plan retained in admin with all data and existing subscriptions intact, absent from the public grid and detail URL |

<details>
<summary>📸 Evidence for 059 (click to expand)</summary>
<img width="1289" height="342" alt="image" src="https://github.com/user-attachments/assets/8326ce6b-ded4-4c7c-88ea-026735b83322" />
<img width="1111" height="844" alt="image" src="https://github.com/user-attachments/assets/4e7f55b1-eb95-46ba-803f-9c5ad198e65a" />
<img width="1009" height="473" alt="image" src="https://github.com/user-attachments/assets/96515280-54e0-4b94-a780-0f15c75256aa" />
<img width="1026" height="762" alt="image" src="https://github.com/user-attachments/assets/e05b25d1-da1a-4c84-99bf-aed68a6a9edb" />
<img width="1438" height="614" alt="image" src="https://github.com/user-attachments/assets/cfff7c49-4eb9-48bd-bd61-7261a98e6641" />
<img width="1053" height="612" alt="image" src="https://github.com/user-attachments/assets/dc90243e-3cc6-45d1-b5bc-8f60af3b7a82" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 060 | Display empty Manage Plans page | "No plans yet" message displayed with a "Create your first plan" prompt | PASS | Verified locally with an emptied plans table (staging this on production would require deleting live subscription data) - "No plans yet" message and working "Create your first plan" prompt displayed; production data restored afterwards from a Heroku dumpdata fixture |

<details>
<summary>📸 Evidence for 060 (click to expand)</summary>
<img width="1241" height="505" alt="image" src="https://github.com/user-attachments/assets/036064e0-32db-413a-bf4a-c203c5f11986" />
<img width="1396" height="892" alt="image" src="https://github.com/user-attachments/assets/633e8245-eddd-406c-a011-9cf7f0185009" />
<img width="1320" height="887" alt="image" src="https://github.com/user-attachments/assets/6a52b267-3860-4d36-8da4-d6a3352658b9" />
</details>

#### 1.8 Community and Reviews

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 061 | Display community posts | Posts listed with title, author and publication date | PASS | Displayed community posts from multiple authors, each listed with title, author username and publication date, newest first |

<details>
<summary>📸 Evidence for 061 (click to expand)</summary>
<img width="889" height="910" alt="image" src="https://github.com/user-attachments/assets/2ac50d09-f65a-4a1b-b9d6-85c49726067a" />
<img width="677" height="729" alt="image" src="https://github.com/user-attachments/assets/5f9ff69c-3c4e-4721-b246-2f106c6108d4" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 062 | Require authentication to create a post | Anonymous users redirected to the login page | PASS | Attempted to create a post while logged out - redirected to the login page with a next parameter, and logging in returned to the post form |

<details>
<summary>📸 Evidence for 062 (click to expand)</summary>
<img width="912" height="678" alt="image" src="https://github.com/user-attachments/assets/a57bc61c-5f27-4201-94e9-395fd72bb01e" />
<img width="899" height="869" alt="image" src="https://github.com/user-attachments/assets/4a8b2c1d-f0fc-46ac-aa39-db03de6334c6" />
<img width="1152" height="413" alt="image" src="https://github.com/user-attachments/assets/8a300a8b-a217-4fb7-a849-185739c13788" />
<img width="887" height="907" alt="image" src="https://github.com/user-attachments/assets/f4ccf560-ac2e-4f45-bf51-a62c2bbd923d" />
<img width="907" height="370" alt="image" src="https://github.com/user-attachments/assets/4ad52181-2ffe-41c7-bd16-ad3fe33824dc" />
<img width="663" height="869" alt="image" src="https://github.com/user-attachments/assets/336ed8dd-8f12-4f0c-87fa-eeccc85deef9" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 063 | Create a community post | Newly created post appears in the community list | PASS | Created a new post via the community form - post saved and appeared at the top of the community list with the correct author and date |

<details>
<summary>📸 Evidence for 063 (click to expand)</summary>
<img width="934" height="482" alt="image" src="https://github.com/user-attachments/assets/0b7ce0d6-e311-4d03-81a9-39864396f84b" />
<img width="936" height="558" alt="image" src="https://github.com/user-attachments/assets/c78e46e7-721a-42a9-a80a-5b828ab34c4f" />
<img width="869" height="529" alt="image" src="https://github.com/user-attachments/assets/64ffc319-6f25-45ca-9168-eb9bf457c180" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 064 | Edit or delete own community post | Changes saved successfully or post removed | PASS | Edited own post via the pre-filled form and changes saved correctly; deleted a second post via the confirmation page and it was removed from the list |

<details>
<summary>📸 Evidence for 064 (click to expand)</summary>
<img width="877" height="454" alt="image" src="https://github.com/user-attachments/assets/b448a5d4-1343-4e57-9138-e397886453ba" />
<img width="887" height="321" alt="image" src="https://github.com/user-attachments/assets/34efc25a-e1b2-4d1a-9713-fd247cf7cbd9" />
<img width="918" height="518" alt="image" src="https://github.com/user-attachments/assets/5943e7b7-82cc-4366-8fda-1b026af6acb0" />
<img width="869" height="583" alt="image" src="https://github.com/user-attachments/assets/177e747e-8714-4733-be88-d12dbbec8e2e" />
<img width="961" height="440" alt="image" src="https://github.com/user-attachments/assets/ef0274f6-0e9c-458f-8c62-6fead584e997" />
<img width="886" height="569" alt="image" src="https://github.com/user-attachments/assets/5cf812cb-91dc-4a6a-b9af-f59549cfeea8" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 065 | Submit a product review with a rating | Review displayed on the relevant product page | PASS | Submitted reviews with ratings on two products from different accounts - each review displayed on its own product page with username, star rating, comment and date, with no leakage to other products |

<details>
<summary>📸 Evidence for 065 (click to expand)</summary>
<img width="879" height="640" alt="image" src="https://github.com/user-attachments/assets/281d302e-bd48-436d-a033-4789048bb32f" />
<img width="894" height="337" alt="image" src="https://github.com/user-attachments/assets/3a1e63bb-db3c-4dc3-85a4-7dfb87e60aa2" />
<img width="894" height="687" alt="image" src="https://github.com/user-attachments/assets/496e6c5e-9f66-4cdf-93ef-dd9f79a41fe5" />
<img width="936" height="529" alt="image" src="https://github.com/user-attachments/assets/eee11545-60d2-4b0f-ad37-bc09bd43917a" />
<img width="919" height="344" alt="image" src="https://github.com/user-attachments/assets/181202a7-db28-4e24-b780-d96dec8d53c7" />
<img width="665" height="540" alt="image" src="https://github.com/user-attachments/assets/d977ea47-ae5a-4e1b-96f3-ea71cc70deb3" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 066 | Reject an invalid review rating | Validation error displayed for ratings outside the permitted range | PASS | Automated: `test_rating_too_high_is_invalid` — bypassed the browser's min/max via DevTools and submitted out-of-range ratings; server-side validation rejected them with a field error and no review was saved |

<details>
<summary>📸 Evidence for 066 (click to expand)</summary>
<img width="901" height="246" alt="image" src="https://github.com/user-attachments/assets/a5a55b86-b812-4f28-96c4-5435be6a67eb" />
<img width="905" height="248" alt="image" src="https://github.com/user-attachments/assets/76027dbc-b927-4b74-a34f-344b25fac9b8" />
<img width="894" height="245" alt="image" src="https://github.com/user-attachments/assets/72550887-74c2-4230-88c1-21141e7181d5" />
<img width="1589" height="344" alt="image" src="https://github.com/user-attachments/assets/7133be44-4ee4-4228-97fa-802e98ff95c8" />
<img width="554" height="124" alt="image" src="https://github.com/user-attachments/assets/e4c668a4-3e62-4225-8566-4c108e86a871" />
<img width="525" height="146" alt="image" src="https://github.com/user-attachments/assets/7db435bf-125e-4880-a3e2-2e3d97d602f3" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 067 | Edit or delete own review | Updates saved successfully or review removed | PASS | Edited own review via the pre-filled form - rating and comment both updated on the product page; deleted a review from the other account via its confirmation step and it was removed |

<details>
<summary>📸 Evidence for 067 (click to expand)</summary>
<img width="908" height="611" alt="image" src="https://github.com/user-attachments/assets/4b5fbcbd-0545-4f66-b936-324566b8a38d" />
<img width="894" height="253" alt="image" src="https://github.com/user-attachments/assets/42be1337-3825-4ee9-94aa-b64059025306" />
<img width="928" height="259" alt="image" src="https://github.com/user-attachments/assets/1ba6919c-8fc9-45a1-afbd-78eb9188750c" />
<img width="886" height="656" alt="image" src="https://github.com/user-attachments/assets/313c7c57-edab-4e62-a0fc-b7fcd62ef360" />
<img width="689" height="216" alt="image" src="https://github.com/user-attachments/assets/86a41989-a859-4d74-bab8-3445fde31025" />
<img width="676" height="478" alt="image" src="https://github.com/user-attachments/assets/bd81a21f-2a6c-4edc-a65a-bde5ce95a67a" />
</details>

---

#### 2. SECURITY AND ACCESS CONTROL TESTING

[⬆ Back to Table of Contents](#table-of-contents)

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 068 | Access order history without authentication | Anonymous users redirected to the login page | PASS | Automated: `test_history_requires_login` — direct URL access while logged out redirected to the login page with a next parameter, and logging in returned to the order history |

<details>
<summary>📸 Evidence for 068 (click to expand)</summary>
<img width="1298" height="806" alt="image" src="https://github.com/user-attachments/assets/4f76ae73-84ba-4311-b816-072c38c28708" />
<img width="1278" height="968" alt="image" src="https://github.com/user-attachments/assets/e5318de7-c03a-4862-9fa3-ede5c80faafc" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 069 | Verify users can view only their own orders | Orders belonging to other users are never displayed | PASS | Automated: `test_history_lists_own_orders_only` — second account's history shows only its own orders, and direct URL access to another user's order returns the branded 404; also completes the manual ownership verification referenced in 045 |

<details>
<summary>📸 Evidence for 069 (click to expand)</summary>
<img width="887" height="626" alt="image" src="https://github.com/user-attachments/assets/cafff150-5103-406c-86eb-37691412eceb" />
<img width="994" height="779" alt="image" src="https://github.com/user-attachments/assets/2ba28956-7c5b-4a9b-908d-408185c34b83" />
<img width="1402" height="776" alt="image" src="https://github.com/user-attachments/assets/7e46e31d-e209-4238-ab1a-695f3b52063a" />
<img width="1337" height="873" alt="image" src="https://github.com/user-attachments/assets/d48196f3-df1f-4242-bb5f-16af1d99e19e" />
<img width="1467" height="658" alt="image" src="https://github.com/user-attachments/assets/4a22c0fd-d6fd-4adf-9f31-7bd0b0d62c0c" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 070 | Attempt to access another user's order details | Request returns a 404 response, preventing data disclosure | PASS | Automated: `test_detail_ownership_guard_404` — direct URL access to another user's order returns the branded 404, identical to a nonexistent order, so the response does not disclose whether the order exists |

<details>
<summary>📸 Evidence for 070 (click to expand)</summary>
<img width="1298" height="880" alt="image" src="https://github.com/user-attachments/assets/0cffdd11-96a9-46ed-bfe9-e1e14d443e94" />
<img width="1411" height="647" alt="image" src="https://github.com/user-attachments/assets/b465907a-61ad-4760-9359-2ae985d25656" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 071 | Prevent visitors from accessing plan management | Anonymous requests to `/plans/manage/` return HTTP 403 | PASS | Automated: `test_non_staff_gets_403` — all four management URLs (list, create, edit, archive) return HTTP 403 for anonymous requests; deliberately a refusal rather than a login redirect |

<details>
<summary>📸 Evidence for 071 (click to expand)</summary>
<img width="637" height="397" alt="image" src="https://github.com/user-attachments/assets/a4c4008f-ecf7-4cbf-ab13-1927a4991e4c" />
<img width="632" height="286" alt="image" src="https://github.com/user-attachments/assets/45a9ff26-c688-482f-986e-75eee43a9a59" />
<img width="666" height="302" alt="image" src="https://github.com/user-attachments/assets/58f57d87-960a-48da-a590-e575b2d319a9" />
<img width="1063" height="333" alt="image" src="https://github.com/user-attachments/assets/46471f27-e3ac-4d43-832d-19bb0f0af8c2" />
<img width="551" height="200" alt="image" src="https://github.com/user-attachments/assets/1d7e1202-9eb8-4b4b-9c1a-7574acf88982" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 072 | Prevent non-staff members from accessing plan management | Authenticated non-staff users receive HTTP 403 across all four management routes, including direct URL access | PASS | Automated: `test_non_staff_gets_403` — all four management URLs return HTTP 403 for a logged-in non-staff member; authentication alone grants no access, only staff status |

<details>
<summary>📸 Evidence for 072 (click to expand)</summary>
<img width="520" height="143" alt="image" src="https://github.com/user-attachments/assets/a2c8dac4-b449-4d39-8426-39532cd6f853" />
<img width="596" height="254" alt="image" src="https://github.com/user-attachments/assets/18f46f93-6854-499a-967e-b784d196ae79" />
<img width="649" height="154" alt="image" src="https://github.com/user-attachments/assets/3a1bbf70-a9df-4bbb-911f-d94ffdf84fc6" />
<img width="691" height="149" alt="image" src="https://github.com/user-attachments/assets/8f30e5dd-763b-4fc6-b60b-006885644fd7" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 073 | Attempt to edit another user's community post | Action blocked successfully | PASS | Automated: `test_user_cannot_edit_another_users_post` — no edit controls shown on another user's post, and direct URL access redirected to the community list with a "You can only edit your own posts." error; the automated test additionally confirms a forced POST leaves the post unchanged |

<details>
<summary>📸 Evidence for 073 (click to expand)</summary>
<img width="686" height="819" alt="image" src="https://github.com/user-attachments/assets/efb13a3e-343f-460e-af89-81cd91c9db9a" />
<img width="1027" height="476" alt="image" src="https://github.com/user-attachments/assets/4391727d-5c4b-4eb7-835e-2b65ae13c169" />
<img width="989" height="286" alt="image" src="https://github.com/user-attachments/assets/2f6b4ab4-9957-49e3-bece-360540b90847" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 074 | Attempt to delete another user's product review | Action prevented successfully | PASS | Automated: `test_user_cannot_delete_another_users_review` — no delete controls shown on another user's review, and direct URL access redirected to the product page with a "You can only delete your own reviews." error, the review remaining intact; the automated test additionally confirms a forced POST leaves it in the database |

<details>
<summary>📸 Evidence for 074 (click to expand)</summary>
<img width="1032" height="847" alt="image" src="https://github.com/user-attachments/assets/708b15eb-f78a-422a-b261-59f868b88232" />
<img width="474" height="114" alt="image" src="https://github.com/user-attachments/assets/07ca370d-380a-41a2-b590-43360b25010d" />
<img width="993" height="766" alt="image" src="https://github.com/user-attachments/assets/e1d37fb4-c9d2-4b9e-8f82-d993e064a8cf" />
<img width="987" height="763" alt="image" src="https://github.com/user-attachments/assets/52119490-c353-48fd-8a9b-d22ddb923a47" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 075 | Submit a webhook request with an invalid signature | Forged request to `/orders/wh/` returns HTTP 400 and no order is created | PASS | Automated: `test_bad_signature_rejected` — forged POSTs to the live endpoint with an invalid signature and with no signature header both returned HTTP 400 ("Invalid signature") and no order was created |
<details>
<summary>📸 Evidence for 075 (click to expand)</summary>
<img width="1096" height="350" alt="image" src="https://github.com/user-attachments/assets/85322308-b958-489b-934c-8dc666b0f9ff" />
<img width="1102" height="187" alt="image" src="https://github.com/user-attachments/assets/c613126e-0419-47d6-9edf-02184def25b4" />
<img width="1109" height="155" alt="image" src="https://github.com/user-attachments/assets/5200e01d-a576-4fad-ab01-a6b8300df4b2" />
<img width="381" height="493" alt="image" src="https://github.com/user-attachments/assets/40c1f220-cc0a-49f8-b7bc-e3514c85d698" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 076 | Verify CSRF protection on application forms | All forms include CSRF tokens; POST requests without a valid token are rejected | PASS | CSRF tokens confirmed in form markup across the application; POSTs without a valid token rejected with HTTP 403 by Django middleware. The webhook is intentionally `csrf_exempt` because Stripe's signed webhook provides the authenticity guarantee instead - demonstrated in row 075, where an unsigned POST returned 400 via signature verification rather than a CSRF 403 |

<details>
<summary>📸 Evidence for 076 (click to expand)</summary>
<img width="1797" height="559" alt="image" src="https://github.com/user-attachments/assets/bb326330-280d-4934-8fe3-13e95847510f" />
<img width="1766" height="948" alt="image" src="https://github.com/user-attachments/assets/04aeba74-bb8e-4cc2-9b53-58d6cca4f647" />
<img width="1806" height="963" alt="image" src="https://github.com/user-attachments/assets/60366458-bfc3-43ea-8d0c-1e6f064cb11b" />
<img width="1110" height="154" alt="image" src="https://github.com/user-attachments/assets/8cc34f1a-8a31-4b3c-86f4-b9c69e75c56a" />
<img width="895" height="308" alt="image" src="https://github.com/user-attachments/assets/ef7c7e4c-692b-4c34-9ecd-6c3958e6c94f" />
<img width="515" height="67" alt="image" src="https://github.com/user-attachments/assets/f30f0dd3-3e56-4574-9f07-e56265060392" />
<img width="1099" height="699" alt="image" src="https://github.com/user-attachments/assets/581c08f7-803f-4e66-9d71-f6bfdb72a668" />
<img width="480" height="138" alt="image" src="https://github.com/user-attachments/assets/eaf1d8f2-4d34-49db-be60-d6f19702491a" />
<img width="1092" height="146" alt="image" src="https://github.com/user-attachments/assets/eb456704-a086-4677-81be-a05225dfe8be" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 077 | Confirm secrets are stored securely | No API keys or passwords present in the repository; `env.py` excluded from version control; Heroku Config Vars used | PASS | Repository audited via git: no secret patterns in tracked files, `env.py` absent from the entire git history, history searches for real key prefixes empty (only a fake test fixture and documentation placeholders reference secret formats); all sensitive settings read from environment variables held in Heroku Config Vars. Audit surfaced an unreplaced placeholder production SECRET_KEY; full credential rotation performed and verified end-to-end |

<details>
<summary>📸 Evidence for 077 (click to expand)</summary>
<img width="1213" height="612" alt="image" src="https://github.com/user-attachments/assets/2bfb96ca-a6e7-4fd0-a575-ad62aa5d0dfd" />
<img width="328" height="492" alt="image" src="https://github.com/user-attachments/assets/c40bddeb-11aa-4f80-a09d-7eee67b82cdf" />
<img width="229" height="799" alt="image" src="https://github.com/user-attachments/assets/700621a6-56c8-4c1c-bd41-ab9a8ef1e5b0" />
<img width="1015" height="113" alt="image" src="https://github.com/user-attachments/assets/7da8944c-d5df-4bad-9cbc-32d68f309a67" />
<img width="725" height="152" alt="image" src="https://github.com/user-attachments/assets/3e6f0a48-8e5c-4cba-9817-e4b7df249b0a" />
<img width="690" height="124" alt="image" src="https://github.com/user-attachments/assets/756fdc35-d422-4a1a-b165-c793567c3f9c" />
<img width="896" height="754" alt="image" src="https://github.com/user-attachments/assets/4a523a0f-6648-4968-a895-e4fdc4fa9b88" />
<img width="1105" height="435" alt="image" src="https://github.com/user-attachments/assets/d731643d-ec4d-4b68-9eb4-c3af64764731" />
<img width="1107" height="632" alt="image" src="https://github.com/user-attachments/assets/fbe947c5-d5a6-4853-ba8e-2e1714d1a6b0" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 078 | Confirm `DEBUG` is disabled in production | Generic 404 and 500 error pages displayed instead of configuration details or stack traces | PASS | Branded 404 renders on production, which is direct evidence of DEBUG=False since custom error templates only render then; DEBUG derives from the DEVELOPMENT env var's presence, absent from Heroku config; production 500s during D9/D10 showed the plain server error page with no stack trace |

<details>
<summary>📸 Evidence for 078 (click to expand)</summary>
<img width="1298" height="537" alt="image" src="https://github.com/user-attachments/assets/55e4e886-1528-4d2a-8bab-e0de36161a8a" />
<img width="1404" height="979" alt="image" src="https://github.com/user-attachments/assets/f85e5cc4-b029-4920-ae12-7b88e562e850" />
<img width="745" height="253" alt="image" src="https://github.com/user-attachments/assets/d2e07662-fe4a-47f2-9880-dceb5fbc7d99" />
<img width="1230" height="627" alt="image" src="https://github.com/user-attachments/assets/c504bca5-7538-4593-aaef-864a7d48e047" />

  **NOTE:**
  Branded 404 renders on production (custom error templates only render when DEBUG=False, so this is direct evidence); DEBUG derives from the DEVELOPMENT env var's presence, absent from Heroku config vars; production 500s during defects D9/D10 showed the plain server error page with no stack trace
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 079 | Verify payment card details never reach the server | Card information handled exclusively by the Stripe Elements iframe; no payment fields included in Django POST requests | PASS | Verified at both layers: card inputs render inside a js.stripe.com iframe isolated from the page DOM, and DevTools network capture of a live checkout shows card data posted only to api.stripe.com (PaymentIntent confirm), while the Django checkout POST carries just the CSRF token, client_secret reference and delivery fields; a network-wide search for the test card number matches Stripe requests only |

<details>
<summary>📸 Evidence for 079 (click to expand)</summary>
<img width="498" height="197" alt="image" src="https://github.com/user-attachments/assets/5f299bb4-b718-4bbd-944f-d8b52d6e466c" />
<img width="1099" height="887" alt="image" src="https://github.com/user-attachments/assets/05ebfbf4-6194-45b0-b13b-6dbec1b05559" />
<img width="163" height="657" alt="image" src="https://github.com/user-attachments/assets/f17a63e0-6c9e-43eb-8fc2-ad9e32735409" />
<img width="355" height="703" alt="image" src="https://github.com/user-attachments/assets/3fcda507-42e1-405a-9f55-c02d0c1fe68c" />
<img width="575" height="722" alt="image" src="https://github.com/user-attachments/assets/6e30c4e5-4846-4def-9385-c0236d780eca" />
<img width="1694" height="938" alt="image" src="https://github.com/user-attachments/assets/54edc2d5-9af6-445a-8583-bfe27ebff739" />
<img width="940" height="817" alt="image" src="https://github.com/user-attachments/assets/b0949738-936f-4234-9029-f3f7ac8bbc13" />
<img width="752" height="723" alt="image" src="https://github.com/user-attachments/assets/e9bdbfdf-99ac-4730-af5a-98169b7acc25" />
<img width="772" height="564" alt="image" src="https://github.com/user-attachments/assets/97ab8513-e785-4107-bec8-eb41c67173df" />
<img width="767" height="540" alt="image" src="https://github.com/user-attachments/assets/e265d4e0-f0ec-4fcc-a303-0b92a3e3be6c" />
<img width="753" height="367" alt="image" src="https://github.com/user-attachments/assets/a00bde41-21cb-4a42-8728-bc322aa57b13" />
</details>

---

#### 3. PAYMENT AND INTEGRATION TESTING

[⬆ Back to Table of Contents](#table-of-contents)

#### 3.1 Stripe Test Card Matrix (One-Time Purchases)

| Test ID | Card | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 080 | 4242 4242 4242 4242 | Process a successful payment | Payment completed successfully; order created; confirmation page displayed | PASS | Processed a payment with the standard success card - payment completed without challenge, order created with line items, confirmation page displayed, and the payment shows as Succeeded in the Stripe Dashboard |

<details>
<summary>📸 Evidence for 080 (click to expand)</summary>
<img width="926" height="836" alt="image" src="https://github.com/user-attachments/assets/018439c5-fdf6-467c-a63b-34b3804c80e9" />
<img width="911" height="839" alt="image" src="https://github.com/user-attachments/assets/17e0fb52-7bc2-4508-908a-760fbb83f893" />
<img width="914" height="875" alt="image" src="https://github.com/user-attachments/assets/b59c778e-daa5-4329-9da0-8f03153a41c2" />
<img width="813" height="713" alt="image" src="https://github.com/user-attachments/assets/3df1ee41-846e-4704-bd93-e16b819e84f0" />
<img width="1334" height="132" alt="image" src="https://github.com/user-attachments/assets/05ae746e-2e45-4607-80ff-80dd8ebc3a27" />
<img width="1715" height="865" alt="image" src="https://github.com/user-attachments/assets/776b2ec6-70a7-4536-b68d-04bbf2b4ccf5" />
</details>

| Test ID | Card | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 081 | 4000 0000 0000 0002 | Attempt payment with a declined card | "Your card was declined." message displayed; payment form re-enabled; no order generated | PASS | Declined card surfaced the "Your card was declined." message inline on the checkout page; the form re-enabled and a retry with the success card completed normally; the declined attempt generated no order, confirmed in admin, and shows as Failed in the Stripe Dashboard |

<details>
<summary>📸 Evidence for 081 (click to expand)</summary>
<img width="920" height="736" alt="image" src="https://github.com/user-attachments/assets/6c17e4a3-726b-4807-a881-56f2104bea9d" />
<img width="912" height="477" alt="image" src="https://github.com/user-attachments/assets/86a5928c-4973-4a44-aa40-2830d635b741" />
<img width="904" height="826" alt="image" src="https://github.com/user-attachments/assets/24f88e40-5cab-4150-8c45-0b187a7dcb5a" />
<img width="564" height="557" alt="image" src="https://github.com/user-attachments/assets/b0c8dd87-759c-4772-b244-2450da4df76f" />
<img width="918" height="301" alt="image" src="https://github.com/user-attachments/assets/cca7f6a3-1db6-4da7-a5b5-337f680f19a0" />
<img width="1168" height="302" alt="image" src="https://github.com/user-attachments/assets/a89319ed-e931-4fbf-ab9d-bc8f6a12935d" />
<img width="1307" height="808" alt="image" src="https://github.com/user-attachments/assets/b92041d3-14d6-4be3-b91a-32135a3af017" />
</details>

| Test ID | Card | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 082 | 4000 0025 0000 3155 | Complete 3D Secure authentication | Authentication dialogue displayed; payment succeeds after verification | PASS | 3D Secure challenge modal displayed on submit; completing authentication resumed the payment, which succeeded with the order created and confirmation page shown; the Stripe Dashboard records the authentication step in the payment timeline |

<details>
<summary>📸 Evidence for 082 (click to expand)</summary>
<img width="958" height="826" alt="image" src="https://github.com/user-attachments/assets/da7e20a3-785f-4fa4-860f-26994484e7f9" />
<img width="890" height="782" alt="image" src="https://github.com/user-attachments/assets/780daf5c-acee-42c8-b4f5-644c054c2ebf" />
<img width="677" height="708" alt="image" src="https://github.com/user-attachments/assets/ed06ef6b-1d99-4611-9c36-4c0fd14f4575" />
<img width="936" height="855" alt="image" src="https://github.com/user-attachments/assets/896209b2-967c-4ce0-ba0e-fe0aadb1cc20" />
<img width="783" height="592" alt="image" src="https://github.com/user-attachments/assets/6552d3ca-10bd-46c3-9a55-2d34ffb94fcb" />
<img width="1223" height="319" alt="image" src="https://github.com/user-attachments/assets/12a4e2b8-5559-46b0-9bab-e11e582f2f87" />
<img width="1307" height="765" alt="image" src="https://github.com/user-attachments/assets/5795f3f2-f939-4d02-ba58-aef2c79ea897" />
</details>

| Test ID | Card | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 083 | 4242 with incorrect CVC format | Validate card details on the client side | Stripe Elements displays an inline validation error while the user enters card details | PASS | Incomplete CVC produced an immediate inline "security code is incomplete" error from Stripe Elements without any server contact; the element also blocks non-numeric input, and submission is refused while the error stands |
<details>
<summary>📸 Evidence for 083 (click to expand)</summary>
<img width="903" height="370" alt="image" src="https://github.com/user-attachments/assets/06c64afc-574d-4b6e-89d9-4dd12f5f8c32" />
<img width="910" height="484" alt="image" src="https://github.com/user-attachments/assets/a472d850-977d-4fc0-80e5-8ff91f49c3b4" />
<img width="892" height="853" alt="image" src="https://github.com/user-attachments/assets/7009a611-96e1-42fa-b96e-67308cac74b5" />
</details>

| Test ID | Card | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 084 | — | Prevent duplicate form submission | Submit button and Stripe card element disabled while payment is being processed | PASS | Submit button and card element disabled for the duration of payment processing - repeat clicks during processing had no effect and exactly one order was created; captured on video |

<details>
<summary>📸 Evidence for 084 (click to expand)</summary>
<video src="https://github.com/user-attachments/assets/71049d10-2d58-4f83-962d-7e70a038535f" controls width="700"></video>
</details>

#### 3.2 Stripe Webhook

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 085 | Receive webhook events on the local endpoint (Stripe CLI) | `stripe trigger payment_intent.succeeded` successfully delivered; server logs `POST /orders/wh/ 200` | PASS | Verified live: stripe listen forwarded all four triggered events (payment_intent.created/succeeded, charge.succeeded/updated) to the local endpoint with [200] responses, matched by POST /orders/wh/ 200 in the dev server log. Setup surfaced two real issues along the way: the CLI's cached pre-rotation API key had expired (refreshed via stripe login), and a stray leading character in the local signing secret caused signature-verification 400s until diagnosed by checking the loaded value's length |

<details>
<summary>📸 Evidence for 085 (click to expand)</summary>
<img width="1110" height="176" alt="image" src="https://github.com/user-attachments/assets/2180f88e-ae7b-4896-93c2-d1e142535375" />
<img width="1091" height="366" alt="image" src="https://github.com/user-attachments/assets/7f516bf3-6301-41a4-94d4-d7a71a72f436" />
<img width="1108" height="337" alt="image" src="https://github.com/user-attachments/assets/9fa98b10-b87f-4b86-83f2-980a40c9c735" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 086 | Receive webhook events on the production endpoint (Heroku) | Stripe Workbench records successful event delivery (HTTP 200) following a live test checkout | PASS | Stripe Workbench's delivery log shows 200 OK for payment_intent.succeeded events from live test checkouts, corroborated by Heroku router logs recording the matching POST /orders/wh/ 200 requests |

<details>
<summary>📸 Evidence for 086 (click to expand)</summary>
<img width="943" height="728" alt="image" src="https://github.com/user-attachments/assets/9d5768f4-5b7a-4ace-baa3-5f4bcca69134" />
<img width="783" height="286" alt="image" src="https://github.com/user-attachments/assets/b25ff889-8672-4285-9959-7711b297eb2d" />
<img width="892" height="607" alt="image" src="https://github.com/user-attachments/assets/ce090d3e-570d-4863-8ad8-14082b2ef69a" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 087 | Verify webhook idempotency | Replayed webhook event does not create a duplicate order | PASS | Automated: `test_duplicate_event_is_idempotent` — replayed a real production payment_intent.succeeded event (£92.96 order) via Workbench's manual Resend; the redelivery returned 200, and a production shell query confirmed the order count for that PaymentIntent remained exactly one. The proof is the database count rather than the response code, since the handler correctly acknowledges replays with 200 |

<details>
<summary>📸 Evidence for 087 (click to expand)</summary>
<img width="928" height="517" alt="image" src="https://github.com/user-attachments/assets/15899f7b-2978-470f-8b9d-55413d98c0f2" />
<img width="920" height="283" alt="image" src="https://github.com/user-attachments/assets/37360d5d-89ba-43ca-84de-f32a925894ac" />
<img width="351" height="614" alt="image" src="https://github.com/user-attachments/assets/01319902-0b02-441f-9f83-18ae9130ac69" />
<img width="1851" height="484" alt="image" src="https://github.com/user-attachments/assets/597b658b-e457-4b94-acf4-7015cd0a2a75" />
<img width="897" height="538" alt="image" src="https://github.com/user-attachments/assets/393bce56-c212-4c55-af9e-f4c08efd0bf6" />
<img width="321" height="630" alt="image" src="https://github.com/user-attachments/assets/270280d4-e469-4d5f-ae4c-c617b80b1c39" />
<img width="1096" height="201" alt="image" src="https://github.com/user-attachments/assets/ebed3d2a-7954-40cc-a8cf-f430f2a9d89c" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 088 | Skip webhook processing when checkout has already created the order | Existing order retained; duplicate order not created; stock deducted only once | PASS | Automated: `test_webhook_skips_when_order_already_exists` — fresh live purchase: checkout created the single order with its PaymentIntent id recorded, the subsequent webhook delivery arrived and returned 200 having skipped creation (Heroku logs show the Stripe POST), and stock reduced exactly once with no double deduction |

<details>
<summary>📸 Evidence for 088 (click to expand)</summary>
<img width="683" height="652" alt="image" src="https://github.com/user-attachments/assets/d3e71d6e-3f6e-4532-adf8-682843071e79" />
<img width="255" height="377" alt="image" src="https://github.com/user-attachments/assets/81738aa3-ac35-4cff-9043-1db8c94e9acc" />
<img width="1061" height="394" alt="image" src="https://github.com/user-attachments/assets/24fff891-c7b9-4557-9b7a-2f1bf3972596" />
<img width="1069" height="907" alt="image" src="https://github.com/user-attachments/assets/21f6bb2b-7268-467f-b828-c05517813350" />
<img width="1489" height="994" alt="image" src="https://github.com/user-attachments/assets/8f957b63-ed09-4204-8ca2-03e900af4c13" />
<img width="1113" height="417" alt="image" src="https://github.com/user-attachments/assets/147ca650-c6f2-4902-b821-d3990a4217cb" />
<img width="1618" height="606" alt="image" src="https://github.com/user-attachments/assets/cfaa4c4e-2286-4dc4-ad2b-168969f449f8" />
<img width="1032" height="319" alt="image" src="https://github.com/user-attachments/assets/a425b58f-4a3a-4639-b65e-fd7c12378832" />
<img width="1351" height="759" alt="image" src="https://github.com/user-attachments/assets/fb9e35c7-fc4d-4170-ad3d-ae66bb2ce6e3" />
<img width="736" height="643" alt="image" src="https://github.com/user-attachments/assets/051c6e3e-db1b-4445-a9bc-a9e65422dada" />
<img width="1185" height="531" alt="image" src="https://github.com/user-attachments/assets/3aeb23e9-bdf3-4870-9321-a12aebd45694" />
<img width="445" height="732" alt="image" src="https://github.com/user-attachments/assets/31f2e7cd-93d4-450b-b164-c3fb0847e398" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 089 | Create an order when checkout does not complete | Order reconstructed from `PaymentIntent` metadata with accurate details and correct stock deduction | PASS | Automated: `orders.test_webhooks.PaymentIntentWebhookTests.test_valid_event_creates_order` passed successfully. Verified individually and as part of the full automated test suite (94 tests passed). Demonstrates that the webhook reconstructs the order from the `PaymentIntent` metadata without relying on the checkout success page. |

<details>
<summary>📸 Evidence for 089 (click to expand)</summary>
<img width="1640" height="533" alt="image" src="https://github.com/user-attachments/assets/d02e5d1d-a193-4588-b162-0cf98cb7f28b" />
<img width="222" height="373" alt="image" src="https://github.com/user-attachments/assets/c236a18c-ffbc-4848-9828-df985c33ab4f" />
<img width="939" height="750" alt="image" src="https://github.com/user-attachments/assets/05c97979-2458-47f0-9f94-7c142b898f93" />
<img width="928" height="793" alt="image" src="https://github.com/user-attachments/assets/011a6c33-3624-475c-9d5c-0f17960890c2" />
<img width="923" height="940" alt="image" src="https://github.com/user-attachments/assets/7e92a6f0-af37-4132-937c-ca900c30f93e" />
<img width="718" height="676" alt="image" src="https://github.com/user-attachments/assets/814d463a-aed0-4b59-a99e-5105d9942e94" />
<img width="1202" height="421" alt="image" src="https://github.com/user-attachments/assets/73272bbe-25fd-4b39-a64a-9fa268f62ee8" />
<img width="1197" height="307" alt="image" src="https://github.com/user-attachments/assets/19569cf3-b023-448d-846e-2b08c702de26" />
<img width="1311" height="747" alt="image" src="https://github.com/user-attachments/assets/60f4f055-2c99-4983-9cfa-e826e371710f" />
<img width="1591" height="478" alt="image" src="https://github.com/user-attachments/assets/bd13107e-d256-429d-9c08-9ff214ba5b75" />
<img width="930" height="429" alt="image" src="https://github.com/user-attachments/assets/4919b524-32cc-4327-84ac-6c1fa3682c87" />
<img width="1164" height="428" alt="image" src="https://github.com/user-attachments/assets/756f13e2-b4ff-4ea5-bdc5-620cde88bc37" />
<img width="1107" height="256" alt="image" src="https://github.com/user-attachments/assets/11f9ebdb-3040-4d99-be35-5062efd7e94d" />
<img width="1243" height="748" alt="image" src="https://github.com/user-attachments/assets/b57f9088-2c0c-47db-868f-d8881594c4e4" />
<img width="1242" height="622" alt="image" src="https://github.com/user-attachments/assets/8ca7f0e2-07d7-4ed1-8cbb-f82d702342fc" />
</details>

#### 3.3 Email Integration

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 090 | Deliver order confirmation email in production | Confirmation email successfully received by the customer | PASS | Manual: Production purchase completed successfully with Gmail App Password configured. Confirmation email received immediately after payment with the correct order details and delivery information. |

<details>
<summary>📸 Evidence for 090 (click to expand)</summary>
<img width="1246" height="502" alt="image" src="https://github.com/user-attachments/assets/9cf6b085-8ccc-4e07-a441-ed0f27dbfe71" />
<img width="1049" height="923" alt="image" src="https://github.com/user-attachments/assets/e9104c31-30c5-481c-9284-fa64f4a1ccff" />
<img width="944" height="922" alt="image" src="https://github.com/user-attachments/assets/6c8a255c-486e-41d1-a97c-a24d078f4adc" />
<img width="702" height="931" alt="image" src="https://github.com/user-attachments/assets/6be8c31a-2491-46e2-9f1c-fc17c1dcebc0" />
<img width="669" height="719" alt="image" src="https://github.com/user-attachments/assets/dd400f66-8836-4f22-8b70-9e033b4b04fd" />
<img width="1135" height="310" alt="image" src="https://github.com/user-attachments/assets/4feafb53-93f8-43e7-a1eb-3318bbe7c525" />
<img width="1305" height="770" alt="image" src="https://github.com/user-attachments/assets/a480e8f7-b1b2-4d13-aebc-c38ed6ea1d4b" />
<img width="926" height="357" alt="image" src="https://github.com/user-attachments/assets/49d12f93-e3b2-4ad7-a5f3-5a687a75f1c0" />
<img width="766" height="345" alt="image" src="https://github.com/user-attachments/assets/82791271-d4d1-4741-a62d-c8796e4cb2ab" />
<img width="1397" height="328" alt="image" src="https://github.com/user-attachments/assets/cb923f6b-3012-4e20-bada-bca8253db789" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 091 | Handle email delivery failure gracefully | Confirmation page continues to render even if email delivery fails; error recorded in the logs | PASS | Verified locally with the SMTP backend temporarily forced on and a deliberately broken password: the success page returned HTTP 200 while the email failure was logged with the order number and full SMTPSenderRefused traceback. The manual test initially revealed failures were silently swallowed by fail_silently=True - fixed in 9f0511e so errors are now caught and logged, preserving the D9 page-render guarantee. The fix is deployed to production; the failure simulation was kept local by design |

<details>
<summary>📸 Evidence for 091 (click to expand)</summary>
<img width="1065" height="402" alt="image" src="https://github.com/user-attachments/assets/2816e846-73db-418d-98b5-ba967ab9433e" />
<img width="1030" height="936" alt="image" src="https://github.com/user-attachments/assets/f65c1274-984d-4a17-8575-ccdbf17e1106" />
<img width="1005" height="877" alt="image" src="https://github.com/user-attachments/assets/c97794d3-c6fc-4196-930a-dc6219ce82e3" />
<img width="1337" height="558" alt="image" src="https://github.com/user-attachments/assets/1c0f9616-29dd-4a74-85a6-624e8ad1b990" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 092 | Verify account verification and password reset emails | Emails delivered successfully and links operate correctly | PASS | Both flows verified on production: verification email received for a new registration with a working confirmation link, and password reset email received with a working reset link. The test surfaced a stale Sites-framework domain (the pre-rename Heroku URL) in email footers; the production Site record was corrected, and intermittent recurrence was traced to Django's per-worker Site cache serving pre-fix values - resolved with a dyno restart, after which repeated fresh emails were consistent |

<details>
<summary>📸 Evidence for 092 (click to expand)</summary>
<img width="1004" height="809" alt="image" src="https://github.com/user-attachments/assets/93d9489b-02af-4731-a393-54c251209312" />
<img width="1070" height="513" alt="image" src="https://github.com/user-attachments/assets/cb255584-03e1-49ce-ae3d-0903a81769fa" />
<img width="1856" height="478" alt="image" src="https://github.com/user-attachments/assets/f830c082-3666-45d3-86b4-55d45919658b" />
<img width="1428" height="408" alt="image" src="https://github.com/user-attachments/assets/eced146e-e06d-4955-bddb-ddc87f07fc78" />
<img width="1314" height="530" alt="image" src="https://github.com/user-attachments/assets/369cefbe-76fe-4237-8fa6-4d767bf7c0ec" />
<img width="1354" height="761" alt="image" src="https://github.com/user-attachments/assets/e1b03384-6ecb-414e-b305-602214e33eab" />
<img width="1330" height="789" alt="image" src="https://github.com/user-attachments/assets/7969ab0f-d592-43ae-b443-44d0796434b1" />
<img width="1325" height="779" alt="image" src="https://github.com/user-attachments/assets/270e9d4c-bdbf-4148-8ae1-5d394ccf7b94" />
<img width="1339" height="925" alt="image" src="https://github.com/user-attachments/assets/acc20820-2073-4900-a03e-82535be0a8cb" />
<img width="1359" height="656" alt="image" src="https://github.com/user-attachments/assets/194d05c5-4b54-41f7-b725-2f28e3a67b93" />
<img width="1388" height="450" alt="image" src="https://github.com/user-attachments/assets/f1eb8eb3-cd7a-4d5f-9190-7333e22336aa" />
<img width="1433" height="584" alt="image" src="https://github.com/user-attachments/assets/396ce9c4-1af5-4d61-98fc-7a854426d067" />
<img width="1853" height="287" alt="image" src="https://github.com/user-attachments/assets/f2a9fa8a-dad1-4e64-ae76-91b941d15901" />
<img width="825" height="285" alt="image" src="https://github.com/user-attachments/assets/2d325a66-cd22-424f-8909-0c74bc398bad" />
</details>

---

#### 4. USABILITY AND TYPOGRAPHY TESTING

[⬆ Back to Table of Contents](#table-of-contents)

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 093 | Verify consistent navigation across the website | Navigation links function correctly; active page indicators are visible; basket counter updates accurately | PASS | Navigation verified across all three auth states (logged out, member, staff): links function correctly and the active page indicator reflects the current section |

<details>
<summary>📸 Evidence for 093 - Logged out</summary>
<video src="https://github.com/user-attachments/assets/2d0a0419-7e32-48af-a7a3-462c216e2cc1" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 093 - Logged in as member</summary>
<video src="https://github.com/user-attachments/assets/c400db5e-1973-45d8-8d02-8d449254b3b8" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 093 - Logged in as staff</summary>
<video src="https://github.com/user-attachments/assets/25631ab3-81c4-4f97-8e28-433167911d97" controls width="700"></video>
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 094 | Confirm breadcrumb navigation on secondary pages | Shop, checkout, order confirmation, order history and management pages display accurate breadcrumb trails | PASS | Breadcrumbs verified on secondary pages (product detail, checkout, order confirmation, order history and plan management) with accurate trails and working parent links; management pages checked as staff. Correctly absent from top-level pages (Home, Plans, Shop listings) where no hierarchy exists to trace |

<details>
<summary>📸 Evidence for 094 (click to expand)</summary>
<img width="592" height="435" alt="image" src="https://github.com/user-attachments/assets/563bef36-63f7-4769-8108-e7245a6c9531" />
<img width="588" height="445" alt="image" src="https://github.com/user-attachments/assets/223ec79d-f212-471e-8ef1-c1b9eb41f434" />
<img width="607" height="554" alt="image" src="https://github.com/user-attachments/assets/cc69be5f-97c1-4d05-8863-b9a23c613a7a" />
<img width="578" height="442" alt="image" src="https://github.com/user-attachments/assets/9bc247c4-9f6f-42d4-9e1f-1eccaf2a0482" />
<img width="1016" height="511" alt="image" src="https://github.com/user-attachments/assets/15a72582-5531-4689-987c-74c05e5e9d3f" />
<img width="1015" height="517" alt="image" src="https://github.com/user-attachments/assets/68ca0264-39ef-43c1-9cfe-9c3895771200" />
<img width="1029" height="514" alt="image" src="https://github.com/user-attachments/assets/515967b8-2871-46a9-b26a-e038935bebd2" />
<img width="1083" height="553" alt="image" src="https://github.com/user-attachments/assets/cfc7181a-a6c0-4266-a7a2-216d911670d5" />
<img width="1175" height="516" alt="image" src="https://github.com/user-attachments/assets/93c88d75-9baf-4e06-ad58-03df19c8424a" />
<img width="1022" height="522" alt="image" src="https://github.com/user-attachments/assets/eca809b0-75c3-4e49-8d84-441f987b2a45" />
<img width="1017" height="519" alt="image" src="https://github.com/user-attachments/assets/0f526254-a591-4614-9b2f-462d65f77601" />
<img width="1068" height="534" alt="image" src="https://github.com/user-attachments/assets/0a176777-0f1e-4df7-8cb7-6beef5e8f3c1" />
<img width="1064" height="550" alt="image" src="https://github.com/user-attachments/assets/ab68d8db-7d85-4097-8d26-90166b0577b2" />
<img width="1078" height="577" alt="image" src="https://github.com/user-attachments/assets/ef9c5291-7d4e-485c-964b-134d9269daa2" />
<img width="1039" height="536" alt="image" src="https://github.com/user-attachments/assets/26559b38-5ad6-4f2d-a725-384feedc792f" />
<img width="1018" height="528" alt="image" src="https://github.com/user-attachments/assets/a0d7ac48-2d8c-4deb-9c6a-10f83bb3c13a" />
<img width="1023" height="292" alt="image" src="https://github.com/user-attachments/assets/18ee027b-b1cc-4ef4-b545-409cd67b6742" />
<img width="1032" height="446" alt="image" src="https://github.com/user-attachments/assets/816b821a-d7d4-4f87-91fb-7def8b168399" />
<img width="1030" height="690" alt="image" src="https://github.com/user-attachments/assets/1ac49aff-9915-4398-943e-9b7e5bb14312" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 095 | Display user feedback for all key actions | Visible feedback messages shown for adding, updating or removing basket items, placing orders, saving or archiving plans, and authentication errors | PASS | Django messages verified across all key actions: basket add/update/remove, order placement, plan save and archive, and authentication errors (failed login) each display a visible, consistently styled feedback banner |

<details>
<summary>📸 Evidence for 095 (click to expand)</summary>
<img width="1021" height="133" alt="image" src="https://github.com/user-attachments/assets/d256189c-b5f6-4a2e-ad8f-c532f6e63a3e" />
<img width="1021" height="366" alt="image" src="https://github.com/user-attachments/assets/1d852586-11c7-4d95-b7b8-9b9b0143beb6" />
<img width="1026" height="918" alt="image" src="https://github.com/user-attachments/assets/7b39aa8c-e17f-49e0-9d78-2798e94a8547" />
<img width="1038" height="182" alt="image" src="https://github.com/user-attachments/assets/a3865a98-c23d-442e-998d-6f523f2dd0cb" />
<img width="1023" height="301" alt="image" src="https://github.com/user-attachments/assets/3dae7fa2-dc95-4602-bf19-2fc638241435" />
<img width="1024" height="130" alt="image" src="https://github.com/user-attachments/assets/5e2f05cb-b20f-4b2e-ae21-ecee6eb2ecdc" />
<img width="886" height="687" alt="image" src="https://github.com/user-attachments/assets/767d77cf-2f72-4573-baeb-9b106ce731e3" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 096 | Verify consistent typographic hierarchy | Each page contains a single H1 heading; heading levels follow the correct sequence; font sizes remain clear and readable | PASS | Heading structure audited via a DevTools console script across eight representative pages (home, shop, plans, community, dashboard, basket, terms, privacy): each has exactly one H1 with heading levels descending in sequence and no skipped levels. Font sizing is consistent and readable throughout via the shared base template |

<details>
<summary>📸 Evidence for 096 (click to expand)</summary>
<img width="1632" height="925" alt="image" src="https://github.com/user-attachments/assets/91e372f0-005f-4dcc-bf76-eb6ef4573048" />
<img width="1621" height="878" alt="image" src="https://github.com/user-attachments/assets/399bf063-67d6-4288-ad7c-72824ed0779e" />
<img width="1613" height="957" alt="image" src="https://github.com/user-attachments/assets/3618efb3-aaca-4fc2-8e5e-bf9d742a9598" />
<img width="1624" height="845" alt="image" src="https://github.com/user-attachments/assets/1abb4c73-330e-4ea6-8c47-8a3d1be27290" />
<img width="1612" height="793" alt="image" src="https://github.com/user-attachments/assets/aa591b48-f3f2-40be-aea6-84f8e2fcb970" />
<img width="1617" height="671" alt="image" src="https://github.com/user-attachments/assets/9c336467-dcff-421b-b279-18aa511c3b1d" />
<img width="1625" height="915" alt="image" src="https://github.com/user-attachments/assets/51c5d9b1-884c-4dce-b6ed-c6ae68e14b56" />
<img width="1605" height="793" alt="image" src="https://github.com/user-attachments/assets/f5618289-d761-4d23-a0f7-71d07c9c09f9" />
<img width="1699" height="796" alt="image" src="https://github.com/user-attachments/assets/6188b365-df18-485c-960d-fc759af638eb" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 097 | Ensure buttons and links use descriptive labels | Generic phrases such as "click here" are avoided; order links identify the specific order (e.g. "View order FH-…") | PASS | Audited buttons and links across the site: no "click here" or similar generic phrasing; order links name the specific order ("View order <number>"). All calls-to-action use descriptive labels (Browse Plans, Shop Now, Add to Basket, etc.). The one borderline "Learn More" homepage link was made self-describing ("Explore the Community") during this test |

<details>
<summary>📸 Evidence for 097 (click to expand)</summary>

**Homepage**

<img width="1018" height="401" alt="image" src="https://github.com/user-attachments/assets/3b058db9-6faf-4692-b3df-69930c1e044c" />
<img width="1004" height="880" alt="image" src="https://github.com/user-attachments/assets/dd8b1ae5-b2e4-404c-a77b-b68e28193239" />
<img width="1060" height="633" alt="image" src="https://github.com/user-attachments/assets/835c9220-1054-4dda-af60-f0c1adc5ceac" />
<img width="1039" height="290" alt="image" src="https://github.com/user-attachments/assets/dd3fc944-7d7e-471e-8d4c-3a8b28bf47ac" />

**Plans**

<img width="997" height="755" alt="image" src="https://github.com/user-attachments/assets/3b60c247-8ab7-4477-b19e-63bb660db99d" />
<img width="1058" height="595" alt="image" src="https://github.com/user-attachments/assets/5fb228b0-d278-48b6-9ac6-a8ea97b44226" />

**Shop**

<img width="1034" height="724" alt="image" src="https://github.com/user-attachments/assets/80466322-a1f2-40e5-aee9-0b15f741e5ad" />
<img width="1058" height="759" alt="image" src="https://github.com/user-attachments/assets/ed70ff67-e64c-4a27-ace9-1a376328c671" />
<img width="1058" height="242" alt="image" src="https://github.com/user-attachments/assets/04087ce8-f0d3-4c52-8d63-7a0ff9e0a06a" />

**Basket**

<img width="1003" height="674" alt="image" src="https://github.com/user-attachments/assets/54d79a77-7127-4e1c-8fb6-2a418108ef79" />

**Manage**

<img width="1035" height="759" alt="image" src="https://github.com/user-attachments/assets/7b9861f0-9cb3-4221-ade1-27f9306b5dbd" />

**Dashboard**

<img width="999" height="930" alt="image" src="https://github.com/user-attachments/assets/06a9963d-54ce-470f-9e94-560ee7aeb691" />
<img width="762" height="520" alt="image" src="https://github.com/user-attachments/assets/75f05f28-d072-4191-b90a-b5b36c219ec9" />
<img width="742" height="217" alt="image" src="https://github.com/user-attachments/assets/3d55fada-10ca-4787-81c2-4b6013f8612f" />
<img width="747" height="365" alt="image" src="https://github.com/user-attachments/assets/955844d7-8ef2-43f6-a064-742c8b211855" />
<img width="731" height="299" alt="image" src="https://github.com/user-attachments/assets/c38ac687-1c06-4a90-96ef-caca42771d52" />

**Sign Out**

<img width="1037" height="471" alt="image" src="https://github.com/user-attachments/assets/112f0e8b-087d-4458-b660-eee5953e1cc0" />

**Login**

<img width="1031" height="840" alt="image" src="https://github.com/user-attachments/assets/d10d0046-ad83-4cdc-a492-122bbbb7d4b4" />

**Register**

<img width="1011" height="817" alt="image" src="https://github.com/user-attachments/assets/ad00a477-6e60-44c2-ab3b-384db0780d96" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 098 | Preserve form data after validation errors | Previously entered values remain populated when a form is redisplayed following validation failures | PASS | Verified that forms redisplay with previously entered values intact after validation errors (checkout delivery details and other multi-field forms), so users needn't re-enter data. Password fields correctly clear on the registration form, as expected for security |

<details>
<summary>📸 Evidence for 098 (click to expand)</summary>
<img width="1046" height="948" alt="image" src="https://github.com/user-attachments/assets/68eb9729-0467-4c3d-9f0a-30d9d01bdac8" />
<img width="699" height="841" alt="image" src="https://github.com/user-attachments/assets/03730722-8485-4883-a501-51462d626fb2" />
<img width="1021" height="882" alt="image" src="https://github.com/user-attachments/assets/bd1560eb-7408-459d-a368-5e248d5c08bb" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 099 | Verify helpful empty-state pages | Empty basket, order history and Manage Plans pages provide clear guidance and an appropriate next action | PASS | All three empty states were verified in earlier rows and each provides a clear message with a working next action: empty basket ("Your basket is empty" + Browse Products, row 031), empty order history ("You haven't placed any orders yet" + Browse the Shop, row 049, also covered by test_history_empty_state), and empty Manage Plans ("No plans yet" + Create your first plan, row 060, verified locally as staging an empty plans table on production would require deleting live subscription data) |


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 100 | Confirm custom 404 page usability | Branded 404 page displayed with a clear navigation route back into the application | PASS | A nonexistent URL on production renders the branded FitHub 404 page (nav and footer intact, not Django's default) with three clear routes back into the app - Back to Home, Browse Plans and Browse Products - all functional. Custom 404 templates render only under DEBUG=False, so this reflects production behaviour |

<details>
<summary>📸 Evidence for 100 (click to expand)</summary>
<img width="1620" height="601" alt="image" src="https://github.com/user-attachments/assets/4a50d512-8923-4c36-89bd-83d260b80f16" />
</details>


---

#### 5. RESPONSIVENESS TESTING

[⬆ Back to Table of Contents](#table-of-contents)

The following pages were tested across each responsive breakpoint: Home, Plans, Plan Detail, Shop, Product Detail, Basket, Checkout, Order Confirmation, Order History, Dashboard and Manage Plans.

| Test ID | Breakpoint | Test Case | Expected Result | Status | Notes |
|---------|------------|-----------|-----------------|--------|-------|
| 101 | Mobile (375×667) | Verify all pages display correctly without horizontal scrolling | Content stacks appropriately; navigation collapses into a hamburger menu; touch targets remain suitably sized | PASS | Pages verified at mobile width in both portrait (375×667) and landscape (667×375): content stacks into a single column, navigation collapses into a working hamburger menu, touch targets are suitably sized, and no page exhibits horizontal scrolling |

<details>
<summary>📸 Evidence for 101 - Mobile (375×667)</summary>
<video src="https://github.com/user-attachments/assets/690f8073-af32-40c6-8278-9cc21ba143a5" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 101 - Mobile (667x375)</summary>
<video src="https://github.com/user-attachments/assets/6593901c-970a-405a-b63d-d916e3ef74f0" controls width="700"></video>
</details>

| Test ID | Breakpoint | Test Case | Expected Result | Status | Notes |
|---------|------------|-----------|-----------------|--------|-------|
| 102 | Mobile | Confirm checkout functionality on small screens | Delivery form fields display in a single column; order summary remains accessible; Stripe payment element functions correctly | PASS | At mobile width (375×667) the delivery form displays in a single column, the order summary remains accessible, and the Stripe card element renders and accepts input - a full 4242 test payment completed through to the confirmation page. Captured on video |

<details>
<summary>📸 Evidence for 102 - Form fill (375×667)</summary>
<video src="https://github.com/user-attachments/assets/b0773dde-1e66-4b1d-8fd7-860c4f5f46d4" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 102 - Purchase confirmation (375x667)</summary>
<video src="https://github.com/user-attachments/assets/ce0acf48-e98f-4aca-a3ff-42fc4e549fab" controls width="700"></video>
</details>

| Test ID | Breakpoint | Test Case | Expected Result | Status | Notes |
|---------|------------|-----------|-----------------|--------|-------|
| 103 | Tablet (768×1024) | Verify responsive layout across all pages | Intended two-column layouts displayed correctly; tables either reflow or provide horizontal scrolling where necessary | PASS | Pages verified at tablet width (768×1024): two-column layouts render correctly and tabular data (order history, plan management) remains usable without forcing whole-page horizontal scrolling. Captured on video |

<details>
<summary>📸 Evidence for 103 (768x1024)</summary>
<video src="https://github.com/user-attachments/assets/a03a2b9c-a4a3-4459-aab9-cdf99742630f" controls width="700"></video>
</details>

| Test ID | Breakpoint | Test Case | Expected Result | Status | Notes |
|---------|------------|-----------|-----------------|--------|-------|
| 104 | Desktop (1920×1080) | Confirm efficient use of available screen width | Grid layouts display the maximum number of columns; checkout page retains a sticky order summary | PASS | At desktop width (1920×1080) grid layouts display their maximum number of columns, using the full screen width efficiently, and the checkout page's order summary remains sticky - staying visible while the delivery form scrolls. Captured on video |

<details>
<summary>📸 Evidence for 104 - PT 1 (1920×1080)</summary>
<video src="https://github.com/user-attachments/assets/a57a2ed2-4187-4a12-a883-1eb0bb13ac66" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 104 - PT 2 (1920x1080)</summary>
<video src="https://github.com/user-attachments/assets/463f32d4-8637-4243-ae29-b5a7b3ae4a42" controls width="700"></video>
</details>

| Test ID | Breakpoint | Test Case | Expected Result | Status | Notes |
|---------|------------|-----------|-----------------|--------|-------|
| 105 | Small screens | Verify usability of order-related tables | Order History and Manage Plans tables remain fully accessible using horizontal scrolling within a responsive table container (`table-responsive`) | PASS | Both the Order History and Manage Plans tables are wrapped in Bootstrap's table-responsive container; at 375px each table scrolls horizontally within its own area (swipe/drag left-right) to reveal all columns while the page itself does not scroll sideways. Captured on video |

<details>
<summary>📸 Evidence for 105 (375x667)</summary>
<video src="https://github.com/user-attachments/assets/b7f87834-466e-4018-b58f-11d93fdb2472" controls width="700"></video>
</details>

---

#### 6. ACCESSIBILITY TESTING

[⬆ Back to Table of Contents](#table-of-contents)

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 106 | Verify all form controls have associated labels | Every input field is linked to a `<label for>` element and all mandatory fields are clearly identified | PASS | WAVE audit of the site's forms: checkout, community and auth forms all showed 0 missing-form-label errors with form-label features on each field. The review add/edit forms were found to have orphaned labels (present but not bound via `for`) - fixed by binding each label to its field id, then re-verified with WAVE showing the alerts cleared. Mandatory fields are marked with a red asterisk |

<details>
<summary>📸 Evidence for 106</summary>
<img width="1393" height="819" alt="image" src="https://github.com/user-attachments/assets/e01d9b4e-8cf3-4084-8efc-54228e3dfe8a" />
<img width="1837" height="977" alt="image" src="https://github.com/user-attachments/assets/5451f44e-9b1a-4c97-90fd-2e58eaff017b" />
<img width="1633" height="946" alt="image" src="https://github.com/user-attachments/assets/0c90af3b-07e8-419f-9b69-ae2be1536f80" />
<img width="1787" height="968" alt="image" src="https://github.com/user-attachments/assets/f05beb48-21b4-49ee-ab70-73d17a4ed1a8" />
<img width="1586" height="973" alt="image" src="https://github.com/user-attachments/assets/a8dbad03-ff20-4c43-a846-2deb4a290717" />
<img width="1623" height="793" alt="image" src="https://github.com/user-attachments/assets/f7610a03-e7da-48f9-95d4-de7550a9a60d" />
<img width="1687" height="981" alt="image" src="https://github.com/user-attachments/assets/94607b70-773e-4ae5-bcd4-d9b5ef50520d" />
<img width="1696" height="772" alt="image" src="https://github.com/user-attachments/assets/adb8ca2a-9f35-450a-9514-900bf9cbc967" />
<img width="1663" height="880" alt="image" src="https://github.com/user-attachments/assets/e644f3ca-6519-49a4-9caf-5a8f8db2f21f" />
<img width="1696" height="795" alt="image" src="https://github.com/user-attachments/assets/f7bf9489-b450-47de-a1bd-e2a9df956eae" />
<img width="1598" height="980" alt="image" src="https://github.com/user-attachments/assets/60f1da1f-ce6f-419d-a2e5-b7ab1c55fe1c" />
<img width="1602" height="987" alt="image" src="https://github.com/user-attachments/assets/57ebafcd-5d7e-4b66-a84d-14311abd9fd9" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 107 | Confirm validation errors are communicated in text | Error messages displayed as text rather than relying solely on colour; error summary visible | PASS | Validation errors render as text, not colour alone: an error summary alert (role="alert") appears at the top of the form when errors occur, and each field shows a specific text message. Demonstrated by evidence from tests 036 (incomplete checkout form — error summary and field-level text messages), 037 (invalid email — "Enter a valid email address.") and 083 (Stripe card field — inline text validation). Colour is used only as an additional cue |

<details>
<summary>📸 Evidence for 107</summary>
<img width="991" height="864" alt="image" src="https://github.com/user-attachments/assets/9422b19e-b910-4f87-b84e-acc38f651639" />
<img width="978" height="850" alt="image" src="https://github.com/user-attachments/assets/30ce7fff-277a-4e91-9f0f-08b789b820b2" />
<img width="991" height="848" alt="image" src="https://github.com/user-attachments/assets/bf74fea9-ed24-4c17-8075-45dbef96d520" />
<img width="1017" height="852" alt="image" src="https://github.com/user-attachments/assets/8a557c8e-f517-48a4-ba9e-1f32f42e3ba6" />
<img width="1007" height="853" alt="image" src="https://github.com/user-attachments/assets/b2fce4dd-de82-444d-b8a2-77f278cca3b4" />
<img width="1008" height="839" alt="image" src="https://github.com/user-attachments/assets/29703d43-4727-4cc7-b76b-750e8a4895a8" />
<video src="https://github.com/user-attachments/assets/71049d10-2d58-4f83-962d-7e70a038535f" controls width="700"></video>
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 108 | Verify status information is communicated using text and colour | Order and plan status badges include descriptive text instead of colour-only indicators | PASS | All status badges carry descriptive text alongside colour: order badges (Processing, Dispatched, Delivered, Cancelled, Refunded) and plan badges (Published, Draft, Archived) each render the status word inside the coloured badge, so status is never conveyed by colour alone |

<details>
<summary>📸 Evidence for 108</summary>
<img width="1107" height="705" alt="image" src="https://github.com/user-attachments/assets/83c92ed3-4884-42c2-98dd-8db2ac283f1a" />
<img width="1043" height="528" alt="image" src="https://github.com/user-attachments/assets/2eae492c-5d7e-4a5c-82d9-38f093722a90" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 109 | Confirm images include alternative text | Product and membership plan images contain meaningful `alt` attributes | PASS | Product and plan images render a meaningful alt attribute tied to the item name (e.g. alt="Yoga Mat", alt="Elite"), including related-item thumbnails and the plans hero image ("FitHub members training together"). WAVE reported no missing-alternative-text errors on the shop and plans pages |

<details>
<summary>📸 Evidence for 109</summary>
<img width="1560" height="809" alt="image" src="https://github.com/user-attachments/assets/c521a406-bc15-4700-a274-7974ea5981c8" />
<img width="1567" height="977" alt="image" src="https://github.com/user-attachments/assets/1978b9e2-3196-471f-bf79-84c0d3718884" />
<img width="1028" height="774" alt="image" src="https://github.com/user-attachments/assets/019857bd-b854-4940-a282-505c832baf9f" />
<img width="1776" height="712" alt="image" src="https://github.com/user-attachments/assets/78ed038f-1bda-4ebe-b9b8-c52046c0fc0f" />
<img width="1526" height="915" alt="image" src="https://github.com/user-attachments/assets/66b54699-dcf3-4d55-864f-8c43e623cf83" />
<img width="933" height="814" alt="image" src="https://github.com/user-attachments/assets/250d355c-e6f1-4165-afb5-12ac4d75fdc1" />
<img width="1577" height="978" alt="image" src="https://github.com/user-attachments/assets/2c556469-73f7-4516-beb4-500850ef78d9" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 110 | Verify keyboard accessibility | All interactive elements can be reached and operated using only the keyboard; skip-to-content link functions correctly | PASS | All interactive elements (nav, buttons, form fields including the Stripe card element) are reachable and operable by keyboard with a visible focus indicator, verified across the site. The skip-to-content link — found broken in rows 106-109 (pointed at a non-existent target) and fixed by adding a `<main id="main-content">` landmark — now appears on Tab and jumps focus to the main content; WAVE confirms 0 errors with both "Skip link" and "Skip link target" detected |

<details>
<summary>📸 Evidence for 110 - WAV Screenshots</summary>
<img width="1649" height="989" alt="image" src="https://github.com/user-attachments/assets/6276860b-1597-4b8a-a3a8-b43a0de7bd93" />
<img width="972" height="976" alt="image" src="https://github.com/user-attachments/assets/3771480d-0a34-4d54-84e0-d23eebadc9b3" />
<img width="1864" height="986" alt="image" src="https://github.com/user-attachments/assets/b6c63ee2-0808-451c-87f5-e2bec7341d49" />
<img width="1866" height="950" alt="image" src="https://github.com/user-attachments/assets/36311d51-abda-4933-af16-f9b6583c14fc" />
<img width="1585" height="985" alt="image" src="https://github.com/user-attachments/assets/25a6ad47-6966-4773-9710-9544855977c4" />
<img width="1882" height="985" alt="image" src="https://github.com/user-attachments/assets/c6ad6855-983d-455f-a02f-4ae1738dbc39" />
<img width="1593" height="1010" alt="image" src="https://github.com/user-attachments/assets/7ee98439-2371-4887-8029-63de12b41130" />
<img width="1869" height="981" alt="image" src="https://github.com/user-attachments/assets/696441d9-31c0-4627-8676-5ea4ce818acd" />
<img width="1633" height="1006" alt="image" src="https://github.com/user-attachments/assets/01c7db05-0925-48fb-9f64-d334c5b60745" />
<img width="1884" height="981" alt="image" src="https://github.com/user-attachments/assets/82ed3b32-277b-41ea-bc53-e65cf829e5dc" />
<img width="1678" height="960" alt="image" src="https://github.com/user-attachments/assets/a7158072-bc8d-4c4b-a72c-559055a8efac" />
<img width="1831" height="966" alt="image" src="https://github.com/user-attachments/assets/1c5b37dc-175b-466f-bef2-f12ffd68d556" />
<img width="1689" height="976" alt="image" src="https://github.com/user-attachments/assets/3dec45f2-9679-4c8d-a19a-e44eebfcc469" />
<img width="1681" height="1020" alt="image" src="https://github.com/user-attachments/assets/8ba936bb-4042-4888-9149-de3c810bd424" />
<img width="1703" height="1010" alt="image" src="https://github.com/user-attachments/assets/0c13b700-96a3-4e08-96bd-faac5cf71503" />
<img width="1659" height="976" alt="image" src="https://github.com/user-attachments/assets/0625f9bf-ef63-47a8-801c-063fa8ff1395" />
</details>

<details>
<summary>📸 Evidence for 110 - PT 1</summary>
<video src="https://github.com/user-attachments/assets/f112aeba-c208-4acd-907c-de4d9d2fd180" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 2</summary>
<video src="https://github.com/user-attachments/assets/ee5f610f-d493-4a1b-bfc4-f606295fa530" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 3</summary>
<video src="https://github.com/user-attachments/assets/aa019dca-9ef8-4054-b6d4-9a7a7ecf7559" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 4</summary>
<video src="https://github.com/user-attachments/assets/165079c1-c0f2-4a66-9ab8-d88fa7a2efd0" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 5</summary>
<video src="https://github.com/user-attachments/assets/dd89b2d0-6cbc-4d35-b609-cde287e05508" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 6</summary>
<video src="https://github.com/user-attachments/assets/142f1c8e-9afd-47d2-b1f6-fa9f15750af2" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 7</summary>
<video src="https://github.com/user-attachments/assets/b07dd4ac-4e5a-40f4-9757-3c6e86c9c291" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 8</summary>
<video src="https://github.com/user-attachments/assets/199b8acd-8f83-4e9a-b4ba-4283800c63ee" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 9</summary>
<video src="https://github.com/user-attachments/assets/2171928d-0a78-44c6-b178-95f38a99811a" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 10</summary>
<video src="https://github.com/user-attachments/assets/f0ea87f3-131f-445f-9a81-1d67716f98c6" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 11</summary>
<video src="https://github.com/user-attachments/assets/b6b08797-3df8-4370-8f54-d2dfc22d2c37" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 12</summary>
<video src="https://github.com/user-attachments/assets/7b2cdccc-ce37-4b61-a33a-2ab4f420c10c" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 13</summary>
<video src="https://github.com/user-attachments/assets/b68901fa-a4db-4626-82a8-f7c559bcc6c8" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 14</summary>
<video src="https://github.com/user-attachments/assets/b20400ad-629d-40a9-bc18-81870e21a20f" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 15</summary>
<video src="https://github.com/user-attachments/assets/22e399b9-fdb3-4bf3-b153-cd200505707d" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 16</summary>
<video src="https://github.com/user-attachments/assets/8411ea48-03f5-4763-9313-4285e2fe47b4" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 17</summary>
<video src="https://github.com/user-attachments/assets/15257678-f7e9-4f92-81cd-72a59a3774f7" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 18</summary>
<video src="https://github.com/user-attachments/assets/bf8360a3-c0ff-4425-bbec-eaf395f490cf" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 19</summary>
<video src="https://github.com/user-attachments/assets/21b25c71-2cb6-4e10-8ff1-4a609c71e7fb" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 20</summary>
<video src="https://github.com/user-attachments/assets/4f7e4663-120e-4f74-ac38-aae2a1b8b9c8" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 21</summary>
<video src="https://github.com/user-attachments/assets/a9329a4e-aea9-412c-88ba-1ef0ada988e0" controls width="700"></video>
</details>

<details>
<summary>📸 Evidence for 110 - PT 22</summary>
<video src="https://github.com/user-attachments/assets/19836a8a-57c8-4b26-a717-c9b88983dd37" controls width="700"></video>
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 111 | Verify `aria-live` region on the order confirmation page | Confirmation heading is announced correctly by screen readers | PASS | The confirmation heading is wrapped in a region marked `aria-live="polite"` (confirmed in the rendered DOM), so its content is announced by screen readers when the page loads without interrupting. WAVE detects the live region as an ARIA feature on the confirmation page |

<details>
<summary>📸 Evidence for 111</summary>
<img width="1561" height="884" alt="image" src="https://github.com/user-attachments/assets/a56c7ec4-e2aa-4477-a8b4-c5ed6f1503c7" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 112 | Confirm colour contrast complies with WCAG AA | Lighthouse and axe audits report no colour contrast failures | PASS | Lighthouse initially flagged low-contrast muted text (`.text-secondary`/`.text-muted`); fixed by darkening to #565E6C (verified ≥5.9:1) and moving form inputs from low-contrast placeholders to visible labels. Both Lighthouse and WAVE now report 0 contrast errors on checkout, with WAVE scoring 10/10. The one remaining Lighthouse ARIA item is the third-party Stripe iframe, outside application control |

<details>
<summary>📸 Evidence for 112</summary>
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4eb1ac31-03c2-429e-aeb0-fd2bb0f88c18" />
<img width="821" height="742" alt="image" src="https://github.com/user-attachments/assets/7d4d968c-2dbd-4f52-b70f-67157778efe5" />
<img width="1800" height="987" alt="image" src="https://github.com/user-attachments/assets/a8be031a-758f-417c-83ae-ba80afa4ec5b" />
<img width="1548" height="978" alt="image" src="https://github.com/user-attachments/assets/e4324a07-24b6-47aa-a696-750529d0789f" />
<img width="1890" height="896" alt="image" src="https://github.com/user-attachments/assets/2115f4dd-7bdf-4bd7-9f3b-c376c5cdba8a" />
<img width="1678" height="977" alt="image" src="https://github.com/user-attachments/assets/65ec24ec-7348-43bf-9d46-ee55ea84dc33" />
<img width="1880" height="910" alt="image" src="https://github.com/user-attachments/assets/54221781-3b01-4fbd-ab47-2b614466cebc" />
<img width="1871" height="959" alt="image" src="https://github.com/user-attachments/assets/1d21820b-cb97-4d06-913e-24163e5ce0e2" />
<img width="1896" height="971" alt="image" src="https://github.com/user-attachments/assets/eb46857e-0c02-4e08-a8fe-c7239e3c42f9" />
<img width="1879" height="966" alt="image" src="https://github.com/user-attachments/assets/b8b94eaa-43ed-4298-a82e-74bce0ce8f56" />
<img width="1880" height="972" alt="image" src="https://github.com/user-attachments/assets/e8fe257d-0e33-4448-b90e-a0c743aea7e2" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 113 | Perform WAVE accessibility evaluation | No accessibility errors detected on key application pages | PASS | WAVE evaluated across all key pages (home, shop, product detail, plans, plan detail, basket, checkout, dashboard, order history, community, auth and content pages). The sweep surfaced and fixed several real issues along the way: low-contrast muted text and placeholders, low-contrast outline-secondary and outline-danger buttons, an empty table header in the basket totals, and (from rows 106-110) orphaned review labels and a broken skip link. After fixes, all key pages report 0 WAVE errors and 0 contrast errors; remaining items are non-blocking alerts (redundant links, possible headings) |

<details>
<summary>📸 Evidence for 113</summary>
<img width="1589" height="384" alt="image" src="https://github.com/user-attachments/assets/66a1bb1a-420b-4ebd-8cdb-f79f20994bad" />
<img width="1556" height="393" alt="image" src="https://github.com/user-attachments/assets/63350407-6431-4e54-89ce-f361f32e82a9" />
<img width="1508" height="649" alt="image" src="https://github.com/user-attachments/assets/9f8799b9-42f8-4da5-95d3-daf12ff59e85" />
<img width="1526" height="500" alt="image" src="https://github.com/user-attachments/assets/b3fb212b-84a9-4d83-985b-e10862410ee8" />
<img width="1617" height="806" alt="image" src="https://github.com/user-attachments/assets/c2efed99-4c9f-4ea7-9e0f-436db11fbd56" />
<img width="1513" height="535" alt="image" src="https://github.com/user-attachments/assets/1e959e31-5fe4-4123-b4f6-17e059c8d534" />
<img width="1611" height="596" alt="image" src="https://github.com/user-attachments/assets/b22975c0-95cc-4fdc-be1b-58465b1e085b" />
<img width="1561" height="808" alt="image" src="https://github.com/user-attachments/assets/208b9887-9613-4f75-8f2c-3fdb1543e05e" />
<img width="1531" height="830" alt="image" src="https://github.com/user-attachments/assets/c38cad14-6177-4039-b6b1-d592fbe07e60" />
<img width="1653" height="725" alt="image" src="https://github.com/user-attachments/assets/66376b02-40f1-4cdb-b540-d25af4623f98" />
<img width="1556" height="660" alt="image" src="https://github.com/user-attachments/assets/9a1ffc3d-1c56-426c-a027-3883cb116213" />
<img width="1559" height="880" alt="image" src="https://github.com/user-attachments/assets/37eadf18-d6af-48fd-8420-f1bb5f9e63c9" />
<img width="1793" height="745" alt="image" src="https://github.com/user-attachments/assets/1c6f5b5a-ada4-4eb3-b239-545034ef01c3" />
<img width="1478" height="885" alt="image" src="https://github.com/user-attachments/assets/8be52cea-3d0e-40fc-b676-4cea91e0ec92" />
<img width="1435" height="850" alt="image" src="https://github.com/user-attachments/assets/b7527651-168a-4976-afec-034870b810e7" />
<img width="1714" height="660" alt="image" src="https://github.com/user-attachments/assets/a90f7123-f8cd-4a6f-b27c-ce5b86b7504b" />
<img width="1553" height="789" alt="image" src="https://github.com/user-attachments/assets/98cc039b-8ba7-4c39-925b-4a86def0cc7d" />
<img width="1579" height="796" alt="image" src="https://github.com/user-attachments/assets/d4e8fbf2-1c0e-47f5-9667-27b685a5e278" />
<img width="1534" height="850" alt="image" src="https://github.com/user-attachments/assets/9e99b72d-8fee-43dc-8b49-78283f373307" />
<img width="1661" height="797" alt="image" src="https://github.com/user-attachments/assets/431a6e24-92b8-4c82-81bc-851849ecdc7d" />
<img width="1553" height="908" alt="image" src="https://github.com/user-attachments/assets/263cf685-965f-46cb-987f-6caf98951af5" />
<img width="1611" height="944" alt="image" src="https://github.com/user-attachments/assets/532757b1-7173-47ea-9fa3-38c011dd4423" />
<img width="1532" height="945" alt="image" src="https://github.com/user-attachments/assets/e993cdf7-2628-4588-9284-d3d0319471de" />
<img width="1599" height="960" alt="image" src="https://github.com/user-attachments/assets/b384ed45-7e24-40f4-bd8b-1a700f25d340" />
<img width="1572" height="916" alt="image" src="https://github.com/user-attachments/assets/60265061-0287-4832-acdb-857e676c8a67" />
<img width="1611" height="893" alt="image" src="https://github.com/user-attachments/assets/4415f3bd-a19d-4083-854f-d86396752808" />
<img width="1584" height="927" alt="image" src="https://github.com/user-attachments/assets/dd73ce9e-9df5-494f-b5df-d7f4b38f172d" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 114 | Verify Lighthouse Accessibility score | Accessibility score of **90 or above** achieved on key pages | PASS | Lighthouse Accessibility audits scored 90+ across key pages (home, shop, checkout, dashboard) following the accessibility fixes in rows 106-113. Checkout scored 97, with the only sub-100 item being the third-party Stripe iframe's aria-hidden input, outside application control |

<details>
<summary>📸 Evidence for 114</summary>
<img width="1876" height="1006" alt="image" src="https://github.com/user-attachments/assets/572c7dee-68a5-4d9e-9a10-a39bcbde254b" />
<img width="1884" height="979" alt="image" src="https://github.com/user-attachments/assets/a88ab69f-f05c-4ec3-9b5b-c8ffe3fe8f35" />
<img width="1893" height="990" alt="image" src="https://github.com/user-attachments/assets/e0ffb5ac-7aee-44bd-a18e-4795ba83ff14" />
<img width="1821" height="1004" alt="image" src="https://github.com/user-attachments/assets/de40fed1-1792-408c-848e-9d6d75b544c7" />
<img width="1881" height="944" alt="image" src="https://github.com/user-attachments/assets/3e1b287d-cd28-46aa-9120-5c5f4f94f15b" />
</details>

---

#### 7. PERFORMANCE TESTING

[⬆ Back to Table of Contents](#table-of-contents)

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 115 | Evaluate Home page performance with Lighthouse | Performance score recorded with no critical issues identified | PASS | Lighthouse Performance audit on the Home page (desktop): FCP 0.7-0.9s, LCP 2.2-2.4s, Total Blocking Time 0ms, Speed Index 0.7-0.9s across runs. No critical issues. Cumulative Layout Shift varies (0.096-0.237) due to images lacking explicit width/height - identified as a non-critical optimisation opportunity; images are already served as WebP |

<details>
<summary>📸 Evidence for 115</summary>
<img width="1866" height="979" alt="image" src="https://github.com/user-attachments/assets/2542bec9-93f1-4e8a-990b-06bfa08f8a6d" />
<img width="1886" height="973" alt="image" src="https://github.com/user-attachments/assets/e40b1dca-be04-4b7d-b8df-98bc20550e98" />
<img width="1884" height="970" alt="image" src="https://github.com/user-attachments/assets/c76c5ab2-8142-4866-ba22-ae22147ceaea" />
<img width="1847" height="909" alt="image" src="https://github.com/user-attachments/assets/ed4450a3-d828-40ab-91ab-f8d2c087ae92" />
<img width="1864" height="1028" alt="image" src="https://github.com/user-attachments/assets/8c04d8bf-bdcd-49a7-90a6-7a54107542e4" />
<img width="1877" height="1005" alt="image" src="https://github.com/user-attachments/assets/1f1cc0a9-8f96-4946-a936-4fa1fea860aa" />
<img width="1878" height="970" alt="image" src="https://github.com/user-attachments/assets/ad950c94-5486-4b41-896c-04dc49ca69c6" />
<img width="1872" height="967" alt="image" src="https://github.com/user-attachments/assets/07ffb3c7-8165-4add-b610-694f2766f410" />
<img width="1874" height="988" alt="image" src="https://github.com/user-attachments/assets/60a32046-7616-436f-8f47-3dfab169e49b" />
<img width="1866" height="973" alt="image" src="https://github.com/user-attachments/assets/bf1a6517-2a8b-4c18-bb9d-cab52c9d88ea" />
<img width="1871" height="979" alt="image" src="https://github.com/user-attachments/assets/0529c0d9-def0-4023-87af-6cf77296ac5c" />
<img width="1891" height="976" alt="image" src="https://github.com/user-attachments/assets/3af41c9b-8715-4620-8e02-41b67ee77a94" />
<img width="1879" height="1007" alt="image" src="https://github.com/user-attachments/assets/d74e752f-94ab-4c44-bb53-dde59c92c436" />
<img width="1883" height="1025" alt="image" src="https://github.com/user-attachments/assets/863be03c-afe6-4dee-bfa5-8e35b5b584e6" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 116 | Evaluate Shop page performance with Lighthouse | Performance score recorded; product images correctly optimised using the WebP format | PASS | Lighthouse Performance audit on the Shop page recorded (see evidence). All 13 product images are served in WebP format (confirmed in the Network panel), satisfying the image-optimisation requirement. Being the most image-heavy page, it scores lower than Home; the remaining "image delivery" opportunity concerns further sizing/compression rather than format, and is non-critical |

<details>
<summary>📸 Evidence for 116</summary>
<img width="1889" height="1027" alt="image" src="https://github.com/user-attachments/assets/db1ad52f-a1bd-4f94-bcb0-bac4a796d944" />
<img width="1887" height="1010" alt="image" src="https://github.com/user-attachments/assets/6a262186-7499-44fc-b860-0651b15074f1" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 117 | Evaluate Checkout page performance with Lighthouse | Performance score successfully recorded | PASS | Lighthouse Performance audit on the Checkout page recorded (see evidence). The page loads Stripe.js for PCI-compliant payment processing, which accounts for the third-party/render-blocking insights - a necessary and expected cost. No critical issues |

<details>
<summary>📸 Evidence for 117</summary>
<img width="1865" height="976" alt="image" src="https://github.com/user-attachments/assets/fd816847-5cd8-421d-b694-106ca3aceb59" />
<img width="1842" height="977" alt="image" src="https://github.com/user-attachments/assets/e405c414-8f5f-4e5e-bf1f-15beaa9c326f" />
<img width="1835" height="968" alt="image" src="https://github.com/user-attachments/assets/b785c8a3-57ac-4c56-9ffb-68f444fc77ab" />
<img width="1870" height="976" alt="image" src="https://github.com/user-attachments/assets/4caf68b6-b81f-48b2-b05d-b9818387675b" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 118 | Verify efficient delivery of static assets | WhiteNoise serves hashed, cacheable static files in the production environment | PASS | WhiteNoise is configured via middleware and `CompressedManifestStaticFilesStorage`, serving hashed, compressed static files in production. Live response headers on static assets show `Cache-Control: max-age=31536000, immutable` and gzip/brotli `Content-Encoding`, and page source references hashed filenames (e.g. style.<hash>.css), enabling long-term browser caching |

<details>
<summary>📸 Evidence for 118</summary>
<img width="1858" height="956" alt="image" src="https://github.com/user-attachments/assets/b3fa50bb-9776-495f-8a5d-2c47e220e40d" />
<img width="864" height="239" alt="image" src="https://github.com/user-attachments/assets/0ca505c4-da5a-470f-841b-6828e317c97b" />
</details>

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 119 | Verify database query efficiency on listing pages | Order History page uses `prefetch_related` for line items, preventing N+1 query issues | PASS | The order history view uses `.prefetch_related('line_items__product')` (orders/views.py line 193). Validated via database query logging: WITH prefetch_related the listing issues 3 queries; WITHOUT it issues 51 (one per line item and product) - a 17× reduction confirming the N+1 problem is prevented |

<details>
<summary>📸 Evidence for 119</summary>
<img width="1221" height="234" alt="image" src="https://github.com/user-attachments/assets/0a22a81a-0fdf-43d9-bc97-2a26a45d4fd9" />
<img width="1013" height="518" alt="image" src="https://github.com/user-attachments/assets/02f8f064-c180-4af4-8763-fd9315cc733a" />
</details>

---

#### 8. REGRESSION TESTING

[⬆ Back to Table of Contents](#table-of-contents)

**Strategy:** The complete automated test suite (89 tests) is executed before every commit, with any failed test preventing the code from being pushed to the repository. In addition, manual regression testing is performed on areas potentially affected by each change to ensure existing functionality remains unaffected.

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 120 | Verify the complete test suite after each new feature | `python manage.py test` → OK, 0 test failures | PASS | Performed consistently throughout development; the automated suite expanded from 67 to 94 tests as new functionality was introduced. Final run confirms all 94 tests pass (Ran 94 tests, OK) with no failures or errors |

<details>
<summary>📸 Evidence for 120</summary>
<img width="880" height="244" alt="image" src="https://github.com/user-attachments/assets/2a8e0297-8f6a-4014-a834-e5b14128b64f" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 121 | Confirm checkout functionality after webhook modifications | Existing checkout process continues to operate correctly following webhook enhancements | PASS | Checkout confirmed working alongside the webhook enhancements: the full automated suite (94 tests, row 120) covers webhook handling and checkout/order creation and passes together, and a fresh live checkout completed end-to-end - payment accepted, confirmation page rendered, order recorded in history, with the corresponding webhook event delivered successfully |

<details>
<summary>📸 Evidence for 121</summary>
<img width="880" height="244" alt="image" src="https://github.com/user-attachments/assets/2a8e0297-8f6a-4014-a834-e5b14128b64f" />
<img width="1250" height="654" alt="image" src="https://github.com/user-attachments/assets/6eeb947b-4abf-4daf-8c85-20c258efb0f3" />
<img width="1073" height="917" alt="image" src="https://github.com/user-attachments/assets/d9c6fc7b-6b9b-472d-a0e6-58ab6039e9a4" />
<img width="1128" height="938" alt="image" src="https://github.com/user-attachments/assets/814693d7-bc35-4de3-bece-0577df51880a" />
<img width="1061" height="746" alt="image" src="https://github.com/user-attachments/assets/02715153-c4b0-4414-9233-6aa89e1ebbf4" />
<img width="1033" height="589" alt="image" src="https://github.com/user-attachments/assets/bed20178-ae74-4bd9-8619-c62706820962" />
<img width="1384" height="365" alt="image" src="https://github.com/user-attachments/assets/1da7495f-9e93-4be2-b4f3-e67d142a1571" />
<img width="1554" height="856" alt="image" src="https://github.com/user-attachments/assets/ed0446d5-8f34-4121-842d-48189c2fd7e7" />
<img width="1832" height="717" alt="image" src="https://github.com/user-attachments/assets/b3590714-3fcb-4436-8fd6-d5873fd4564b" />
<img width="1376" height="424" alt="image" src="https://github.com/user-attachments/assets/697d0ae9-f308-47c3-ae8c-94b37867abd4" />
</details>


| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 122 | Verify the public Plans page after management updates | Only published membership plans remain visible to members after the introduction of staff CRUD functionality | ☐ | |

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 123 | Confirm order confirmation page after email-related fix | Successful live checkout returns an HTTP 200 response instead of the previous HTTP 500 error | PASS | Verified on Heroku following implementation of defect fix D9 |

| Test ID | Test Case | Expected Result | Status | Notes |
|---------|-----------|-----------------|--------|-------|
| 124 | Verify basket behaviour after stock quantity capping | Standard basket operations (add, update and remove) continue to function correctly alongside stock capping rules | ☐ | |

---

#### 9. PYTHON/DJANGO AUTOMATED TESTING

[⬆ Back to Table of Contents](#table-of-contents)

**Test Suite Size:** **89 automated tests, all successfully passing.**

```bash
python manage.py test
# Found 89 test(s).
# Ran 89 tests — OK
```

<!-- Screenshot: terminal showing "Ran 89 tests ... OK" -->

| App | Tests | Coverage Focus |
|-----|-------|----------------|
| accounts | 5 | Profile model, one-to-one user relationship and default values |
| cart | 11 | Basket add/update/remove operations, stock quantity limits, out-of-stock protection and context processor totals |
| orders | 19 | Order and line-item models, checkout workflow, stock deduction and clamping, validation error handling, order history, ownership protection and **Stripe webhook functionality (signature verification, idempotency, order creation and duplicate prevention)** |
| shop | 9 | Product and category models, product listings, availability checks and 404 responses |
| plans | 23 | Membership plan model and features, public plan filtering, Stripe subscription flow, idempotent success handling and **staff CRUD functionality (403 access control, create, edit, archive and validation)** |
| community | 11 | Community post model and form, authentication-protected creation, owner-only editing and deletion |
| reviews | 11 | Review model and form, rating validation and owner-only editing and deletion |
| **Total** | **89** | |

**Testing Techniques Demonstrated:**

- **External service mocking** — Stripe `PaymentIntent` creation is mocked during checkout testing, allowing the automated suite to execute deterministically without requiring an internet connection.
- **Signed event simulation** — Webhook tests generate correctly HMAC-signed Stripe events, exercising the application's genuine signature verification process.
- **Negative-path testing** — Validation includes invalid form submissions, forged webhook signatures, oversell scenarios and attempts to access resources belonging to other users.
- **Security verification** — Ownership protection and HTTP 403 access control are asserted directly within the automated test suite.

---

#### 10. CODE VALIDATION AND STATIC ANALYSIS

[⬆ Back to Table of Contents](#table-of-contents)

| Test ID | Tool | Test Case | Expected Result | Status | Notes |
|---------|------|-----------|-----------------|--------|-------|
| 125 | W3C HTML Validator | Validate the rendered HTML source of every page (using **View Source**, not Django templates) | No validation errors | ☐ | Validate authenticated pages by pasting the rendered source |
| 126 | W3C Jigsaw Validator | Validate the project's CSS | No validation errors | ☐ | |
| 127 | JSHint | Validate custom JavaScript, including the Stripe checkout integration | No validation errors | ☐ | |
| 128 | flake8 | Verify PEP 8 compliance for each application | No warnings reported (or documented exceptions where applicable) | ☐ | |
| 129 | Pylint | Assess code quality for each application | Score greater than **8.0/10** for every app | ☐ | Record individual application scores following the Milestone 3 format |
| 130 | isort | Verify import ordering for each application | `isort <app> --check` returns exit code **0** | ☐ | |
| 131 | Lighthouse | Perform the **Best Practices** audit | Best Practices score recorded for each key page | ☐ | |

<!-- Paste tool outputs beneath each row, following the Milestone 3 convention -->

---

#### 11. DEFECT LOG

[⬆ Back to Table of Contents](#table-of-contents)

The following table documents the defects identified during development, together with their underlying causes and the solutions implemented. Where appropriate, each fix is supported by automated regression tests to prevent future reoccurrence.

| ID | Defect | Root Cause | Fix | Status |
|----|--------|-----------|-----|--------|
| D1 | No error message displayed after an unsuccessful login | The form template failed to render `non_field_errors` | Added support for displaying non-field errors within the shared allauth form component, resolving the issue across all authentication forms | FIXED |
| D2 | Password reset and email-related pages displayed at full width | Template overrides were located in a directory ignored by allauth (`templates/allauth/account/`) | Relocated the template overrides to `templates/account/` | FIXED |
| D3 | Step 2 profile setup appeared after every login | Login redirection always pointed to the profile setup page without checking completion status | Updated the login flow to redirect users to the dashboard while performing completion checks in both directions | FIXED |
| D4 | Product and membership plan images failed to display | Templates relied solely on the empty model image field | Integrated the static image-map template filters | FIXED |
| D5 | Basket allowed unrestricted quantities | Basket views did not validate `product.stock` | Introduced stock quantity limits, prevented out-of-stock additions and clamped stock values at zero | FIXED |
| D6 | Stock levels remained unchanged after successful purchases | Checkout created orders without updating inventory | Implemented stock deduction within `transaction.atomic()`, ensuring values are clamped at zero where necessary | FIXED |
| D7 | Checkout validation errors were not visible | Invalid POST requests discarded the bound form, preventing field errors from being rendered | Re-rendered the bound form with an error summary, field-level validation messages and `is-invalid` styling | FIXED |
| D8 | Orders could be lost if the browser closed immediately after payment | Order creation relied entirely on the client-side checkout process | Implemented a signature-verified, idempotent Stripe webhook to create orders server-side | FIXED |
| D9 | Production order confirmation page returned an HTTP 500 error after payment | Confirmation email was sent with `fail_silently=False`, allowing Gmail SMTP failures on Heroku to interrupt page rendering | Wrapped email sending within a `try/except` block so failures are logged without affecting the customer's confirmation page | FIXED |

**Rationale:** Recording defects alongside their root causes and corresponding resolutions demonstrates an authentic iterative development process rather than suggesting the project was free from defects. Furthermore, several corrections (D5–D9) resulted in permanent additions to the automated regression test suite, reducing the likelihood of similar issues recurring in future development.

---

## Heroku Deployment

[⬆ Back to Table of Contents](#table-of-contents)

---

### Introduction

[⬆ Back to Table of Contents](#table-of-contents)

This section outlines the deployment process used to move the FitHub fitness subscription and e-commerce application from the local development environment in Visual Studio Code to its live production deployment on Heroku. Unlike a standard Django application, deploying an e-commerce platform introduces additional technical considerations. These include securely managing payment credentials across different environments, configuring and validating a server-to-server Stripe webhook endpoint, and ensuring that transactional emails operate reliably in the production environment.

#### Purpose of Deployment

##### 1. **Production Environment Validation**

Deploying the application verifies that it operates correctly within a live production environment rather than only during local development. This includes validating production-specific components such as the PostgreSQL database, SMTP email delivery, WhiteNoise static asset serving, and—most importantly for this project—Stripe payment processing together with secure webhook communication over the public internet.

##### 2. **Portfolio Demonstration**

Hosting the application on a publicly accessible URL allows assessors to evaluate the complete purchasing and subscription workflows using Stripe test payment cards. This provides clear evidence of full-stack development skills and successful third-party payment integration.

##### 3. **Production Configuration Management**

The deployment demonstrates good environment management practices by maintaining separate configuration values for development and production. This includes distinct Stripe webhook signing secrets, disabling `DEBUG` in the live environment, and centralising database configuration through the `DATABASE_URL` environment variable, allowing the underlying database service to be changed with minimal effort.

##### 4. **DevOps Experience**

The deployment process provided practical experience of modern DevOps practices, including Platform-as-a-Service (PaaS) deployment, Heroku's automated release phase for running database migrations, and the configuration, registration and verification of a secure webhook endpoint with the Stripe platform.

##### 5. **Assessment Requirements**

The completed deployment satisfies the requirements of Milestone Project 4 by delivering a fully operational, cloud-hosted e-commerce application that incorporates online payment processing and can be accessed, tested and evaluated by assessors.

### Live Application

[⬆ Back to Table of Contents](#table-of-contents)

**Production URL:** https://fithub-rp-90631f751ed4.herokuapp.com/

**Deployment Status:** Live and Operational

---

### Deployment Configuration

[⬆ Back to Table of Contents](#table-of-contents)

#### Application Details

| Setting | Value |
|---------|-------|
| **App Name** | fithub-rp |
| **Region** | United States (us) |
| **Stack** | Heroku-24 |
| **Buildpack** | heroku/python |
| **Python Version** | 3.12.13 |
| **Web Process** | Gunicorn WSGI Server |

**Note:** The application was initially provisioned using a Heroku-generated application name before being renamed to `fithub-rp` with `heroku apps:rename fithub-rp`. Following the rename, the Git remote was updated using `heroku git:remote -a fithub-rp`. This step is documented because changing the application name also modifies both the public deployment URL and the associated Git remote. Anyone recreating the deployment should create the Heroku application using its final name from the outset.

#### Environment Configuration

**Config Vars (Heroku Dashboard → Settings → Config Vars):**

| Variable | Purpose | Status |
|----------|---------|--------|
| `DATABASE_URL` | Connection string for the PostgreSQL production database (automatically configured by the Heroku Postgres add-on) | Set |
| `SECRET_KEY` | Django application secret key | Set |
| `STRIPE_PUBLIC_KEY` | Stripe publishable API key (test mode, `pk_test_...`) | Set |
| `STRIPE_SECRET_KEY` | Stripe secret API key (test mode, `sk_test_...`) | Set |
| `STRIPE_WH_SECRET` | Stripe webhook signing secret for the **production webhook endpoint** (`whsec_...`) | Set |
| `EMAIL_HOST_USER` | Gmail account used for sending transactional emails | Set |
| `EMAIL_HOST_PASS` | Gmail App Password (16-character password requiring two-factor authentication) | Set |

**Note:** Sensitive configuration values are intentionally concealed for security reasons and are never committed to the Git repository. During local development, the same environment variables are supplied through `env.py`, which is excluded from version control via `.gitignore`. The local `STRIPE_WH_SECRET` is different from its production counterpart, as explained in the [Stripe Webhook Configuration](#stripe-webhook-configuration) section.

#### Heroku Add-ons

| Add-on | Plan | Purpose |
|--------|------|---------|
| **Heroku Postgres** | Essential-0 | Production PostgreSQL database |

---

### Deployment Process

[⬆ Back to Table of Contents](#table-of-contents)

#### Initial Deployment

**Method:** Deployment performed by pushing the project to the Heroku Git remote.

**Commands Used:**

```bash
# Log in to Heroku
heroku login

# Create the Heroku application (or rename an existing app)
heroku create fithub-rp

# Provision a PostgreSQL database
heroku addons:create heroku-postgresql:essential-0

# Configure environment variables
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set STRIPE_PUBLIC_KEY="pk_test_..."
heroku config:set STRIPE_SECRET_KEY="sk_test_..."
heroku config:set STRIPE_WH_SECRET="whsec_..."   # Production webhook secret — see webhook section
heroku config:set EMAIL_HOST_USER="youraddress@gmail.com"
heroku config:set EMAIL_HOST_PASS="your-gmail-app-password"

# Deploy the application
git push heroku main

# Create an administrative user
heroku run python manage.py createsuperuser
```

**Automatic Database Migrations:** Unlike Milestone 3, database migrations are not executed manually following each deployment. Instead, the `Procfile` defines a **release phase** (`release: python manage.py migrate`), which Heroku automatically runs before the newly deployed application becomes live. This ensures that the production database schema remains synchronised with the latest application code while also executing the idempotent data migration responsible for seeding the additional catalogue products.

#### Recent Deployment

**Latest Deployment:** 7 July 2026  
**Commit:** 0a8c199  
**Build Status:** Successful  
**Release Version:** v96

**Deployment Output:**

```text
-----> Building on the Heroku-24 stack
-----> Using buildpack: heroku/python
-----> Python app detected
-----> Using Python 3.12 specified in .python-version
-----> Installing dependencies using 'pip install -r requirements.txt'
-----> $ python manage.py collectstatic --noinput
       156 static files copied to '/tmp/build_87b1e5f2/staticfiles', 412 post-processed.
-----> Discovering process types
       Procfile declares types -> release, web
-----> Compressing...
       Done: 66.9M
-----> Launching...
 !     Release command declared: this new release will not be available until the command succeeds.
       Released v96
       https://fithub-rp-90631f751ed4.herokuapp.com/ deployed to Heroku
Verifying deploy... done.
Running release command...
Operations to perform:
  Apply all migrations: account, accounts, admin, auth, community, contenttypes, orders, plans, reviews, sessions, shop, sites
Running migrations:
  No migrations to apply.
Waiting for release.... done.
```
---

### Project Files for Deployment

[⬆ Back to Table of Contents](#table-of-contents)

#### 1. Procfile

**Location:** Project root

**Purpose:** Defines how the application is executed on Heroku.

```text
release: python manage.py migrate
web: gunicorn fithub.wsgi --log-file -
```

**Explanation:**

- `release:` — Specifies a Heroku **release phase** command that is executed automatically during every deployment before the new release begins serving traffic. Running `migrate` at this stage keeps the production database schema and data migrations synchronised with the deployed code, representing a significant improvement over the manual migration process used in Milestone 3.
- `web:` — Defines the application's web dyno process.
- `gunicorn fithub.wsgi` — Launches the production WSGI application using the Gunicorn server.
- `--log-file -` — Directs application logs to standard output, allowing them to be captured by `heroku logs`.

#### 2. requirements.txt

**Location:** Project root

**Purpose:** Records every Python package required by the application.

**Key Dependencies:**

```txt
Django==4.2.23
django-allauth==65.18.0
stripe==15.2.1
gunicorn
psycopg2-binary
dj-database-url
whitenoise
```

**Total Packages:** <!-- paste from `(Get-Content requirements.txt).Count` or `pip freeze | measure` -->

Before submitting the project, regenerate the file to ensure it accurately reflects the installed environment:

```bash
pip freeze > requirements.txt
```

#### 3. .python-version

**Location:** Project root

**Purpose:** Specifies the Python version used by Heroku during deployment.

```text
3.12
```

<!-- Verify this file exists in your project root (it replaced the deprecated
     runtime.txt). If your project still uses runtime.txt, document that
     instead, or migrate to .python-version. -->

#### 4. Django Settings Configuration

**File:** `fithub/settings.py`

The project uses a single **`DEVELOPMENT` environment variable** to determine whether the application is running locally or in production, while all sensitive configuration values are loaded from environment variables.

- **`SECRET_KEY`** — Retrieved from the environment and never hard-coded within the project.
- **`DEBUG`** — Enabled only during local development when `DEVELOPMENT` is defined; automatically disabled in production.
- **`ALLOWED_HOSTS`** — Configured as `['localhost', '127.0.0.1', '.herokuapp.com']`.
- **Database** — `dj_database_url` reads the `DATABASE_URL` environment variable when available, connecting to the Heroku PostgreSQL database. If absent, the application automatically falls back to SQLite for local development. This centralises database configuration within a single environment variable, making future database changes straightforward.
- **Email** — Uses Django's console email backend during development, with emails written to the terminal, while the production deployment uses Gmail SMTP configured through `EMAIL_HOST_USER` and `EMAIL_HOST_PASS`.
- **Stripe** — The `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_CURRENCY` (`gbp`) and `STRIPE_WH_SECRET` settings are all read directly from the environment.

During local development these variables are supplied through the gitignored `env.py` file, whereas the production deployment retrieves the same variables from Heroku Config Vars. Using identical variable names across both environments removes the need for code modifications when deploying the application.

---

### Static Files Handling

[⬆ Back to Table of Contents](#table-of-contents)

- **WhiteNoise** middleware delivers static assets directly from the Heroku dyno, removing the need for a separate static file hosting service.
- During each Heroku build, `python manage.py collectstatic` is executed automatically.
- WhiteNoise's compressed manifest storage generates hashed filenames (for example, `kettlebell-16kg.c4ec98bd.webp`), allowing long-term browser caching while providing reliable cache invalidation whenever files change.
- Product and membership plan images are supplied as pre-optimised `.webp` static assets.

---

### Database

[⬆ Back to Table of Contents](#table-of-contents)

| Environment | Database | Configuration |
|-------------|----------|---------------|
| Development | SQLite (`db.sqlite3`) | Default database used whenever `DATABASE_URL` is not defined |
| Production | Heroku PostgreSQL | `DATABASE_URL` environment variable parsed using `dj_database_url` |

Using `DATABASE_URL` as the single source of database configuration allows the application to switch between development and production databases without requiring any code changes. In addition, both schema and data migrations are applied automatically to the production database during Heroku's release phase.

---

### Stripe Configuration

[⬆ Back to Table of Contents](#table-of-contents)

FitHub integrates Stripe in **test mode** through **two separate payment workflows**, each serving a different purpose within the application.

| Integration | Used for | Technology |
|-------------|----------|------------|
| **Stripe Elements + PaymentIntents** | One-off shop purchases (basket checkout) | Embedded card element within the checkout page; payments confirmed client-side using `confirmCardPayment`; orders created server-side |
| **Stripe Checkout** | Membership subscriptions | Stripe-hosted checkout page; subscription recorded when the customer returns to the application |

#### Keys and Environments

| Variable | Development (`env.py`) | Production (Heroku Config Var) |
|----------|------------------------|--------------------------------|
| `STRIPE_PUBLIC_KEY` | Test publishable key | Same test publishable key |
| `STRIPE_SECRET_KEY` | Test secret key | Same test secret key |
| `STRIPE_WH_SECRET` | **Stripe CLI** webhook signing secret | **Stripe Workbench endpoint** webhook signing secret (different value — see below) |

**Security Notes:**

- Payment card details are entered through a Stripe-hosted iframe provided by Stripe Elements and **never pass through the Django application**. Consequently, card information is never included in POST requests, application logs or the database.
- The application stores only the PaymentIntent identifier (`stripe_payment_intent_id` on the order), providing support for webhook idempotency without retaining sensitive payment data.
- All Stripe credentials operate exclusively in **test mode**, meaning the application does not process live customer card payments.

**Test Cards** (use any future expiry date and any CVC):

| Card | Behaviour |
|------|-----------|
| `4242 4242 4242 4242` | Successful payment |
| `4000 0000 0000 0002` | Payment declined |
| `4000 0025 0000 3155` | Triggers 3D Secure authentication |

---

### Stripe Webhook Configuration

[⬆ Back to Table of Contents](#table-of-contents)

#### Purpose

Whenever a payment is successfully completed, Stripe sends a server-to-server `payment_intent.succeeded` event to the application. Because this communication takes place independently of the customer's browser, **orders are still recorded even if the customer closes their browser immediately after payment**—a scenario that cannot be handled reliably by the standard client-driven checkout flow alone.

The webhook implementation incorporates several important security and reliability features:

- **Signature verification** — Every incoming request is authenticated using the endpoint's webhook signing secret through `stripe.Webhook.construct_event()`. Requests with invalid or forged signatures are rejected with an HTTP 400 response.
- **Idempotent processing** — Orders are matched using the `stripe_payment_intent_id`, ensuring that replayed or duplicate webhook events never generate duplicate orders or perform stock deductions more than once.
- **Intentional CSRF exemption** — As Stripe cannot provide a Django CSRF token, the cryptographic webhook signature serves as the authenticity mechanism in place of CSRF protection.

**Endpoint:** `/orders/wh/` → `https://fithub-rp-90631f751ed4.herokuapp.com/orders/wh/`

**Subscribed Event:** `payment_intent.succeeded`

#### Two Signing Secrets — One Environment Variable

To avoid a common source of confusion, it is important to note that **two separate webhook signing secrets** are used, although both are assigned to the same `STRIPE_WH_SECRET` environment variable within their respective environments.

| Environment | Source of the Signing Secret | Where It Is Configured |
|-------------|------------------------------|------------------------|
| Local development | Generated each time `stripe listen` is started via the Stripe CLI | `env.py` |
| Production | Displayed for the webhook endpoint in **Stripe Workbench → Webhooks** | Heroku Config Var |

#### Local Webhook Testing (Stripe CLI)

```bash
# Terminal 1 — forward Stripe events to the local application
stripe listen --forward-to localhost:8000/orders/wh/
# → outputs: "Your webhook signing secret is whsec_..." → copy this into env.py

# Terminal 2 — start the Django development server
python manage.py runserver

# Terminal 3 — trigger a test webhook event
stripe trigger payment_intent.succeeded
```

**Verified Result:** The Stripe CLI reports that the webhook event has been forwarded successfully, while the Django development server logs `POST /orders/wh/ HTTP/1.1 200`, confirming that the endpoint is reachable and the webhook signature has been successfully validated.

**Note:** The Stripe CLI generates a **new webhook signing secret each time** `stripe listen` is started. Consequently, the value stored in `env.py` must be updated whenever a new CLI session begins.

#### Production Webhook Configuration (Stripe Workbench)

Webhook management within Stripe is now handled through **Workbench**, replacing the previous Developers Dashboard.

1. Sign in to the Stripe Dashboard in **test mode (sandbox)** and navigate to **Workbench → Webhooks**.
2. Create a new **Webhook endpoint** as the event destination.
3. Configure the **Endpoint URL** as `https://fithub-rp-90631f751ed4.herokuapp.com/orders/wh/`.
4. Select **Your account** as the event source and subscribe to the `payment_intent.succeeded` event.
5. Once the endpoint has been created, reveal its webhook signing secret (`whsec_...`).
6. Store the signing secret on Heroku:

```bash
heroku config:set STRIPE_WH_SECRET=whsec_... -a fithub-rp
```

Setting or updating a Heroku Config Var automatically restarts the application's dyno.

**Verified Result:** Following a successful payment using Stripe Test Mode, the Heroku router logs record `POST /orders/wh/ ... status=200` requests originating from Stripe. At the same time, the Stripe Workbench delivery log confirms that the webhook event was delivered and processed successfully.

<!-- Screenshot: Workbench endpoint delivery log showing payment_intent.succeeded → 200 -->
<!-- Screenshot: heroku logs showing POST /orders/wh/ 200 -->

**Important:** The webhook endpoint must be created within the **same Stripe mode** as the API keys used by the application. A webhook signing secret generated in **test mode** cannot validate events originating from **live mode**, and the reverse is equally true.

---

### Email Configuration

[⬆ Back to Table of Contents](#table-of-contents)

| Environment | Backend | Behaviour |
|-------------|---------|-----------|
| Development | Console | Emails are written to the terminal, eliminating the possibility of delivery failures during development |
| Production | Gmail SMTP | Transactional emails are sent using `EMAIL_HOST_USER` and `EMAIL_HOST_PASS` (a Gmail **App Password**, requiring two-factor authentication on the associated Google account) |

**Built-in Resilience:** The order confirmation email is dispatched within a `try/except` block so that any email delivery failure—for example, invalid SMTP credentials—is recorded in the application logs without interrupting the user experience. As a result, customers who have successfully completed payment always receive the order confirmation page, even if the email cannot be delivered.

This design decision originated from an actual production issue (see **Defect Log D9**). Initially, the confirmation email was sent before the page rendered with `fail_silently=False`. Consequently, a Gmail SMTP failure on Heroku caused the success page to return an HTTP 500 error, despite the payment, order creation and Stripe webhook having completed successfully.

---

### Deployment Checklist

[⬆ Back to Table of Contents](#table-of-contents)

- [ ] Confirm `env.py` is included in `.gitignore` and that no secrets are committed to the repository.
- [ ] Verify `DEBUG` is disabled in production (the `DEVELOPMENT` environment variable is not configured on Heroku).
- [ ] Ensure all required Config Vars are configured: `SECRET_KEY`, `DATABASE_URL`, `STRIPE_PUBLIC_KEY`, `STRIPE_SECRET_KEY`, `STRIPE_WH_SECRET`, `EMAIL_HOST_USER` and `EMAIL_HOST_PASS`.
- [ ] Regenerate `requirements.txt` using `pip freeze > requirements.txt`.
- [ ] Verify that the `Procfile` exists and defines both the release phase and the web process.
- [ ] Create the Stripe Workbench webhook endpoint for the production URL and configure its signing secret on Heroku.
- [ ] Confirm `git push heroku main` completes successfully and that the Heroku release phase applies all migrations.
- [ ] Create a production superuser using `heroku run python manage.py createsuperuser`.
- [ ] Complete and verify a full end-to-end checkout using the Stripe test card `4242...`, including successful order creation, webhook delivery (HTTP 200), confirmation page rendering and email dispatch.
- [ ] Verify that the deployed application matches the latest commit in the GitHub repository.

---

### Deployment Verification

[⬆ Back to Table of Contents](#table-of-contents)

The following functionality was verified after deployment on the live production environment:

| Feature | Status | Notes |
|---------|--------|-------|
| **Home page loads** | ☐ | |
| **User registration and email verification** | ☐ | |
| **User login and logout** | ☐ | |
| **Membership plans listing and detail pages** | ☐ | |
| **Stripe subscription checkout** | ☐ | |
| **Shop, basket and stock quantity limiting** | ☐ | |
| **Checkout payment (Stripe Elements)** | Pass | Verified using a Stripe test card following implementation of defect D9 — confirmation page returned HTTP 200 |
| **Live webhook delivery** | Pass | Heroku logs confirmed successful `POST /orders/wh/ 200` requests from Stripe |
| **Order confirmation page** | Pass | Correctly renders complete order details following the D9 fix |
| **Order history and ownership protection** | ☐ | |
| **Staff plan management and HTTP 403 protection for non-staff users** | ☐ | |
| **Django admin interface** | ☐ | |
| **Static assets (CSS, JavaScript and images)** | ☐ | |
| **Responsive layout** | ☐ | |

---

### Monitoring and Logs

[⬆ Back to Table of Contents](#table-of-contents)

```bash
# Display a live stream of recent application logs
heroku logs --tail -a fithub-rp

# Display the latest 100 log entries
heroku logs -n 100 -a fithub-rp

# Stream logs from the web dyno only
heroku logs --tail --dyno web -a fithub-rp
```

Successful webhook requests appear within the Heroku router logs in the following format:

```text
heroku[router]: at=info method=POST path="/orders/wh/" ... status=200
```

```bash
# View dyno status, restart the application or inspect app details
heroku ps -a fithub-rp
heroku restart -a fithub-rp
heroku apps:info -a fithub-rp
```

---

### Deployment Performance Optimisation

[⬆ Back to Table of Contents](#table-of-contents)

1. **Compressed static assets** — WhiteNoise delivers compressed, hash-versioned static files together with long-term browser caching headers.
2. **Optimised images** — Product and membership plan images are supplied in the `.webp` format to reduce page load times.
3. **Efficient database queries** — The Order History view uses `prefetch_related('line_items__product')`, preventing N+1 query issues when rendering product thumbnails.
4. **Automatic release-phase migrations** — Database schema updates are applied before new application code receives traffic, eliminating mixed-version deployment issues.

---

### Security Configuration

[⬆ Back to Table of Contents](#table-of-contents)

1. **Environment variables** — All sensitive configuration values, including the Django secret key, database connection string, Stripe API keys, webhook signing secret and email credentials, are stored securely within Heroku Config Vars or the gitignored `env.py` file. No secrets are committed to source control.
2. **Production debug settings** — `DEBUG` is disabled in the production environment, ensuring that error pages never expose sensitive configuration details or stack traces.
3. **Allowed hosts** — Application access is restricted to `localhost` and the `.herokuapp.com` domain.
4. **HTTPS enforcement** — Secure HTTPS connections are provided through Heroku's SSL infrastructure.
5. **CSRF protection** — Django's CSRF middleware safeguards all application forms. The Stripe webhook endpoint is intentionally marked `csrf_exempt` because webhook authenticity is guaranteed through Stripe's cryptographic signature verification instead of CSRF tokens.
6. **Webhook signature validation** — Invalid, forged or modified webhook requests are rejected with an HTTP 400 response. This behaviour is verified by the automated test suite.
7. **Payment card isolation** — Card details are entered exclusively within Stripe's secure iframe, ensuring that sensitive payment information never reaches the Django application.
8. **Access control** — Ownership protection prevents users from accessing other users' orders (returning HTTP 404 where appropriate), management routes are secured with `staff_required` (HTTP 403), and community posts and product reviews can only be edited or deleted by their respective owners.
9. **SQL injection protection** — Database queries are executed through Django's ORM, which automatically parameterises queries to protect against SQL injection attacks.

---

### Deployment Commands Reference

[⬆ Back to Table of Contents](#table-of-contents)

```bash
# Deploy the latest application version
# (database migrations are executed automatically during the Heroku release phase)
git push heroku main

# Create a production superuser account
heroku run python manage.py createsuperuser -a fithub-rp

# Launch the deployed application in the browser
heroku open -a fithub-rp

# Stream live application logs
heroku logs --tail -a fithub-rp

# View and manage configuration variables
heroku config -a fithub-rp
heroku config:set VARIABLE_NAME=value -a fithub-rp
heroku config:get STRIPE_WH_SECRET -a fithub-rp

# View and manage dynos
heroku ps -a fithub-rp
heroku restart -a fithub-rp

# Open the Django shell or connect to the production database
heroku run python manage.py shell -a fithub-rp
heroku pg:psql -a fithub-rp
```

---

### Troubleshooting

[⬆ Back to Table of Contents](#table-of-contents)

##### Issue: HTTP 500 on the Order Confirmation Page (Payment Successful)

This was a genuine production defect encountered during development (D9). Although payment processing, order creation and Stripe webhook processing all completed successfully, the request to `GET /orders/checkout/success/...` returned an HTTP 500 error.

**Cause:** Before rendering the confirmation page, the application attempted to send the confirmation email using `fail_silently=False`. On Heroku, a Gmail SMTP failure (typically caused by a missing or outdated App Password) raised an exception, preventing the page from loading.

**Solution:** The email-sending process was wrapped in a `try/except` block so that any email failure is logged without interrupting the customer journey. In addition, valid `EMAIL_HOST_USER` and `EMAIL_HOST_PASS` configuration variables must be present to enable successful email delivery.

```bash
heroku config -a fithub-rp        # Verify both email configuration variables exist
heroku logs -n 100 -a fithub-rp   # Check for "confirmation email failed" log entries
```

##### Issue: Webhook Requests Return HTTP 400

**Cause:** The `STRIPE_WH_SECRET` configured on Heroku does not match the webhook endpoint's signing secret. This commonly occurs when the local Stripe CLI secret is mistakenly used instead of the Stripe Workbench webhook secret, or when the webhook endpoint has been created in the incorrect mode (live instead of test, or vice versa).

**Solution:** Reveal the webhook signing secret within **Stripe Workbench → Webhooks** (Test Mode) and update the Heroku configuration accordingly.

```bash
heroku config:set STRIPE_WH_SECRET=whsec_... -a fithub-rp
```

##### Issue: General Application Error (HTTP 500)

```bash
heroku logs --tail -a fithub-rp

# Common causes include:
# - Missing or incorrect configuration variables
# - Failed release-phase database migrations
```

##### Issue: Static Assets Fail to Load

Static assets are collected automatically during the Heroku build process using `collectstatic`. If CSS, JavaScript or images are missing, inspect the build logs and confirm that the WhiteNoise middleware is positioned immediately after `SecurityMiddleware` within the `MIDDLEWARE` setting.

##### Issue (Windows/OneDrive): `.git/objects` Deletion Prompts During Git Push

When a Git repository is stored inside a OneDrive-synchronised folder, pushing changes may generate repeated messages such as `Deletion of directory '.git/objects/..' failed`. This occurs because OneDrive temporarily locks Git's internal object files while synchronising.

**Solution:** Pause OneDrive synchronisation before running Git push operations. If the prompts appear, selecting `n` is harmless because the repository data has already been transferred successfully. As a long-term solution, store Git repositories outside folders synchronised by OneDrive.

---

### Continuous Deployment

[⬆ Back to Table of Contents](#table-of-contents)

```bash
# 1. Make local changes and execute the automated test suite
python manage.py test        # All 89 tests must pass before deployment

# 2. Stage, commit and push changes to GitHub
git add <files>
git commit -m "feat: description of change"
git push origin main

# 3. Deploy the latest version to Heroku
git push heroku main

# During deployment, Heroku automatically:
# - Installs project dependencies
# - Executes collectstatic
# - Runs the release phase (python manage.py migrate)
# - Restarts the application dynos
```

---

### Production Environment Validation

[⬆ Back to Table of Contents](#table-of-contents)

```bash
heroku run "python --version" -a fithub-rp
# Output: <!-- paste -->

heroku run python manage.py --version -a fithub-rp
# Output: 4.2.23

heroku pg:info -a fithub-rp
# Output:
# <!-- paste (plan, status, PostgreSQL version, data size, tables) -->

heroku ps -a fithub-rp
# Output: <!-- paste -->
```

---

### Conclusion

[⬆ Back to Table of Contents](#table-of-contents)

**Deployment Status:** **SUCCESSFUL**

The FitHub application has been successfully deployed to Heroku and is fully operational in the production environment. Key production features include:

- Secure user authentication with email verification and a two-step profile registration process.
- Membership subscriptions processed through Stripe Checkout.
- A complete e-commerce platform featuring a shopping basket, stock integrity controls and Stripe Elements for secure one-off payments.
- A signature-verified, idempotent Stripe webhook that guarantees orders are recorded even if a customer closes their browser immediately after payment, verified in production through successful `POST /orders/wh/ 200` requests.
- Transactional order confirmation emails with graceful error handling to prevent email failures from affecting the customer experience.
- Secure order history protected by ownership checks together with staff-only membership plan management.
- A fully responsive user interface delivered using optimised static assets.

**Live Application:** https://fithub-rp-90631f751ed4.herokuapp.com/

**Last Updated:** <!-- date -->  
**Release Version:** <!-- vNN -->  
**Deployment Method:** Git push to Heroku with automatic release-phase database migrations  
**Status:** Active and Operational

---

## References

[⬆ Back to Table of contents](#table-of-contents)

- **W3C (2023) Web Content Accessibility Guidelines (WCAG) 2.1.**
Available at: https://www.w3.org/TR/WCAG21/
  (Accessed: 31 May 2026).

- **MDN Web Docs (2024) Client-side form validation.**
Available at: https://developer.mozilla.org/en-US/docs/Learn/Forms/Form_validation
  (Accessed: 31 May 2026).

- **MDN Web Docs (2024) HTML: HyperText Markup Language.**
Available at: https://developer.mozilla.org/en-US/docs/Web/HTML
  (Accessed: 31 May 2026).

- **Nielsen, J. (2020) 10 Usability Heuristics for User Interface Design. Nielsen Norman Group.**
Available at: https://www.nngroup.com/articles/ten-usability-heuristics/
  (Accessed: 31 May 2026).

- **Stripe (2025) Stripe Checkout Documentation.**
Available at: https://stripe.com/docs/payments/checkout
  (Accessed: 31 May 2026).

- **Stripe (2025) Stripe API Documentation.**
Available at: https://stripe.com/docs/api
  (Accessed: 31 May 2026).

- **Mozilla Developer Network (2024) Web Application Security.**
Available at: https://developer.mozilla.org/en-US/docs/Web/Security
  (Accessed: 31 May 2026).

- **Django Software Foundation (2025) Django Documentation.**
Available at: https://docs.djangoproject.com/en/stable/
  (Accessed: 31 May 2026).
  
- **Jazzband (2025) django-allauth Documentation.**
Available at: https://django-allauth.readthedocs.io/en/latest/
  (Accessed: 31 May 2026).

- **Python Software Foundation (2025) PEP 8 – Style Guide for Python Code.**
Available at: https://peps.python.org/pep-0008/
  (Accessed: 31 May 2026).
  
- **Code Institute (2025) Full Stack Frameworks with Django – Milestone Project 4 Specification.**
Available at: https://codeinstitute.net/
  (Accessed: 31 May 2026).
  
- **PostgreSQL Global Development Group (2025) PostgreSQL Documentation.**
Available at: https://www.postgresql.org/docs/
  (Accessed: 31 May 2026).
  
- **SQLite (2025) SQLite Documentation.**
Available at: https://www.sqlite.org/docs.html
  (Accessed: 31 May 2026).




