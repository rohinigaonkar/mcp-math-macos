# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import time

# from pywinauto.application import Application
# import win32gui
# import win32con
# from win32api import GetSystemMetrics

import subprocess
import platform

#win32gui / win32con	pyobjc (AppKit, Quartz)
#win32api	osascript,
#pywinauto	pyautogui

from AppKit import NSWorkspace
#import pyautogui
#import psutil

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


# @mcp.tool()
# async def win_draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
#     """Draw a rectangle in Paint from (x1,y1) to (x2,y2)"""
#     global paint_app
#     try:
#         if not paint_app:
#             return {
#                 "content": [
#                     TextContent(
#                         type="text",
#                         text="Paint is not open. Please call open_paint first."
#                     )
#                 ]
#             }
        
#         # Get the Paint window
#         paint_window = paint_app.window(class_name='MSPaintApp')
        
#         # Get primary monitor width to adjust coordinates
#         primary_width = GetSystemMetrics(0)
        
#         # Ensure Paint window is active
#         if not paint_window.has_focus():
#             paint_window.set_focus()
#             time.sleep(0.2)
        
#         # Click on the Rectangle tool using the correct coordinates for secondary screen
#         paint_window.click_input(coords=(530, 82 ))
#         time.sleep(0.2)
        
#         # Get the canvas area
#         canvas = paint_window.child_window(class_name='MSPaintView')
        
#         # Draw rectangle - coordinates should already be relative to the Paint window
#         # No need to add primary_width since we're clicking within the Paint window
#         canvas.press_mouse_input(coords=(x1+2560, y1))
#         canvas.move_mouse_input(coords=(x2+2560, y2))
#         canvas.release_mouse_input(coords=(x2+2560, y2))
        
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
#                 )
#             ]
#         }
#     except Exception as e:
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Error drawing rectangle: {str(e)}"
#                 )
#             ]
#         }
    
# @mcp.tool()
# def get_os_name():
#     """
#     Get a human-readable name of the current operating system.
    
#     Returns:
#         str: OS name (e.g., 'macOS', 'Windows', 'Linux')
#     """
#     system = platform.system()
#     if system == 'Darwin':
#         return 'macOS'
#     return system



# @mcp.tool()
# async def win_add_text_in_paint(text: str) -> dict:
#     """Add text in Paint in Windows"""
#     global paint_app
#     try:
#         if not paint_app:
#             return {
#                 "content": [
#                     TextContent(
#                         type="text",
#                         text="Paint is not open. Please call open_paint first."
#                     )
#                 ]
#             }
        
#         # Get the Paint window
#         paint_window = paint_app.window(class_name='MSPaintApp')
        
#         # Ensure Paint window is active
#         if not paint_window.has_focus():
#             paint_window.set_focus()
#             time.sleep(0.5)
        
#         # Click on the Rectangle tool
#         paint_window.click_input(coords=(528, 92))
#         time.sleep(0.5)
        
#         # Get the canvas area
#         canvas = paint_window.child_window(class_name='MSPaintView')
        
#         # Select text tool using keyboard shortcuts
#         paint_window.type_keys('t')
#         time.sleep(0.5)
#         paint_window.type_keys('x')
#         time.sleep(0.5)
        
#         # Click where to start typing
#         canvas.click_input(coords=(810, 533))
#         time.sleep(0.5)
        
#         # Type the text passed from client
#         paint_window.type_keys(text)
#         time.sleep(0.5)
        
#         # Click to exit text mode
#         canvas.click_input(coords=(1050, 800))
        
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Text:'{text}' added successfully"
#                 )
#             ]
#         }
#     except Exception as e:
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Error: {str(e)}"
#                 )
#             ]
#         }

# @mcp.tool()
# async def win_open_paint() -> dict:
    # """Open Microsoft Paint maximized on secondary monitor in Windows"""
    # global paint_app
    # try:
    #     paint_app = Application().start('mspaint.exe')
    #     time.sleep(0.2)
        
    #     # Get the Paint window
    #     paint_window = paint_app.window(class_name='MSPaintApp')
        
    #     # Get primary monitor width
    #     primary_width = GetSystemMetrics(0)
        
    #     # First move to secondary monitor without specifying size
    #     win32gui.SetWindowPos(
    #         paint_window.handle,
    #         win32con.HWND_TOP,
    #         primary_width + 1, 0,  # Position it on secondary monitor
    #         0, 0,  # Let Windows handle the size
    #         win32con.SWP_NOSIZE  # Don't change the size
    #     )
        
    #     # Now maximize the window
    #     win32gui.ShowWindow(paint_window.handle, win32con.SW_MAXIMIZE)
    #     time.sleep(0.2)
        
    #     return {
    #         "content": [
    #             TextContent(
    #                 type="text",
    #                 text="Paint opened successfully on secondary monitor and maximized"
    #             )
    #         ]
    #     }
    # except Exception as e:
    #     return {
    #         "content": [
    #             TextContent(
    #                 type="text",
    #                 text=f"Error opening Paint: {str(e)}"
    #             )
    #         ]
    #     }
# DEFINE RESOURCES

# @mcp.tool()
# async def win_draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
#     """Draw a rectangle in Paint from (x1,y1) to (x2,y2) in Windows"""
#     global paint_app
#     try:
#         if not paint_app:
#             return {
#                 "content": [
#                     TextContent(
#                         type="text",
#                         text="Paint is not open. Please call open_paint first."
#                     )
#                 ]
#             }
        
#         # Get the Paint window
#         paint_window = paint_app.window(class_name='MSPaintApp')
        
#         # Get primary monitor width to adjust coordinates
#         primary_width = GetSystemMetrics(0)
        
#         # Ensure Paint window is active
#         if not paint_window.has_focus():
#             paint_window.set_focus()
#             time.sleep(0.2)
        
#         # Click on the Rectangle tool using the correct coordinates for secondary screen
#         paint_window.click_input(coords=(530, 82 ))
#         time.sleep(0.2)
        
#         # Get the canvas area
#         canvas = paint_window.child_window(class_name='MSPaintView')
        
#         # Draw rectangle - coordinates should already be relative to the Paint window
#         # No need to add primary_width since we're clicking within the Paint window
#         canvas.press_mouse_input(coords=(x1+2560, y1))
#         canvas.move_mouse_input(coords=(x2+2560, y2))
#         canvas.release_mouse_input(coords=(x2+2560, y2))
        
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
#                 )
#             ]
#         }
#     except Exception as e:
#         return {
#             "content": [
#                 TextContent(
#                     type="text",
#                     text=f"Error drawing rectangle: {str(e)}"
#                 )
#             ]
#         }

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")

@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

@mcp.tool()
async def mac_open_keynote() -> dict:
    """Open Keynote on macOS and create a new document."""
    try:
        # AppleScript to open Keynote and create a new document
        applescript = '''
        tell application "Keynote"
            activate
            if (count of documents) = 0 then
                set newDoc to make new document
            end if
        end tell
        '''
        
        # Run AppleScript
        subprocess.run(["osascript", "-e", applescript])
        time.sleep(1.5)  # Allow time for Keynote to open


        return {
            "content": [
                {
                    "type": "text",
                    "text": "Keynote opened successfully with a new document"
                }
            ]
        }
    except Exception as e:
        return {
            "content": [
                {
                    "type": "text",
                    "text": f"Error opening Keynote: {str(e)}"
                }
            ]
        }
    
@mcp.tool()
async def mac_draw_rectangle() -> dict:
    # async def mac_draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Keynote on macOS from (x1,y1) to (x2,y2).  Keynote must be open before calling this tool."""

    x1 = 780;
    y1 = 380;
    x2= 1140;
    y2= 700;

    try:
        # Check if Keynote is running
        applescript_check = '''
        tell application "System Events"
            return exists (processes where name is "Keynote")
        end tell
        '''
        result = subprocess.run(["osascript", "-e", applescript_check], capture_output=True, text=True)
        if "true" not in result.stdout.lower():
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Keynote is not open. Please call mac_open_keynote first."
                    )
                ]
            }

        # Convert (x1, y1, x2, y2) to width and height
        width = abs(x2 - x1)
        height = abs(y2 - y1)

        # AppleScript to add a rectangle to the current slide
        applescript = f'''
        tell application "Keynote"
            activate
            tell front document
                tell current slide
                    make new shape at end of shapes
                    set position of last shape to {{{x1}, {y1}}}
                    set width of last shape to {width}
                    set height of last shape to {height}
                end tell
            end tell
        end tell
        '''

        # Run AppleScript to execute the commands in Keynote
        subprocess.run(["osascript", "-e", applescript])
        time.sleep(1)  # Allow time for Keynote to process

        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Rectangle drawn in Keynote from ({x1},{y1}) to ({x2},{y2})"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error drawing rectangle in Keynote: {str(e)}"
                )
            ]
        }
    
@mcp.tool()
async def mac_add_text_in_keynote(text: str) -> dict:
    """Add text in Keynote on macOS inside a rectangle shape. Keynote must be open and rectangle must be drawn before calling this tool."""
    try:
        # Check if Keynote is running
        applescript_check = '''
        tell application "System Events"
            return exists (processes where name is "Keynote")
        end tell
        '''
        result = subprocess.run(["osascript", "-e", applescript_check], capture_output=True, text=True)
        if "true" not in result.stdout.lower():
            return {
                "content": [
                    TextContent(
                        type="text",
                        text="Keynote is not open. Please open keynote first."
                    )
                ]
            }

        # AppleScript to add text to the current slide in Keynote
        applescript = f'''
        tell application "Keynote"
            activate
        end tell

        tell application "System Events"
            tell process "Keynote"
                -- Click on the last shape (assuming it's at the center of the slide)
                click at {{960, 540}}
                delay 0.5
                
                -- Press Command+T to add text
                keystroke "t" using command down
                delay 0.5
                
                -- Type the text
                keystroke "{text}"
            end tell
        end tell
        '''

        # Run AppleScript to execute the commands in Keynote
        subprocess.run(["osascript", "-e", applescript])
        time.sleep(1)  # Allow time for Keynote to process

        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Text '{text}' added successfully to Keynote"
                )
            ]
        }
    except Exception as e:
        return {
            "content": [
                TextContent(
                    type="text",
                    text=f"Error adding text to Keynote: {str(e)}"
                )
            ]
        }

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
