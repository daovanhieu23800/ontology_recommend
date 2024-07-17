import os
from spraql_topic import SpraqlTopic

# Define start and end topics
startID = "Matrices and linear algebra fundamentals"  # Replace with the actual start topic ID
endID = "Machine Learning"    # Replace with the actual end topic ID

# Path to the RDF file
rdf_path = "rdf/draft-topic-onto.rdf"

# Ensure the path to save the JSON file exists
output_dir = os.path.join(os.getcwd(), 'ontology', 'json')
os.makedirs(output_dir, exist_ok=True)

# Initialize the SpraqlTopic class
spraql = SpraqlTopic(startID, endID, rdf_path)

# Run the spraqlTopic method and get paths
paths = spraql.spraqlTopic()

# Print the paths
for path in paths:
    print(path)
