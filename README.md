# Telegram Printer Bot

A Telegram bot that automatically downloads documents sent by users and prints them via the system's default printer.

## Features

- Receives and downloads all document types supported by Telegram.
- Prints files using the `lp` command (CUPS) on Linux.
- Sends confirmation message to the user after printing.
- Logs downloaded and printed files for monitoring.

## Tech Details

- Python 3.10+
- `python-telegram-bot` library
- Linux environment with a configured default printer
- Uses `os.system("lp <file>")` for printing
- Files are saved temporarily in a configurable `DOWNLOAD_DIR`
- Asynchronous handling of Telegram messages using `asyncio`
