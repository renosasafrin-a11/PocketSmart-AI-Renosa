def create_home_prompt(
    budget: float,
    room_type: str,
    style: str,
    requirements: str
):
    return f"""
You are PocketSmart AI, a smart budget recommendation assistant.

The user wants home decor recommendations.

Budget: {budget}
Room type: {room_type}
Style: {style}
Additional requirements: {requirements}

Give practical and affordable recommendations.
Make sure the recommendations stay within the user's budget.

For each recommendation include:
- Product name
- Category
- Estimated price
- Platform
- Reason
"""


def fallback_home_recommendations(
    budget: float,
    room_type: str,
    style: str
):
    recommendations = []

    if budget >= 500:
        recommendations.append({
            "name": "Decorative Wall Art",
            "category": "Wall Decor",
            "price": 499,
            "platform": "Amazon",
            "reason": f"Suitable for a {style} {room_type}."
        })

    if budget >= 800:
        recommendations.append({
            "name": "LED Decorative Light",
            "category": "Lighting",
            "price": 699,
            "platform": "Flipkart",
            "reason": "Adds attractive lighting while staying budget-friendly."
        })

    if budget >= 1200:
        recommendations.append({
            "name": "Decorative Indoor Plant",
            "category": "Decor",
            "price": 399,
            "platform": "IKEA",
            "reason": "Adds a simple decorative touch to the room."
        })

    if not recommendations:
        recommendations.append({
            "name": "Budget Wall Decor",
            "category": "Wall Decor",
            "price": budget,
            "platform": "Demo Recommendation",
            "reason": "Selected to stay within your available budget."
        })

    return recommendations


def create_party_prompt(
    budget: float,
    event_type: str,
    guests: int,
    theme: str
):
    return f"""
You are PocketSmart AI, a smart budget recommendation assistant.

The user wants party planning recommendations.

Budget: {budget}
Event type: {event_type}
Number of guests: {guests}
Theme: {theme}

Give practical and affordable party recommendations.
Make sure the recommendations stay within the user's budget.

For each recommendation include:
- Item name
- Category
- Estimated price
- Platform
- Reason
"""


def fallback_party_recommendations(
    budget: float,
    event_type: str,
    guests: int,
    theme: str
):
    recommendations = []

    if budget >= 500:
        recommendations.append({
            "name": "Party Decoration Set",
            "category": "Decorations",
            "price": 399,
            "platform": "Amazon",
            "reason": f"Suitable for a {theme or 'simple'} {event_type}."
        })

    if budget >= 1000:
        recommendations.append({
            "name": "Party Cake",
            "category": "Food",
            "price": 599,
            "platform": "Swiggy",
            "reason": f"Suitable for approximately {guests} guests."
        })

    if budget >= 1500:
        recommendations.append({
            "name": "Disposable Party Tableware",
            "category": "Tableware",
            "price": 399,
            "platform": "Flipkart",
            "reason": "Useful for serving food and drinks at the party."
        })

    if not recommendations:
        recommendations.append({
            "name": "Budget Party Decorations",
            "category": "Decorations",
            "price": budget,
            "platform": "Demo Recommendation",
            "reason": "Selected to stay within your available budget."
        })

    return recommendations


def create_jewelry_prompt(
    budget: float,
    occasion: str,
    jewelry_type: str,
    outfit_description: str
):
    return f"""
You are PocketSmart AI, a smart budget recommendation assistant.

The user wants jewelry recommendations.

Budget: {budget}
Occasion: {occasion}
Jewelry type: {jewelry_type}
Outfit description: {outfit_description}

Give practical and affordable jewelry recommendations.
Make sure the recommendations stay within the user's budget.

For each recommendation include:
- Jewelry name
- Category
- Estimated price
- Platform
- Reason
"""


def fallback_jewelry_recommendations(
    budget: float,
    occasion: str,
    jewelry_type: str
):
    recommendations = []

    if budget >= 500:
        recommendations.append({
            "name": "Elegant Stud Earrings",
            "category": jewelry_type,
            "price": 399,
            "platform": "Amazon",
            "reason": f"Suitable for a {occasion} occasion."
        })

    if budget >= 1000:
        recommendations.append({
            "name": "Minimal Pendant Necklace",
            "category": "Necklace",
            "price": 699,
            "platform": "Flipkart",
            "reason": "A simple option that can complement many outfits."
        })

    if budget >= 1500:
        recommendations.append({
            "name": "Classic Bracelet",
            "category": "Bracelet",
            "price": 599,
            "platform": "Myntra",
            "reason": "Adds a subtle finishing touch to the overall look."
        })

    if not recommendations:
        recommendations.append({
            "name": "Budget Jewelry Item",
            "category": jewelry_type,
            "price": budget,
            "platform": "Demo Recommendation",
            "reason": "Selected to stay within your available budget."
        })

    return recommendations