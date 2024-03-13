# Define the path to your text file
file_path = "config.txt"


def parse_config():

	# Create an empty dictionary to store key-value pairs
	config_data = {}

	# Open the file and read line by line
	with open(file_path, "r") as file:
		for line in file:
			# Ignore lines starting with // or containing only whitespace/newline characters
			if not line.strip() or line.strip().startswith("//"):
				continue

			# Split each line by '=' character to separate key and value
			key, value = line.strip().split("=")

			# Strip whitespace from key and value
			key = key.strip()
			value = value.strip().strip('"')  # Strip quotes if present

			# Store key-value pair in the dictionary
			config_data[key] = value

	# Print the extracted key-value pairs
	for key, value in config_data.items():
		if key == "PASSWORD":
			print("PASSWORD: Hidden")
		else:
			print(f"{key}: {value}")

	return config_data
