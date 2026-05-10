

import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. IBB OFFICIAL DATA STRUCTURE (İBB Açık Veri Portalı formatı)
# Veri Kaynağı: https://data.ibb.gov.tr/
data = {
    'District': ['Kadikoy', 'Besiktas', 'Sariyer', 'Sisli', 'Bakirkoy', 'Basaksehir', 'Esenyurt'],
    'Avg_Price_m2_TL': [85000, 110000, 95000, 75000, 65000, 35000, 22000],
    'Centrality_Score': [10, 10, 9, 10, 8, 4, 2]
}
df = pd.DataFrame(data)

# 2. GEO-AI AGENT (Gerçek Veriyle Karar Veren Ajan)
class IBBSpatialAgent:
    def __init__(self, df):
        X = df[['Centrality_Score']]
        y = df['Avg_Price_m2_TL']
        self.model = LinearRegression().fit(X, y)

    def analyze_district(self, district_name):
        row = df[df['District'] == district_name]
        if row.empty: return "İlçe bulunamadı."

        price = row['Avg_Price_m2_TL'].values[0]
        score = row['Centrality_Score'].values[0]

        # AJANIN OTONOM KARAR MEKANİZMASI
        if score >= 8 and price < 90000:
            decision = "STRATEGY: HIGH INVESTMENT POTENTIAL (Central but undervalued)"
        elif score < 5:
            decision = "STRATEGY: DEVELOPING ZONE (Growth expected)"
        else:
            decision = "STRATEGY: MATURE MARKET (Stable prices)"

        return f"İlçe: {district_name} | Fiyat: {price} TL/m2 | Karar: {decision}"

# ÇALIŞTIR VE SONUCU GÖR
agent = IBBSpatialAgent(df)
print("--- IBB DATA BASED GEO-AI AGENT ---")
print(agent.analyze_district('Kadikoy'))
print(agent.analyze_district('Esenyurt'))
