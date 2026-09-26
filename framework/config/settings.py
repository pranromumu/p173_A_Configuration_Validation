from dataclasses import dataclass

@dataclass
class Settings:
    BASE_URL: str = "https://the-internet.herokuapp.com/"
    BROWSER: str = "chromium"
    HEADLESS: bool = True
    TIMEOUT: int = 30000

    def validate(self):
        errors = []
        
        # 1. BASE_URL must not be empty
        if not self.BASE_URL:
            errors.append("BASE_URL cannot be empty.")
            
        # 2. BROWSER must be one of the supported Playwright browsers
        supported_browsers = ["chromium", "firefox", "webkit"]
        if self.BROWSER not in supported_browsers:
            errors.append(f"BROWSER must be one of {supported_browsers}, but got '{self.BROWSER}'.")
            
        # 3. HEADLESS must be a boolean
        if not isinstance(self.HEADLESS, bool):
            errors.append(f"HEADLESS must be a boolean (True/False), but got {type(self.HEADLESS).__name__}.")
            
        # 4. TIMEOUT must be an integer greater than 0
        if not isinstance(self.TIMEOUT, int) or self.TIMEOUT <= 0:
            errors.append(f"TIMEOUT must be an integer greater than 0, but got {self.TIMEOUT}.")
            
        # If any errors were collected, raise them all at once!
        if errors:
            error_message = "\n".join(errors)
            raise ValueError(f"Configuration validation failed:\n{error_message}")

config = Settings()