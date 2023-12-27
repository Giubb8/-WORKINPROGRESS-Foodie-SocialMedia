from openfoodfacts import API, APIVersion, Country, Environment, Flavor
import openfoodfacts

api = API(
    user_agent="Foodie",
    username=None,
    password=None,
    country=Country.world,
    flavor=Flavor.off,
    version=APIVersion.v2,
    environment=Environment.org,
)
api = openfoodfacts.API(user_agent="Foodie")

results = api.product.text_search("pizza")
print(results)