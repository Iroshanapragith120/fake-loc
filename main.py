import time
import os
import random
import sys
from rich.console import Console
from rich.progress import track
from rich.text import Text
from rich.align import Align

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def scary_face():
    clear()
    face = """
          .-'''''-.
        .'  _     _  '.
       /   (o)   \\
      |                 |
      |      .---.      |
      |     /     \\     |
       \\    \\     /    /
        '.   '---'   .'
          '-._____.-'
    """
    console.print(Align.center(Text(face, style="bold red")))
    console.print(Align.center(Text(">>> INTRUSION DETECTED <<<", style="bold red blink")))
    time.sleep(2)

def fake_hacking():
    tasks = ["ACCESSING GLOBAL SATELLITE...", "BYPASSING FIREWALL...", "DECRYPTING COORDINATES...", "TRIANGULATING SIGNAL..."]
    for task in track(tasks, description="Processing..."):
        time.sleep(1)

def globe_animation():
    clear()
    console.print("\n\n")
    console.print(Align.center(Text("🌍", style="green")), style="bold")
    console.print(Align.center(Text("TARGET ACQUIRED: ASIA REGION", style="yellow")))
    time.sleep(1.5)
    clear()
    console.print("\n\n")
    console.print(Align.center(Text("📍", style="red")))
    console.print(Align.center(Text("ZOOMING: SRI LANKA", style="yellow")))
    time.sleep(1.5)

def final_location():
    clear()
    locations = ["Nuwara Eliya", "Colombo Fort", "Jaffna Library", "Galle Face Green", "Bokundara", "Kandy Lake", "Sigiriya"]
    chosen = random.choice(locations)
    
    console.print("\n\n")
    console.print(Align.center(Text("[ TARGET LOCKED ]", style="bold green")))
    console.print(Align.center(Text(f">> {chosen.upper()} <<", style="bold red blink")))
    time.sleep(1)
    console.print(Align.center(Text("IP ADDRESS LOCATED AT THIS POINT", style="yellow")))
    console.print(Align.center(Text("Coordinates: 6.9271° N, 79.8612° E", style="dim")))
    console.print("\n")
    console.print(Align.center(Text("Have a nice day... 😈", style="bold red")))

# MAIN PROGRAM
try:
    scary_face()
    clear()
    console.print("ENTER TARGET ID TO TRACE LOCATION:", style="bold red")
    target = console.input("[bold yellow]LOCATION_GET_NUMBER >>> [/]")
    
    if target:
        fake_hacking()
        globe_animation()
        final_location()
    else:
        console.print("\nNO TARGET SPECIFIED. ABORTING.", style="bold red")

except KeyboardInterrupt:
    clear()
    console.print("\nCONNECTION TERMINATED BY USER", style="bold red")

console.input("\n\nPress Enter to exit...")
