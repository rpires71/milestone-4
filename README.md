# Milestone 4 Project – Full Stack Frameworks with Django – FitHub Fitness Subscription Application

---

## Links

- [Link to Live Website](https://portuguese-kitchen-rp-a1a93004e977.herokuapp.com/)
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
  - [FitHub Fitness Subscription Application Wireframes](#fithub-fitness-subscription-application)
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

# Project Goals
 
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




