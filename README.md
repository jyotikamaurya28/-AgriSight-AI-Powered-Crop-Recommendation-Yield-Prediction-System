# AgriSight-AI-Powered-Crop-Recommender-Risk-Forecaster-Virtual-AgriBot
AgriSight is an AI-powered farming assistant that recommends crops, predicts success, shows live weather, and offers smart tips. It features a chatbot for instant farming help. Built with Botpress, it helps UP farmers make smart, data-driven decisions.

AgriSight is an intelligent, full-stack agricultural decision-support web app built with Streamlit and Python, designed specifically to empower farmers in regions like Uttar Pradesh, India. The system integrates machine learning for crop recommendation and farming risk forecasting, live weather forecasting via WeatherAPI, and a conversational assistant powered by Botpress and LLMs to provide real-time farming guidance.

Project Overview
At its core, AgriSight addresses two major challenges faced by farmers: choosing the right crop for given soil and weather conditions, and assessing the likelihood of successful crop production. To solve these, the app uses pre-trained ML models—one for crop recommendation and another for success prediction—both trained on regional data. The user interface is built with Streamlit, offering an intuitive experience for farmers or agriculture officers with minimal technical knowledge.

The application simulates or pulls in real-world values for essential farming parameters such as soil nutrients (NPK), pH, rainfall, and weather. Users can interactively input their district and intended farming date, and the app predicts the best crop to plant along with a success score indicating the risk level. It also integrates an LLM module for smart farming advice, and includes real-time district-wise weather forecasts and alerts, providing a holistic view for decision-making.

Intelligent Prediction System
The crop recommendation model utilizes soil macronutrients and environmental conditions to suggest the most suitable crop. The success prediction model evaluates micronutrients (like Zinc, Iron, Manganese, Copper, Sulphur, and Boron), land area, and production data to estimate the probability of a successful harvest. These predictions are visualized within the app using intuitive indicators—success messages for high probabilities, warnings for moderate, and alerts for high risk.

Real-Time Weather Integration
AgriSight integrates the WeatherAPI to offer real-time district-wise forecasts for all 75 districts in Uttar Pradesh. The user selects their district and a preferred forecast range (1 to 8 days), and the app fetches relevant data including daily max/min temperatures, weather conditions, and rain probability. Additionally, the application fetches and displays government weather alerts, enabling early preparation against extreme events like floods or droughts.

Smart Farming Advice (LLM)
Beyond numerical predictions, AgriSight offers intelligent farming insights powered by a Large Language Model (via OpenAI) through a custom-built module. This system generates context-aware advice based on the predicted crop, date, and location. Users receive practical, dynamic farming tips relevant to their conditions—helping bridge the knowledge gap and encourage modern farming techniques.

AgriBot – AI Chat Assistant
The platform also includes a virtual AgriBot, integrated via Botpress. It is embedded as an HTML widget inside the app and serves as a 24/7 conversational agent. Farmers can use AgriBot to ask queries in simple language, get fertilizer recommendations, or understand best practices in real time. This chatbot experience is particularly valuable for users who prefer natural interaction over forms or buttons.

## 🧠 Technologies Used

- **Python 3.8+**
- **Streamlit** – UI framework for dashboards
- **scikit-learn** – ML model development
- **Pandas / NumPy** – Data processing
- **OpenAI API** – For LLM-based advisories
- **Joblib** – Model serialization
- **dotenv** – For environment variable management
- **Botpress** – For AgriBot – AI Chat Assistant
- 
Setup and Deployment
The application uses a .env file to manage secrets such as the WeatherAPI key and OpenAI key. Trained models are loaded from the /models directory, and all code is modularized into llm/, models/, and app/ folders. With the included Python scripts and requirements, users can deploy the app locally or on cloud platforms like Streamlit Sharing or Heroku.

To run it:

Set up Python and install dependencies via requirements.txt.

Add your API keys in .env.

Launch using: streamlit run app/streamlit_app.py.

Real-World Applications
AgriSight is best suited for:

Farmers needing personalized crop and risk planning.

Government officers advising rural communities.

NGOs promoting climate-resilient agriculture.

Educational institutes teaching agri-tech innovations.

Final Thoughts
AgriSight is more than a prediction tool—it’s a digital assistant for farmers. By combining machine learning, weather forecasting, and language models, it provides proactive, accessible, and smart agricultural planning support. With its scalable architecture, it can easily be expanded to other states or countries and incorporate satellite or IoT data in the future.
