# -*- coding: utf-8 -*-
"""
Cotton Mitra Project Report - Content for Chapter 1 and Chapter 2
"""

CHAPTER_1_CONTENT = {
    '1.1': [
        (
            "Cotton (Gossypium hirsutum L.), popularly revered as 'White Gold', is among the most pivotal "
            "commercial cash crops globally and forms the bedrock of India's agrarian economy and textile industrial sector. "
            "India holds the distinguished status of being the world's largest producer and second-largest exporter of cotton, "
            "supporting the livelihoods of over 6 million smallholder farmers directly and employing more than 50 million "
            "people in allied ginning, spinning, processing, and garmenting industries across prominent cotton belts such as "
            "Vidarbha and Marathwada in Maharashtra, Gujarat, Telangana, and Punjab. Despite its immense economic footprint, "
            "cotton cultivation and its subsequent post-harvest management remain fraught with systemic vulnerabilities, "
            "structural information asymmetry, and technological disenfranchisement."
        ),
        (
            "The traditional cotton farming cycle is characterized by fragmented decision-making. At the pre-sowing stage, "
            "farmers routinely face severe uncertainty regarding soil chemical balance, optimal crop rotation compatibility, "
            "and precise mineral nutrition. This often leads to either catastrophic crop failures or excessive, uncalibrated "
            "fertilizer applications that deplete farmer capital and degrade arable soil quality. At the post-harvest stage, "
            "the lack of decentralized scientific storage facilities forces growers into immediate distress selling to local "
            "middlemen (Adatyas and commission agents) at prices drastically below the Minimum Support Price (MSP) or ruling "
            "spot market indices. Meanwhile, warehouse operators struggle with suboptimal inventory tracking, unmonitored "
            "storage microclimates that trigger microbial fiber degradation, and an absence of data-driven demand forecasting."
        ),
        (
            "Cotton Mitra ('Friend of the Cotton Farmer') is conceived and engineered as an innovative, end-to-end "
            "cyber-physical software ecosystem that bridges the structural divide between grassroots cotton producers and "
            "commercial warehouse managers. By unifying machine learning-powered econometric forecasting, precision soil "
            "nutrient diagnostic engines, real-time Internet of Things (IoT) warehouse environmental telemetry, automated "
            "inventory aging risk management, and peer-to-peer end-to-end encrypted direct negotiation channels, Cotton Mitra "
            "transforms the traditional fragmented cotton supply chain into a transparent, scientifically managed, and "
            "digitally orchestrated agri-industrial network."
        )
    ],
    '1.2': [
        (
            "The modern cotton ecosystem in developing agricultural nations like India suffers from four acute, interrelated "
            "systemic crises that compromise farming sustainability and supply chain efficiency:"
        ),
        (
            "1. Severe Soil Degradation and Unscientific Nutrient Management: Due to lack of accessible, personalized soil "
            "testing facilities and automated advisory systems, farmers predominantly rely on empirical guesswork or retailer-driven "
            "recommendations. This results in severe nitrogen over-application, micronutrient depletion (particularly Zinc, Boron, "
            "and Magnesium), soil acidification, and groundwater contamination, alongside escalating operational input expenditures."
        ),
        (
            "2. Exploitative Intermediation and Price Asymmetry: Smallholder cotton growers have virtually zero direct communication "
            "channels with institutional buyers or modern warehouse facilities. Exploitative intermediary networks capitalize on "
            "this structural gap, extracting massive commissions (often 12% to 20% of net produce value) while imposing arbitrary "
            "quality grading deductions that push farmers into cyclical rural indebtedness."
        ),
        (
            "3. Post-Harvest Storage Loss and Fiber Degradation: Cotton is a highly hygroscopic organic fiber exceptionally "
            "vulnerable to ambient humidity and temperature fluctuations. In traditional unmonitored godowns and warehouses, "
            "uncontrolled relative humidity exceeding 60% leads to lint yellowing, microbial mold growth, staple fiber tensile "
            "weakening, and spontaneous combustion hazards. Furthermore, the absence of automated aging lot tracking results in "
            "cotton bales lingering beyond 90 days, suffering steep commercial depreciation."
        ),
        (
            "4. Absence of Accessible Predictive Market Intelligence: Warehouse managers and farming cooperatives lack localized, "
            "predictive forecasting models that synthesize macroeconomic trends, textile industrial indices, historical price lags, "
            "and seasonal precipitation patterns. Consequently, inventory procurement and release decisions remain purely reactive, "
            "causing catastrophic bullwhip effects across the agricultural supply chain."
        )
    ],
    '1.3': [
        (
            "To resolve the multifaceted challenges outlined in the problem statement, the Cotton Mitra project sets forth "
            "the following primary research and engineering objectives:"
        ),
        (
            "1. Develop an Intelligent Precision Agronomy Module: Formulate an automated, soil-test crop response (STCR) "
            "fertilizer recommendation engine that ingests soil physicochemical parameters (Nitrogen, Phosphorus, Potassium, pH) "
            "and generates scientifically optimized, stage-wise commercial fertilizer doses (Urea, DAP, MOP, SSP) with detailed "
            "soil health scoring cards."
        ),
        (
            "2. Design and Deploy a Machine Learning Forecasting Engine: Train and validate an advanced Random Forest Regression "
            "model utilizing historical Indian cotton market indicators, temporal lags, textile industry indices, and rainfall "
            "covariates to deliver high-accuracy, 3-month multi-step rolling forecasts of national cotton consumption and demand trends."
        ),
        (
            "3. Architect a Decoupled Multi-Tier Cloud Software Architecture: Build an asynchronous full-stack enterprise platform "
            "combining a high-performance Node.js/Express application gateway, an independent Python/Flask machine learning microservice, "
            "and a MongoDB document database supporting dual responsive web portals tailored for Farmers and Warehouse Managers."
        ),
        (
            "4. Implement Real-Time Environmental Telemetry and Inventory Aging Analytics: Construct a proactive warehouse "
            "monitoring subsystem that tracks ambient relative humidity and temperature, automatically generates severity-graded "
            "alerts upon critical threshold breaches, and dynamically identifies aging lots exceeding 90 days of storage."
        ),
        (
            "5. Establish Secure Peer-to-Peer Direct Communication Channels: Integrate duplex WebSocket connections (Socket.IO) "
            "and AES-256 client-side payload encryption to facilitate real-time, transparent, and private price negotiations and delivery "
            "scheduling directly between farmers and certified warehouse operators, eliminating exploitative middlemen."
        ),
        (
            "6. Deploy a Natural Language Agricultural Knowledge Assistant: Implement an embedded, context-aware rule-based AI "
            "assistant capable of parsing farmer and warehouse operator natural language inquiries regarding inventory valuation, "
            "reorder planning (ROL), quality grade distributions, and microclimatic storage health."
        )
    ]
}

CHAPTER_2_CONTENT = {
    '2.1': [
        (
            "The integration of digital information technology, artificial intelligence, and smart logistics into agriculture "
            "— collectively recognized as Agriculture 4.0 or Smart Agritech — has emerged as one of the most transformative paradigms "
            "of the modern era. To establish a rigorous theoretical and empirical foundation for the Cotton Mitra architecture, "
            "this literature review synthesizes prior research across four core technical domains: Machine Learning in Crop Modeling, "
            "Decision Support Systems for Soil Nutrient Management, Smart Warehousing & Storage Telemetry, and Digital Disintermediation "
            "in Agricultural Supply Chains."
        ),
        (
            "2.1.1 Machine Learning and AI in Precision Crop Modeling:\n"
            "Machine learning algorithms have been extensively applied to agricultural yield prediction, crop suitability classification, "
            "and price forecasting. Wolfert et al. (2017) conducted a comprehensive survey on big data applications in smart farming, "
            "demonstrating that predictive machine learning models offer superior generalization compared to classical biophysical "
            "simulation frameworks (such as DSSAT and APSIM) when operating on real-world, noisy agro-climatic datasets. Kamilaris and "
            "Prenafeta-Boldú (2018) highlighted the efficacy of ensemble decision tree architectures, specifically Random Forest (RF) and "
            "Gradient Boosted Trees, in modeling non-linear agronomic relationships. In the context of cash crops, studies by Sharma et al. "
            "(2020) demonstrated that Random Forest regression consistently outperforms classical Autoregressive Integrated Moving Average "
            "(ARIMA) models in agricultural commodity forecasting by effectively capturing exogenous covariates such as precipitation anomalies, "
            "industrial demand shifts, and historical price autoregression without suffering from stationarity constraints."
        ),
        (
            "2.1.2 Soil Nutrient Analysis and Decision Support Systems:\n"
            "Site-Specific Nutrient Management (SSNM) and Soil Test Crop Response (STCR) methodologies represent the pinnacle of scientific "
            "fertilization. Ramamoorthy et al. pioneered the STCR approach in India, establishing targeted yield equations that correlate "
            "initial soil available nutrients (N, P, K) with crop nutrient uptake efficiencies. Recent investigations by Pathak et al. (2021) "
            "emphasized that blanket fertilizer recommendations formulated at national or provincial levels fail to account for field-level "
            "heterogeneity, resulting in severe nutrient use inefficiencies. Modern mobile and web-based decision support platforms have "
            "attempted to digitize STCR equations; however, existing commercial tools often present complex, confusing chemical terminology "
            "to rural farmers without translating elemental deficits into practical, commercially available fertilizer bags (e.g., Urea, "
            "DAP, MOP) or providing growth-stage-specific split application guidelines tailored to cotton's extended phenological cycle."
        ),
        (
            "2.1.3 Smart Warehousing, IoT Telemetry, and Post-Harvest Management:\n"
            "Post-harvest management is a critical determinant of commercial fiber quality. Cotton lint possesses high moisture regain "
            "capacity (typically 7% to 8.5% at standard conditions). Research by Anthony (2018) on cotton ginning and storage demonstrated "
            "that maintaining storage relative humidity between 50% and 55% at temperatures between 20°C and 25°C is vital to prevent staple "
            "fiber brittleness, yellowing (color grade degradation), and bacterial degradation. Pal and Kant (2019) reviewed IoT-based wireless "
            "sensor networks (WSN) in grain and fiber warehouses, showing that real-time multi-point telemetry significantly reduces spoilage "
            "events. Nevertheless, traditional warehouse management systems (WMS) remain isolated industrial enterprise systems designed solely "
            "for internal accounting, completely detached from the primary producers who supply the raw commodity."
        ),
        (
            "2.1.4 Supply Chain Disintermediation and Agricultural Market Platforms:\n"
            "The traditional agricultural marketing system in South Asia is notoriously dominated by multi-layered intermediary cartels. "
            "The Government of India's electronic National Agriculture Market (e-NAM) initiative represents a significant step toward "
            "pan-India electronic trading. However, empirical assessments by Reddy and Chand (2020) revealed that smallholder farmers face "
            "formidable barriers to entry on central trading portals due to lack of localized storage tie-ups, complex bidding mechanisms, "
            "and the absence of end-to-end communication channels with warehouse custodians. Peer-to-peer digital communication systems "
            "incorporating cryptographic privacy and mobile authentication have been widely advocated by agritech researchers as the most "
            "promising mechanism to democratize farm trade."
        ),
        (
            "2.1.5 Synthesis of Research Gaps and Cotton Mitra Value Proposition:\n"
            "An exhaustive review of contemporary academic literature and commercial agritech solutions identifies three critical "
            "research and engineering voids: (1) The complete disconnect between pre-harvest crop agronomy advisory and post-harvest "
            "storage economics; (2) The lack of localized, lag-aware econometric forecasting models embedded directly within farmer-facing "
            "dashboards; and (3) The absence of an integrated, cryptographically secure direct negotiation channel linking farmers with "
            "certified regional warehouse managers. Cotton Mitra explicitly bridges these gaps by synthesizing these disparate domains "
            "into a cohesive, cloud-native, and accessible cyber-physical ecosystem."
        )
    ]
}
