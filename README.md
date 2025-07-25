# ⚡EV Charging Station Smart Planner

A smart, interactive, and intuitive web app to **identify optimal EV charging station locations** based on location, footfall, area, vehicle count. Designed using **Streamlit**, it simplifies urban EV infrastructure planning by letting users upload their own data and visualize results through maps, charts, and downloadable insights.

---

## 🌐 Live Demo
https://github.com/user-attachments/assets/b027721d-4008-4518-ac49-009a7565e1ee

---

## 📸 Screenshots

<img width="1358" height="623" alt="image" src="https://github.com/user-attachments/assets/e5d8f541-0411-434c-9a07-71787c00b4c5" />
<img width="1365" height="711" alt="image" src="https://github.com/user-attachments/assets/0a901080-d96a-4266-a09f-b119ecd6f3f2" />
<img width="1363" height="711" alt="image" src="https://github.com/user-attachments/assets/fc4bc636-d34b-46f6-8355-9b21c8c2d338" />


---

## 🚀 Features

✅ Upload your own Excel file (with `Location`, `Latitude`, `Longitude`, `Area`, `Vehicles`, `Footfall`)  
✅ Automatically calculate distances between locations  
✅ Normalize data for scoring  
✅ Customize weights for Area, Vehicles, Footfall, and Distance  
✅ View Top-N optimal locations  
✅ Interactive map (Folium) with clickable location markers  
✅ Bar chart comparison of scores  
✅ Download results as Excel

---

## 📂 Folder Structure
````
EVChargerPlannerApp/
│
├── app.py           # Main Streamlit app
├── images/          # Dashboard and map screenshots
├── requirements.txt # All Python dependencies
├── style.css        # Custom UI styling
└── README.md        # Project description
````
---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **Folium**
- **Altair/Plotly**
- **HTML/CSS (for design)**

---

## 🔧 Installation & Run Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sunidhi009/EVChargerPlannerApp.git
   cd EVChargerPlannerApp

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Run the App**
   ```bash
   streamlit run app.py
Open your browser at http://localhost:8501 to access the app.

---

## 📊Functionalities & Workflow

### Step-by-Step Use

1. Upload Excel File
-  Ensure your file includes columns: Location, Latitude, Longitude, Area, Vehicles, Footfall.

2. Adjust Weights
-  Use sliders to set the importance of each factor.

3. Visualize Results
-  View best locations on an interactive map with clickable markers.

4. Compare Scores
-  A bar chart shows a ranked comparison of scores.

5. Download Excel Report
-  Export the top-N ranked locations for documentation or planning use.

---

## Security Notes

- **User data is processed locally; no cloud storage or external APIs are used.**
- **Ensure data uploaded contains valid values for accurate scoring.**
- **Application is read-only and does not store any data unless downloaded.**

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 👥 Developer

- 👩‍💻 **[Sunidhi Choudhary](https://github.com/sunidhi009)** 
