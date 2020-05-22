import collections
import csv
import json


class FileHelper(object):
    def __init__(self, file_name, extension):
        self.file_name = file_name
        self.extension = extension

    # -----------------------------------------------------------
    # Download the provided data in a .csv or .json file
    #
    # -----------------------------------------------------------
    def download(self, json_data):
        if self.extension == "csv":
            self.download_as_csv(json_data)
        else:
            if self.extension == "json":
                self.download_as_json(json_data)
            else:
                return False
        return True

    def download_as_csv(self, json_data):
        # Load CSV file
        output_file = open(self.file_name, 'w')
        # Create writer
        output = csv.writer(output_file)

        # Check if the data has values, and if it is a collection of objects or a single one
        # If the is no data, the files only shows "No-data"
        if json_data is not None:
            if isinstance(json_data, collections.Sequence) and len(json_data) > 0:
                # Add headers
                output.writerow(json_data[0].keys())
                # Add rows
                for row in json_data:
                    output.writerow(row.values())
            else:
                if isinstance(json_data, dict) is True:
                    output.writerow(json_data.keys())
                    output.writerow(json_data.values())
                else:
                    output.writerow(["Data"])
                    output.writerow(json_data)
        else:
            output.writerow(["No-data"])

    def download_as_json(self, json_data):
        # Create output file
        output_file = open(self.file_name, 'w')
        # Convert object to string and write it in file
        json_str = json.dumps(json_data)
        output_file.write(json_str)
