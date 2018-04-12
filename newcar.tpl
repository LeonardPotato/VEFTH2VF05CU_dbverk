<!doctype html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>

    <form action="/db/add" method="POST">
        <fieldset>
            <legend>Nýskrá</legend>
            <label>Skráningarnúmer:</label>
            <input type="text" name="skr_nr" required>
            <br><br>
            <label>Tegund:</label>
            <input type="text" name="tegund" required>
            <br><br>
            <label>Verksmiðjunúmer:</label>
            <input type="text" name="vrk_nr" required>
            <br><br>
            <label>Skráningardagur:</label>
            <input type="text" name="skr_dags" required placeholder="áááá-mm-dd">
            <br><br>
            <label>CO2 gildi:</label>
            <input type="number" name="co2" required>
            <br><br>
            <label>Þyngd:</label>
            <input type="number" name="tyngd" required>
            <br><br>
            <label>Skoðunardagur:</label>
            <input type="text" name="sko_dags" required placeholder="áááá-mm-dd">
            <br><br>
            <label>Staða:</label>
            <input type="text" name="stada" required>
            <br><br>

            <input type="submit" value="Skrá">
        </fieldset>
    </form>

</body>
</html>