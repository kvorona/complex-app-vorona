class StartPageConstants:
    # Sign in
    SIGN_IN_USERNAME = './/input[@name="username" and @placeholder="Username"]'
    SIGN_IN_PASSWORD = './/input[@name="password" and @placeholder="Password"]'
    SIGN_IN_ERROR_MESSAGE = ''
    SIGN_IN__ERROR_TEXT = ".//div[contains(text(),'Invalid username / password')]"
    SIGN_IN_BUTTON = ".//button[contains(text(),'Sign In')]"

    # Sign Up
    SIGN_UP_USERNAME = './/input[@name="username" and @id="username-register"] '
    SIGN_UP_EMAIL = './/input[@name="email"]'
    SIGN_UP_PASSWORD = './/input[@name="password" and @id="password-register"]'
    SIGN_UP_BUTTON = ".//button[contains(text(),'Sign up for OurApp')]"
    SIGN_UP_USERNAME_ERROR = ".//div[contains(text(),'Username must be at least 3 characters.')]"
    SIGN_UP_USERNAME_ERROR2 = ".//div[contains(text(),'Username can only contain letters and numbers.')]"
    SIGN_UP_EMAIL_ERROR = ".//div[contains(text(),You must provide a valid email address.')]"
    SIGN_UP_PASSWORD_ERROR = ".//div[contains(text(),'Password must be at least 12 characters.')]"

    # Profile page
    CREATE_POST = './/a[@href="/create-post"]'
    SIGN_OUT = ".//button[contains(text(),'Sign Out')]"
    MY_PROFILE_BUTTON = './/img[@data-original-title="My Profile"]'
