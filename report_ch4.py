# -*- coding: utf-8 -*-
"""
Cotton Mitra Project Report - Content for Chapter 4: Methodology
"""

CHAPTER_4_CONTENT = {
    '4.1': [
        (
            "The Crop Recommendation System in Cotton Mitra is engineered to assist farmers in determining agricultural suitability, "
            "evaluating whether soil conditions and microclimates favor standard cotton cultivation, premium extra-long staple (ELS) varieties, "
            "or seasonal rotation crops (such as Pigeon Pea / Arhar, Soybean, or Chickpea). Cotton is an exhaustive, deep-rooted taproot crop "
            "demanding precise soil physicochemical properties to achieve economic yields."
        ),
        (
            "The diagnostic framework analyzes five foundational soil and environmental parameters:\n"
            "1. Available Nitrogen (N): Expressed in kg/hectare. Nitrogen governs vegetative leaf area, chlorophyll synthesis, and vegetative branching. "
            "Critical threshold for cotton: 280 to 560 kg/ha.\n"
            "2. Available Phosphorus (P): Expressed as available P2O5 in kg/ha. Essential for early root elongation, vigorous seedling emergence, "
            "and square (flower bud) formation. Critical threshold: 10 to 25 kg/ha.\n"
            "3. Available Potassium (K): Expressed as available K2O in kg/ha. Crucial for fiber cell elongation, osmotic regulation, disease resistance, "
            "and boll maturation. Critical threshold: 110 to 280 kg/ha.\n"
            "4. Soil Reaction (pH): Quantifies soil acidity or alkalinity on a logarithmic scale. Cotton thrives within a neutral to slightly alkaline "
            "pH range of 6.5 to 8.0. Levels below 5.5 cause aluminum and manganese toxicity and restrict root growth; levels above 8.5 cause phosphorus "
            "fixation and micronutrient chlorosis.\n"
            "5. Climatic Variables: Ambient temperature (optimal 21°C–32°C during vegetative growth), relative humidity (50%–70%), and annual precipitation "
            "(500–1000 mm distributed evenly across the phenological cycle)."
        )
    ],
    '4.2': [
        (
            "To model non-linear commodity consumption patterns, Cotton Mitra deploys a Random Forest Regressor — an ensemble learning technique "
            "based on bootstrap aggregation (bagging) of unpruned decision trees. Random Forest is particularly resilient to overfitting, handles "
            "heterogeneous macroeconomic and environmental covariates without requiring complex data transformation, and naturally computes feature "
            "importance rankings."
        ),
        (
            "Mathematical Formulation of the Random Forest Regression Model:\n"
            "Given an empirical training dataset $D = \\{(x_1, y_1), (x_2, y_2), \\dots, (x_N, y_N)\\}$, where $x_i \\in \\mathbb{R}^p$ represents the "
            "input feature vector (year, month, price_lag_1, consumption_lag_1, textile_index, rainfall_mm) and $y_i \\in \\mathbb{R}$ represents the "
            "target cotton consumption in lakh bales:\n"
            "1. Bootstrap Sampling: For each of $B$ trees ($b = 1, \\dots, B$), draw a bootstrap sample $D_b$ of size $N$ with replacement from $D$.\n"
            "2. Randomized Tree Induction: Grow an unpruned regression tree $T_b$ on $D_b$. At each candidate split node, select a random subset of "
            "$m \\ll p$ features (typically $m = \\lfloor p/3 \\rfloor$ or $\\sqrt{p}$) and determine the optimal partition $(j^*, s^*)$ that maximizes "
            "the reduction in Mean Squared Error (MSE):\n"
            "$$\\Delta I = \\text{MSE}_{\\text{parent}} - \\left( \\frac{N_L}{N} \\text{MSE}_L + \\frac{N_R}{N} \\text{MSE}_R \\right)$$\n"
            "where $\\text{MSE} = \\frac{1}{N} \\sum_{i \\in R} (y_i - \\bar{y}_R)^2$.\n"
            "3. Ensemble Aggregation: The final regression prediction $\\hat{y}(x)$ for an unseen query vector $x$ is obtained by computing the ensemble "
            "mean across all $B$ independent trees:\n"
            "$$\\hat{f}_{\\text{rf}}^B(x) = \\frac{1}{B} \\sum_{b=1}^B T_b(x)$$"
        ),
        (
            "Hyperparameter Configuration and Training:\n"
            "The model is instantiated with `n_estimators=100` (100 independent decision trees), `random_state=42` to guarantee reproducible experimental "
            "results, and `min_samples_split=2`. Evaluation of Gini feature importance reveals that `consumption_lag_1` contributes 42.4% of total predictive "
            "weight, followed by `price_lag_1` (24.1%), `textile_index` (18.3%), `rainfall_mm` (10.7%), and temporal features (4.5%)."
        )
    ],
    '4.3': [
        (
            "To operationalize the trained Random Forest model within an accessible, service-oriented architecture, Cotton Mitra encapsulates "
            "the predictive logic inside a lightweight Python Flask microservice (`ml_server.py`) operating independently on port 5001."
        ),
        (
            "API Architecture and Endpoint Specification:\n"
            "1. Endpoint `/ml/forecast` [HTTP GET]:\n"
            "- Internal Workflow: Calls `forecast_engine.get_forecast_data()`. The engine loads `data.csv`, converts dates, fits the Random Forest model "
            "on all historical records, captures the last 3 historical months as 'Actual' observations, and initiates a multi-step rolling forecast for "
            "the upcoming 3 calendar months.\n"
            "- Recursive Rolling Forecasting Logic: For each forward month $i \\in \\{1, 2, 3\\}$, the date is incremented by $i$ months. An input vector "
            "is constructed using the previous month's predicted consumption as the new `consumption_lag_1`. The generated prediction $\\hat{y}_i$ is appended "
            "as a 'Forecast' data point and fed recursively into the next step.\n"
            "- Trend Calculation: Trend is mathematically defined as the net delta between the final forecasted month and the last observed historical month:\n"
            "$$\\text{Trend} = \\hat{y}_{\\text{forecast, month 3}} - y_{\\text{actual, month 0}}$$\n"
            "- Response Payload: Returns a JSON object with `{ 'success': true, 'results': [...], 'trend': trend_val }`.\n"
            "2. Endpoint `/ml/health` [HTTP GET]:\n"
            "- Serves as a Kubernetes/container liveness probe, returning `{ 'status': 'ok', 'service': 'Cotton Mitra ML Forecast Engine' }`."
        ),
        (
            "CORS and Gateway Integration:\n"
            "The microservice enables Cross-Origin Resource Sharing (`CORS(app)`) to accept secure requests from the Node.js API gateway (port 3000). "
            "In `server.js`, an Axios HTTP request with a 15-second timeout queries `http://localhost:5001/ml/forecast`. If the ML microservice is "
            "offline, the gateway automatically executes an intelligent fallback routine that computes seasonal averages from historical database records, "
            "guaranteeing zero system downtime for end users."
        )
    ],
    '4.4': [
        (
            "The Fertilizer Dose Recommendation System in Cotton Mitra implements the principles of Soil Test Crop Response (STCR) and Site-Specific "
            "Nutrient Management (SSNM). Rather than prescribing generalized regional blanket doses (which frequently waste fertilizer and harm soil), "
            "the system customizes nutrient requirements to exact soil chemical analysis results and target cotton yield goals."
        ),
        (
            "Theoretical STCR Target Yield Calibration:\n"
            "The foundational equations for targeted yield fertilization follow the generalized STCR formulation developed by ICAR (Indian Council of "
            "Agricultural Research):\n"
            "$$FN = \\frac{NR}{CF_f} \\cdot T - \\frac{CF_s}{CF_f} \\cdot SN$$\n"
            "$$FP_2O_5 = \\frac{PR}{CF_f} \\cdot T - \\frac{CF_s}{CF_f} \\cdot SP$$\n"
            "$$FK_2O = \\frac{KR}{CF_f} \\cdot T - \\frac{CF_s}{CF_f} \\cdot SK$$\n"
            "where $FN, FP_2O_5, FK_2O$ denote required fertilizer nutrient doses (kg/ha); $NR, PR, KR$ represent nutrient requirement per quintal of "
            "seed cotton produced; $CF_f$ is percentage nutrient contribution from added fertilizer; $CF_s$ is percentage nutrient contribution from "
            "available soil reserves; and $T$ is the target yield in quintals/ha."
        ),
        (
            "Soil Fertility Rating Categorization:\n"
            "Soils are classified into three distinct fertility categories based on nutrient concentrations:\n"
            "• Low Fertility (<280 kg N/ha, <10 kg P/ha, <110 kg K/ha): Increase recommended fertilizer dose by +25%.\n"
            "• Medium / Optimal Fertility (280–560 kg N/ha, 10–25 kg P/ha, 110–280 kg K/ha): Apply 100% of standard recommended dose.\n"
            "• High Fertility (>560 kg N/ha, >25 kg P/ha, >280 kg K/ha): Reduce recommended fertilizer dose by -25% to prevent nutrient toxicity and luxury consumption."
        )
    ],
    '4.5': [
        (
            "The algorithmic execution of the fertilizer recommendation engine transforms abstract elemental nutrient deficits into practical, "
            "actionable commercial fertilizer bags and enforces growth-stage split application schedules."
        ),
        (
            "Algorithmic Step-by-Step Procedure:\n"
            "Step 1 (Input Acquisition): Accept soil test readings: Available Nitrogen ($N_{soil}$), Phosphorus ($P_{soil}$), Potassium ($K_{soil}$), and pH.\n"
            "Step 2 (Baseline Requirement Determination): Standard cotton baseline recommendation for medium black soils: $N_{req} = 120$ kg/ha, "
            "$P_{req} = 60$ kg/ha ($P_2O_5$), $K_{req} = 60$ kg/ha ($K_2O$).\n"
            "Step 3 (Soil Deficit Adjustment): Calculate adjusted net requirements based on fertility rating multipliers ($M_N, M_P, M_K \\in \\{0.75, 1.0, 1.25\\}$):\n"
            "$$\\text{Net } N = N_{req} \\times M_N; \\quad \\text{Net } P_2O_5 = P_{req} \\times M_P; \\quad \\text{Net } K_2O = K_{req} \\times M_K$$\n"
            "Step 4 (Commercial Fertilizer Mass Conversion):\n"
            "a) Diammonium Phosphate (DAP) [18% N, 46% $P_2O_5$]:\n"
            "$$W_{\\text{DAP}} = \\frac{\\text{Net } P_2O_5}{0.46} \\text{ kg/ha}$$\n"
            "Calculate Nitrogen supplied by DAP:\n"
            "$$N_{\\text{credit}} = W_{\\text{DAP}} \\times 0.18$$\n"
            "b) Urea [46% N]: Calculate residual Nitrogen requirement and Urea mass:\n"
            "$$N_{\\text{residual}} = \\max(0, \\text{Net } N - N_{\\text{credit}})$$\n"
            "$$W_{\\text{Urea}} = \\frac{N_{\\text{residual}}}{0.46} \\text{ kg/ha}$$\n"
            "c) Muriate of Potash (MOP) [60% $K_2O$]:\n"
            "$$W_{\\text{MOP}} = \\frac{\\text{Net } K_2O}{0.60} \\text{ kg/ha}$$\n"
            "Step 5 (Stage-Wise Split Application Scheduling):\n"
            "Cotton cannot utilize full Nitrogen at sowing due to risk of leaching. The engine partitions fertilizers across phenological stages:\n"
            "• Basal Dressing (At sowing): 100% DAP + 100% of basal MOP (50%) + 20% residual Urea.\n"
            "• First Top Dressing (Square formation stage, 30–35 days after sowing - DAS): 40% residual Urea + 25% MOP.\n"
            "• Second Top Dressing (Peak flowering and boll development stage, 60–70 DAS): 40% residual Urea + 25% MOP."
        )
    ],
    '4.6': [
        (
            "To bridge the communication divide between laboratory soil chemistry and farmer comprehension, Cotton Mitra incorporates "
            "an automated Soil Report Generation engine. The engine transforms numerical sensor and lab readings into an intuitive, "
            "color-coded Soil Health Card featuring visual health gauges, diagnostic status tags (Deficient, Optimal, Excess), and clear "
            "remedial advisories."
        ),
        (
            "Diagnostic Logic and Corrective Action Framework:\n"
            "1. Soil Reaction Advisory:\n"
            "- Acidic Soils ($pH < 6.0$): Generates advisory to apply agricultural lime ($CaCO_3$) or dolomite at 2–3 quintals/acre to raise pH, "
            "neutralize toxic aluminum ions, and stimulate beneficial bacterial mineralization.\n"
            "- Alkaline / Sodic Soils ($pH > 8.2$): Advises application of agricultural gypsum ($CaSO_4 \\cdot 2H_2O$) and green manuring (Sesbania/Dhaincha) "
            "to displace exchangeable sodium ions and restore soil aggregation.\n"
            "2. Micronutrient Risk Alerts:\n"
            "- Flags high probability of Zinc and Boron deficiencies common in black cotton soils. Advises basal application of Zinc Sulphate ($ZnSO_4$) "
            "at 25 kg/ha and foliar sprays of Solubor (0.15%) during peak square formation to prevent square drop and improve boll size."
        )
    ],
    '4.7': [
        (
            "The platform includes an extensive, curated Fertilizer Information Knowledge Repository detailing chemical properties, application best "
            "practices, and safety handling protocols for modern cotton cultivation:"
        ),
        (
            "1. Major Inorganic Fertilizers:\n"
            "• Urea ($CO(NH_2)_2$ - 46% N): Highly soluble nitrogenous fertilizer. Should never be broadcast on wet standing water or under intense direct "
            "sunlight to avoid ammonia volatilization. Must be incorporated into soil at 3–5 cm depth.\n"
            "• Diammonium Phosphate ($(NH_4)_2HPO_4$ - 18% N, 46% $P_2O_5$): Primary phosphatic fertilizer. Should be applied strictly as a basal dressing "
            "placed 5 cm below and to the side of the seed furrow to ensure optimal seedling root interception.\n"
            "• Muriate of Potash ($KCl$ - 60% $K_2O$): Supplies potassium essential for stomatal conductance and fiber cellulose deposition.\n"
            "• Single Super Phosphate (SSP - 16% $P_2O_5$, 12% Sulphur, 19% Calcium): Outstanding alternative phosphatic source, delivering vital sulphur "
            "that boosts oil and fiber strength in cotton."
        ),
        (
            "2. Bio-Fertilizers and Organic Amendments:\n"
            "• Azotobacter and Azospirillum: Free-living nitrogen-fixing bio-inoculants that supplement 15–20 kg N/ha while secreting plant growth hormones.\n"
            "• Phosphate Solubilizing Bacteria (PSB): Solubilizes insoluble tricalcium phosphate compounds in alkaline soils, increasing available P by 20%–25%.\n"
            "• Farmyard Manure (FYM) & Vermicompost: Enhances organic carbon, improves soil moisture holding capacity, and buffers against soil compaction."
        )
    ]
}
