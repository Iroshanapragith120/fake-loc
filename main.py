import time
import os
import random
import sys
from rich.console import Console
from rich.live import Live
from rich.text import Text
from rich.align import Align

console = Console()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def matrix_rain(duration=3):
    """Terminal එක පුරාම code වැටෙනවා වගේ"""
    chars = "01アカサタナハマヤラワガザダバパイキシチニヒミリヰギジヂビピウクスツヌフムユルグズヅブプエケセテネヘメレヱゲゼデベペオコソトノホモヨロヲゴゾドボポヴッン"
    width = console.width
    height = console.height - 2
    
    start_time = time.time()
    with Live(console=console, screen=True) as live:
        while time.time() - start_time < duration:
            lines = []
            for _ in range(height):
                line = "".join(random.choice(chars) for _ in range(width))
                lines.append(Text(line, style="green"))
            live.update(Text("\n".join([str(l) for l in lines])))
            time.sleep(0.08)

def draw_globe_from_code():
    """Code වලින් globe එක අඳිනවා"""
    clear()
    console.print(Align.center("[bold red]COMPILING GLOBAL SATELLITE NETWORK...[/]"))
    time.sleep(1)
    
    globe_code = [
        " 0x7F 0x45 0x4C 0x46 0x01 0x00",
        " 0x00",
        " 0x02 0x00 0x03 0x00 0x01 0x00 0x80 0x90",
        "0x04 0x08 0x34 0x00",
        " 0x34 0x00 0x20 0x00 0x0A 0x00 0x28 0x00 0x1E 0x00",
        " 0x1D 0x00 0x06 0x00 0x34 0x00",
        " 0x34 0x00 0x34 0x00 0xE0 0x00",
    ]
    
    for i, line in enumerate(globe_code):
        console.print(Align.center(Text(line, style="cyan")))
        time.sleep(0.15)
    
    time.sleep(0.5)
    console.print(Align.center("[bold yellow]>>> GLOBE RENDERED <<<[/]"))
    time.sleep(1.5)
    
    # Zoom effect
    for i in range(3):
        clear()
        zoom_text = f"[bold green]ZOOMING x{(i+1)*25}...[/]"
        console.print(Align.center(zoom_text))
        time.sleep(0.5)

def draw_sri_lanka_from_code():
    """Code වලින් ලංකා සිතියම අඳිනවා"""
    clear()
    console.print(Align.center("[bold red]TARGET LOCKED: 6.9271°N 79.8612°E[/]"))
    time.sleep(1)
    
    # ලංකාවේ shape එක hex code වලින්
    sl_map = [
        " 0xFF 0xD8 0xFF 0xE0",
        " 0x00 0x10 0x4A 0x46 0x49 0x46",
        " 0x00 0x01 0x00 0x48 0x00",
        " 0x48 0x00 0xFF 0xDB 0x00 0x43 0x00",
        " 0x08 0x06 0x07 0x06 0x05 0x08 0x07 0x07",
        " 0x07 0x09 0x08 0x0A 0x0C 0x14 0x0D 0x0C",
        " 0x0B 0x0B 0x0C 0x19 0x12 0x13 0x0F 0x14 0x1D",
        " 0x1A 0x1F 0x1E 0x1D 0x1A 0x1C 0x1C 0x20 0x24",
        " 0x2E 0x27 0x20 0x22 0x2C 0x23 0x1C 0x1C 0x28",
        " 0x37 0x29 0x2C 0x30 0x31 0x34 0x1F",
        " 0x27 0x39 0x3D 0x38 0x32 0x3C 0x2E 0x33 0x34",
        " 0x32 0xFF 0xC0 0x00 0x11 0x08 0x00 0xF0 0x01",
        " 0x40 0x03 0x01 0x22 0x00 0x02 0x11 0x01 0x03",
        " 0x11 0x01 0xFF 0xDA 0x00 0x0C 0x03 0x01 0x00",
    ]
    
    for line in sl_map:
        console.print(Align.center(Text(line, style="bold yellow")))
        time.sleep(0.1)
    
    time.sleep(1)

def final_target():
    """අන්තිමට රතු dot එකයි location එකයි"""
    clear()
    
    # ලංකාව ආයෙ පෙන්නලා රතු dot එක දානවා
    sl_with_dot = """
[bold yellow] 0xFF 0xD8 0xFF 0xE0
        0x00 0x10 0x4A 0x46 0x49 0x46
      0x00 0x01 0x00 0x48 0x00
     0x48 0x00 0xFF 0xDB 0x00 0x43 0x00
    0x08 0x06 0x07 0x06 0x05 0x08 0x07 0x07
    0x07 0x09 0x08 0x0A 0x0C 0x14 0x0D 0x0C[/]
[bold red] ● <<< TARGET ACQUIRED >>> [/]
[bold yellow] 0x1A 0x1F 0x1E 0x1D 0x1A 0x1C 0x1C 0x20 0x24
       0x2E 0x27 0x20 0x22 0x2C 0x23 0x1C 0x1C 0x28
        0x37 0x29 0x2C 0x30 0x31 0x34 0x1F
         0x27 0x39 0x3D 0x38 0x32 0x3C 0x2E 0x33 0x34
          0x32 0xFF 0xC0 0x00 0x11 0x08 0x00 0xF0 0x01[/]
    """
    
    console.print(Align.center(sl_with_dot))
    time.sleep(1)
    
    console.print("\n")
    console.print(Align.center(Text(">>> LOCATION TRACK COMPLETE <<<", style="bold red blink")))
    time.sleep(1)
    console.print(Align.center(Text("SUBJECT: FRIEND_01", style="bold white")))
    console.print(Align.center(Text("STATUS: LOCATED", style="bold green")))
    console.print(Align.center(Text("COORDINATES: 7.8731° N, 80.7718° E", style="dim")))
    console.print("\n")
    console.print(Align.center(Text("ACCESS GRANTED. HAVE A NICE DAY.", style="bold red")))

# MAIN PROGRAM
try:
    clear()
    console.print(Align.center("[bold red]INITIALIZING DARK_NET PROTOCOL v3.7[/]"))
    time.sleep(1)
    
    matrix_rain(3) # තප්පර 3ක් code වැටෙනවා
    
    console.print(Align.center("[bold yellow]ENTER TARGET HASH:[/]"))
    target = console.input(Align.center("[bold red]>>> [/]"))
    
    if target:
        clear()
        console.print(Align.center(f"[green]TARGET_HASH [{target}] ACCEPTED[/]"))
        time.sleep(0.5)
        console.print(Align.center("[green]INITIATING TRACE...[/]"))
        time.sleep(1)
        
        draw_globe_from_code()
        draw_sri_lanka_from_code()
        final_target()
    else:
        console.print(Align.center("[bold red]NO TARGET. ABORTING.[/]"))

except KeyboardInterrupt:
    clear()
    console.print(Align.center("[bold red]CONNECTION TERMINATED BY OPERATOR[/]"))

console.input("\n\n[dim]Press Enter to close session...[/]")
