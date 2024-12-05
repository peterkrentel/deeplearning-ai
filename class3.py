from helper_functions import print_llm_response, get_llm_response, display_table
from IPython.display import Markdown
import csv

def read_csv(file):
    f = open(file, "r")
    
    csv_reader = csv.DictReader(f)
    data = []
    for row in csv_reader:
        data.append(row)
    f.close()
    
    return data

# Read the itinerary.csv file
itinerary = read_csv("itinerary.csv")

# Display the itinerary
display_table(itinerary)

# The function called 'read_journal'
def read_journal(journal_file):
    f = open(journal_file, "r")
    journal = f.read() 
    f.close()

    # Return the journal content
    return journal

journal = read_journal("sydney.txt")

print(journal)

# Write the prompt
prompt = f"""Please extract a comprehensive list of the restaurants 
and their respective specialties mentioned in the following journal entry. 
Ensure that each restaurant name is accurately identified and listed. 
Provide your answer in CSV format, ready to save. 
Exclude the "```csv" declaration, don't add spaces after the comma, include column headers.

Format:
Restaurant, Specialty
Res_1, Sp_1
...

Journal entry:
{journal}
"""

# Print the prompt
print_llm_response(prompt)

# Use the read_csv function
sydney_restaurants = read_csv("Sydney.csv")

display_table(sydney_restaurants)

# Select Sydney from the 'itinerary' list
trip_stop = itinerary[6]

city = trip_stop["City"]
country = trip_stop["Country"]
arrival = trip_stop["Arrival"]
departure = trip_stop["Departure"]
restaurants = sydney_restaurants

# Write the prompt
prompt = f"""I will visit {city}, {country} from {arrival} to {departure}. 
Create a daily itinerary with detailed activities. 
Designate times for breakfast, lunch, and dinner. 

I want to visit the restaurants listed in the restaurant dictionary 
without repeating any place. Make sure to mention the specialty
that I should try at each of them.

Restaurant dictionary:
{restaurants}

"""

response = get_llm_response(prompt)

# Print the LLM response in Markdown format
display(Markdown(response))

# Create an empty dictionary to store the itinerary for each destination
detailed_itinerary = {}

 # Use the 'for' loop over the 'itinerary' list   
for trip_stop in itinerary:
    city = trip_stop["City"]
    country = trip_stop["Country"]
    arrival = trip_stop["Arrival"]
    departure = trip_stop["Departure"]

    rest_dict = read_csv(f"{city}.csv")
    
    print(f"Creating detailed itinerary for {city}, {country}.")
    
    prompt = f"""I will visit {city}, {country} from {arrival} to {departure}. 
    Create a daily itinerary with detailed activities. 
    Designate times for breakfast, lunch, and dinner. 

    I want to visit the restaurants listed in the restaurant dictionary without repeating any place.
    Make sure to mention the specialty that I should try at each of them.

    Restaurant dictionary:
    {rest_dict}

    """
    # Store the detailed itinerary for the city to the dictionary
    detailed_itinerary[city] = get_llm_response(prompt)

# Print in Markdown format
display(Markdown(detailed_itinerary["Tokyo"]))