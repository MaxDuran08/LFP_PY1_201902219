class Reportes:
    def __init__(self) -> None:
        pass
    
    def ReporteTokens(self,info):
        text="""
        <html>
        <title>
        Reporte de Tokens
        </title>
        <head>
        <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
        </head>
        <body style="background-color: #E7FAF8;">

        <font face="nunito,arial,verdana">

        <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
        <tbody style="border: hidden;">
        <tr style="border: hidden; height: 104px;">
        <td style="height: 90px; width: 8%; text-align: left;"><img src="https://i.ibb.co/xhT1W0r/escudo10.png" alt="Usac" width="100" height="100" border="0" /></td>
        <td style="height: 90px; width: 92%;">
        <h2><strong>Nombre: Max Rodrigo Dur&aacute;n Canteo</strong></h2>
        <h2><strong>RA: 201902219</strong></h2>
        </td>
        </tr>
        </tbody>
        </table>
        <h3 style="text-align: center;">REPORTE DE TOKENS</h3>
        <table style="height: 54px; width: 100%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="3">
        <tbody>
        <tr style="height: 36px;background-color: #13b6a7">
        <td style="width: 25%; height: 36px; text-align: center;">TIPO DE TOKEN</td>
        <td style="width: 25%; height: 36px; text-align: center;">FILA</td>
        <td style="width: 25%; height: 36px; text-align: center;">COLUMNA</td>
	    <td style="width: 25%; height: 36px; text-align: center;">TOKEN</td>
        </tr>
        """
        for token in info:
            text+="""
            <tr style="height: 18px;background-color: #FFFFFF">
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.tipo)+"""</td>
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.linea)+"""</td>
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.columna)+"""</td>
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.lexema)+"""</td>
            </tr>
            """

        text+="""
        </tbody>
        </table>
        </font>
        </body>
        </html>
        """
    
        Reporte=open("./Reportes/ReporteTokens.html","w+")
        Reporte.write(text)
        Reporte.close

    def ReporteErrores(self,info):
        text="""
        <html>
        <title>
        Reporte de Errores
        </title>
        <head>
        <link rel="icon" href="https://i.ibb.co/xhT1W0r/escudo10.png">
        </head>
        <body style="background-color: #E7FAF8;">

        <font face="nunito,arial,verdana">

        <table style="border: hidden; width: 100%; height: 90px; margin-left: auto; margin-right: auto;">
        <tbody style="border: hidden;">
        <tr style="border: hidden; height: 104px;">
        <td style="height: 90px; width: 8%; text-align: left;"><img src="https://i.ibb.co/xhT1W0r/escudo10.png" alt="Usac" width="100" height="100" border="0" /></td>
        <td style="height: 90px; width: 92%;">
        <h2><strong>Nombre: Max Rodrigo Dur&aacute;n Canteo</strong></h2>
        <h2><strong>RA: 201902219</strong></h2>
        </td>
        </tr>
        </tbody>
        </table>
        <h3 style="text-align: center;">REPORTE DE ERRORES</h3>
        <table style="height: 54px; width: 100%; border-collapse: collapse; margin-left: auto; margin-right: auto;" border="3">
        <tbody>
        <tr style="height: 36px;background-color: #13b6a7">
        <td style="width: 25%; height: 36px; text-align: center;">TOKEN</td>
        <td style="width: 25%; height: 36px; text-align: center;">FILA</td>
        <td style="width: 25%; height: 36px; text-align: center;">COLUMNA</td>
        </tr>
        """
        for token in info:
            text+="""
            <tr style="height: 18px;background-color: #FFFFFF">
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.descripcion)+"""</td>
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.linea)+"""</td>
            <td style="width: 25%; height: 18px; text-align: center;">"""+str(token.columna)+"""</td>
            </tr>
            """

        text+="""
        </tbody>
        </table>
        </font>
        </body>
        </html>
        """
    
        Reporte=open("./Reportes/ReporteErrores.html","w+")
        Reporte.write(text)
        Reporte.close