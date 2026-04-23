from utility.settings import Settings

def list_settings(compony_code):
    """Retrieve all settings for a company, ensuring defaults are present."""
    settings_manager = Settings(compony_code)
    return settings_manager.get_all()

def update_settings(compony_code, new_settings, value):
    """Update a specific setting for a company."""
    settings_manager = Settings(compony_code)
    return settings_manager.update(new_settings, value)
