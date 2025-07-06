def calculate_risk_score(model_prob, amount, is_night, channel):
    score = model_prob * 0.6
    if amount > 1500:
        score += 0.2
    if is_night:
        score += 0.1
    if channel == "Online":
        score += 0.1
    return min(score, 1.0)

