# PTIT CTF 2025 Discord Bot

## Overview

This is a Discord bot built with Python and discord.py for the PTIT CTF 2025 event. The bot provides welcome messages, basic utility commands, calculator functionality, and server information commands. It features a modular architecture with separate modules for commands, utilities, and configuration management.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Core Framework
- **Discord.py**: Main framework for Discord bot development
- **Commands Extension**: Uses discord.py's commands extension for structured command handling
- **Cog System**: Modular command organization using Discord.py's cog system

### Architecture Pattern
- **Modular Design**: Commands are organized into separate cogs for better maintainability
- **Configuration Management**: Centralized configuration using environment variables
- **Logging System**: Comprehensive logging with both file and console output
- **Error Handling**: Built-in cooldown and error handling mechanisms

## Key Components

### 1. Bot Core (`main.py`)
- **PTITBot Class**: Main bot class inheriting from commands.Bot
- **Intents Configuration**: Enables member and message content intents
- **Event Handlers**: Handles bot ready events and member join events
- **Cog Loading**: Automatically loads command modules

### 2. Configuration Management (`config.py`)
- **Environment Variables**: Loads configuration from .env file
- **Default Values**: Provides fallback values for optional settings
- **Validation**: Ensures required configuration values are present
- **Channel IDs**: Manages Discord channel references

### 3. Command System (`commands/`)
- **Basic Commands**: Greeting, calculation, and utility commands
- **Cooldown System**: Prevents command spam with configurable cooldowns
- **Error Handling**: Graceful handling of invalid inputs
- **Embed Messages**: Rich message formatting for better user experience

### 4. Utility System (`utils/`)
- **Logger Setup**: Configurable logging with file and console output
- **Log Management**: Automatic log directory creation and file handling

## Data Flow

### Bot Initialization
1. Load environment variables from .env file
2. Validate required configuration values
3. Initialize bot with proper intents and command prefix
4. Load command cogs during setup phase
5. Set bot status and presence

### Command Processing
1. User sends command with configured prefix
2. Discord.py parses command and arguments
3. Cooldown check prevents spam
4. Command logic executes with error handling
5. Response sent back to user (often as embed)

### Event Handling
1. Member joins server
2. Bot detects member_join event
3. Welcome message sent to configured channel
4. Message includes server rules reference

## External Dependencies

### Python Packages
- **discord.py**: Core Discord API wrapper
- **python-dotenv**: Environment variable management
- **asyncio**: Asynchronous programming support (built-in)
- **logging**: Logging functionality (built-in)
- **datetime**: Date and time handling (built-in)
- **random**: Random number generation (built-in)
- **os**: Operating system interface (built-in)

### Discord Platform
- **Discord Bot Token**: Required for bot authentication
- **Discord Developer Portal**: Bot registration and permissions
- **Server Permissions**: Bot needs appropriate permissions for functionality

## Deployment Strategy

### Environment Setup
- Python 3.8+ required
- Install dependencies via pip
- Configure environment variables in .env file
- Set up Discord bot token and channel IDs

### Configuration Requirements
- **DISCORD_TOKEN**: Bot authentication token (required)
- **COMMAND_PREFIX**: Command prefix (default: '!')
- **WELCOME_CHANNEL_ID**: Channel for welcome messages
- **RULES_CHANNEL_ID**: Channel referenced in welcome messages
- **LOG_LEVEL**: Logging verbosity (default: INFO)
- **LOG_FILE**: Log file name (default: bot.log)

### Runtime Features
- **Automatic Logging**: Creates logs directory and files automatically
- **Error Recovery**: Graceful handling of missing channels or permissions
- **Status Updates**: Bot presence shows help command and event branding
- **Cooldown Management**: Prevents abuse with configurable command cooldowns

### Extensibility
- **Modular Cog System**: Easy to add new command modules
- **Configuration-Driven**: Most settings configurable via environment variables
- **Logging Framework**: Comprehensive logging for debugging and monitoring
- **Error Handling**: Robust error handling with user-friendly messages

The bot is designed to be easily deployable on various platforms including local development environments, cloud services, or containerized deployments. The modular architecture allows for easy extension with additional features specific to CTF events or Discord server management.