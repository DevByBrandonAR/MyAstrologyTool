# MyAstrologyTool


> ⚠️ **Development Status: Beta**  
> This project is currently in active beta. The core structures are stable, but specific calculation logic and available features are in flux. Basically you can enter latitude and longitude, birth time and date, and timezone, and get a chart. This leverages several libraries to get this astronomical information into a usable arrangement.

## Installation
```bash
git clone https://github.com/DevByBrandonAR/MyAstrologyTool.git
cd MyAstrologyTool
python3 -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
python3 -m pip install .
```

## Sample Partial Terminal Session 
```
#The output is lengthy, but this is an example of what to expect from terminal input/output
#After entering date and time, the chart is generated, a listing of house and planet placements, 
#and aspects between planets is printed to stdout. 
#The swisseph library provides more house system options but the app is providing options for some
#of them pending more testing 

(venv) ~/Desktop/Test2/MyAstrologyTool ¶ python3 main.py
Enter location: NYC
These are some options for house systems. Enter an option from these
Placidus
Alcabitius
Porphyry
Enter here: Alcabitius
Enter timezone. Enter HELP to see options:America/New_York
Please enter date and time as d/m/yyyy,hh:mm (24-hour): 1/1/1970,3:36
```

## Known Issues
* **Plotting Layout:** Certain overlapping components or crowded markers may occasionally affect rendering. A fix is currently being investigated for the next revision.

### Sample Plot Output
![Generated Plot Output](Figure_1.png)
