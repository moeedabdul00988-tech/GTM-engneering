## GTM Lead Scoring & Routing Pipeline (Make.com)

### What it does
Automatically scores, routes, and creates CRM contacts for inbound leads.

### Pipeline flow
Webhook → Score Lead → Route by Tier → Create HubSpot Contact → Slack Alert

### Scoring logic
- Company size: up to 40 points
- Lead source: up to 40 points  
- Uses Salesforce: 20 points

### Routing
- Score ≥ 80: Hot → Senior AE + Slack alert
- Score ≥ 50: Warm → Junior AE
- Score < 50: Cold → Nurture sequence

### Tools used
Make.com, HubSpot CRM, Slack
