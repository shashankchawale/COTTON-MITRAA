# -*- coding: utf-8 -*-
"""
Cotton Mitra Project Report - Comprehensive Academic Content Data
Contains detailed text, tables, equations, and metadata for all chapters.
"""

CO_PO_DATA = {
    'intro': (
        "The Course Outcomes (COs) for the Cotton Mitra project are formulated in alignment "
        "with the National Board of Accreditation (NBA) and Outcome-Based Education (OBE) guidelines. "
        "These outcomes represent the specialized engineering competencies, domain insights, and "
        "practical software engineering skills acquired and demonstrated through the design, implementation, "
        "and evaluation of this cyber-physical agricultural software platform."
    ),
    'cos': [
        ("CO1", "Analyze and formulate engineering solutions for agricultural supply chain inefficiencies, post-harvest losses, and soil health management in cotton cultivation."),
        ("CO2", "Design, train, and validate supervised machine learning models (Random Forest regression) for cotton consumption forecasting and demand estimation."),
        ("CO3", "Architect and develop an asynchronous full-stack web platform using Node.js, Express, Flask, and MongoDB with dual specialized user interfaces."),
        ("CO4", "Implement cyber-secure, real-time communication protocols (AES-256 encrypted WebSockets) and IoT environmental monitoring telemetry with threshold alerts."),
        ("CO5", "Evaluate system efficacy through statistical performance metrics (R², RMSE, MAE), conduct economic and social utility assessments, and map project outcomes to UN Sustainable Development Goals.")
    ],
    'matrix': [
        # CO, PO1, PO2, PO3, PO4, PO5, PO6, PO7, PO8, PO9, PO10, PO11, PO12, PSO1, PSO2
        ["CO1", "3", "3", "2", "2", "1", "3", "3", "1", "1", "2", "2", "3", "3", "2"],
        ["CO2", "3", "3", "3", "3", "3", "2", "2", "1", "2", "2", "1", "3", "3", "3"],
        ["CO3", "3", "2", "3", "2", "3", "2", "1", "2", "3", "2", "2", "3", "3", "2"],
        ["CO4", "3", "2", "3", "2", "3", "2", "2", "3", "2", "3", "1", "3", "3", "2"],
        ["CO5", "2", "3", "2", "3", "2", "3", "3", "2", "2", "3", "3", "3", "2", "3"],
    ],
    'justification': (
        "Justification of CO-PO-PSO Mapping:\n"
        "• PO1 (Engineering Knowledge) is strongly addressed (Level 3) across all COs through the rigorous application of mathematics, computing fundamentals, and regression algorithms.\n"
        "• PO2 (Problem Analysis) and PO3 (Design/Development of Solutions) are addressed at Level 3 through comprehensive requirement engineering, soil chemistry modelling, and full-stack software architecture.\n"
        "• PO4 (Investigations of Complex Problems) and PO5 (Modern Tool Usage) correlate strongly with the deployment of Scikit-Learn, Random Forest ensembles, MongoDB, Node.js, and WebSocket communication.\n"
        "• PO6 (Engineer & Society) and PO7 (Environment & Sustainability) receive high mapping (Level 3) because Cotton Mitra directly empowers distressed smallholder farmers and promotes soil conservation through balanced fertilization.\n"
        "• PO8 (Ethics) is addressed via AES-256 end-to-end cryptographic privacy for farm trade negotiations.\n"
        "• PO11 & PO12 (Project Management & Lifelong Learning) are achieved through full product-lifecycle implementation and adaptation to dynamic agritech advances.\n"
        "• PSO1 & PSO2 (Computer Science & Applied AI) correlate at Level 3 due to state-of-the-art enterprise software engineering and data science integration."
    )
}

LIST_OF_TABLES = [
    ("Table 1.1", "Functional and Non-Functional Technical Specifications of Cotton Mitra", "2"),
    ("Table 2.1", "Comparative Analysis of Existing Agritech Platforms vs. Cotton Mitra", "6"),
    ("Table 3.1", "Cotton Mitra Multi-Tier Architectural Technology Stack", "16"),
    ("Table 3.2", "Econometric and Environmental Features for ML Forecast Model", "25"),
    ("Table 4.1", "Soil Physicochemical Parameters and Cotton Agro-Ecological Thresholds", "29"),
    ("Table 4.2", "Soil Nutrient Fertility Rating Classes and Fertilizer Adjustment Factors", "41"),
    ("Table 4.3", "Commercial Fertilizer Formulations and Nutrient Conversion Equivalents", "44"),
    ("Table 4.4", "Recommended Stage-Wise Split Fertilizer Application Schedule for Cotton", "48"),
    ("Table 5.1", "Performance Benchmark of Predictive Regression Models on Cotton Dataset", "55"),
    ("Table 5.2", "Quarterly Cotton Consumption Forecast and Trend Projection Summary", "57"),
    ("Table 5.3", "Warehouse Environmental Telemetry Thresholds and Risk Classifications", "60"),
    ("Table 6.1", "Cotton Mitra Direct Alignment Matrix with UN Sustainable Development Goals", "68")
]

LIST_OF_FIGURES = [
    ("Figure 1.1", "Cotton Supply Chain Information Asymmetry and Stakeholder Disconnect", "2"),
    ("Figure 2.1", "Evolutionary Paradigm from Traditional Agriculture to Cyber-Physical Agritech", "4"),
    ("Figure 3.1", "Cotton Mitra Dual-Portal High-Level System Architecture", "9"),
    ("Figure 3.2", "Complete End-to-End Operational Workflow of the Cotton Mitra Platform", "20"),
    ("Figure 3.3", "Layered Microservices and Data Flow Architecture", "22"),
    ("Figure 3.4", "Data Preprocessing, Temporal Sorting, and Lag Feature Engineering Pipeline", "24"),
    ("Figure 4.1", "Precision Crop Recommendation Diagnostic Processing Pipeline", "29"),
    ("Figure 4.2", "Random Forest Regressor Decision Tree Ensemble and Bootstrap Aggregation", "32"),
    ("Figure 4.3", "Flask Machine Learning REST Microservice Architecture and Endpoint Topology", "36"),
    ("Figure 4.4", "Algorithmic Flowchart for Soil-Test Crop Response (STCR) Fertilizer Engine", "43"),
    ("Figure 4.5", "Automated Soil Health Card and Diagnostic Output Generation Pipeline", "50"),
    ("Figure 5.1", "Actual vs. Predicted Monthly Cotton Consumption in India (2025–2026)", "56"),
    ("Figure 5.2", "Warehouse Ambient Humidity and Temperature Telemetry Distribution", "60"),
    ("Figure 6.1", "Cotton Mitra Socio-Economic Value Creation Framework for Farming Communities", "67")
]
