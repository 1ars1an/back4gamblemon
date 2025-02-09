import requests
from .models import Poketype  # Import your Poketype model

POKEAPI_TYPES_URL = "https://pokeapi.co/api/v2/type/"

def populate_poketype_database():
    try:
        response = requests.get(POKEAPI_TYPES_URL)
        response.raise_for_status()  # Check for HTTP errors
        type_data = response.json()

        for type_entry in type_data['results']:
            name = type_entry['name']
            url = type_entry['url']

            # Check if the type already exists (case-insensitive) before creating
            poketype, created = Poketype.objects.get_or_create(
                name__iexact=name,  # Case-insensitive lookup
                defaults={'url': url}  # Only set URL if creating
            )

            if created:
                print(f"Created Poketype: {name}")
            else:
                print(f"Poketype {name} already exists.")


    except requests.exceptions.RequestException as e:
        print(f"Error fetching type data: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    populate_poketype_database()