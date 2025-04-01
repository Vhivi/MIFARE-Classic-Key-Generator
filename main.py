# This project generates a file containing hexadecimal keys of 12 characters like MIFARE Classic keys,
# ranging from `000000000000` to `FFFFFFFFFFFF`.

import configparser
import os


def load_config(config_file="config.ini"):
    """
    Loads configuration settings from a specified INI file.

    Args:
        config_file (str): The path to the configuration file. Defaults to "config.ini".

    Returns:
        tuple: A tuple containing the following:
            - output_file (str): The name of the output file for generated keys. Defaults to "keys.txt".
            - key_length (int): The length of the keys to be generated. Defaults to 12.
            - start (int): The starting value for key generation, parsed as a hexadecimal. Defaults to 0x0.
            - end (int): The ending value for key generation, parsed as a hexadecimal. Defaults to 0xFFFFFFFFFFFF.

    Raises:
        FileNotFoundError: If the configuration file does not exist or cannot be loaded.
        KeyError: If the "KeyGenerator" section is missing in the configuration file.
        ValueError: If any of the expected values cannot be parsed correctly.
    """

    # Check if the configuration file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(
            f"The configuration file '{config_file}' does not exist."
        )

    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Load the configuration file
    read_files = config.read(config_file)
    if not read_files:
        raise FileNotFoundError(
            f"The configuration file '{config_file}' could not be loaded."
        )

    # Check if the KeyGenerator section exists
    if "KeyGenerator" not in config:
        raise KeyError(
            "The 'KeyGenerator' section is missing in the configuration file."
        )

    gen_config = config["KeyGenerator"]

    # Extract values from the KeyGenerator section
    try:
        output_file = gen_config.get("output_file", "keys.txt")
        key_length = gen_config.getint("key_length", 12)
        start = int(gen_config.get("start", "0x0"), 16)
        end = int(gen_config.get("end", "0xFFFFFFFFFFFF"), 16)
    except ValueError as e:
        raise ValueError(f"Error while reading values in the configuration file: {e}")

    return output_file, key_length, start, end


def main():
    """
    Main function to generate MIFARE Classic keys and save them to a file.

    This function performs the following steps:
    1. Loads configuration settings from a `config.ini` file, including:
       - The output file path where the keys will be saved.
       - The length of the keys to be generated.
       - The start and end range for key generation.
    2. Calculates the total number of keys to be generated and displays it.
    3. Iterates through the specified range to generate hexadecimal keys of the specified length.
    4. Writes each generated key to the specified output file.
    5. Displays a confirmation message once the keys are successfully saved.

    Note:
        The keys are formatted as uppercase hexadecimal strings with leading zeros
        to match the specified key length.

    Raises:
        Any exceptions related to file operations or configuration loading
        should be handled by the caller or within the `load_config` function.
    """
    # Load the configuration from the config.ini file
    try:
        output_file, key_length, start, end = load_config()
    except Exception as e:
        print(f"Error while loading the configuration: {e}")
        return

    # Calculate the total number of keys to generate
    total_keys = end - start + 1
    print(f"Total number of keys to generate: {total_keys}")

    try:
        os.remove(output_file)  # Delete the file if it already exists
    except FileNotFoundError:
        pass

    try:
        with open(output_file, "w") as file:
            # Loop to generate all 12-character keys from 0 to F
            for i in range(start, end + 1):
                # The expression {i:0{key_length}X} indicates that `i` should be displayed as
                # an uppercase hexadecimal number (thanks to "X") and that the total width of
                # the string should be equal to `key_length`, with zeros added at the beginning
                # if necessary (the "0" before the width).
                key = f"{i:0{key_length}X}"
                # Write the key to the file with a newline character
                file.write(key + "\n")
    except Exception as e:
        print(f"Error while writing keys to the file {output_file}: {e}")
        return

    # Display a confirmation message
    print(f"Keys generated and saved in {output_file}")


if __name__ == "__main__":
    main()
