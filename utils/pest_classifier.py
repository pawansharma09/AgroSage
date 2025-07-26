from PIL import Image
import os

class PestClassifier:
    """Simulated pest/disease classification based on image filename keywords"""

    pests = [
        {
            "name": "Brown Planthopper",
            "keywords": ["brownplanthopper", "bph", "planthopper"],
            "crop": "Rice",
            "treatment": "Use Imidacloprid 17.8% SL @ 100ml/acre",
            "organic_treatment": "Neem oil spray, encourage natural predators"
        },
        {
            "name": "Aphids",
            "keywords": ["aphid", "aphids"],
            "crop": "Multiple crops",
            "treatment": "Thiamethoxam 25% WG @ 100g/acre",
            "organic_treatment": "Soap water spray, ladybird beetles"
        },
        {
            "name": "Leaf Blight",
            "keywords": ["blight", "leafblight"],
            "crop": "Wheat",
            "treatment": "Propiconazole 25% EC @ 250ml/acre",
            "organic_treatment": "Copper fungicide, proper spacing"
        },
        {
            "name": "Stem Borer",
            "keywords": ["stemborer", "stem_borer"],
            "crop": "Rice, Maize",
            "treatment": "Carbofuran 3G @ 10kg/acre",
            "organic_treatment": "Use Trichogramma chilonis parasitoids"
        },
        {
            "name": "Fruit Fly",
            "keywords": ["fruitfly", "fruit_fly"],
            "crop": "Fruits (Mango, Guava)",
            "treatment": "Malathion bait spray",
            "organic_treatment": "Fermented jaggery traps"
        },
        {
            "name": "Powdery Mildew",
            "keywords": ["powdery", "mildew"],
            "crop": "Grapes, Peas, Cucurbits",
            "treatment": "Sulfex @ 3g/L",
            "organic_treatment": "Baking soda + oil spray"
        },
        {
            "name": "Root Knot Nematode",
            "keywords": ["nematode", "rootknot"],
            "crop": "Vegetables",
            "treatment": "Carbofuran 3G @ 10kg/acre",
            "organic_treatment": "Neem cake, marigold intercrop"
        },
        {
            "name": "Shoot Fly",
            "keywords": ["shootfly", "shoot_fly"],
            "crop": "Sorghum, Maize",
            "treatment": "Phorate 10G @ 10kg/acre",
            "organic_treatment": "Early sowing, neem kernel extract"
        },
        {
            "name": "Tobacco Caterpillar",
            "keywords": ["tobaccocaterpillar", "caterpillar"],
            "crop": "Soybean, Cotton",
            "treatment": "Indoxacarb 14.5% SC",
            "organic_treatment": "Neem oil, NPV spray"
        },
        {
            "name": "Downy Mildew",
            "keywords": ["downy", "downymildew"],
            "crop": "Grapes, Mustard",
            "treatment": "Metalaxyl 8% + Mancozeb 64%",
            "organic_treatment": "Garlic extract spray"
        },
        {
            "name": "Cutworm",
            "keywords": ["cutworm", "cut_worm"],
            "crop": "Groundnut, Maize",
            "treatment": "Chlorpyrifos 20% EC",
            "organic_treatment": "Ash + neem powder barrier"
        },
        {
            "name": "Whitefly",
            "keywords": ["whitefly", "white_fly"],
            "crop": "Cotton, Brinjal",
            "treatment": "Acetamiprid 20 SP",
            "organic_treatment": "Sticky traps, neem oil"
        },
        {
            "name": "Helicoverpa",
            "keywords": ["helicoverpa", "bollworm"],
            "crop": "Chickpea, Cotton",
            "treatment": "Spinosad 45% SC",
            "organic_treatment": "HNPV, marigold trap crop"
        },
        {
            "name": "Red Spider Mite",
            "keywords": ["spidermite", "redmite"],
            "crop": "Tea, Okra",
            "treatment": "Dicofol 18.5% EC",
            "organic_treatment": "Garlic + chilli extract"
        },
        {
            "name": "Jassids",
            "keywords": ["jassid", "jassids"],
            "crop": "Cotton, Okra",
            "treatment": "Imidacloprid 17.8% SL",
            "organic_treatment": "Neem + castor leaf extract"
        }
    ]

    @staticmethod
    def classify_image(image):
        """Classify pest based on filename keywords (basic simulation)"""
        if hasattr(image, "name"):
            filename = image.name.lower()
        else:
            filename = "unknown"

        for pest in PestClassifier.pests:
            if any(keyword in filename for keyword in pest["keywords"]):
                return {
                    "name": pest["name"],
                    "confidence": 0.9,  # simulated confidence
                    "crop": pest["crop"],
                    "treatment": pest["treatment"],
                    "organic_treatment": pest["organic_treatment"]
                }

        # If nothing matches, return unknown
        return {
            "name": "Unknown",
            "confidence": 0.45,
            "crop": "N/A",
            "treatment": "No confident match. Try a clearer image or rename file to include pest name.",
            "organic_treatment": "-"
        }
