class CreatePostConstants:
    # Create post
    CREATE_POST = './/a[@href="/create-post"]'
    TITLE = './/input[@name="title" and @id="post-title"]'
    BODY_CONTENT = './/textarea[@name="body" and @id="post-body"]'
    UNIQUE_POST_CHECKBOX = ''
    SELECT_VALUE = './/select[@name="select1"]'
    SELECT_VALUE_ALL = './/option[@value="All Users"]'
    SELECT_VALUE_PERSONALITY = './/option[@value="One Person"]'
    SELECT_VALUE_GROUP = './/option[@value="Group Message"]'
    SAVE_NEW_POST = './/button[@class="btn btn-primary"]'
