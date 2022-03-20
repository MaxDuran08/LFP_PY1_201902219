class Formularios:
    def __init__(self,entrada):
        self.Lista=[]
        self.idGrupoOption=1
        self.idGrupoRadio=1
        self.contador=0
        self.entrada = entrada
        

    def Crear(self,Lista):
        key=False
        ListaTemp=[]
        for i in Lista:
            ListaTemp.append(i.valor())
        ListaTemp2=[]
        ListaTemp3=[]
        for i in range(len(ListaTemp)):
            if ListaTemp[i][0]=="<":
                key=True
            elif ListaTemp[i][0]==">":
                key=False
                
            if key==True:
                ListaTemp2.append(ListaTemp[i])
            else:
                if len(ListaTemp2)>4:
                    ListaTemp2.append(ListaTemp[i])
                    ListaTemp3.append(ListaTemp2)
                    ListaTemp2=[]
        for i in ListaTemp3:
            ListaTemp4=[]
            for j in range(len(i)):
                if self.esReservadaFacil(i[j][1]):
                    ListaTemp5=[]
                    ListaTemp5.append(i[j][0])
                    palabra=""
                    j+=3
                    while True:
                        try:
                            if str(i[j][1])=="palabra" or str(i[j][1])=="guion" or self.esReservadaFacil(i[j][1]):
                                palabra+=str(i[j][0])
                                try:
                                    if str(i[j+1][1])=="guion" or str(i[j+1][1])=="palabra" or self.esReservadaFacil(i[j+1][1]):
                                        if str(i[j+1][1])=="palabra" or self.esReservadaFacil(i[j+1][1]):
                                            palabra+=" "
                                        if str(i[j][1])=="guion":
                                            palabra=palabra[:-1]
                                        j+=1
                                    else:
                                        break
                                except:
                                    break
                        except:
                            break
                    ListaTemp5.append(palabra)
                    if ListaTemp5[0]!=""and ListaTemp5[1]!="":
                        ListaTemp4.append(ListaTemp5)
                try:
                    if str(i[j][1])=="reservada_valores":
                        ListaTemp5=[]
                        ListaTemp5.append(i[j][0])
                        j+=4
                        key1=True
                        while key1:
                            palabra=""
                            while True:
                                try:
                                    if str(i[j][1])=="palabra" or self.esReservadaFacil(i[j][1]):
                                        palabra+=str(i[j][0])
                                        try:
                                            if str(i[j+1][1])=="palabra" or self.esReservadaFacil(i[j+1][1]):
                                                if str(i[j+1][1])=="palabra" or self.esReservadaFacil(i[j+1][1]):
                                                    palabra+=" "
                                                j+=1
                                            else:
                                                break
                                        except:
                                            break
                                except:
                                    break
                            ListaTemp5.append(palabra)
                            try:
                                if str(i[j+4][1])=="palabra" or self.esReservadaFacil(i[j+4][1]):
                                    j+=4
                                else:
                                    key1=False
                            except:
                                key1=False
                        if ListaTemp5[0]!=""and ListaTemp5[1]!="":
                            ListaTemp4.append(ListaTemp5)
                except:
                    break
                if str(i[j][1])=="reservada_evento":
                    ListaTemp5=[]
                    ListaTemp5.append(i[j][0])
                    x=0
                    while True:
                        if str(i[j+x][1])=="palabra":
                            ListaTemp5.append(i[j+x][0])
                            break
                        else:
                            x+=1
                    if ListaTemp5[0]!=""and ListaTemp5[1]!="":
                            ListaTemp4.append(ListaTemp5)
            self.Lista.append(ListaTemp4)
        self.generarFormulario()
        

    def generarFormulario(self):
        txt="""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario</title>
    <link rel="stylesheet" href="Estilo.css" />
</head>
<body>
<form class="form" id ='form'>
        """

        


        for i in self.Lista:
            print("==========================>")
            print(i)
            if i[0][1]=="etiqueta":
                print("crea etiqueta")
                txt+="""
                <div class="Etiqueta">
                <p>"""+i[1][1]+""":</p>
                </div>
                """
            if i[0][1]=="texto":
                print("crea texto")
                txt+="""
                <div class="contenedorTxt">
                <input class="Txt" type="text" name=\""""+i[1][1]+"""\" id=\""""+str(self.contador)+"""\" """
                try:
                    txt+="""
                    placeholder=\""""+i[2][1]+"""\" 
                    """
                except:
                    True
                txt+=""">
                </div>
                """
                self.contador+=1
            if i[0][1]=="grupo-radio":
                print("crear grupo-radio")
                txt+="""
                <div class="containerRadio">
                <div>
                    <label>"""+i[1][1]+""":</label>
                </div>
                <div class="seleccionRadio">"""

                for j in range(len(i[2])):
                    if j>0:
                        txt+="""
                <div class="OpccionesRadio" id=\""""+str(self.contador)+"""\">
                    <input type="radio" class="radio" id=\""""+i[2][j]+"""\" name=\""""+str(self.idGrupoRadio)+"""\">
                    <label for=\""""+i[2][j]+"""\">"""+i[2][j]+"""</label>
                </div>
                """
                        self.contador +=1
                txt+="""</div>
                </div>
                """
                self.idGrupoRadio += 1
            if i[0][1]=="grupo-option":
                print("crear grupo-option")
                txt+="""
                <div class="container">
                <h2>"""+i[1][1]+"""</h2>
                <div class="select-box">
                <div id="c1">
                """
                
                for j in range(len(i[2])):
                    if j>0:
                        txt+="""
                        <div class="option" id=\""""+str(self.contador)+"""\">
                        <input type="radio" class="radio"  name=\""""+str(self.idGrupoRadio)+"""\">
                        <label for=\""""+i[2][j]+"""\">"""+i[2][j]+"""</label>
                        </div>
                        """
                        self.contador += 1
                txt+="""
                </div>
                </div>
                </div>
                """
                self.idGrupoRadio += 1
            if i[0][1]=="boton":
                print("crear boton")
                txt+="""
                <div class="Boton">
                <input class="boton" type="submit"  info=\""""+i[2][1]+"""\" id=\""""+str(self.contador)+"""\" value=\""""+i[1][1]+"""\"/>
                </div>
                """
                self.contador+=1

        txt+="""
</form>
<script>
    document.getElementById('form').addEventListener('submit', (e) => {
        e.preventDefault();
    })
    let infoEntrada = `""" + str(self.entrada)+"""`
    let ids="""+str(self.contador)+"""
    var component=[]
    var componentesIngreso =[]
    let buttons;
    
    
    document.addEventListener('DOMContentLoaded',(e)=> {
        for(let i=0;i<ids;i++){
            component[i]=document.getElementById(`${i}`)
        }
        
        buttons = component.filter((data) => {
            return data.type == 'submit'
        })

        componentesIngreso = component.filter((data) => {
            return data.type != 'submit'
        })
        
        buttons.forEach((element, i ) => {
            element.addEventListener('click', (e) => {
                const info = e.path[0].attributes.info.value
                if(info == 'info'){
                    
                    alert('Datos: ');
                }else if(info == 'entrada'){
                    alert(`Datos de entrada: ${infoEntrada}`);
                }
            })
        })

        console.log(buttons)
    })
</script>
<script src="Formulario/main.js"></script>
</body>
</html>
        """
        try:
            Reporte=open("./Formulario/Formulario.html","w+")
            Reporte.write(txt)
            Reporte.close
        except:
            True

            
    def esReservadaFacil(self,lexema):
        if lexema=="reservada_valor":
            return True
        elif lexema=="reservada_tipo":
            return True
        elif lexema=="reservada_fondo":
            return True
        elif lexema=="reservada_nombre":
            return True
        else:
            return False
        #'reservada_valor' or 'reservada_tipo' or 'reservada_fondo' or 'reservada_nombre' or 'reservada_valores' or 'reservada_evento'