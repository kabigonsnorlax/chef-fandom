import json
import requests
import re
from bs4 import BeautifulSoup

with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    url = item['URL']
    print(f"Processing {item['Name']}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        estimate_fans = None
        elements = soup.find_all('p', class_='MdMN05Txt')

        for element in elements:
            text = element.get_text().strip()

            if text.startswith('Members '):
                match = re.search(r'Members\s+([\d,]+)', text)
                if match:
                    estimate_fans = int(match.group(1).replace(',', ''))
                    break

        item['EstimateFans'] = estimate_fans
        print(f"Fans: {estimate_fans}")

    except Exception as e:
        print(f"Error: {e}")
        item['EstimateFans'] = None

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Done")
