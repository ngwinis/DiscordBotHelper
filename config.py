import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the Discord bot"""
    
    # Discord Bot Settings
    DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
    COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')
    
    # Channel IDs
    WELCOME_CHANNEL_ID = int(os.getenv('WELCOME_CHANNEL_ID', '1395586238123086025'))
    RULES_CHANNEL_ID = int(os.getenv('RULES_CHANNEL_ID', '1395586838256943245'))
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'bot.log')
    
    # Bot Settings
    MAX_MESSAGE_LENGTH = 2000
    COMMAND_COOLDOWN = 3  # seconds
    
    @classmethod
    def validate_config(cls):
        """Validate required configuration values"""
        required_vars = ['DISCORD_TOKEN']
        missing_vars = []
        
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
