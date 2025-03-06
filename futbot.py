import discord
import requests
import os
from discord.ext import commands

# Enable Discord bot intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

# ESPN API Base URL
BASE_URL = "http://site.api.espn.com/apis/site/v2/sports/soccer/uefa.champions"


### **1. Live Match Updates** (`!ucl_scores`)
@bot.command()
async def ucl_scores(ctx):
    url = f"{BASE_URL}/scoreboard"

    try:
        response = requests.get(url)
        data = response.json()

        if "events" not in data:
            await ctx.send("❌ No live or recent UCL scores available.")
            return

        matches = []
        for event in data["events"]:
            home = event["competitions"][0]["competitors"][0]["team"][
                "displayName"]
            away = event["competitions"][0]["competitors"][1]["team"][
                "displayName"]
            home_score = event["competitions"][0]["competitors"][0].get(
                "score", "N/A")
            away_score = event["competitions"][0]["competitors"][1].get(
                "score", "N/A")
            status = event["status"]["type"]["description"]

            matches.append(
                f"⚽ {home} **{home_score} - {away_score}** {away} ({status})")

        message = "🏆 **Live UEFA Champions League Scores** 🏆\n```" + "\n".join(
            matches) + "```"
        await ctx.send(message)

    except Exception as e:
        await ctx.send("⚠️ Error retrieving UCL scores.")
        print(f"Error: {e}")


### **2. Upcoming Fixtures** (`!ucl_fixtures`)
@bot.command()
async def ucl_fixtures(ctx):
    url = f"{BASE_URL}/scoreboard"

    try:
        response = requests.get(url)
        data = response.json()

        if "events" not in data:
            await ctx.send("❌ No upcoming UCL fixtures available.")
            return

        fixtures = []
        for event in data["events"]:
            home = event["competitions"][0]["competitors"][0]["team"][
                "displayName"]
            away = event["competitions"][0]["competitors"][1]["team"][
                "displayName"]
            date = event["date"]

            fixtures.append(f"📅 {home} vs {away} - {date}")

        message = "📅 **Upcoming UEFA Champions League Matches** 📅\n```" + "\n".join(
            fixtures) + "```"
        await ctx.send(message)

    except Exception as e:
        await ctx.send("⚠️ Error retrieving UCL fixtures.")
        print(f"Error: {e}")


### **3. League Standings & Group Stage Table** (`!ucl_standings`)
@bot.command()
async def ucl_standings(ctx):
    url = f"{BASE_URL}/standings"

    try:
        response = requests.get(url)
        data = response.json()

        if "standings" not in data:
            await ctx.send("❌ No UCL standings available.")
            return

        standings = []
        for group in data["standings"]:
            group_name = group["name"]
            standings.append(f"\n📊 **{group_name}**")
            for team in group["entries"]:
                rank = team["stats"][0]["value"]
                name = team["team"]["displayName"]
                points = team["stats"][1]["value"]

                standings.append(f"{rank}. {name} - {points} pts")

        message = "🏆 **UEFA Champions League Standings** 🏆\n```" + "\n".join(
            standings) + "```"
        await ctx.send(message)

    except Exception as e:
        await ctx.send("⚠️ Error retrieving UCL standings.")
        print(f"Error: {e}")


### **4. Player & Team Stats** (`!ucl_team_stats team_name`)
@bot.command()
async def ucl_team_stats(ctx, *, team_name):
    url = f"{BASE_URL}/teams"

    try:
        response = requests.get(url)
        data = response.json()

        if "sports" not in data:
            await ctx.send("❌ No UCL teams found.")
            return

        teams = data["sports"][0]["leagues"][0]["teams"]
        for team in teams:
            if team_name.lower() in team["team"]["displayName"].lower():
                name = team["team"]["displayName"]
                abbreviation = team["team"].get("abbreviation", "N/A")
                team_url = team["team"]["links"][0]["href"]

                message = f"📊 **{name} ({abbreviation})**\n🔗 [More Info]({team_url})"
                await ctx.send(message)
                return

        await ctx.send(f"❌ Team '{team_name}' not found in UCL.")

    except Exception as e:
        await ctx.send("⚠️ Error retrieving UCL team stats.")
        print(f"Error: {e}")


### **5. Latest UCL News** (`!ucl_news`)
@bot.command()
async def ucl_news(ctx):
    url = f"{BASE_URL}/news"

    try:
        response = requests.get(url)
        data = response.json()

        if "articles" not in data:
            await ctx.send("❌ No UCL news available.")
            return

        news_list = []
        for article in data["articles"][:5]:  # Get top 5 news articles
            title = article["headline"]
            link = article["links"]["web"]["href"]
            news_list.append(f"📰 [{title}]({link})")

        message = "📰 **Latest UEFA Champions League News** 📰\n" + "\n".join(
            news_list)
        await ctx.send(message)

    except Exception as e:
        await ctx.send("⚠️ Error retrieving UCL news.")
        print(f"Error: {e}")


bottoken = os.getenv("TOKEN", "").strip()  # Ensure it's a string
if not bottoken:
    print(
        "❌ ERROR: No Discord bot token found! Set your TOKEN environment variable."
    )
    exit()

bot.run(bottoken)
