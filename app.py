from bottle import *
import requests

application = Bottle()

# Serve static files
@application.route("/static/<filepath:path>")
def serve_static(filepath):
    return static_file(filepath, root="./static")

@application.route("/", method=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.forms.get("city").lower()
        try:
            url = f"https://api.waqi.info/feed/{city}/?token=50d6cd8173c467f1d4a92f687b3ea2b080b18abc"
            res = requests.get(url)
            data = res.json()

            if data["status"] != "ok":
                return template("home", msg="Enter valid City name", apl="", hi="", cs="")

            aqi = data["data"]["aqi"]
            msg = f"Air Quality Index : {aqi}"

            if 0 <= aqi <= 50:
                apl = "Air pollution Level : Good"
                hi = "Health Implications : Air quality is considered satisfactory, and air pollution poses little or no risk"
                cs = "Cautionary Statement : None"
            elif 51 <= aqi <= 100:
                apl = "Air pollution Level : Moderate"
                hi = "Health Implications : Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a small number of people who are unusually sensitive to air pollution"
                cs = "Cautionary Statement : Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
            elif 101 <= aqi <= 150:
                apl = "Air pollution Level : Unhealthy for Sensitive People"
                hi = "Health Implications : Members of sensitive groups may experience health effects. The general public is not likely to be affected."
                cs = "Cautionary Statement : Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion."
            elif 151 <= aqi <= 200:
                apl = "Air pollution Level : Unhealthy"
                hi = "Health Implications : Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
                cs = "Cautionary Statement : Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion."
            elif 201 <= aqi <= 300:
                apl = "Air pollution Level : Very Unhealthy"
                hi = "Health Implications : Health warnings of emergency conditions. The entire population is more likely to be affected."
                cs = "Cautionary Statement : Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion."
            else:
                apl = "Air pollution Level : Hazardous"
                hi = "Health Implications : Health Alert: Everyone may experience more serious health effects."
                cs = "Cautionary Statement : Everyone should avoid all outdoor exertion."

            return template("home", msg=msg, apl=apl, hi=hi, cs=cs)

        except Exception:
            return template("home", msg="Enter valid City name", apl="", hi="", cs="")
    else:
        return template("home", msg="", apl="", hi="", cs="")

run(application, debug=True, reloader=True, port=9000)
