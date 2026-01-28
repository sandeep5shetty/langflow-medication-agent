import requests
import os
import uuid


# The complete API endpoint URL for this flow
url = "https://aws-us-east-2.langflow.datastax.com/lf/10be64e5-4f25-4909-b69a-543e025afd76/api/v1/run/39582018-a2ab-4318-8372-75d85b41003a"

# Request payload configuration
payload = {
    "output_type": "chat",
    "input_type": "chat",
    "input_value": "[\n                {\n                        \"fields\": [\n                                \"patient_id\",\n                                \"medication_name\",\n                                \"refill_number\",\n                                \"prev_days_supply\",\n                                \"days_gap\",\n                                \"supply_trend\",\n                                \"gap_trend\",\n                                \"adherent_ratio_so_far\"\n                        ],\n                        \"values\": [\n                                [\n                                        \"P004\",\n                                        \"Insulin\",\n                                        2,\n                                        15,\n                                        7,\n                                        0,\n                                        0,\n                                        0\n                                ],\n                                [\n                                        \"P004\",\n                                        \"Insulin\",\n                                        3,\n                                        15,\n                                        11,\n                                        -5,\n                                        4,\n                                        0\n                                ],\n                                [\n                                        \"P004\",\n                                        \"Insulin\",\n                                        4,\n                                        10,\n                                        13,\n                                        -5,\n                                        2,\n                                        0\n                                ],\n                                [\n                                        \"P004\",\n                                        \"Insulin\",\n                                        5,\n                                        10,\n                                        15,\n                                        0,\n                                        2,\n                                        0\n                                ]\n                        ]\n                }\n        ]\n"
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