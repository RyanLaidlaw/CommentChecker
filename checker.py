import os, sys, re, subprocess, platform, argparse
import prompts
from argparse import RawDescriptionHelpFormatter
from dotenv import load_dotenv, find_dotenv
from groq import Groq

RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

DESCRIPTION = """
    Code Comment Checker.

    This script is designed to allow you to pass in a file (of any language)
    and will use AI to determine the quality of your code comments.
    
    If a file is not specified as a flag, you will be asked to specify one later."""

def read_file(file):
    try:
        with open(file, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{file}': {e}")
        sys.exit(1)

def create_prompt(file_content):
    prompt = prompts.generate_prompt(file_content)
    return prompt

def check_file(file):
    file_content = read_file(file)
    prompt = create_prompt(file_content)

    model="llama3-8b-8192"
    temperature = 0.2
    max_tokens = 500

    messages=[
        {"role": "system", "content": prompts.system_message},
        {"role": "user", "content": prompt}
        ]
    
    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    result = chat_completion.choices[0].message.content
    print(format_response(result))

def format_response(response):
    result = re.sub(r'^[^:]*:', '', response).lstrip("\n")
    if "No changes needed." in result:
        result = result.replace("No changes needed.", '')
    if "let me know" in result.lower():
        result = result.replace("let me know", '')
    result = re.sub(r'^\d+\.', f"{GREEN}\\g<0>{RESET}", result, flags=re.M)
    formatted_lines = []
    for line in result.splitlines():
        line_lower = line.lower()
        if "code" in line_lower and "change" in line_lower and ":" in line_lower:
            line = f"{GREEN}{line}{RESET}"
        elif "@param" in line_lower or "@return" in line_lower:
            line = re.sub(r'(@param|@return)', f"{RED}\\1{RESET}", line, flags=re.I)
        elif '**' in line:
            line = re.sub(r'\*\*(.*?)\*\*', f"{GREEN}**\\1**{RESET}", line)
        formatted_lines.append(line)
    result = "\n".join(formatted_lines)
    return result

def install_dependencies(packages):
    os_type = platform.system() #possibly add support for other OS
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing missing dependency: {package}")
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--quiet", package],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=True
            )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage="python3 checker.py [-h] [-f FILE]", 
        description=DESCRIPTION, 
        formatter_class=RawDescriptionHelpFormatter
        )
    
    parser.add_argument (
        '-f', '--file',
        type=str,
        help='File to parse'
    )

    args = parser.parse_args()
    
    if not args.file:
        print("What file would you like to check?")
        file = input()
    else:
        file = args.file

    install_dependencies(["termcolor", "dotenv", "groq"])   
    
    print("\n") 

    _ = load_dotenv(find_dotenv())
    global client
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    
    check_file(file)

