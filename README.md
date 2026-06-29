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
  - [Testing](#testing)
    - [Automated Testing](#automated-testing)
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

<img width="1536" height="1024" alt="plans_detail wireframe v2" src="https://github.com/user-attachments/assets/7046db37-25fc-4661-8c9c-1564895db6a8" />

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




