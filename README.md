# PTIT CTF 2025 Discord Bot

A Discord bot built with Python and discord.py featuring welcome messages, basic commands, and extensible architecture for the PTIT CTF 2025 event.

## Features

- 🎉 **Welcome Messages**: Automatically welcome new members with embedded messages
- 🤖 **Basic Commands**: Support for various utility commands
- 🧮 **Calculator Commands**: Basic math operations (add, subtract, multiply, divide)
- 📊 **Server Information**: Display server and user information
- 🔧 **Configurable**: Easy configuration through environment variables
- 📝 **Logging**: Comprehensive logging for debugging and monitoring
- ⚡ **Error Handling**: Robust error handling with user-friendly messages

## Commands

### Basic Commands
- `!hello` - Greet the user
- `!ping` - Check bot latency
- `!help` - Show available commands
- `!help <command>` - Show detailed help for a specific command

### Calculator Commands
- `!add <num1> <num2>` - Add two numbers
- `!subtract <num1> <num2>` - Subtract two numbers
- `!multiply <num1> <num2>` - Multiply two numbers
- `!divide <num1> <num2>` - Divide two numbers

### Information Commands
- `!serverinfo` - Display server information
- `!userinfo [@user]` - Display user information

## Setup

### Prerequisites
- Python 3.8 or higher
- Discord bot token from Discord Developer Portal
- discord.py library
- python-dotenv library

### Installation

1. **Clone or download the bot files**

2. **Install required dependencies**
   ```bash
   pip install discord.py python-dotenv
   