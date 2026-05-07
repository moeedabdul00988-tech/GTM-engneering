import json

leads = [
    {"email": "ali@techcorp.com", "firstname": "Ali", "lastname": "Hassan", "company": "TechCorp", "employees": 500, "source": "Referral", "uses_salesforce": True},
    {"email": "sara@growfast.com", "firstname": "Sara", "lastname": "Khan", "company": "GrowFast", "employees": 8, "source": "Paid Ad", "uses_salesforce": False},
    {"email": "john@enterprise.com", "firstname": "John", "lastname": "Smith", "company": "Enterprise Co", "employees": 1200, "source": "Demo Request", "uses_salesforce": True}
]

def validate(lead):
    if not lead["email"]:
        raise ValueError("Email required")
    if "@" not in lead["email"]:
        raise ValueError("Invalid email")
    return True

def score_lead(lead):
    score = 0
    if lead["employees"] >= 500:
        score += 40
    elif lead["employees"] > 100:
        score += 25
    elif lead["employees"] > 20:
        score += 10
    if lead["source"] == "Demo Request":
        score += 40
    elif lead["source"] == "Referral":
        score += 30
    elif lead["source"] == "Organic":
        score += 20
    else:
        score += 5
    if lead["uses_salesforce"] == True:
        score += 20
    return score

def route_lead(score):
    if score >= 80:
        return "🔥 Hot → Senior AE"
    elif score >= 50:
        return "Warm → Junior AE"
    else:
        return "Cold → Nurture Sequence"

def create_contact(lead, score, route, contact_id):
    return {
        "id": contact_id,
        "status": "created",
        "email": lead["email"],
        "score": score,
        "assigned_to": route
    }

for index, lead in enumerate(leads):
    try:
        validate(lead)
        score = score_lead(lead)
        route = route_lead(score)
        contact = create_contact(lead, score, route, 10000 + index)

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("GTM PIPELINE — LEAD PROCESSED")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"Name:        {lead['firstname']} {lead['lastname']}")
        print(f"Company:     {lead['company']} ({lead['employees']} employees)")
        print(f"Source:      {lead['source']}")
        print(f"Score:       {contact['score']}")
        print(f"Assigned:    {contact['assigned_to']}")
        print(f"CRM ID:      {contact['id']}")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    except ValueError as e:
        print(f"❌ Pipeline failed: {e}")
