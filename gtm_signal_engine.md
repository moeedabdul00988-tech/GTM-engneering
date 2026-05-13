## GTM Signal Engine — Funding Pipeline

### Problem
Automatically identify and route companies that raise funding rounds.

### Pipeline
Webhook → Score → Route → HubSpot → Slack

### Scoring Logic
- Funding ≥ $5M: 80 points
- Funding $1M-$5M: 60 points  
- Funding < $1M: 20 points
- Employees ≥ 500: +40 points
- Employees > 100: +25 points
- Employees > 20: +10 points

### Routing
- Score ≥ 80: Hot → Senior AE + Slack alert
- Score ≥ 50: Warm → Junior AE
- Score < 50: Cold → Nurture

### Tools
Python, Make.com, HubSpot CRM, Slack
