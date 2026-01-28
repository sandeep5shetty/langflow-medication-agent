import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/10be64e5-4f25-4909-b69a-543e025afd76/api/v1/run/39582018-a2ab-4318-8372-75d85b41003a"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "The patient ID is P004, and the medication prescribed is Insulin.\n\nThere are four refill records, listed in chronological order from older to most recent.\n\nRefill record 1:\nThis is refill number 2.\nThe patient received a 15-day supply of the medication.\nThere was a 7-day gap before the next refill.\nThe supply trend value is 0, the gap trend value is 0, and the adherent ratio so far is 0.\n\nRefill record 2:\nThis is refill number 3.\nThe patient again received a 15-day supply.\nThere was an 11-day gap before the next refill.\nThe supply trend value is -5, the gap trend value is 4, and the adherent ratio so far is 0.\n\nRefill record 3:\nThis is refill number 4.\nThe patient received a 10-day supply.\nThere was a 13-day gap before the next refill.\nThe supply trend value is -5, the gap trend value is 2, and the adherent ratio so far is 0.\n\nRefill record 4 (most recent):\nThis is refill number 5.\nThe patient received a 10-day supply.\nThere was a 15-day gap before this refill.\nThe supply trend value is 0, the gap trend value is 2, and the adherent ratio so far is 0."
}
payload["session_id"] = str(uuid.uuid4())

headers = {
    "X-DataStax-Current-Org": "99dd3730-c860-488c-ba03-835c2705e33d", 
    "Authorization": "Bearer <YOUR_APPLICATION_TOKEN>",
    "Content-Type": "application/json", 
    "Accept": "application/json",
}

try:
    # Send API request
    response = requests.request("POST", url, json=payload, headers=headers)
    response.raise_for_status()  # Raise exception for bad status codes

    # Print response
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Error making API request: {e}")
except ValueError as e:
    print(f"Error parsing response: {e}")