
def render_market_info():
    """Render market information"""
    st.header("💰 Market Prices")
    
    prices = KnowledgeBase.get_market_prices()
    
    # Create DataFrame for better display
    df = pd.DataFrame(prices)
    
    # Display as styled table
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )
    
    # Price alerts
    st.markdown("### 🔔 Price Alerts")
    selected_crop = st.selectbox("Select crop for price alerts", [p["crop"] for p in prices])
    target_price = st.number_input("Target price (₹/quintal)", min_value=1000, value=3000)
    
    if st.button("Set Price Alert"):
        st.success(f"Price alert set for {selected_crop} at ₹{target_price}/quintal")
