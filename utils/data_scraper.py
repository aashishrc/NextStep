import re
import json

import re
import json

def extract_college_info_as_json(raw_text: str) -> str:
    """
    1. Finds the text inside content="..." 
    2. Parses it into structured JSON with fields:
       'Rank', 'Name', 'Location', 'Website', 'Program', 'Enrollment', 
       'Acceptance Rate', 'Graduation Rate', 'Explanation'.
    3. Returns a JSON string containing a list of college dictionaries.
    """

    # === STEP 1: EXTRACT TEXT INSIDE content=" ... " =================================
    pattern = r'content="([^"]+)"'
    match = re.search(pattern, raw_text, re.DOTALL)
    if not match:
        return json.dumps({"error": "No content found"}, indent=2)

    extracted_content = match.group(1).strip()

    # === STEP 2: SPLIT CONTENT INTO SECTIONS FOR EACH COLLEGE =======================
    # A typical section starts with something like:
    # "### 1. **Alabama A & M University**"
    # We'll split on lines that match "### <number>."
    college_blocks = re.split(r"(?=###\s+\d+\.)", extracted_content)

    # We'll store the results here
    colleges_data = []

    # === STEP 3: PARSE EACH COLLEGE BLOCK ===========================================
    # Example block:
    # ### 1. **Alabama A & M University**
    #    - **Location:** Normal, AL
    #    - **Website:** [www.aamu.edu](http://www.aamu.edu)
    #    - **Mathematics Program:** Yes
    #    - **Enrollment:** Approximately 10,024 students
    #    - **Acceptance Rate:** 65.36%
    #    - **Graduation Rate:** 46.13%
    #
    #    **Explanation:** ...
    
    for block in college_blocks:
        block = block.strip()
        if not block:
            continue

        # Parse rank and name from a line like:
        # ### 1. **Alabama A & M University**
        # We'll use a regex capturing group
        header_match = re.search(
            r"^###\s+(\d+)\.\s+\*\*(.*?)\*\*", block, re.MULTILINE | re.DOTALL
        )
        if not header_match:
            # No valid college header; skip or continue
            continue

        rank = header_match.group(1).strip()
        name = header_match.group(2).strip()

        # Extract lines that look like: "- **Location:** Normal, AL"
        # We'll build a dictionary as we go
        location = None
        website = None
        program = None
        enrollment = None
        acceptance_rate = None
        graduation_rate = None
        explanation = None

        # We'll iterate over each line
        for line in block.splitlines():
            line = line.strip()
            # e.g. "- **Location:** Normal, AL"
            loc_match = re.search(r"\*\*Location:\*\*\s+(.*)", line, re.IGNORECASE)
            site_match = re.search(r"\*\*Website:\*\*\s+\[?(.*?)\]?\(?.*?\)?", line, re.IGNORECASE)
            prog_match = re.search(r"\*\*Mathematics Program:\*\*\s+(.*)", line, re.IGNORECASE)
            enroll_match = re.search(r"\*\*Enrollment:\*\*\s+(.*)", line, re.IGNORECASE)
            accept_match = re.search(r"\*\*Acceptance Rate:\*\*\s+(.*)", line, re.IGNORECASE)
            grad_match = re.search(r"\*\*Graduation Rate:\*\*\s+(.*)", line, re.IGNORECASE)

            if loc_match:
                location = loc_match.group(1).strip()
            if site_match:
                # The site_match pattern captures what's inside [] if it exists
                website = site_match.group(1).strip()
            if prog_match:
                program = prog_match.group(1).strip()
            if enroll_match:
                # For "Approximately 10,024 students" we can remove non-digits or parse carefully
                enrollment = enroll_match.group(1).strip()
            if accept_match:
                acceptance_rate = accept_match.group(1).strip()
            if grad_match:
                graduation_rate = grad_match.group(1).strip()

            # Explanation lines typically start with "**Explanation:**"
            # We'll just capture everything after that label
            expl_match = re.search(r"\*\*Explanation:\*\*\s+(.*)", line, re.IGNORECASE)
            if expl_match:
                explanation = expl_match.group(1).strip()

        # Add this college to our list
        colleges_data.append({
            "Rank": rank,
            "Name": name,
            "Location": location,
            "Website": website,
            "Program": program,
            "Enrollment": enrollment,
            "Acceptance Rate": acceptance_rate,
            "Graduation Rate": graduation_rate,
            "Explanation": explanation
        })

    # === STEP 4: CONVERT TO JSON ================================================
    # Return the list of colleges as a JSON string
    return json.dumps(colleges_data, indent=2)


if __name__ == "__main__":
    # Example usage:
    raw_text = """
    content="Based on your preferences for mathematics and your location in Normal,\
         AL, here are the top college recommendations ranked with explanations:\n\n### \
         1. **Alabama A & M University**\n   - **Location:** Normal, AL\n   - **Website:** [www.aamu.edu](http://www.aamu.edu)\n   - **Mathematics Program:** Yes\n   - **Enrollment:** Approximately 10,024 students\n   - **Acceptance Rate:** 65.36%\n   - **Graduation Rate:** 46.13%\n   \n   **Explanation:** Alabama A & M University is the most relevant choice for you as it is located in Normal, AL, and offers a mathematics program. The university's proximity to your location makes it convenient for commuting or living on campus. Additionally, the acceptance and graduation rates indicate a supportive environment for students, which can be beneficial for your academic journey in mathematics.\n\n### 2. **Illinois State University**\n   - **Location:** Normal, IL (approximately 30 miles from Normal, AL)\n   - **Website:** [illinoisstate.edu](http://illinoisstate.edu)\n   - **Mathematics Program:** Yes\n   - **Enrollment:** Approximately 15,170 students\n   - **Acceptance Rate:** 30.34%\n   - **Graduation Rate:** 81.92%\n   \n   **Explanation:** Although Illinois State University is located in a different state, it is a strong contender due to its robust mathematics program and high graduation rate. The university has a larger student body, which may provide more resources and networking opportunities. However, the distance from your current location may be a consideration if you prefer to stay closer to home.\n\n### Summary\nBoth Alabama A & M University and Illinois State University offer strong mathematics programs, but Alaby\nBoth Alabama A & M University and Illinois State University offer strong mathematics programs, but Alabama A & M is the top recommendation due to its location in Normal, AL. Illinois State University is a great option if you are open to traveling a bit further for a potentially more comprehensive academic experience." additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 403, 'prompt_tokens': 399, 'total_tokens': 802, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_7fcd609668', 'finish_reason': 'stop', 'logprobs': None} id='run-b9a28044-1199-4452-86e6-bdf0f259b29e-0' usage_mett option if you are open to traveling a bit further for a potentially more comprehensive academic experience." additional_kwargs={'refusal': None} response_metadata={'token_usage': {'completion_tokens': 403, 'prompt_tokens': 399, 'total_tokens': 802, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_7fcd609668', 'finish_reason': 'stop', 'logprobs': None} id='run-b9a28044-1199-4452-86e6-bdf0f259b29e-0' usage_metadata={'input_tokens': 399, 'output_tokens': 403, 'total_tokens': 802, 'input_token_details': {'audio': 0,mpt_tokens': 399, 'total_tokens': 802, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_7fcd609668', 'finish_reason': 'stop', 'logprobs': None} id='run-b9a28044-1199-4452-86e6-bdf0f259b29e-0' usage_metadata={'input_tokens': 399, 'output_tokens': 403, 'total_tokens': 802, 'input_token_details': {'audio': 0,okens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-4o-mini-2024-07-18', 'system_fingerprint': 'fp_7fcd609668', 'finish_reason': 'stop', 'logprobs': None} id='run-b9a28044-1199-4452-86e6-bdf0f259b29e-0' usage_metadata={'input_tokens': 399, 'output_tokens': 403, 'total_tokens': 802, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}} adata={'input_tokens': 399, 'output_tokens': 403, 'total_tokens': 802, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}} \
    """
    
    json_output = extract_college_info_as_json(raw_text)
    print(json_output)  # This is the JSON string you can send via a POST request
