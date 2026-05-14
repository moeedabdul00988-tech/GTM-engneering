def score_funding(prospect):
    score = 0
    
    if prospect["employees"] >= 100:
        score += 50
    else:
        score += 20
    
    if prospect["industry"] == "SaaS":
        score += 10
    else:
        score += 0
    
    if prospect["title"] == "VP of Sales" or prospect["title"] == "Head of Sales":
        score += 20
    else:
        score += 0
    
    return score
          
    

def route_lead(score):
    if score >= 80:
        return "Perfect Client"
    else: 
        return "Not my lead"
    
prospect = {
    "name": "John Smith",
    "email": "john@techco.com",
    "company": "TechCo",
    "industry": "SaaS",
    "employees": 15,
    "title": "VP of Sales"
}


score = score_funding(prospect)
route = route_lead(score)

print(f"name: {prospect['name']}")   
print(f"title: {prospect ['title']}")
print(f"employees: {prospect['employees']}")
print(f"Route: {route}")
