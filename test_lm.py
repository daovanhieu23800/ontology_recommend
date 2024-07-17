import os
from spraql_LM import SpraqlLM, Style

# Define path to the RDF file
rdf_path = "rdf/draft-system-onto.rdf"

# Ensure the path to save the JSON file exists
output_dir = os.path.join(os.getcwd(), 'ontology', 'json')
os.makedirs(output_dir, exist_ok=True)

# Initialize the Style class
learning_style = Style()

# Initialize the SpraqlLM class
spraql = SpraqlLM(rdf_path)

# Run the spraql_lm method and get results
results = spraql.spraql_lm(learning_style)

# Print the results
for result in results:
    print('result: ',result)
