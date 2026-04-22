"""
CS2 Demo Legality Analyzer
--------------------------
Checks robots.txt, attempts ToS fetching, and documents anti-scraping measures
for HLTV.org and related platforms (ESL, Faceit, Valve).

Run:
    pip install requests beautifulsoup4 rich
    python analyze.py
"""

import requests
from bs4 import BeautifulSoup
from rich.console import Console
from rich.table import Table
from rich import print as rprint
import json
import time

console = Console()

TARGETS = {
    "HLTV.org": {
        "robots_url": "https://www.hltv.org/robots.txt",
        "tos_url": "https://www.hltv.org/terms",
        "notes": "Primary source of CS2 pro demos; owned by Better Collective (DK)"
    },
    "ESL Gaming": {
        "robots_url": "https://www.eslgaming.com/robots.txt",
        "tos_url": "https://www.eslgaming.com/terms-and-conditions",
        "notes": "Major tournament organizer; hosts demo files"
    },
    "Faceit": {
        "robots_url": "https://www.faceit.com/robots.txt",
        "tos_url": "https://www.faceit.com/en/terms_and_conditions",
        "notes": "Matchmaking platform with public demo API"
    },
    "Valve (Steam)": {
        "robots_url": "https://store.steampowered.com/robots.txt",
        "tos_url": "https://store.steampowered.com/subscriber_agreement/",
        "notes": "Game developer; owns .dem file format and GOTV protocol"
    },
}

HEADERS = {
    # Identify ourselves honestly as a research script
    "User-Agent": "Mozilla/5.0 (compatible; academic-research-bot/1.0; +mailto:student@university.edu)"
}


def fetch_robots(name: str, url: str) -> dict:
    """
    Fetch and parse a robots.txt file.
    Returns status, raw content, and whether scraping is disallowed for *.
    """
    result = {"url": url, "status": None, "disallow_all": False, "raw": None, "error": None}
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        result["status"] = resp.status_code
        if resp.status_code == 200:
            result["raw"] = resp.text
            # Check if wildcard user-agent disallows root (= everything)
            lines = resp.text.lower().splitlines()
            in_wildcard = False
            for line in lines:
                if line.startswith("user-agent: *"):
                    in_wildcard = True
                elif line.startswith("user-agent:"):
                    in_wildcard = False
                if in_wildcard and line.startswith("disallow: /"):
                    result["disallow_all"] = True
        elif resp.status_code == 403:
            result["error"] = "403 Forbidden — Cloudflare or server-level block"
        elif resp.status_code == 404:
            result["error"] = "404 Not Found — no robots.txt present"
    except requests.exceptions.Timeout:
        result["error"] = "Request timed out"
    except requests.exceptions.ConnectionError as e:
        result["error"] = f"Connection error: {e}"
    return result


def fetch_tos(name: str, url: str) -> dict:
    """
    Attempt to fetch a ToS page.
    Returns status code and whether access was blocked.
    """
    result = {"url": url, "status": None, "blocked": False, "error": None, "excerpt": None}
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        result["status"] = resp.status_code
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            # Grab first 500 chars of visible text as a preview
            text = soup.get_text(separator=" ", strip=True)
            result["excerpt"] = text[:500] if text else "(no text extracted)"
        elif resp.status_code in (403, 429, 503):
            result["blocked"] = True
            result["error"] = f"HTTP {resp.status_code} — likely anti-bot protection (Cloudflare/WAF)"
    except Exception as e:
        result["error"] = str(e)
    return result


def print_robots_table(results: dict):
    table = Table(title="robots.txt Fetch Results", show_lines=True)
    table.add_column("Platform", style="bold cyan")
    table.add_column("HTTP Status")
    table.add_column("Disallow All?")
    table.add_column("Notes / Error")

    for name, r in results.items():
        status = str(r["status"]) if r["status"] else "N/A"
        disallow = "[red]YES[/red]" if r["disallow_all"] else ("[green]NO[/green]" if r["status"] == 200 else "—")
        notes = r["error"] or "OK"
        table.add_row(name, status, disallow, notes)

    console.print(table)


def print_tos_table(results: dict):
    table = Table(title="ToS Page Fetch Results", show_lines=True)
    table.add_column("Platform", style="bold cyan")
    table.add_column("HTTP Status")
    table.add_column("Blocked?")
    table.add_column("Notes / Error")

    for name, r in results.items():
        status = str(r["status"]) if r["status"] else "N/A"
        blocked = "[red]YES[/red]" if r["blocked"] else ("[green]NO[/green]" if r["status"] == 200 else "—")
        notes = r["error"] or "Accessible"
        table.add_row(name, status, blocked, notes)

    console.print(table)


def save_results(robots_results: dict, tos_results: dict):
    """Save raw results to JSON for use in the notebook."""
    import os
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, "..", "wyniki")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "fetch_results.json")
    output = {
        "robots": robots_results,
        "tos": tos_results
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    console.print(f"\n[green]Results saved to {output_path}[/green]")


def main():
    console.rule("[bold]CS2 Demo Legality — Platform Access Analysis[/bold]")
    console.print("Checking robots.txt and ToS accessibility for CS2-related platforms.\n")

    robots_results = {}
    tos_results = {}

    for name, info in TARGETS.items():
        console.print(f"[yellow]Checking {name}...[/yellow]")

        robots_results[name] = fetch_robots(name, info["robots_url"])
        time.sleep(1)  # polite delay between requests

        tos_results[name] = fetch_tos(name, info["tos_url"])
        time.sleep(1)

    console.print()
    print_robots_table(robots_results)
    console.print()
    print_tos_table(tos_results)

    # Print any successfully fetched robots.txt content
    console.rule("Raw robots.txt Content (where accessible)")
    for name, r in robots_results.items():
        if r["raw"]:
            console.print(f"\n[bold cyan]{name}[/bold cyan]")
            console.print(r["raw"][:2000])  # cap at 2000 chars

    save_results(robots_results, tos_results)
    console.rule("Done")


if __name__ == "__main__":
    main()
