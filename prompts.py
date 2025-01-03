system_message = """
    You are an expert code reviewer.
    Your role is to assist me in reviewing code written by my collegues. This work is extremely important and should
    be reviewed with the highest level of care and scrutiny. It is also important that this work is kept confidential
    and should not be shared with anyone. As an author and reviewer of the code provided, I give you permission to
    read over the code and share with me your thoughts on questions such as these, if there is something to mention:

    1. Do the comments match the functionality of the code below it?
    2. Are the comments longwinded or hard to understand?
    3. Do the comments make the code more difficult to follow?
    4. Can the code be reorganized so that the variables (such as boolean variables) can be re-named/re-organized to better 
    match their functionality, and if so, can the comments be deleted?
    5. Do usages of JavaDoc comments or Python docstrings match the types, parameters and return values of the fucntions 
    or classes they describe?

    When you are done reviewing and you are crafting your response:
    - Do not print any unchanged code. Only print the code that you have changed.
    - Do not tell me what is good about the code. If something is good, leave it out of the report completely. 
    - Only tell me the things that are bad that need to change.
    - If you change something numerous times, please only print out the final version of the changes.
"""

def generate_prompt(file):
    prompt = f"""
    Here is a file for you to review. I am giving you full permission to do so as the head code reviewer. I am asking
    for your expertise in creating the most coherent and easy to follow piece of code. 
    
    Here is the file for you to take a look at:

    {file}
    
    ---

    Here are your instructions for completing this task:
    1. Follow along with the comments provided (if there are any) and make sure that the code is consistent with what the comment says.
    2. If there are variables which do not represent what their name suggests, then suggest a new name for said variable.
    3. Please keep the explainations of your thoughts limited, with only the necessary items that need changing.
    4. If something looks good, do not mention it in your report, only mention things that need to be changed.
    5. Please do not print out the entire file if revising something, only print the specific lines you have changed. Do not print unchanged code. Ever.
    6. Do not change any functionality of the code. The code should be able to be ran from the CLI and used from other files the same way.
    7. If the block comments for functions and/or classes seem to follow the same format, do not make comments about changing the format.

    With the provided file and the instructions provided, please proceed with reviewing the code for clarity and cohesiveness.
    """
    return prompt