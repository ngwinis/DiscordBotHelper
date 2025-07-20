import logging
import os
from datetime import datetime
from config import Config

def setup_logger():
    """Setup logging configuration for the bot"""
    
    # Create logs directory if it doesn't exist
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create logger
    logger = logging.getLogger('discord_bot')
    logger.setLevel(getattr(logging, Config.LOG_LEVEL.upper()))
    
    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    simple_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )
    
    # File handler
    file_handler = logging.FileHandler(
        os.path.join(log_dir, Config.LOG_FILE),
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(simple_formatter)
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

def log_command_usage(ctx, command_name):
    """Log command usage"""
    logger = logging.getLogger('discord_bot')
    logger.info(f"Command '{command_name}' used by {ctx.author.name} (ID: {ctx.author.id}) in {ctx.guild.name}")

def log_error(error, context=None):
    """Log errors with context"""
    logger = logging.getLogger('discord_bot')
    if context:
        logger.error(f"Error in {context}: {error}")
    else:
        logger.error(f"Error: {error}")
