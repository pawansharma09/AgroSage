class KnowledgeBase:
    """Simulated RAG system with Indian agricultural knowledge"""
    
    @staticmethod
    def get_crop_info(crop_name, state=""):
        """Get crop-specific information"""
        crop_db = {
            "rice": {
                "best_season": "Kharif (June-November)",
                "water_requirement": "1200-1500mm",
                "soil_type": "Clay loam, well-drained",
                "fertilizer": "NPK 120:60:40 kg/ha",
                "pests": ["Brown planthopper", "Stem borer", "Leaf folder"]
            },
            "wheat": {
                "best_season": "Rabi (November-April)",
                "water_requirement": "450-650mm",
                "soil_type": "Well-drained loam",
                "fertilizer": "NPK 120:60:40 kg/ha",
                "pests": ["Aphids", "Termites", "Rust diseases"]
            },
            "cotton": {
                "best_season": "Kharif (April-October)",
                "water_requirement": "700-1300mm",
                "soil_type": "Black cotton soil",
                "fertilizer": "NPK 100:50:50 kg/ha",
                "pests": ["Bollworm", "Aphids", "Whitefly"]
            },
            "sugarcane": {
                "best_season": "Year-round",
                "water_requirement": "1800-2500mm",
                "soil_type": "Deep, well-drained soil",
                "fertilizer": "NPK 300:75:75 kg/ha",
                "pests": ["Early shoot borer", "Root borer", "Scale insects"]
            }
        }
        
        return crop_db.get(crop_name.lower(), {
            "message": "Crop information not found. Please consult local agricultural extension officer."
        })
    
    @staticmethod
    def get_government_schemes():
        """Get information about government schemes"""
        schemes = [
            {
                "name": "PM-KISAN",
                "description": "₹6000 per year direct income support",
                "eligibility": "Small and marginal farmers"
            },
            {
                "name": "Pradhan Mantri Fasal Bima Yojana",
                "description": "Crop insurance against natural calamities",
                "eligibility": "All farmers"
            },
            {
                "name": "Kisan Credit Card",
                "description": "Easy access to credit for farming needs",
                "eligibility": "All farmers with land documents"
            },
            {
                "name": "Soil Health Card",
                "description": "Free soil testing and nutrient recommendations",
                "eligibility": "All farmers"
            }
        ]
        return schemes
    
    @staticmethod
    def get_market_prices():
        """Simulated market prices (in real app, would connect to AgriPortal API)"""
        crops = ["Rice", "Wheat", "Cotton", "Sugarcane", "Onion", "Potato", "Tomato"]
        prices = []
        
        for crop in crops:
            base_price = random.randint(1500, 5000)
            prices.append({
                "crop": crop,
                "price": f"₹{base_price}/quintal",
                "market": "Mandal Average",
                "trend": random.choice(["📈 Rising", "📉 Falling", "➖ Stable"])
            })
        
        return prices