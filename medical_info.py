import json

def get_medical_info(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data_file = 'medical_info.json'
    file_content = get_medical_info(data_file)
   
    # to print the keys in the JSON file and number of keys
    
    keys = file_content.keys()
    print("Keys in the JSON file: ", keys)
    print("Total number of keys: ", len(file_content))

    # to print insurance details

    insurance_details = file_content['insurance']
    print("Insurance Details:", insurance_details)

    # to print insurance provider name
    insurance_provider = insurance_details['provider']
    print("Insurance Provider: ", insurance_provider)