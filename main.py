import request as localRequests
import extractor as localExtractor
from IPython.display import display, HTML
import pandas as pd
# Example usage
urls = [
    'https://dummyjson.com/users/1',
    'https://dummyjson.com/users/2',
    'https://dummyjson.com/users/3'
]

responseData = localRequests.getListLogApi(urls)

# Variable to store all extracted key-value pairs along with URLs
all_extracted_items = []

for url, (data, error) in zip(urls, responseData):
    if error:
        print(f"Error: {error}")
    else:
        # Extract all key-value pairs
        extractedItems = localExtractor.extract_json(data)
        all_extracted_items.append((url, extractedItems))


# Create a list of dictionaries for the DataFrame
data_for_df = []
for url, extractedItems in all_extracted_items:
    key_value_pairs = "<div style='text-align:left;'>" + "<br>".join([f"{key}: {value}" for key, value in extractedItems]) + "</div>"
    data_for_df.append({'URL': url, 'KeyValuePairs': key_value_pairs})

print (data_for_df)


# # Create a list of dictionaries for the DataFrame
# data_for_df = []
# for url, extractedItems in all_extracted_items:
#     key_value_pairs = "<div style='text-align:left;'>" + "<br>".join([f"{key}: {value}" for key, value in extractedItems]) + "</div>"
#     data_for_df.append({'URL': url, 'KeyValuePairs': key_value_pairs})

# # Create a pandas DataFrame
# df = pd.DataFrame(data_for_df)

# # Display the DataFrame with HTML rendering and left alignment for key-value pairs
# html = df.to_html(escape=False)
# display(HTML(html))