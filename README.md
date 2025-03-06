Bot hosted in: https://replit.com/~

# ⚽ UEFA Champions League Teams API

This project uses the **ESPN API** to fetch **UEFA Champions League (UCL) teams** for the current season. The API provides real-time team data without requiring an API key.

## 📌 API Endpoint

Base URL: http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions/teams

## 📌 How It Works

1. Sends a `GET` request to the ESPN API.
2. Extracts **team names**, **abbreviations**, and **official links**.
3. Formats the data for easy use in a Discord bot or web app.

## 📌 Example API Response (JSON)
```json
{
    "sports": [
        {
            "leagues": [
                {
                    "teams": [
                        {
                            "team": {
                                "id": "359",
                                "displayName": "Arsenal",
                                "abbreviation": "ARS",
                                "links": [
                                    {
                                        "href": "https://www.espn.com/soccer/club/_/id/359/arsenal"
                                    }
                                ]
                            }
                        },
                        {
                            "team": {
                                "id": "86",
                                "displayName": "Real Madrid",
                                "abbreviation": "RMA",
                                "links": [
                                    {
                                        "href": "https://www.espn.com/soccer/club/_/id/86/real-madrid"
                                    }
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    ]
}


