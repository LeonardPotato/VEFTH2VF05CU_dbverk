<!doctype html>
<html lang="is">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=yes, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>{{bill[0]}}</title>
</head>
<body>
    % for b in bill:
    <p>{{b}}</p>
    % end

    <p><a href="/db/del/{{bill[0]}}">Eyða færslu</a></p>
    <p><a href="/db/update/{{bill[0]}}">Breyta færslu</a></p>
</body>
</html>