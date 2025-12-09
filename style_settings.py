settings = {
    "theme": "light",
    "refresh_rate": 2
}

def set_theme(theme):
    settings["theme"] = theme

def set_refresh_rate(seconds):
    settings["refresh_rate"] = seconds

def get_settings():
    return settings
