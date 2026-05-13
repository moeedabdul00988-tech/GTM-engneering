def score_funding(company):
    score = 0
    if company["funding"] >= 5000000:
        score += 80
    elif company["funding"] >= 1000000:
        score += 60
    elif company["funding"] < 1000000:
        score += 20
    if company["employees"] >= 500:
        score += 40
    elif company["employees"] > 100:
        score += 25
    elif company["employees"] > 20:
        score += 10
    return score

def route_lead(score):
    if score >= 80:
        return "🔥 Hot → Senior AE"
    elif score >= 50:
        return "Warm → Junior AE"
    else:
        return "Cold → Nurture Sequence"

companies = [
    {"name": "BigRaise Co", "domain": "bigraise.io", "funding": 8000000, "employees": 200},
    {"name": "MidStage Inc", "domain": "midstage.io", "funding": 2000000, "employees": 45},
    {"name": "Tiny Startup", "domain": "tiny.io", "funding": 500000, "employees": 8}
]

for company in companies:
    score = score_funding(company)
    route = route_lead(score)
    print(f"{company['name']} | ${company['funding']:,} | Score: {score} | {route}")
