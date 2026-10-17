# -*- coding: utf-8 -*-
"""
Cotton Mitra Project Report - Content for Chapter 3: Work Done
"""

CHAPTER_3_CONTENT = {
    '3.1': [
        (
            "The engineering development of Cotton Mitra is guided by user-centric design principles, high-availability "
            "microservices architecture, and clean separation of concerns. The platform is designed to accommodate two primary "
            "stakeholder personas with radically different operational workflows and computational proficiencies: rural cotton "
            "cultivators seeking intuitive crop guidance and direct warehouse selling, and industrial warehouse custodians managing "
            "inventory throughput, environmental telemetry, and logistics dispatches."
        ),
        (
            "To satisfy these operational requirements, the system is decomposed into five core interoperable modules:\n"
            "1. Farmer Operations & Advisory Portal: A streamlined, mobile-responsive web interface accessible via secure mobile OTP "
            "authentication. It presents simplified soil health inputs, generates automated diagnostic fertilizer cards, displays "
            "localized crop rotation recommendations, and provides a direct messaging console for warehouse interaction.\n"
            "2. Warehouse Operations & Inventory Telemetry Dashboard: A comprehensive enterprise management dashboard featuring "
            "real-time key performance indicators (KPIs), multi-warehouse stock tracking, inventory aging analytics, shipment scheduling, "
            "and dynamic reorder level (ROL) planning.\n"
            "3. Autonomous Machine Learning Forecasting Microservice: A standalone computational service running an optimized Random Forest "
            "Regressor that dynamically predicts monthly cotton consumption and demand trends for the forward quarter.\n"
            "4. Environmental Monitoring and Threshold Alert Engine: An active telemetry watcher that processes ambient humidity and "
            "temperature readings from warehouse storage sections, generating color-coded alerts (Danger, Warning, Info, Success) when safety "
            "thresholds are breached.\n"
            "5. Direct Negotiation and Real-Time Communication Hub: A full-duplex communication pipeline built upon Socket.IO WebSockets and "
            "client-side AES-256 cryptographic encryption, enabling confidential, peer-to-peer price quotes and delivery contracts."
        )
    ],
    '3.2': [
        (
            "The Cotton Mitra technological ecosystem leverages modern, robust, and industry-standard open-source frameworks "
            "across the frontend, backend, database, machine learning, and security tiers:"
        ),
        (
            "• Frontend Presentation Layer:\n"
            "- HTML5 & Semantic Elements: Establishes accessible, standard-compliant document structures across farmer and warehouse views.\n"
            "- Cascading Style Sheets (CSS3) & Bootstrap 5: Delivers a premium, responsive UI featuring curated agricultural color palettes "
            "(deep forest green #1B4D3E, harvest amber, sleek dark slate), glassmorphism cards, micro-animations, and fluid grid layouts.\n"
            "- JavaScript (ES6+): Powers dynamic client-side interactions, asynchronous fetch API requests, DOM updates, and WebSocket event handlers.\n"
            "- Chart.js & HTML5 Canvas: Renders high-performance, interactive data visualizations including 12-month historical yield charts, "
            "forecast trajectory curves, and quality grade distribution pie charts."
        ),
        (
            "• Backend Application Layer:\n"
            "- Node.js (v18+) & Express Framework (v5.2): Serves as the primary enterprise API gateway and application server (running on port 3000), "
            "handling RESTful routes, session state management, middleware authentication, and static asset streaming.\n"
            "- Python (v3.10+) & Flask: Deployed in a dual capacity: (a) Hosting the dedicated Machine Learning microservice (`ml_server.py`) on "
            "port 5001, and (b) Providing a lightweight, standalone Python web application alternative (`app.py`) on port 8000 for edge environments.\n"
            "- Axios: Manages inter-service asynchronous HTTP communication between the Node.js API gateway and the Python ML forecast engine."
        ),
        (
            "• Database and Persistence Layer:\n"
            "- MongoDB (v7.0+): Document-oriented NoSQL database providing horizontal scalability, dynamic schema flexibility, and high-throughput "
            "JSON document storage for inventory batches, shipments, telemetry alerts, forecast logs, and messaging transcripts.\n"
            "- Mongoose (v9.3): Object Data Modeling (ODM) library enforcing robust data validation, indexing, and asynchronous querying across "
            "nine production collections (Inventory, Shipment, Alert, Forecast, Chat, Yield, UserProfile, Conversation, DirectMessage)."
        ),
        (
            "• Machine Learning & Numerical Computing Stack:\n"
            "- Scikit-Learn: Employs `RandomForestRegressor` with 100 decision tree estimators for robust non-linear regression.\n"
            "- Pandas & NumPy: Executes high-speed data manipulation, temporal datetime conversions, sliding-window lag feature generation, "
            "and matrix mathematics on historical cotton datasets (`data.csv`)."
        ),
        (
            "• Security, Cryptography & Real-Time Protocols:\n"
            "- Socket.IO (v4.8): Manages persistent, bidirectional WebSocket channels for real-time chat, typing indicators, and instant telemetry alerts.\n"
            "- CryptoJS: Executes 256-bit Advanced Encryption Standard (AES) cryptographic ciphering on direct messaging payloads, guaranteeing end-to-end "
            "confidentiality between farmers and warehouse custodians.\n"
            "- OTP Authentication Engine: Custom phone-based one-time password verification module with 10-minute validity and rate-limiting."
        )
    ],
    '3.3': [
        (
            "The operational flow of Cotton Mitra seamlessly guides users through interconnected agricultural and logistics workflows:"
        ),
        (
            "1. Farmer Authentication and Session Inception: A farmer visits `/farmer/login` and inputs their 10-digit Indian mobile number. "
            "The backend validates the number against standard telecom formats (`/^[6-9]\\d{9}$/`), applies rate limiting (maximum 3 attempts "
            "within 10 minutes), generates a cryptographically random 6-digit OTP, stores it in an ephemeral memory cache with a 600-second TTL, "
            "and verifies the submitted code upon submission. Upon verification, a persistent farmer session is established, redirecting the user "
            "to `/farmer/dashboard`."
        ),
        (
            "2. Warehouse Manager Authentication: Warehouse operators authenticate via standard credential authentication or Google OAuth 2.0 "
            "integration (`/api/login/google`), gaining access to `/dashboard` upon verification of privileged role privileges."
        ),
        (
            "3. Inventory Intake, Grade Segregation, and Aging Analysis: When cotton bales arrive at a warehouse, the operator registers a new batch "
            "specifying batch ID, quality grade (Premium, Standard, Economy), quantity in bales, warehouse facility (Warehouse A, B, or C), section "
            "location, initial price per bale, and environmental storage conditions. The system continuously evaluates each lot's arrival date against "
            "current time; if the residency duration exceeds 90 days, the batch is dynamically tagged with an 'Aging Stock Risk' flag."
        ),
        (
            "4. Environmental Monitoring and Threshold Alert Triggering: Warehouse environmental sensors continuously report relative humidity and "
            "temperature. If humidity surpasses the critical safety ceiling of 60% (as observed in Warehouse B at 61%), the Alert engine instantly "
            "creates a high-priority Danger alert, dispatches notification banners to active operators, and advises dehumidifier activation."
        ),
        (
            "5. Direct Peer-to-Peer Negotiation: Farmers browse certified warehouse custodians within their geographic cluster. Initiating a chat creates "
            "a conversation record. As either party types, WebSocket events (`typing`, `stop_typing`) update the UI. The sender's text is encrypted "
            "via AES-256 before transmission and stored encrypted in MongoDB, decrypting seamlessly on the verified recipient's interface."
        )
    ],
    '3.4': [
        (
            "Cotton Mitra implements a robust, multi-tier decoupled microservices architecture designed for resilience, horizontal scalability, "
            "and clean maintainability. The architectural topology is structured across four functional tiers:"
        ),
        (
            "1. Presentation Tier (Web Clients): Consists of the modern single-page and responsive multi-page layouts running within the client browser. "
            "It communicates with the application tier via standard RESTful JSON HTTP endpoints and maintains an asynchronous duplex connection via Socket.IO."
        ),
        (
            "2. Application Gateway Tier (Node.js & Express - Port 3000): Acts as the primary orchestrator, reverse proxy, and business logic coordinator. "
            "It enforces session authentication (`requireAuth`, `requireFarmerAuth`, `requireMsgAuth`), handles CRUD operations for inventory and shipments, "
            "manages the in-memory OTP verification lifecycle, coordinates WebSocket rooms for direct messaging (`user-{userId}`), and delegates predictive "
            "computation requests to the machine learning microservice."
        ),
        (
            "3. Machine Learning Microservice Tier (Flask & Scikit-Learn - Port 5001): A specialized Python microservice dedicated strictly to "
            "predictive mathematical modeling. Exposing `/ml/forecast` and `/ml/health` REST endpoints, it isolates CPU-intensive regression algorithms "
            "from the I/O-bound web gateway, ensuring that complex multi-step forecast computations never block client web traffic."
        ),
        (
            "4. Data Persistence Tier (MongoDB - Port 27017): Provides a document-oriented datastore with robust indexing across unique identifiers "
            "(`batchId`, `shipmentId`, `userId`). The system also incorporates an automatic gracefully degrading Demo In-Memory Data Store, enabling "
            "flawless local testing, academic demonstration, and resilience during database connectivity interruptions."
        )
    ],
    '3.5': [
        (
            "The forecasting capabilities of Cotton Mitra rely on an empirical macroeconomic dataset (`data.csv`) capturing monthly cotton supply, "
            "demand, price dynamics, and climatic factors in India over multiple crop years. To prepare this data for robust machine learning model "
            "training, a meticulous pre-processing and feature engineering pipeline was developed:"
        ),
        (
            "1. Chronological Sorting and Date Standardization: Raw agricultural time series frequently suffer from inconsistent date formatting. "
            "The pipeline parses date records with explicit day-first interpretation (`pd.to_datetime(df['date'], dayfirst=True)`), chronologically "
            "sorting the dataframe and resetting the index. This rigorous temporal sequencing eliminates chronological drift and completely resolves "
            "historical date repetition artifacts (such as the 'Jan 2026' loop bug)."
        ),
        (
            "2. Lag Feature Engineering (Autoregressive Covariates): In commodity economics, current consumption and market prices are heavily "
            "dependent on immediate historical values. Two critical lag features were engineered:\n"
            "- `consumption_lag_1`: Monthly cotton consumption lagged by one month ($t-1$), capturing immediate industrial uptake inertia.\n"
            "- `price_lag_1`: Market price per quintal lagged by one month ($t-1$), reflecting commodity procurement cost dynamics."
        ),
        (
            "3. Macroeconomic and Climatic Covariate Integration:\n"
            "- `textile_index`: A normalized monthly index quantifying capacity utilization and output across Indian spinning and composite mills.\n"
            "- `rainfall_mm`: Total precipitation across core cotton agro-ecological zones, reflecting weather-induced transportation and harvesting shifts.\n"
            "- `year` and `month`: Decomposed temporal indicators capturing seasonal cyclicality, harvesting peaks (October to January), and lean summer ginning periods."
        ),
        (
            "4. Target Feature Isolation: The model's dependent target variable is established as `consumption_lakh_bales`, representing total domestic "
            "cotton consumption in units of lakh bales (1 bale = 170 kg of lint cotton)."
        )
    ]
}
