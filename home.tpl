<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Air Quality Index Finder</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <div class="wrapper">
        <div class="card fade-in">
            <h1>🌫️ Air Quality Index Finder</h1>
            <p class="subtitle">Enter your city name below to check real-time air quality levels.</p>
            
            <form method="post" class="aqi-form">
                <input type="text" name="city" placeholder="Enter city name..." required>
                <button type="submit">Check AQI</button>
            </form>

            % if msg:
                <div class="result-box">
                    <h2>{{msg}}</h2>
                    % if apl:
                        <div class="aqi-result">
                            <h3>{{apl}}</h3>
                            <p>{{hi}}</p>
                            <p>{{cs}}</p>
                        </div>
                    % end
                </div>
            % end
        </div>
        
        <footer>
            <p>💧 Powered by Bottle & OpenWeather API</p>
        </footer>
    </div>
</body>
</html>
