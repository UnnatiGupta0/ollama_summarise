

import subprocess

def summarize_with_ollama(text):
    prompt = "Please provide a concise summary of the following text:\n\n" + text

    process = subprocess.Popen(
        ['ollama', 'run', 'mistral'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    output, error = process.communicate(input=prompt)

    if process.returncode != 0:
        print("Error:", error.strip())
        return None

    return output.strip()

document = """
Generative AI (GenAI) tools are software applications that leverage AI to 
create original content, such as text, images, music, video, or code. 
These tools use advanced AI models like GPT (Generative Pre-trained 
Transformer) and GANs (Generative Adversarial Networks) to generate new 
outputs based on input prompts or patterns.
"""

summary = summarize_with_ollama(document)
print("Summary:\n", summary)

