import json

# Read the contents of the README file
with open('README.md', 'r') as file:
    readme_content = file.read()

core_prompt_001 = "I have developed a Standard Operating Procedure (SOP) for Python programming, and the draft is provided below. I am looking to enhance its content and ensure it covers all essential aspects comprehensively. Could you provide a detailed list of topics and areas that I can add or improve in the SOP? Specifically, I am interested in best practices, coding standards, debugging techniques, documentation guidelines, testing procedures, and any other critical elements that should be included to make the SOP more effective and useful for Python developers. Below is my current draft SOP for your reference."
core_prompt_002 = "I have developed a Standard Operating Procedure (SOP) for Python programming, and the draft is provided below. How can I improve it? Please provide a list of topics I can add or improve."

# Create the JSON payload
payload = {
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": core_prompt_002 + "\n\n" + readme_content}],
    "temperature": 0.5
}

# Save the JSON payload to a file
with open('payload.json', 'w') as json_file:
    json.dump(payload, json_file, ensure_ascii=False, indent=4)

print("payload.json created successfully.")
