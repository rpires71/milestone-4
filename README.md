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




