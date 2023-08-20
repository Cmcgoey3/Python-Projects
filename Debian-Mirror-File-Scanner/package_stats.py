"""
Author: Connor McGoey
Version: 1.0.0
Date: July 15, 2023
File: package_stats.py
"""

# import typer CLI library and debianStats function from debian_stats.py
import typer
from debian_stats import debianStats

# initialize typer app
app = typer.Typer()

@app.command()
def main(architecture: str):
    # Call the debianStats function with the provided architecture
    debianStats(architecture)

if __name__ == "__main__":
    app()
