def score_funding(company):
    score = 0
    if company["employees"] >= 50:
        score += 40
    elif company["employees"] < 50:
        score += 20
   
    if company["business_type"] == "saas":
        score += 10
    elif company["business_type"] != "saas":
        score += 5
    return score

def route_lead(score):
    if score >= 50:
        return "🔥 High Priority"
    else: 
        return "Normal"
    


company = {
    "name": "TechStartup Inc",
    "business_type": "saas",
    "employees": 80
}


score = score_funding(company)
route = route_lead(score)

print(f"name: {company['name']}")   
print(f"business_type: {company ['business_type']}")
print(f"employees: {company['employees']}")
print(f"Score: {score}")
print(f"Route: {route}")
