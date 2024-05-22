def add_farm():
    """Adds a farm to the database."""
    # Get the farm information from the user.
    farm_name = input("Enter the farm name: ")
    farm_address = input("Enter the farm address: ")
    farm_phone = input("Enter the farm phone number: ")
    farm_email = input("Enter the farm email address: ")
    farm_website = input("Enter the farm website: ")
    farm_description = input("Enter a description of the farm: ")

    # Create a new farm object.
    farm = Farm(farm_name, farm_address, farm_phone, farm_email, farm_website, farm_description)

    # Add the farm to the database.
    session.add(farm)
    session.commit()

    # Print a success message.
    print("Farm added successfully.")

