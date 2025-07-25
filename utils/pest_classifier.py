class PestClassifier:
    """Simulated pest/disease classification"""
    
    @staticmethod
    def classify_image(image):
        """Simulate pest/disease classification"""
        # In real implementation, this would use a trained CNN model
        pests = [
            {
                "name": "Brown Planthopper",
                "confidence": 0.85,
                "crop": "Rice",
                "treatment": "Use Imidacloprid 17.8% SL @ 100ml/acre",
                "organic_treatment": "Neem oil spray, encourage natural predators"
            },
            {
                "name": "Aphids",
                "confidence": 0.78,
                "crop": "Multiple crops",
                "treatment": "Thiamethoxam 25% WG @ 100g/acre",
                "organic_treatment": "Soap water spray, ladybird beetles"
            },
            {
                "name": "Leaf Blight",
                "confidence": 0.72,
                "crop": "Wheat",
                "treatment": "Propiconazole 25% EC @ 250ml/acre",
                "organic_treatment": "Copper fungicide, proper spacing"
            }
        ]
        
        return random.choice(pests)