<!doctype html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=yes, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Breyta skraningu</title>
</head>
<body>
    <form action="/db/update" method="POST">
        <fieldset>
            <legend>Breyta skráningu</legend>
            <label>Skráningarnúmer:</label>
            <input type="text" name="skr_nr" required value="{{bill[0]}}">
            <br><br>
            <label>Tegund:</label>
            <input type="text" name="tegund" required value="{{bill[1]}}">
            <br><br>
            <label>Verksmiðjunúmer:</label>
            <input type="text" name="vrk_nr" required value="{{bill[2]}}">
            <br><br>
            <label>Skráningardagur:</label>
            <input type="text" name="skr_dags" required value="{{bill[3]}}">
            <br><br>
            <label>CO2 gildi:</label>
            <input type="number" name="co2" required value="{{bill[4]}}">
            <br><br>
            <label>Þyngd:</label>
            <input type="number" name="tyngd" required value="{{bill[5]}}">
            <br><br>
            <label>Skoðunardagur:</label>
            <input type="text" name="sko_dags" required value="{{bill[6]}}">
            <br><br>
            <label>Staða:</label>
            <input type="text" name="stada" required value="{{bill[7]}}">
            <br><br>

            <input type="submit" value="Uppfæra">
        </fieldset>
    </form>
</body>
</html>