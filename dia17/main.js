<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dia 17 - 100 Dias De Código</title>
        <link rel="stylesheet" href="style.css">
    </head>

    <body>
        <img src="logo.png" alt="logo do projeto" class="logo">
        
        <main class="container-input">
            <span>Tamanho<span id="valor"></span>caracteres</span>
            <input type="range" id="slidert" min="5" max="25" value="15">

            <button id="button" class="button-cte" onclick=""></button>
        </main>

        <div class="container-password" onclick="">
            <span class="title">Sua senha gerada é:</span>
            <span id="password" class="password"></span>
            <span class="tooltip">Clique na senha para copiar</span>
        </div>
        
        <script src="main.js"></script>
    </body>
</html>