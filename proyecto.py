#Proyecto número 5 del ramo Fundamentos de Programación.
#Por Bryan Nilo y Javiera Barraza.
#Ingeniería Civil Informática UV 1°año sección 2.

import matplotlib.pyplot as plt
print("\n\n-Bienvenido al programa donde podrá visualizar la información dada por el Ministerio de Salud sobre el avance de la Tasa de Incidencia del COVID-19 en las últimas 7 fechas desde el día 14/06/2021 hasta 05/07/2021.\n\nMENÚ:")
print("---------------------------------------------------------------------------------------------------------------\n1)Ingrese '1' para visualizar las regiones con su respectivo código.\n2)Escriba '2' para ingresar un código de región y desplegar las comunas de la región respectivamente.\n3)Escriba '3' para ingresar una comuna y desplegar el gráfico de la Tasa de Incidencia de las últimas 7 fechas.\n4)Escriba '4' para ingresar una región y desplegar el gráfico de la Tasa de Incidencia de las últimas 7 fechas.\n5)Escriba '5' para seleccionar el grafico de la región con mayor y menor densidad de Tasa de Incidencia, respectivamente.\n6)Escriba '6' para ver el gráfico de la métrica de comparación de la Tasa de Incidencia entre regiones.\n7)Escriba '7' para salir del menú.\n---------------------------------------------------------------------------------------------------------------")
opc=input("INGRESO: ")
opc=int(opc)

#mostrar comunas filtradas por región:

if opc==1 : #menú que contiene el codigo de todas las regiones.
    print("\nMENÚ DE CÓDIGO DE REGIONES:\n")
    print("----------------------------------------------  -------------\nNOMBRE REGIÓN                                   CÓDIGO REGIÓN\nArica y Parinacota                                   15\nTarapacá                                             1\nAntofagasta                                          2\nAtacama                                              3\nCoquimbo                                             4\nValparaíso                                           5\nRegión del Libertador Gral.Bernardo O’Higgins        6\nRegión del Maule                                     7\nRegión del Biobío                                    8\nRegión de la Araucanía                               9\nRegión de los Ríos                                   14\nRegión de los Lagos                                  10\nRegión Aisén del Gral. Carlos Ibáñez del Campo       11\nRegión de Magallanes y de la Antártica Chilena       12\nRegión Metropolitana de Santiago                     13\n----------------------------------------------  -------------\n")
    print("\nPara volver a hacer otra busqueda por el menú, vuelva a ejecutar el programa.")
    
elif opc==2: #por código de región ingresado, se muestran las comunas de aquella región y sus respectivos códigos.
    codigo=str(input("Escriba el código de región para visualizar las comunas de la región ingresada:\nINGRESO:"))
    if codigo =="15":
        arica={"Arica":"15101","Camarones":"15102","Putre":"15201","General Lagos":"15202"}
        print("región de arica:")           
        print(arica)

    elif codigo =="01" :
        tarapaca={"Iquique":"01101","Alto Hospicio":"01107","Pozo Almonte": "01401","Camiña":"01402","Colchane":"01403","Huara":"01404","Pica":"01405"}
        print("región de Tarapacá:")
        print(tarapaca)

    elif codigo =="02":
        antofagasta={"Antofagasta":"02101","Mejillones":"02102","Sierra Gorda":"02103","Taltal":"02104", "Calama":"02201", "Ollagüe":"02202","San Pedro de Atacama":"02203", "Tocopilla":"02301", "María Elena":"02302"}
        print("región de Antofagasta:")
        print(antofagasta)

    elif codigo =="03":
        atacama={"Copiapó":"03101",  "Caldera":"03102", "Tierra Amarilla":"03103", "Chañaral":"03201","Diego de Almagro":"03202", "Vallenar":"03301", "Alto del Carmen":"03302", "Freirina":"03303","Huasco":"03304", }

        print("región de Atacama:")
        print(atacama)

    elif codigo == "04":
        coquimbo={"La Serena":"04101", "Coquimbo":"04102", "Andacollo":"04103", "La Higuera":"04104","Paiguano":"04105", "Vicuña":"04106", "Illapel":"04201", "Canela":"04202", "Los Vilos":"04203","Salamanca":"04204", "Ovalle":"04301", "Combarbalá":"04302", "Monte Patria":"04303","Punitaqui":"04304", "Río Hurtado":"04305"}
        
        print("región de Coquimbo:")
        print(coquimbo)

    elif codigo =="05":
        valparaiso={"Valparaíso":"05101", "Casablanca":"05102", "Concón":"05103", "Juan Fernández":"05104","Puchuncaví":"05105", "Quintero":"05107", "Viña del Mar":"05109", "Isla de Pascua":"05201","Los Andes":"05301", "Calle Larga":"05302","Rinconada":"05303", "San Esteban":"05304","La Ligua":"05401", "Cabildo":"05402", "Papudo":"05403", "Petorca":"05404", "Zapallar":"05405", "Quillota":"05501","Calera":"05502", "Hijuelas":"05503", "La Cruz":"05504", "Nogales":"05506","San Antonio":"05601", "Algarrobo":"05602", "Cartagena"  :"05603", "El Quisco":  "05604","El Tabo"  :"05605", "Santo Domingo":  "05606", "San Felipe":  "05701", "Catemu":  "05702","Llaillay":  "05703", "Panquehue":  "05704","Putaendo":  "05705","Santa María":  "05706","Quilpué":  "05801", "Limache":  "05802","Olmué":  "05803", "Villa Alemana":"05804"}
    
        print("región de Valparaíso:")
        print(valparaiso)

    elif codigo=="06":
        libertador_gral_bernardo_ohiggins={"Rancagua":"06101", "Codegua":"06102", "Coinco":"06103", "Coltauco":"06104","Doñihue":"06105", "Graneros":"06106", "Las Cabras":"06107", "Machalí":"06108", "Malloa":"06109", "Mostazal":"06110","Olivar":"06111", "Peumo":"06112", "Pichidegua":"06113","Quinta de Tilcoco":"06114", "Rengo":"06115",
        "Requínoa":"06116", "San Vicente":"06117",  "Pichilemu":"06201", "La Estrella":"06202", "Litueche":"06203",
        "Marchihue":"06204","Navidad":"06205","Paredones":"06206", "San Fernando":"06301", "Chépica":"06302",
        "Chimbarongo":"06303", "Lolol":"06304","Nancagua":"06305", "Palmilla":"06306", "Peralillo":"06307",
        "Placilla":"06308", "Pumanque":"06309", "Santa Cruz":"06310"}
    
        print("región del Libertador Gral. Bernardo O´higgins:")
        print(libertador_gral_bernardo_ohiggins)

    elif codigo=="07":
        maule={"Talca":"07101", "Constitución":"07102", "Curepto":"07103", "Empedrado":"07104",
        "Maule":"07105", "Pelarco":"07106", "Pencahue":"07107", "Río Claro":"07108", "San Clemente":"07109", 
        "San Rafael":"07110", "Cauquenes":"07201", "Chanco":"07202", "Pelluhue":"07203", "Curicó":"07301",
        "Hualañé":"07302", "Licantén":"07303", "Molina":"07304", "Rauco":"07305", "Romeral":"07306",
        "Sagrada Familia":"07307", "Teno":"07308", "Vichuquén":"07309", "Linares":"07401", "Colbún":"07402",
        "Longaví":"07403", "Parral":"07404", "Retiro":"07405", "San Javier":"07406", "Villa Alegre":"07407", 
        "Yerbas Buenas":"07408"}
        
        print("región del Maule:")
        print(maule)

    elif codigo =="08":
        biobio={"Concepción":"08101", "Coronel":"08102", "Chiguayante":"08103", "Florida":"08104","Hualqui":"08105","Lota":"08106", "Penco":"08107", "San Pedro de la Paz":"08108", "Santa Juana":"08109", "Talcahuano":"08110", "Tomé":"08111", "Hualpén":"08112", "Lebu":"08201", "Arauco":"08202", "Cañete":"08203", "Contulmo":"08204", "Curanilahue":"08205", "Los Álamos":"08206", "Tirúa":"08207", "Los Ángeles":"08301", "Antuco":"08302", 
    "Cabrero":"08303","Laja":"08304", "Mulchén":"08305", "Nacimiento":"08306", "Negrete":"08307","Quilaco":"08308",
    "Quilleco":"08309", "San Rosendo":"08310", "Santa Bárbara":"08311", "Tucapel":"08312", "Yumbel":"08313", 
    "Alto Biobío":"08314", "Chillán":"08401", "Bulnes":"08402", "Cobquecura":"08403", "Coelemu":"08404",
    "Coihueco":"08405", "Chillán Viejo":"08406", "El Carmen":"08407", "Ninhue":"08408", "Ñiquén":"08409",
    "Pemuco":"08410", "Pinto":"08411", "Portezuelo":"08412", "Quillón":"08413", "Quirihue":"08414", 
    "Ránquil":"08415", "San Carlos":"08416", "San Fabián":"08417", "San Ignacio":"08418", "San Nicolás":"08419",
    "Treguaco":"08420", "Yungay":"08421"}
        print("región del Biobío:")
        print(biobio)

    elif codigo =="09":
        araucania={"Temuco":"09101", "Carahue":"09102", "Cunco":"09103", "Curarrehue":"09104", "Freire":"09105", "Galvarino":"09106", "Gorbea":"09107", "Lautaro":"09108", "Loncoche":"09109", "Melipeuco":"09110", "Nueva Imperial":"09111", "Padre las Casas":"09112", "Perquenco":"09113", "Pitrufquén":"09114", "Pucón":"09115", "Saavedra":"09116", "Teodoro Schmidt":"09117", "Toltén":"09118", "Vilcún":"09119", "Villarica":"09120", "Cholchol":"09121", "Angol":"09201", "Collipulli":"09202", "Curacautín":"09203","Ercilla":"09204","Lonquimay":"09205", "Los Sauces":"09206", "Lumaco":"09207", "Purén":"09208", "Renaico":"09209","Traiguén":"09210","Victoria":"09211"}

        print("region de Araucanía:")
        print(araucania)

    elif codigo =="14":
        rios ={"Valdivia":"14101", "Corral":"14102", "Lanco":"14103", "Los Lagos":"14104", "Máfil":"14105", "Mariquina":"14106", "Paillaco":"14107", "Panguipulli":"14108", "La Unión":"14201", "Futrono":"14202", "Lago Ranco":"14203", "Río Bueno":"14204"}
        print("región de Los Ríos:")
        print(rios)

    elif codigo =="10":
        lagos={"Puerto Montt":"10101", "Calbuco":"10102", "Cochamó":"10103", "Fresia":"10104","Frutillar":"10105", "Los Muermos":"10106", "Llanquihue":"10107", "Maullín":"10108", "Puerto Varas":"10109", "Castro":"10201", "Ancud":"10202", "Chonchi":"10203", "Curaco de Vélez":"10204", "Dalcahue":"10205", "Puqueldón":"10206", "Queilén":"10207", "Quellón":"10208", "Quemchi":"10209", "Quinchao":"10210", "Osorno":"10301", "Puerto Octay":"10302", "Purranque":"10303", "Puyehue":"10304", "Río Negro":"10305", "San Juan de la Costa":"10306", "San Pablo":"10307", "Chaitén":"10401", "Futaleufú":"10402", "Hualaihué":"10403", "Palena":"10404"}
        print("región de Los Lagos:")
        print(lagos)

    elif codigo =="11":
        carlos_ibañez_del_campo={"Coihaique":"11101", "Lago Verde":"11102", "Aisén":"11201", "Cisnes":"11202", "Guaitecas":"11203", "Cochrane":"11301", "O’Higgins":"11302", "Tortel":"11303", "Chile Chico":"11401", "Río Ibáñez":"11402"}
        print("región Aisén del Gral.Carlos Ibáñez del Campo:")
        print(carlos_ibañez_del_campo)

    elif codigo =="12":
        magallanes_y_antartica={"Punta Arenas":"12101", "Laguna Blanca":"12102","Río Verde":"12103","San Gregorio":"12104", "Cabo de Hornos":"12201", "Antártica":"12202", "Porvenir":"12301", "Primavera":"12302", "Timaukel":"12303", "Natales":"12401","Torres del Paine":"12402"}
        print("región de Magallanes y de la Antártica Chilena: ")
        print(magallanes_y_antartica)

    
    elif codigo =="13 ":
        metropolitana_de_santiago={"Santiago":"13101", "Cerrillos":"13102", "Cerro Navia":"13103", "Conchalí":"13104", "El Bosque":"13105", "Estación Central":"13106", "Huechuraba":"13107", "Independencia":"13108", "La Cisterna":"13109", "La Florida":"13110", "La Granja":"13111", "La Pintana":"13112", "La Reina":"13113", "Las Condes":"13114", "Lo Barnechea":"13115", "Lo Espejo":"13116", "Lo Prado":"13117", "Macul":"13118", "Maipú":"13119", "Ñuñoa":"13120", "Pedro Aguirre Cerda":"13121", "Peñalolén":"13122", "Providencia":"13123", "Pudahuel":"13124", "Quilicura":"13125", "Quinta Normal":"13126", "Recoleta":"13127", "Renca":"13128", "San Joaquín":"13129", "San Miguel":"13130", "San Ramón":"13131", "Vitacura":"13132", "Puente Alto":"13201", "Pirque":"13202", "San José de Maipo":"13203", "Colina":"13301", "Lampa":"13302", "Tiltil":"13303", "San Bernardo":"13401", "Buin":"13402","Calera de Tango":"13403", "Paine":"13404", "Melipilla":"13501", "Alhué":"13502", "Curacaví":"13503", "María Pinto":"13504", "San Pedro":"13505", "Talagante":"13601", "El Monte":"13602", "Isla de Maipo":"13603", "Padre Hurtado":"13604", "Peñaflor":"13605"}
        print("región Metropolitana de Santiago:")
        print(metropolitana_de_santiago)    

if opc==3:   #graficos por nombres y códigos de comunas:  

    comuna=str(input("Ingrese el código o nombre de la comuna:\nINGRESO:"))
    if  comuna==  "15101" :
                  
        plt.plot([10717.3,	10872.9,	10985.6,	11139.5,	11235.2,	11340.6,	11431.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("últimas 7 fechas")
        plt.show()
    elif comuna ==  "15102" :
        
        plt.plot([4947.3,	5028.4,	5028.4,	5028.4,	5109.5,	5190.6,	5271.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "15202" :
          plt.plot([9753.1,	9753.1,	9876.5,	9876.5,	10000.0,	10617.3,	10740.7])
          plt.xlabel("últimas 7 fechas ")
          plt.ylabel("tasa de incidencia")
          plt.show()   
    elif comuna =="15201" :
        plt.plot([7117.3,	7395.6,	7514.9,	7514.9,	7594.4,	7634.2,	7674.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="01107" :
        plt.plot([10728.3,	10886.9,	10999.6,	11151.5,	11248.7,	11357.3,	11448.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()    
    elif comuna =="01402":
        plt.plot([10972.4,	11093.9,	11160.1,	11240.9,	11304.7,	11377.8,	11427.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="01403":
        plt.plot([14400.0,	14690.9,	14909.1,	14836.4,	14981.8,	14981.8,	15054.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="01404":
        plt.plot([8907.1,	8907.1,	8907.1,	9096.7,	9096.7,	9096.7,	9096.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="01101":
        plt.plot([14000.0,	14200.0,	14266.7,	14300.0,	14366.7,	14366.7,	14433.3])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="01405":
        plt.plot([12168.0,	12272.7,	12344.3,	12424.4,	12483.5,	12537.6,	12590.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna =="01401":
        plt.plot([15861.0,	16079.2,	16129.6,	16230.3,	16364.6,	16431.7,	16448.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02101":
        plt.plot([12348.4,	12503.6,	12572.6,	12641.6,	12676.1,	12727.8,	12733.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02201":
        plt.plot([12092.3,	12207.5,	12277.3,	12356.7,	12418.3,	12477.4,	12528.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02302":
        plt.plot([8623.4,	8707.5,	8771.6,	8825.9,	8895.6,	8949.4,	8990.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna =="02102":
        plt.plot([8702.0,	8810.7,	8890.6,	8984.1,	9049.8,	9134.9,	9184.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02202":
        plt.plot([9304.4,	9627.2,	9656.6,	9685.9,	9818.0,	9862.0,	9891.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()    
    elif comuna =="02203":
        plt.plot([12493.2,	12608.3,	12669.2,	12682.7,	12709.8,	12723.3,	12743.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02103":
        plt.plot([11149.8,	11149.8,	11149.8,	11149.8,	11149.8,	11846.7,	12195.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02104":
        plt.plot([8462.7,	8635.2,	8779.0,	8961.1,	9076.1,	9239.0,	9526.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="02301":
        plt.plot([8992.0,	9163.8,	9163.8,	9221.1,	9278.4,	9392.9,	9450.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03302":
        plt.plot([6033.5,	6062.8,	6092.1,	6150.7,	6267.8,	6363.0,	6480.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03102" :
        plt.plot([6570.7,	6652.7,	6731.0,	6780.9,	6809.4,	6841.4,	6880.6])
        plt.xlabel("últimas 7 días ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03201":
        plt.plot([8699.5,	8794.3,	8865.9,	8932.2,	9000.9,	9065.5,	9116.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03101":
        plt.plot([4119.4,	4206.7,	4293.9,	4311.4,	4346.3,	4451.0,	4485.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03202":
        plt.plot([6939.2,	7129.6,	7248.0,	7371.6,	7433.3,	7546.6,	7613.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03303":
        plt.plot([6206.3,	6343.1,	6411.4,	6586.1,	6707.7,	6966.0,	7087.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03304":
        plt.plot([7937.5,	8119.2,	8228.1,	8378.3,	8462.1,	8626.9,	8711.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03103":
        plt.plot([7758.7,	7912.0,	8051.3,	8239.3,	8385.6,	8587.5,	8629.3])
        plt.xlabel("últimas 7 días ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="03301":
        plt.plot([7876.6,	8058.8,	8163.0,	8267.2,	8280.2,	8358.3,	8397.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="04103":
        plt.plot([6525.2,	6702.8,	6818.2,	6933.6,	7004.6,	7093.4,	7173.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="04102":
        plt.plot([8706.0,	8873.7,	8943.5,	8985.5,	9041.4,	9104.2,	9278.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="04302":
        plt.plot([7777.7,	7963.7,	8091.7,	8179.4,	8251.3,	8342.5,	8426.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="04102":
        plt.plot([5707.4	,5833.3	,5929.1	,6009.3,	6076.7,	6139.0,	6193.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04201":
        plt.plot([5804.7	,6009.0	,6176.6	,6399.2	,6551.6	,6725.4	,6816.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04104":
        plt.plot([7415.7,	7618.0,	7662.9,	7752.8,	7887.6,	8112.4,	8179.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04101":
        plt.plot([5822.4,	5957.4,	6057.5,	6149.7,	6220.2,	6293.1,	6351.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04103":
        plt.plot([7123.3,	7183.2,	7285.9,	7354.3,	7422.8,	7469.8,	7529.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04103":
        plt.plot([5131.1,	5263.3,	5370.9,	5441.6,	5543.1,	5632.2,	5724.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna =="04103":
        plt.plot([6780.8,	6991.1,	7139.5,	7275.6,	7373.7,	7437.2,	7493.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04103":
        plt.plot([5625.7,	6181.8,	6566.8,	6823.5,	6823.5,	6909.1,	6994.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04304":
        plt.plot([6847.5,	7085.9,	7266.7,	7340.7,	7455.8,	7496.9,	7562.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="04305":
        plt.plot([4620.3,	4711.8,	4780.4,	4826.2,	4940.5,	5054.9,	5192.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna =="04204":
        plt.plot([5372.7,	5499.8,	5599.5,	5685.3,	5743.7,	5819.3,	5888.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna =="04106":
        plt.plot([5164.6,	5460.5,	5662.2,	5823.6,	5978.3,	6153.1,	6254.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna =="05602":
        plt.plot([6517.7,	6642.9,	6728.6,	6853.8,	6932.9,	7012.0,	7064.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05402":
        plt.plot([6339.8,	6489.9,	6615.7,	6727.0,	6823.8,	6954.5,	7094.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05502":
        plt.plot([8354.0,	8557.4,	8689.9,	8846.6,	8986.6,	9081.7,	9124.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05302":
        plt.plot([7038.0,	7226.1,	7377.7	,7480.9,	7541.6,	7596.2,	7656.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05603":
        plt.plot([7315.5,	7698.1,	7974.1,	8206.8,	8309.3,	8400.0,	8498.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05102":
        plt.plot([7240.3,	7408.3,	7494.0,	7555.7,	7610.6,	7682.6,	7740.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05702":
        plt.plot([6507.6,	6764.0,	6856.0,	7020.3,	7184.6,	7427.9,	7513.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05103":
        plt.plot([6792.5,	6897.1,	6990.8,	7062.7,	7108.5,	7171.7,	7245.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05604":
        plt.plot([6572.0,	6865.1,	7079.2,	7254.0,	7327.2,	7428.7,	7513.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05605":
        plt.plot([7609.2,	7881.2,	8257.8,	8501.9,	8885.5,	9115.6,	9213.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05503":
        plt.plot([6612.9,	6691.4,	6796.2,	6853.8,	6879.9,	6995.1,	7052.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05201":
        plt.plot([120.8,120.8,120.8,	108.7,	108.7,	120.8,	108.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05104":
        plt.plot([96.8,	96.8,	96.8,	96.8,	96.8,	96.8,	96.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05504":
        plt.plot([6508.4,	6678.3,	6769.1,	6844.1,	6966.5,	7029.7,	7081.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05401":
        plt.plot([7165.0,	7379.6,	7530.7,	7660.5,	7766.5,	7909.6,	7975.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05802":
        plt.plot([7372.2,	7534.4,	7636.5,	7742.7,	7820.8,	7916.9,	7987.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05703":
        plt.plot([6369.4	,6652.1	,6927.2	,7191.0	,7432.3	,7643.3,	7775.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05301":
        plt.plot([7404.6	,7630.7	,7805.5	,7931.8	,8018.4,	8105.1,	8209.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05506":
        plt.plot([7003.0,	7126.4,	7275.4,	7398.9,	7586.2,	7637.3,	7713.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05803":
        plt.plot([6342.8	,6540.0	,6649.0	,6768.4,	6830.7,	6882.6,	6913.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05704":
        plt.plot([6170.6	,6314.7	,6498.1	,6707.7	,6812.5	,6838.7,	6930.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05403":
        plt.plot([7273.0	,7305.3	,7385.9,	7579.4,	7708.4,	7772.9,	7772.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05404":
        plt.plot([5228.3,	5323.0,	5502.9,	5626.1,	5768.1,	5948.1,	6042.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05105":
        plt.plot([6173.1,	6327.5,	6526.8,	6681.3,	6805.8,	6845.7,	6920.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05705":
        plt.plot([5593.7,	5797.7,	5899.7,	5984.7,	6126.4,	6205.7,	6353.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05501":
        plt.plot([7580.0	,7710.2	,7802.4	,7926.5,	7995.1	,8083.3,	8137.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05801":
        plt.plot([6975.5,	7107.8,	7210.7,	7314.8,	7407.0,	7467.5,	7532.1])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="05107":
        plt.plot([6943.4,	7009.8,	7103.9,	7173.1,	7242.3,	7305.9,	7350.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="05303":
        plt.plot([5691.2,	5975.3,	6161.8,	6312.7,	6419.2,	6525.8,	6614.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05601":
        plt.plot([7472.0,	7683.9,	7817.2,	7986.7,	8147.9,	8268.8,	8355.6])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="05304":
        plt.plot([5701.7,	5880.9,	5968.1,	6195.8,	6292.7,	6399.3,	6525.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="05701":
        plt.plot([6841.2,	7097.5,	7224.5,	7396.9,	7484.4,	7585.0,	7672.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="05706":
        plt.plot([6916.4,	7142.4,	7282.9,	7496.8,	7594.6,	7765.6,	7845.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05606":
        plt.plot([6150.5	,6251.0	,6326.5	,6401.9	,6510.8	,6603.0	,6678.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05101":
        plt.plot([9583.4,	9712.0	,9812.4,	9916.6	,9993.0	,10084.8	,10169.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05804":
        plt.plot([7337.6,	7474.7,	7580.9,	7692.2,	7786.9,	7886.0,	7961.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05109":
        plt.plot([7974.4	,8081.4	,8156.7	,8250.2	,8324.4	,8398.6	,8463.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05405":
        plt.plot([6329.7,	6467.4,	6579.9,	6717.5,	6767.6	,6855.1	,6942.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="05402":
        plt.plot([6489.9,	6615.7,	6727.0,	6823.8,	6954.5,	7094.8,	7162.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06101":
        plt.plot([8780.6	,8886.5	,8980.4	,9044.9	,9109.0	,9165.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06102":
        plt.plot([7271.6	,7427.6	,7541.1	,7590.8	,7619.2	,7668.8	,7732.7])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="6103":
        plt.plot([6716.9	,6755.2	,6895.7	,6959.5	,6959.5	,6972.3	,7074.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06104":
        plt.plot([6706.5,	6762.9,	6791.1,	6833.5,	6885.2,	6913.4,	6922.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06105":
        plt.plot([7524.2	,7630.0	,7731.3	,7845.8	,7894.3	,7907.5,	7991.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06106":
        plt.plot([8059.4,	8303.2,	8448.4,	8527.8,	8607.3,	8694.9,	8716.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06107":
        plt.plot([8673.2,	8789.1,	8863.9,	8976.0,	9091.9	,9177.9,	9267.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06108":
        plt.plot([5973.7,	6117.2,	6214.0,	6275.8,	6340.9,	6404.3,	6456.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="06109":
        plt.plot([7526.7,	7639.6,	7696.1,	7802.0,	7851.4,	7893.8,	7907.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06110":
        plt.plot([6649.2,	6911.4,	7031.5,	7206.3,	7293.7,	7421.2,	7457.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06111":
        plt.plot([9306.6,	9443.4,	9525.4,	9573.3,	9621.2,	9621.2,	9641.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06112":
        plt.plot([7677.9,	7791.6,	7878.5,	8005.6,	8052.4,	8126.0,	8152.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06113":
        plt.plot([8152.1,	8373.9,	8484.8,	8552.3,	8624.6,	8658.3,	8668.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06114":
        plt.plot([5728.9,	5822.6,	5930.7,	6024.4,	6118.0,	6197.3,	6240.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06115":
        plt.plot([8377.0,	8507.3,	8609.3,	8681.5,	8733.3,	8802.4,	8858.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06116":
        plt.plot([7401.8,	7503.9,	7592.8,	7638.9,	7717.9,	7780.4	,7852.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06117":
        plt.plot([7783.9,	7904.5,	7981.5,	8070.4,	8145.5,	8188.9,	8266.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06201":
        plt.plot([5899.8,	5989.3,	6089.9,	6173.8,	6369.5,	6414.3	,6447.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06202":
        plt.plot([5330.8,	5427.1,	5523.4,	5587.7,	5748.2,	5973.0,	6101.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06203":
        plt.plot([7583.1,	7790.1,	7923.1,	7997.0,	8233.6,	8277.9,	8322.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06204":
        plt.plot([6433.4,	6499.0,	6538.3,	6564.5,	6577.6,	6656.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06205":
        plt.plot([6097.9,	6300.7,	6546.9,	6662.8,	6720.7,	6764.2,	6836.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06206":
        plt.plot([6898.7,	7056.2,	7119.2,	7213.7,	7229.5,	7245.2,	7292.5])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="06301":
        plt.plot([8302.2,	8423.0,	8512.0,	8579.4,	8635.3,	8677.3,	8706.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="06302":
        plt.plot([6612.2,	6819.5,	6995.3,	7139.7,	7221.4,	7259.0,	7303.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6303":
        plt.plot([5517.8,	5621.3,	5711.5,	5838.8,	5897.2,	5947.6,	5995.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6304":
        plt.plot([3759.1,	3841.4,	3923.7,	3978.6,	4033.5,	4074.6,	4102.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6305":
        plt.plot([7199.2,	7246.2,	7314.1,	7345.5,	7408.2,	7512.7,	7523.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6306":
        plt.plot([6429.1,	6519.3,	6632.1,	6662.2,	6692.2,	6707.3,	6722.3])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="6307":
        plt.plot([7267.0,	7309.3,	7368.3,	7419.0,	7435.9,	7461.2,	7537.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6308":
        plt.plot([7725.9,	7933.2,	7998.7,	8151.5,	8249.7,	8282.4,	8304.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6309":
        plt.plot([6343.8,	6485.4,	6683.7,	6796.9,	6796.9,	6796.9,	6796.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="6310":
        plt.plot([5840.0,	6003.0,	6080.9,	6149.0,	6200.1,	6260.9,	6307.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="7101":
        plt.plot([8145.8,	8272.1,	8376.0,	8451.2,	8542.4,	8621.9,	8684.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="7102":
        plt.plot([8866.3,	9005.3,	9104.6,	9241.7,	9376.7,	9533.6,	9674.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7103":
        plt.plot([6418.4,	6482.1,	6598.8,	6704.9,	6800.3,	6832.2,	6842.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7104":
        plt.plot([7536.9,	7608.2,	7774.6,	7798.4,	7845.9,	7964.8,	8155.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7105":
        plt.plot([7918.3,	8035.0,	8125.0,	8223.3,	8303.3,	8353.3,	8415.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7106":
        plt.plot([8664.5,	8884.7,	9016.8,	9071.9,	9115.9,	9126.9,	9115.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7107":
        plt.plot([8487.4,	8603.7,	8778.0,	8824.6,	8929.2,	8929.2,	8952.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="7108":
        plt.plot([9150.7,	9171.0,	9238.8,	9252.4,	9279.5,	9435.4,	9557.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7109":
        plt.plot([8822.3,	9059.9,	9224.1,	9364.5,	9461.7,	9563.2,	9625.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7110":
        plt.plot([10382.6	,10613.5	,10814.3	,11025.2	,11165.8	,11416.8	,11527.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7201":
        plt.plot([5162.8,	5271.5,	5400.6,	5495.8,	5622.6,	5745.0,	5815.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7202":
        plt.plot([5176.3,	5369.2,	5497.8,	5551.4,	5658.6,	5680.0	,5690.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7203":
        plt.plot([7031.6,	7192.3,	7451.8,	7587.7,	7909.0,	8020.3,	8168.6])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="7301":
        plt.plot([11477.4	,11591.1	,11687.0	,11747.5	,11812.3	,11842.9,	11874.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7302":
        plt.plot([7219.7,	7258.9,	7356.7,	7434.9,	7523.0,	7620.8,	7718.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7303":
        plt.plot([8542.0,	8613.5,	8627.8,	8728.0,	8799.5,	8956.9,	9042.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7304":
        plt.plot([9397.6,	9520.1,	9622.5,	9712.9,	9789.2,	9911.6,	9939.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="7305":
        plt.plot([11166.4,	11282.0,	11344.2,	11442.0,	11522.0,	11593.2,	11646.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7306":
        plt.plot([11311.1,	11502.8,	11583.2,	11614.1,	11682.1,	11756.3,	11805.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7307":
        plt.plot([7119.0,	7252.6,	7334.7,	7442.6,	7524.8,	7545.3,	7565.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7308":
        plt.plot([9400.3,	9624.0,	9753.6,	9863.9,	9990.3,	10022.7,	10061.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7309":
        plt.plot([8194.5,	8308.6,	8354.3,	8331.4,	8399.9,	8468.4,	8491.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7401":
        plt.plot([8355.3,	8514.6,	8622.5,	8739.2,	8845.1,	8924.2,	9019.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "7402":
        plt.plot([9244.4,	9461.6,	9638.8,	9780.6,	9980.1,	10090.8,	10170.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7403":
        plt.plot([9975.6,	10253.0,	10362.7,	10466.3,	10548.6,	10576.0,	10621.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7404":
        plt.plot([8266.0,	8488.2,	8667.8,	8791.3,	8964.2,	9089.9,	9184.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7405":
        plt.plot([7038.1,	7156.8,	7394.0,	7531.7,	7683.5,	7835.4,	8006.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7406":
        plt.plot([9453.8,	9597.4,	9668.2,	9743.0,	9807.7,	9850.2,	9890.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="7407":
        plt.plot([7086.6,	7212.2,	7315.0,	7429.2,	7480.6,	7600.5,	7669.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="7408":
        plt.plot([8807.3,	9010.4,	9182.3,	9312.5,	9453.1,	9531.2,	9583.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8101":
        plt.plot([9495.9,	9620.2,	9698.4,	9779.0,	9843.3,	9908.4,	9973.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8102":
        plt.plot([11545.0,	11634.0,	11722.3,	11856.6,	11941.6,	12058.4,	12125.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8103":
        plt.plot([9833.3,	9981.4,	10068.0,	10155.7,	10209.5,	10266.5,	10317.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8104":
        plt.plot([7913.2,	8031.4,	8175.0,	8360.8,	8495.9,	8597.2,	8639.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8105":
        plt.plot([9992.0,	10114.1,	10186.6,	10251.5,	10301.1,	10369.8	,10388.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8106":
        plt.plot([12443.7,	12592.3,	12649.2,	12747.5,	12795.6,	12841.5,	12869.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8107":
        plt.plot([10983.7,	11069.9,	11148.1,	11228.3,	11278.5,	 11344.6,	11410.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8108":
        plt.plot([9092.2,	9199.8,	9264.9,	9360.8,	9454.0	,9537.0	,9589.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8109":
        plt.plot([9242.8,	9486.4,	9628.5,	9905.9,	10257.8,	10521.7,	10711.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8110":
        plt.plot([10219.5,	10350.2,	10431.7,	10507.4,	10561.1,	10630.0,	10671.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8111":
        plt.plot([8867.9,	8942.8,	9009.2,	9079.0,	9159.0,	9245.9,	9314.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8112":
        plt.plot([10724.5,	10839.6,	10926.0,	11041.1,	11112.0	,11190.2,	11246.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8201":
        plt.plot([7428.0,	7597.8,	7786.0,	8018.5,	8177.1,	8357.9,	8490.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8202":
        plt.plot([11846.2,	11954.8,	12086.7,	12205.6,	12288.3,	12368.5,	12464.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8203":
        plt.plot([9245.2,	9369.5	,9445.2,	9547.9,	9631.7,	9685.7,	9731.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8204":
        plt.plot([7851.5,	7883.1,	7914.7,	7930.5	,7930.5	,8041.1	,8246.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8205":
        plt.plot([11088.2,	11235.7,	11395.0	,11501.2,	11637.0	,11701.9	,11752.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8206":
        plt.plot([9372.2, 9540.9,	9629.7,	9754.0,	9851.7,	10011.5,	10127.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="8207":
        plt.plot([9665.1,	9846.6,	9991.8,	10345.8	,10518.2	,10663.4	,10772.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8301":
        plt.plot([10627.6,	10797.0	,10913.7,	11010.7	,11088.5,	11164.5,	11201.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8302":
        plt.plot([8012.1	,8128.2,	8197.9	,8267.5	,8383.7,	8430.1,	8523.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8303":
        plt.plot([9035.0,	9171.7,	9275.8,	9340.9,	9393.0	,9428.8,	9458.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8304":
        plt.plot([9730.7	,9977.8	,10086.7	,10208.2	,10292.0	,10388.3	,10480.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8305":
        plt.plot([11671.7,	11803.7	,11910.1	,12042.1,	12135.6,	12245.1,	12299.9])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="8306":
        plt.plot([9411.7,	9644.3,	9801.7,	9934.2,	10098.8	,10209.7,	10295.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8307":
        plt.plot([12522.8	,12618.7	,12628.2	,12705.0	,12791.3	,12935.1	,13031.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8308":
        plt.plot([8782.0,	8901.7,	8949.5,	8973.4,	8997.4,	9069.2,	9117.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8309":
        plt.plot([9788.7,	9838.5,	9918.3,	9928.2,	9978.1,	10037.9,	10237.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8310":
        plt.plot([8003.3	,8031.0	,8114.1,	8141.8	,8224.9,	8363.3	,8501.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8311":
        plt.plot([9875.3,	9916.4,	9957.5,	10012.3	,10046.6	,10053.5	,10067.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8312":
        plt.plot([6603.1,	6668.9,	6767.5,	6866.2,	6912.2,	6964.8,	7063.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8313":
        plt.plot([8268.6,	8485.5,	8661.7,	8846.9,	8923.7,	9032.2,	9113.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8314":
        plt.plot([13948.3	,14066.4	,14258.3	,14346.9	,14524.0	,14583.0,	14833.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8401":
        plt.plot([8987.3,	9080.5,	9154.0,	9226.0,	9285.4,	9347.3,	9390.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8402":
        plt.plot([8802.6,	8886.6,	8948.6,	9063.6,	9099.0,	9156.5,	9209.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8403":
        plt.plot([4284.4,	4379.1,	4492.9,	4530.8,	4549.8,	4625.6,	4644.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8404":
        plt.plot([6233.3,	6292.7,	6334.2,	6369.8,	6399.5,	6417.3,	6464.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8405" :
        plt.plot([8063.4,	8211.5,	8334.8,	8398.2,	8486.3,	8567.4,	8623.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8406":
        plt.plot([7612.3,	7695.0,	7745.3,	7798.5,	7863.5,	7896.1,	7937.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="8407":
        plt.plot([5415.9	,5505.1	,5586.2	,5651.0	,5691.6	,5691.6	,5764.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8408":
        plt.plot([7536.0,	7794.6,	7776.1,	7794.6,	7887.0,	7997.8,	8108.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8409":
        plt.plot([9259.1	,9336.9	,9457.9,	9587.6,	9622.2,	9648.1,	9725.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8410":
        plt.plot([7431.4,	7616.6,	7744.0,	7894.4,	8056.5,	8230.1,	8311.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8411":
        plt.plot([5841.8,	5934.3,	6001.7,	6085.9,	6153.2,	6262.6,	6313.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8412":
        plt.plot([5668.0,	5931.2,	6012.1,	6093.1,	6234.8,	6356.3	,6417.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="8413":
        plt.plot([7099.1	,7242.9	,7333.4	,7397.3	,7493.2	,7546.5,	7663.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8414":
        plt.plot([6602.7,	6676.5,	6709.3,	6791.3,	6881.6	,6963.6	,6988.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8415":
        plt.plot([7075.5	,7107.5	,7123.5	,7187.4	,7251.2	,7267.2	,7267.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8416":
        plt.plot([9288.6,	9464.6,	9610.3	,9750.8	,9848.5	,9949.9	,10003.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8417":
        plt.plot([6811.3,	6940.3,	7069.2,	7176.6,	7198.1,	7219.6	,7262.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8418":
        plt.plot([6863.6,	6995.9,	7032.0,	7098.2,	7176.4,	7188.4,	7236.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8419":
        plt.plot([9185.0,	9250.7,	9423.3,	9521.9	,9546.5	,9571.1	,9595.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8420":
        plt.plot([8128.5	,8286.5	,8321.6	,8374.3	,8409.4	,8462.1,	8462.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="8421":
        plt.plot([6350.8,	6458.4,	6555.2,	6646.6,	6673.5,	6678.9	,6727.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9101":
        plt.plot([9738.5	,9830.3	,9901.9	,9980.5	,10052.5	,10114.2	,10168.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9102":
        plt.plot([9499.3,	9632.7,	9793.6,	9966.3,	10056.5,	10123.2	,10174.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="9103":
        plt.plot([8524.0,	8679.0,	8872.9	,9055.7	,9111.0	,9127.7	,9133.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9104":
        plt.plot([9907.7,	10215.3	,10535.8,	10663.9,	10881.8,	11022.8	,11253.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9105":
        plt.plot([9203.8,	9404.2,	9537.8,	9655.7,	9820.8,	9868.0,	9911.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9106":
        plt.plot([16836.9,	17058.5	,17296.0,	17470.1,	17731.3,	18024.2,	18372.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9107":
        plt.plot([8370.7,	8483.0,	8628.2,	8766.8,	8931.9,	8964.9,	9077.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9108":
        plt.plot([10185.0,	10297.9,	10376.5,	10486.9,	10646.4,	10756.9,	10872.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="9109":
        plt.plot([7983.3,	8108.7,	8274.4,	8456.3,	8569.5	,8690.7,	8787.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9110":
        plt.plot([7613.7,	7757.4,	7917.0,	7933.0,	8044.7,	8044.7,	8044.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9111":
        plt.plot([8896.6,	8994.3,	9065.3,	9154.2,	9195.6,	9314.0,	9352.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9112":
        plt.plot([10675.9,	10790.4	,10920.7	,11019.4,	11085.1,	11159.4,	11213.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9113":
        plt.plot([13941.6	,14024.6	,14176.9	,14301.5	,14412.3	,14481.5	,14550.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9114":
        plt.plot([9376.9,	9583.8	,9714.1	,9890.4	,10005.4	,10108.8	,10174.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9115":
        plt.plot([8780.5,	9206.9,	9401.7,	9572.9,	9754.2, 9969.1	,10137.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9116":
        plt.plot([11357.8	,11568.8	,11779.9	,11967.5	,12108.2	,12256.7	,12319.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9117":
        plt.plot([7063.2,	7303.9,	7506.7,	7855.1,	8000.8,	8317.5,	8374.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9118":
        plt.plot([10263.6	,10512.2	,10800.6	,10989.6	,11158.6	,11317.8	,11447.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9119":
        plt.plot([10365.3,	10514.9,10612.4,	10761.9,	10833.4,	10914.6,	11015.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9120":
        plt.plot([8241.5,	8492.0,	8730.5,	8967.4,	9231.3,	9424.2,	9612.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9121":
        plt.plot([8443.4,	8597.4,	8751.3,	8864.8,	8921.5,	9034.9,	9099.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9201":
        plt.plot([10062.8,	10134.1,	10184.1	,10241.2,	10342.9	,10394.6,	10439.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9202":
        plt.plot([11913.0	,12161.5	,12280.1	,12524.9	,12666.4	,12807.9	,12926.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9203":
        plt.plot([6403.3,	6568.4,	6634.4,	6766.4,	6931.5,	7025.0,	7096.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9204":
        plt.plot([14211.4,	14471.5,	14684.3,	14767.1	,15003.5,	15074.5,	15180.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9205":
        plt.plot([6706.5,	6896.6,	7213.3,	7349.1,	7584.4,	7774.5,	7955.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9206":
        plt.plot([10695.8,	10935.2,	11241.2,	11467.3,	11693.5,	11813.2,	11946.3])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="9207":
        plt.plot([10636.8,	10726.4,	10766.2,	10806.0,	10865.7,	10885.6,	10965.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9208":
        plt.plot([7819.2	,7893.0	,7901.2	,7942.2	,7958.6	,7975.1,	7983.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9209":
        plt.plot([15295.9,	15369.7	,15535.9,	15655.9	,15757.4,	15969.7	,15997.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9210":
        plt.plot([9231.6	,9366.3	,9485.3	,9568.2	,9666.6	,9780.5,	9837.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="9211":
        plt.plot([9352.4,	9428.5,	9479.2,	9546.9,	9611.8,	9671.0,	9702.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14101":
        plt.plot([11014.6	,11185.5	,11306.5	,11442.3	,11553.7,	11654.4	,11725.1])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="14102":
        plt.plot([12337.1	,12428.9,	12502.3	,12612.4,	12685.9,	12777.7,	12869.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14103":
        plt.plot([11930.7,	12196.9,	12446.2,	12627.5,	12791.8	,13001.4	,13154.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14104 ":
        plt.plot([15162.3,	15664.3	,15986.0	,16166.3	,16565.9	,16736.5	,16882.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14105":
        plt.plot([13790.8,	13980.2	,14196.8	,14535.1,	14778.7,	14887.0	,15062.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14106":
        plt.plot([13238.7,	13363.4,	13436.6,	13608.6,13673.1,	13789.2	,13862.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14107":
        plt.plot([10698.1,	11015.5,	11179.0, 11380.9,	11539.6,	11731.9	,11861.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14108":
        plt.plot([11439.0,	11908.5,	12191.9,	12614.3,	12964.4,	13453.4,	13847.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14201":
        plt.plot([11869.6,	12021.3,	12130.1,	12286.9,	12405.8,	12491.8,	12572.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14202":
        plt.plot([14389.6,	14835.2,	15143.2,	15411.8,	15837.8,	16230.9	,16683.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14203":
        plt.plot([13039.3,	13700.0,	14030.3,	14584.1,	14972.8,	15575.2,	15993.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="14204":
        plt.plot([9837.5,	9995.4,	10050.1,	10195.9,	10302.2,	10441.9,	10545.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="10202":
        plt.plot([3466.1,	3764.9,	3904.4,	3984.1,	4043.8,	4163.3,	4163.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10102":
        plt.plot([11009.8,	11122.2,	11209.6,	11259.6,	11284.6,	11403.2,	11453.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna =="10201":
        plt.plot([10209.7,	10234.6,	10234.6,	10259.6,	10284.6,	10284.6,	10284.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10401":
        plt.plot([9862.3,	10083.6,	10157.4,	10354.2,	10378.8,	10403.3,	10501.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10203":
        plt.plot([11334.5,	11493.8,	11546.9,	11659.7,	11812.3,	11898.6,	11965.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()        
    elif comuna =="10103":
        plt.plot([10943.4,	11006.6,	11030.3,	11125.2,	11220.0,	11283.2,	11346.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10204":
        plt.plot([12540.2,	12649.0,	12757.8,	12876.4,	12955.5,	13034.7,	13123.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10205":
        plt.plot([2815.4,	2815.4,	2851.0,	2851.0,	2886.7,	2886.7,	2922.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10104":
        plt.plot([12105.0,	12136.5,	12157.5,	12189.0,	12189.0,	12199.5,	12231.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10105":
        plt.plot([12362.4,	12464.4,	12534.2,	12657.8,	12759.8,	12797.4,	12899.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10402":
        plt.plot([11533.9,	11573.2,	11635.0,	11719.1,	11780.9,	11853.8,	11932.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10403":
        plt.plot([15234.3,	15314.9,	15375.3,	15408.9,	15462.6,	15523.0,	15570.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10106":
        plt.plot([10630.9,	10760.6,	10835.6,	10925.6,	11036.3,	11128.5,	11209.8])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                     
    elif comuna =="10108":
        plt.plot([7225.0,	7225.0,	7225.0,	7279.7,	7334.4,	7334.4,	7334.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10301":
        plt.plot([10701.3,	10816.0,	10883.2,	10943.7,	11024.6,	11088.4,	11137.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10404":
        plt.plot([9551.8,	9617.1,	9725.8,	9845.5,	9899.9,	9954.3,	9997.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10101":
        plt.plot([8833.8,	8990.1,	9088.9,	9193.7,	9302.8,	9374.7,	9415.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10302":
        plt.plot([11663.9,	11854.3,	11997.1,	12282.8,	12687.5,	13282.6,	13544.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10109":
        plt.plot([11565.5,	11660.3,	11760.0,	11797.9,	11864.3,	11935.5,	11992.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10206":
        plt.plot([10087.4,	10180.7,	10291.0,	10452.2,	10604.9,	10698.2,	10876.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10303":
        plt.plot([7883.8,	8100.3,	8244.6,	8352.9,	8551.3,	8641.5,	8785.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10304":
        plt.plot([8352.4,	8441.1,	8557.1,	8604.9,	8642.4,	8710.6,	8778.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10207":
        plt.plot([10395.1,	10554.5,	10577.3,	10622.8,	10668.3,	10702.5,	10736.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10208":
        plt.plot([10339.8,	10400.1,	10448.3,	10460.4,	10508.6	,10568.8,	10592.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10209":
        plt.plot([11649.7,	11901.9,	12105.1,	12252.2,	12609.5,	12798.6,	13001.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="10210":
        plt.plot([16441.9,	16559.8,	16651.4,	16795.4,	16900.1,	17096.5,	17175.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="10305":
        plt.plot([10755.2,	10859.5,	10935.3,	11067.9,	11191.1,	11314.3,	11418.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()                    
    elif comuna =="10306":
        plt.plot([10642.1,	10764.9,	10845.6,	10925.4,	11016.0,	11092.8,	11155.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="10307":
        plt.plot([6143.5,	6527.5,	6659.5,	6827.5,	6967.4,	7071.4,	7151.4])
        plt.xlabel("últimas 7 ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="11201":
        plt.plot([7420.4,	7674.3,	7713.3,	7791.4,	7889.1,	7947.7,	8006.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="11401":
        plt.plot([9059.7,	9265.6,	9437.2,	9574.5,	9711.7,	9780.4,	9952.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="11202" :
        plt.plot([5590.2,	5997.3,	6160.1,	6377.2,	6540.0,	6675.7,	6675.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="11301":
        plt.plot([8601.5,	8815.6,	9014.9,	9134.1,	9250.1,	9364.5,	9452.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="11101" :
        plt.plot([11569.7,	11569.7,	11757.3,	11757.3,	11757.3,	11819.9,	12007.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="11203" :
        plt.plot([4347.8,	4673.9,	4673.9,	4565.2,	4565.2,	4565.2,	4565.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="11102" :
        plt.plot([1512.9,	1512.9,	1512.9,	1512.9,	1512.9,	1512.9,	1512.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="11302" :
        plt.plot([6150.4,	6595.0,	7299.0,	7447.2,	7595.4,	7632.5,	7669.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()   
    elif comuna =="11402" :
        plt.plot([3321.7,	3496.5,	3671.3,	4720.3,	4720.3,	4720.3,	4720.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="11303" :
        plt.plot([7776.5,	8041.2,	8223.9,	8358.1,	8477.4,	8579.9,	8664.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="12202":
        plt.plot([43065.7,	43065.7,	43065.7,	43065.7,	43065.7,	43065.7,	43065.7])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna =="12201":
        plt.plot([18406.5,	18406.5,	18406.5,	18356.0,	18406.5,	18406.5,	18406.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12102":
        plt.plot([9090.9,	9090.9,	9090.9,	9090.9,	9090.9,	9090.9,	9090.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12401":
        plt.plot([22710.5,	22861.8,	22975.4,	23084.7,	23118.3	,23164.6,	23236.1])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12301":
        plt.plot([16004.4,	16195.5,	16468.7,	16564.2,	16755.4,	16878.3,	16905.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12302":
        plt.plot([8789.6,	8789.6,	8789.6,	8789.6,	8789.6,	8789.6,	8789.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12101":
        plt.plot([17160.4,	17268.8,	17336.5,	17394.9,	17425.2,	17473.8,	17506.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12103" :
        plt.plot([6161.1,	6161.1,	6161.1,	6161.1,	6161.1,	7582.9,	8056.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="12104":
        plt.plot([10425.8,	10425.8,	10425.8,	10425.8,	10425.8,	10425.8,	10719.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna =="12303":
        plt.plot([14893.6,	14893.6,	14893.6,	14893.6,	14893.6,	14893.6,	14893.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="12402":
        plt.plot([1860.9,	1860.9,	1860.9,	1860.9,	1860.9,	1860.9,	1860.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13502": 
        plt.plot([9736.7,	9871.7,	9939.2,	10033.8,	10087.8	,10141.8,	10276.8])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13402":
        plt.plot([8500.5,	8748.6,	8892.7,	9061.4,	9153.5,	9252.0,	9318.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13403":
        plt.plot([7330.4,	7460.1,	7551.3,	7649.4,	7793.2,	7908.9,	8017.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13102":
        plt.plot([8536.8,	8686.3,	8801.0,	8906.7,	9000.0,	9075.3,	9122.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13103":
        plt.plot([11567.1	,11776.9	,11907.5	,12043.7	,12130.7	,12211.4,	12264.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13301":
        plt.plot([7428.8,	7610.6,	7739.3,	7872.3,	7966.0,	8045.3,	8124.1])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13104":
        plt.plot([9651.9	,9812.9	,9901.9	,9996.0	,10046.3	,10113.2	,10159.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13503":
        plt.plot([9022.8	,9305.5	,9440.0	,9574.5	,9651.4	,9769.4	,9827.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13105":
        plt.plot([11225.6,	11425.0,	11558.1,	11697.7,	11794.2,	11897.1,	11971.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13602":
        plt.plot([9099.3,	9234.3,	9344.2,	9446.7,	9504.2,	9566.7,	9649.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13106":
        plt.plot([8052.1,	8188.9,	8288.0,	8396.4,	8460.2,	8518.7,	8561.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13107":
        plt.plot([8010.5,	8158.9,	8275.3,	8382.8,	8445.9,	8523.2,	8571.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13108":
        plt.plot([9526.6,	9646.3,	9734.3,	9814.5,	9872.9,	9922.9,	9965.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="13603":
        plt.plot([9282.8	,9417.2	,9479.5	,9586.5	,9651.2	,9706.0	,9773.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()                    
    elif comuna =="13109":
        plt.plot([9238.9	,9424.1	,9547.6	,9629.2	,9720.8	,9790.5	,9840.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13110":
        plt.plot([9617.0	,9787.7	,9908.0	,10032.5	,10124.7	,10208.4	,10261.3])
        plt.xlabel("últimas 7 ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13111":
        plt.plot([12756.5	,12976.8	,13122.9	,13255.9	,13353.0,	13447.6	,13508.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13112":
        plt.plot([12722.4, 12926.8	,13061.5,	13198.8	,13288.1	,13368.9	,13429.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13113" :
        plt.plot([6343.0,	6479.7,	6561.5,	6657.2,	6732.0,	6817.8,	6871.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13302":
        plt.plot([7510.8,	7703.8,	7807.1,	7907.1,	7978.8,	8023.8,	8066.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="13114" :
        plt.plot([5208.0,	5308.1,	5367.0,	5432.1,	5473.8,	5523.1,	5553.3])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="13115" :
        plt.plot([6961.9,	7120.6,	7199.6,	7289.1,	7351.1,	7412.4	,7459.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13116" :
        plt.plot([9773.3	,9927.3	,10026.5	,10105.4	,10181.5	,10246.0	,10310.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13117" :
        plt.plot([12183.6	,12391.4	,12589.7	,12725.7	,12819.6	,12935.5	,12993.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()   
    elif comuna =="13118" :
        plt.plot([9307.4,	9481.2,	9590.4,	9713.7,	9781.3,	9845.9,	9904.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13119" :
        plt.plot([7319.0,	7467.8,	7564.4,	7670.9,	7738.4,	7810.7,	7863.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="13504":
        plt.plot([9205.4,	9466.7,	9553.8,	9674.4	,9774.9	,9962.5	,10002.7])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna =="13501":
        plt.plot([7953.4,	8099.6,	8179.4	,8271.9	,8341.1	,8418.1	,8486.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13120":
        plt.plot([6154.9	,6270.4	,6341.5	,6409.1	,6457.0	,6512.6,	6540.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13604":
        plt.plot([9535.2	,9784.6	,9949.0	,10100.0	,10237.5	,10298.2	,10380.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13404":
        plt.plot([8037.1,	8206.3,	8319.8,	8449.1	,8544.6,	8629.1,	8698.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13121":
        plt.plot([10772.4	,11034.9	,11164.8	,11325.3	,11428.3	,11549.8,	11622.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13605":
        plt.plot([8043.9,	8247.7,	8364.5,	8478.3,	8592.1,	8683.1,	8747.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13122" :
        plt.plot([10838.5,	11013.6	,11161.6,	11308.6,	11419.5,	11533.1,	11605.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13202":
        plt.plot([9916.9,	10120.6,	10258.6,	10380.2,	10508.3,	10583.9,	10662.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna =="13123":
        plt.plot([5631.1,	5744.6,	5816.2,	5866.3,	5922.7,	5955.7,	5985.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13124":
        plt.plot([10267.1	,10414.8	,10532.9,	10643.2	,10732.8	,10803.9	,10856.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
#
    elif comuna =="13201" :
        plt.plot([10309.7	,10491.3	,10624.3,	10753.7,	10855.2	,10935.8	,10991.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13125":
        plt.plot([8022.2,	8140.7,	8227.5,	8302.5,	8368.5,	8421.9,	8465.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="13126":
        plt.plot([10771.6,	10969.6	,11128.7	,11233.6,	11329.6,	11401.5,	11460.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna =="13127":
        plt.plot([9237.4,	9358.9,	9446.8,	9535.2,	9593.6,	9663.0,	9711.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13128":
        plt.plot([13775.8,	14062.4,	14244.0,	14430.5,	14538.0,	14651.8,	14739.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13401":
        plt.plot([9645.0, 9822.7,	9946.4,	10068.8,	10162.3,	10242.3,	10311.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13129":
        plt.plot([11814.3	,12039.4	,12181.5	,12317.7	,12436.6	,12505.2	,12572.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13203":
        plt.plot([9064.6,	9257.7,	9375.7,	9488.3,	9590.2,	9649.2,	9751.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13130":
        plt.plot([10678.0,	10844.1,	10966.6	,11077.8,	11169.5,	11248.4	,11332.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13505" :
        plt.plot([7646.6,	7730.3,	7772.1,	7847.4,	7872.5,	7964.5,	8064.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="13131":
        plt.plot([11827.5	,11992.8	,12076.1	,12169.7	,12233.3	,12301.5	,12353.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna =="13101":
        plt.plot([7969.2,	8110.0,	8196.0,	8276.5,	8330.4,	8379.9,	8422.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13601":
        plt.plot([5988.7,	6066.9,	6146.3,	6206.2,	6258.7,	6308.8,	6362.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13303":
        plt.plot([7505.7	,7673.3	,7766.4,	7896.8	,7934.1	,7985.3,	8045.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="13132":
        plt.plot([4903.2	,4972.4	,5021.0	,5070.6	,5110.9	,5160.5	,5176.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Alhue": 
        plt.plot([9736.7,	9871.7,	9939.2,	10033.8,	10087.8	,10141.8,	10276.8])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Buin":
        plt.plot([8500.5,	8748.6,	8892.7,	9061.4,	9153.5,	9252.0,	9318.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Calera de Tango":
        plt.plot([7330.4,	7460.1,	7551.3,	7649.4,	7793.2,	7908.9,	8017.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Cerrillos":
        plt.plot([8536.8,	8686.3,	8801.0,	8906.7,	9000.0,	9075.3,	9122.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Cerro Navia":
        plt.plot([11567.1	,11776.9	,11907.5	,12043.7	,12130.7	,12211.4,	12264.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Colina":
        plt.plot([7428.8,	7610.6,	7739.3,	7872.3,	7966.0,	8045.3,	8124.1])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Conchali":
        plt.plot([9651.9	,9812.9	,9901.9	,9996.0	,10046.3	,10113.2	,10159.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Curacavi":
        plt.plot([9022.8	,9305.5	,9440.0	,9574.5	,9651.4	,9769.4	,9827.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="El Bosque":
        plt.plot([11225.6,	11425.0,	11558.1,	11697.7,	11794.2,	11897.1,	11971.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="El Monte":
        plt.plot([9099.3,	9234.3,	9344.2,	9446.7,	9504.2,	9566.7,	9649.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Estacion Central":
        plt.plot([8052.1,	8188.9,	8288.0,	8396.4,	8460.2,	8518.7,	8561.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Huechuraba":
        plt.plot([8010.5,	8158.9,	8275.3,	8382.8,	8445.9,	8523.2,	8571.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Independencia":
        plt.plot([9526.6,	9646.3,	9734.3,	9814.5,	9872.9,	9922.9,	9965.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="Isla de Maipo":
        plt.plot([9282.8	,9417.2	,9479.5	,9586.5	,9651.2	,9706.0	,9773.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()                    
    elif comuna =="La Cisterna":
        plt.plot([9238.9	,9424.1	,9547.6	,9629.2	,9720.8	,9790.5	,9840.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="La Florida":
        plt.plot([9617.0	,9787.7	,9908.0	,10032.5	,10124.7	,10208.4	,10261.3])
        plt.xlabel("últimas 7 ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="La Granja":
        plt.plot([12756.5	,12976.8	,13122.9	,13255.9	,13353.0,	13447.6	,13508.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="La Pintana":
        plt.plot([12722.4, 12926.8	,13061.5,	13198.8	,13288.1	,13368.9	,13429.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="La Reina" :
        plt.plot([6343.0,	6479.7,	6561.5,	6657.2,	6732.0,	6817.8,	6871.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Lampa":
        plt.plot([7510.8,	7703.8,	7807.1,	7907.1,	7978.8,	8023.8,	8066.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="Las Condes" :
        plt.plot([5208.0,	5308.1,	5367.0,	5432.1,	5473.8,	5523.1,	5553.3])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="Lo Barnechea" :
        plt.plot([6961.9,	7120.6,	7199.6,	7289.1,	7351.1,	7412.4	,7459.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Lo Espejo" :
        plt.plot([9773.3	,9927.3	,10026.5	,10105.4	,10181.5	,10246.0	,10310.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Lo Prado" :
        plt.plot([12183.6	,12391.4	,12589.7	,12725.7	,12819.6	,12935.5	,12993.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()   
    elif comuna =="Macul" :
        plt.plot([9307.4,	9481.2,	9590.4,	9713.7,	9781.3,	9845.9,	9904.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Maipu" :
        plt.plot([7319.0,	7467.8,	7564.4,	7670.9,	7738.4,	7810.7,	7863.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="Maria Pinto":
        plt.plot([9205.4,	9466.7,	9553.8,	9674.4	,9774.9	,9962.5	,10002.7])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna =="Melipilla":
        plt.plot([7953.4,	8099.6,	8179.4	,8271.9	,8341.1	,8418.1	,8486.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Ñuñoa":
        plt.plot([6154.9	,6270.4	,6341.5	,6409.1	,6457.0	,6512.6,	6540.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Padre Hurtado":
        plt.plot([9535.2	,9784.6	,9949.0	,10100.0	,10237.5	,10298.2	,10380.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Paine":
        plt.plot([8037.1,	8206.3,	8319.8,	8449.1	,8544.6,	8629.1,	8698.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Pedro Aguirre Cerda":
        plt.plot([10772.4	,11034.9	,11164.8	,11325.3	,11428.3	,11549.8,	11622.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Peñaflor":
        plt.plot([8043.9,	8247.7,	8364.5,	8478.3,	8592.1,	8683.1,	8747.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Penalolen" :
        plt.plot([10838.5,	11013.6	,11161.6,	11308.6,	11419.5,	11533.1,	11605.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Pirque":
        plt.plot([9916.9,	10120.6,	10258.6,	10380.2,	10508.3,	10583.9,	10662.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna =="Providencia":
        plt.plot([5631.1,	5744.6,	5816.2,	5866.3,	5922.7,	5955.7,	5985.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Pudahuel":
        plt.plot([10267.1	,10414.8	,10532.9,	10643.2	,10732.8	,10803.9	,10856.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
#
    elif comuna =="Puente Alto" :
        plt.plot([10309.7	,10491.3	,10624.3,	10753.7,	10855.2	,10935.8	,10991.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="Quilicura":
        plt.plot([8022.2,	8140.7,	8227.5,	8302.5,	8368.5,	8421.9,	8465.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna =="Quinta Normal":
        plt.plot([10771.6,	10969.6	,11128.7	,11233.6,	11329.6,	11401.5,	11460.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna =="Recoleta":
        plt.plot([9237.4,	9358.9,	9446.8,	9535.2,	9593.6,	9663.0,	9711.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Renca":
        plt.plot([13775.8,	14062.4,	14244.0,	14430.5,	14538.0,	14651.8,	14739.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="San Bernardo":
        plt.plot([9645.0, 9822.7,	9946.4,	10068.8,	10162.3,	10242.3,	10311.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="San Joaquin":
        plt.plot([11814.3	,12039.4	,12181.5	,12317.7	,12436.6	,12505.2	,12572.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="San Jose de Maipo":
        plt.plot([9064.6,	9257.7,	9375.7,	9488.3,	9590.2,	9649.2,	9751.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="San Miguel":
        plt.plot([10678.0,	10844.1,	10966.6	,11077.8,	11169.5,	11248.4	,11332.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="San Pedro" :
        plt.plot([7646.6,	7730.3,	7772.1,	7847.4,	7872.5,	7964.5,	8064.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna =="San Ramon":
        plt.plot([11827.5	,11992.8	,12076.1	,12169.7	,12233.3	,12301.5	,12353.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna =="Santiago":
        plt.plot([7969.2,	8110.0,	8196.0,	8276.5,	8330.4,	8379.9,	8422.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Talagante":
        plt.plot([5988.7,	6066.9,	6146.3,	6206.2,	6258.7,	6308.8,	6362.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Tiltil":
        plt.plot([7505.7	,7673.3	,7766.4,	7896.8	,7934.1	,7985.3,	8045.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Vitacura":
        plt.plot([4903.2	,4972.4	,5021.0	,5070.6	,5110.9	,5160.5	,5176.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif  comuna==   "Arica" :
                  
        plt.plot([10717.3,	10872.9,	10985.6,	11139.5,	11235.2,	11340.6,	11431.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("últimas 7 fechas")
        plt.show()
    elif comuna ==   "Camarones" :
        
        plt.plot([4947.3,	5028.4,	5028.4,	5028.4,	5109.5,	5190.6,	5271.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "General Lagos" :
          plt.plot([9753.1,	9753.1,	9876.5,	9876.5,	10000.0,	10617.3,	10740.7])
          plt.xlabel("últimas 7 fechas ")
          plt.ylabel("tasa de incidencia")
          plt.show()   
    elif comuna =="Putre" :
        plt.plot([7117.3,	7395.6,	7514.9,	7514.9,	7594.4,	7634.2,	7674.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Alto Hospicio":
        plt.plot([10728.3,	10886.9,	10999.6,	11151.5,	11248.7,	11357.3,	11448.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()    
    elif comuna == "Camiña":
        plt.plot([10972.4,	11093.9,	11160.1,	11240.9,	11304.7,	11377.8,	11427.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Colchane":
        plt.plot([14400.0,	14690.9,	14909.1,	14836.4,	14981.8,	14981.8,	15054.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Huara":
        plt.plot([8907.1,	8907.1,	8907.1,	9096.7,	9096.7,	9096.7,	9096.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Iquique":
        plt.plot([14000.0,	14200.0,	14266.7,	14300.0,	14366.7,	14366.7,	14433.3])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna == "Pica":
        plt.plot([12168.0,	12272.7,	12344.3,	12424.4,	12483.5,	12537.6,	12590.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna == "Pozo Almonte":
        plt.plot([15861.0,	16079.2,	16129.6,	16230.3,	16364.6,	16431.7,	16448.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Antofagasta":
        plt.plot([12348.4,	12503.6,	12572.6,	12641.6,	12676.1,	12727.8,	12733.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Calama":
        plt.plot([12092.3,	12207.5,	12277.3,	12356.7,	12418.3,	12477.4,	12528.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
        
    elif comuna == "Maria elena":
        plt.plot([8623.4,	8707.5,	8771.6,	8825.9,	8895.6,	8949.4,	8990.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna == "Mejillones":
        plt.plot([8702.0,	8810.7,	8890.6,	8984.1,	9049.8,	9134.9,	9184.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Ollague":
        plt.plot([9304.4,	9627.2,	9656.6,	9685.9,	9818.0,	9862.0,	9891.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()    
    elif comuna == "San Pedro de Atacama":
        plt.plot([12493.2,	12608.3,	12669.2,	12682.7,	12709.8,	12723.3,	12743.6])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Sierra Gorda":
        plt.plot([11149.8,	11149.8,	11149.8,	11149.8,	11149.8,	11846.7,	12195.1])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Taltal":
        plt.plot([8462.7,	8635.2,	8779.0,	8961.1,	9076.1,	9239.0,	9526.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Tocopilla":
        plt.plot([8992.0,	9163.8,	9163.8,	9221.1,	9278.4,	9392.9,	9450.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Alto del Carmen":
        plt.plot([6033.5,	6062.8,	6092.1,	6150.7,	6267.8,	6363.0,	6480.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Caldera":
        plt.plot([6570.7,	6652.7,	6731.0,	6780.9,	6809.4,	6841.4,	6880.6])
        plt.xlabel("últimas 7 días ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Chanaral":
        plt.plot([8699.5,	8794.3,	8865.9,	8932.2,	9000.9,	9065.5,	9116.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Copiapo":
        plt.plot([4119.4,	4206.7,	4293.9,	4311.4,	4346.3,	4451.0,	4485.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Diego de almagro":
        plt.plot([6939.2,	7129.6,	7248.0,	7371.6,	7433.3,	7546.6,	7613.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Freirina":
        plt.plot([6206.3,	6343.1,	6411.4,	6586.1,	6707.7,	6966.0,	7087.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Huasco":
        plt.plot([7937.5,	8119.2,	8228.1,	8378.3,	8462.1,	8626.9,	8711.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Tierra Amarilla":
        plt.plot([7758.7,	7912.0,	8051.3,	8239.3,	8385.6,	8587.5,	8629.3])
        plt.xlabel("últimas 7 días ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Vallenar":
        plt.plot([7876.6,	8058.8,	8163.0,	8267.2,	8280.2,	8358.3,	8397.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Andacollo":
        plt.plot([6525.2,	6702.8,	6818.2,	6933.6,	7004.6,	7093.4,	7173.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Canela":
        plt.plot([8706.0,	8873.7,	8943.5,	8985.5,	9041.4,	9104.2,	9278.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Combarbala":
        plt.plot([7777.7,	7963.7,	8091.7,	8179.4,	8251.3,	8342.5,	8426.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Coquimbo":
        plt.plot([5707.4	,5833.3	,5929.1	,6009.3,	6076.7,	6139.0,	6193.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()


    elif comuna == "Illapel":
        plt.plot([5804.7	,6009.0	,6176.6	,6399.2	,6551.6	,6725.4	,6816.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "La Higuera":
        plt.plot([7415.7,	7618.0,	7662.9,	7752.8,	7887.6,	8112.4,	8179.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "La Serena":
        plt.plot([5822.4,	5957.4,	6057.5,	6149.7,	6220.2,	6293.1,	6351.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Los Vilos":
        plt.plot([7123.3,	7183.2,	7285.9,	7354.3,	7422.8,	7469.8,	7529.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Monte Patria":
        plt.plot([5131.1,	5263.3,	5370.9,	5441.6,	5543.1,	5632.2,	5724.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna == "Ovalle":
        plt.plot([6780.8,	6991.1,	7139.5,	7275.6,	7373.7,	7437.2,	7493.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Paiguano":
        plt.plot([5625.7,	6181.8,	6566.8,	6823.5,	6823.5,	6909.1,	6994.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Punitaqui":
        plt.plot([6847.5,	7085.9,	7266.7,	7340.7,	7455.8,	7496.9,	7562.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Río Hurtado":
        plt.plot([4620.3,	4711.8,	4780.4,	4826.2,	4940.5,	5054.9,	5192.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna == "Salamanca":
        plt.plot([5372.7,	5499.8,	5599.5,	5685.3,	5743.7,	5819.3,	5888.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna == "Vicuña":
        plt.plot([5164.6,	5460.5,	5662.2,	5823.6,	5978.3,	6153.1,	6254.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()    
    elif comuna == "Algarrobo":
        plt.plot([6517.7,	6642.9,	6728.6,	6853.8,	6932.9,	7012.0,	7064.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cabildo":
        plt.plot([6339.8,	6489.9,	6615.7,	6727.0,	6823.8,	6954.5,	7094.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Calera":
        plt.plot([8354.0,	8557.4,	8689.9,	8846.6,	8986.6,	9081.7,	9124.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Calle Larga ":
        plt.plot([7038.0,	7226.1,	7377.7	,7480.9,	7541.6,	7596.2,	7656.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cartagena":
        plt.plot([7315.5,	7698.1,	7974.1,	8206.8,	8309.3,	8400.0,	8498.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Casablanca":
        plt.plot([7240.3,	7408.3,	7494.0,	7555.7,	7610.6,	7682.6,	7740.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Catemu":
        plt.plot([6507.6,	6764.0,	6856.0,	7020.3,	7184.6,	7427.9,	7513.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Concón":
        plt.plot([6792.5,	6897.1,	6990.8,	7062.7,	7108.5,	7171.7,	7245.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "El Quisco":
        plt.plot([6572.0,	6865.1,	7079.2,	7254.0,	7327.2,	7428.7,	7513.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "El Tabo":
        plt.plot([7609.2,	7881.2,	8257.8,	8501.9,	8885.5,	9115.6,	9213.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Hijuelas":
        plt.plot([6612.9,	6691.4,	6796.2,	6853.8,	6879.9,	6995.1,	7052.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Isla de Pascua":
        plt.plot([120.8,120.8,120.8,	108.7,	108.7,	120.8,	108.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Juan Fernández":
        plt.plot([96.8,	96.8,	96.8,	96.8,	96.8,	96.8,	96.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "La Cruz":
        plt.plot([6508.4,	6678.3,	6769.1,	6844.1,	6966.5,	7029.7,	7081.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "La Ligua ":
        plt.plot([7165.0,	7379.6,	7530.7,	7660.5,	7766.5,	7909.6,	7975.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Limache":
        plt.plot([7372.2,	7534.4,	7636.5,	7742.7,	7820.8,	7916.9,	7987.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="Llaillay":
        plt.plot([6369.4	,6652.1	,6927.2	,7191.0	,7432.3	,7643.3,	7775.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="Los Andes":
        plt.plot([7404.6	,7630.7	,7805.5	,7931.8	,8018.4,	8105.1,	8209.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Nogales":
        plt.plot([7003.0,	7126.4,	7275.4,	7398.9,	7586.2,	7637.3,	7713.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Olmué":
        plt.plot([6342.8	,6540.0	,6649.0	,6768.4,	6830.7,	6882.6,	6913.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Panquehue":
        plt.plot([6170.6	,6314.7	,6498.1	,6707.7	,6812.5	,6838.7,	6930.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Papudo":
        plt.plot([7273.0	,7305.3	,7385.9,	7579.4,	7708.4,	7772.9,	7772.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Petorca":
        plt.plot([5228.3,	5323.0,	5502.9,	5626.1,	5768.1,	5948.1,	6042.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Puchuncaví":
        plt.plot([6173.1,	6327.5,	6526.8,	6681.3,	6805.8,	6845.7,	6920.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Putaendo":
        plt.plot([5593.7,	5797.7,	5899.7,	5984.7,	6126.4,	6205.7,	6353.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Quillota":
        plt.plot([7580.0	,7710.2	,7802.4	,7926.5,	7995.1	,8083.3,	8137.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Quilpué":
        plt.plot([6975.5,	7107.8,	7210.7,	7314.8,	7407.0,	7467.5,	7532.1])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()


    elif comuna == "Quintero":
        plt.plot([6943.4,	7009.8,	7103.9,	7173.1,	7242.3,	7305.9,	7350.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()

    elif comuna == "Rinconada":
        plt.plot([5691.2,	5975.3,	6161.8,	6312.7,	6419.2,	6525.8,	6614.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="San Antonio":
        plt.plot([7472.0,	7683.9,	7817.2,	7986.7,	8147.9,	8268.8,	8355.6])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()

    elif comuna == "San Esteban ":
        plt.plot([5701.7,	5880.9,	5968.1,	6195.8,	6292.7,	6399.3,	6525.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()

    elif comuna == "San Felipe":
        plt.plot([6841.2,	7097.5,	7224.5,	7396.9,	7484.4,	7585.0,	7672.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()

    elif comuna == "Santa María":
        plt.plot([6916.4,	7142.4,	7282.9,	7496.8,	7594.6,	7765.6,	7845.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Santo Domingo":
        plt.plot([6150.5	,6251.0	,6326.5	,6401.9	,6510.8	,6603.0	,6678.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Valparaíso":
        plt.plot([9583.4,	9712.0	,9812.4,	9916.6	,9993.0	,10084.8	,10169.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Villa Alemana":
        plt.plot([7337.6,	7474.7,	7580.9,	7692.2,	7786.9,	7886.0,	7961.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Viña del Mar ":
        plt.plot([7974.4	,8081.4	,8156.7	,8250.2	,8324.4	,8398.6	,8463.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Zapallar":
        plt.plot([6329.7,	6467.4,	6579.9,	6717.5,	6767.6	,6855.1	,6942.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()


    elif comuna == "Cabildo":
        plt.plot([6489.9,	6615.7,	6727.0,	6823.8,	6954.5,	7094.8,	7162.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()



    elif comuna == "Rancagua":
        plt.plot([8780.6	,8886.5	,8980.4	,9044.9	,9109.0	,9165.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Codegua":
        plt.plot([7271.6	,7427.6	,7541.1	,7590.8	,7619.2	,7668.8	,7732.7])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Coinco":
        plt.plot([6716.9	,6755.2	,6895.7	,6959.5	,6959.5	,6972.3	,7074.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Coltauco":
        plt.plot([6706.5,	6762.9,	6791.1,	6833.5,	6885.2,	6913.4,	6922.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Doñihue":
        plt.plot([7524.2	,7630.0	,7731.3	,7845.8	,7894.3	,7907.5,	7991.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Graneros":
        plt.plot([8059.4,	8303.2,	8448.4,	8527.8,	8607.3,	8694.9,	8716.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Las Cabras":
        plt.plot([8673.2,	8789.1,	8863.9,	8976.0,	9091.9	,9177.9,	9267.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Machalí":
        plt.plot([5973.7,	6117.2,	6214.0,	6275.8,	6340.9,	6404.3,	6456.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Malloa":
        plt.plot([7526.7,	7639.6,	7696.1,	7802.0,	7851.4,	7893.8,	7907.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Mostazal":
        plt.plot([6649.2,	6911.4,	7031.5,	7206.3,	7293.7,	7421.2,	7457.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Olivar":
        plt.plot([9306.6,	9443.4,	9525.4,	9573.3,	9621.2,	9621.2,	9641.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Peumo":
        plt.plot([7677.9,	7791.6,	7878.5,	8005.6,	8052.4,	8126.0,	8152.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pichidegua":
        plt.plot([8152.1,	8373.9,	8484.8,	8552.3,	8624.6,	8658.3,	8668.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Quinta de Tilcoco":
        plt.plot([5728.9,	5822.6,	5930.7,	6024.4,	6118.0,	6197.3,	6240.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Rengo":
        plt.plot([8377.0,	8507.3,	8609.3,	8681.5,	8733.3,	8802.4,	8858.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Requínoa":
        plt.plot([7401.8,	7503.9,	7592.8,	7638.9,	7717.9,	7780.4	,7852.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Vicente":
        plt.plot([7783.9,	7904.5,	7981.5,	8070.4,	8145.5,	8188.9,	8266.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
########################################################
    elif comuna == "Pichilemu":
        plt.plot([5899.8,	5989.3,	6089.9,	6173.8,	6369.5,	6414.3	,6447.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="La Estrella":
        plt.plot([5330.8,	5427.1,	5523.4,	5587.7,	5748.2,	5973.0,	6101.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Litueche":
        plt.plot([7583.1,	7790.1,	7923.1,	7997.0,	8233.6,	8277.9,	8322.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Marchihue":
        plt.plot([6433.4,	6499.0,	6538.3,	6564.5,	6577.6,	6656.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Navidad":
        plt.plot([6097.9,	6300.7,	6546.9,	6662.8,	6720.7,	6764.2,	6836.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Paredones":
        plt.plot([6898.7,	7056.2,	7119.2,	7213.7,	7229.5,	7245.2,	7292.5])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "San Fernando":
        plt.plot([8302.2,	8423.0,	8512.0,	8579.4,	8635.3,	8677.3,	8706.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Chépica":
        plt.plot([6612.2,	6819.5,	6995.3,	7139.7,	7221.4,	7259.0,	7303.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Chimbarongo":
        plt.plot([5517.8,	5621.3,	5711.5,	5838.8,	5897.2,	5947.6,	5995.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lolol":
        plt.plot([3759.1,	3841.4,	3923.7,	3978.6,	4033.5,	4074.6,	4102.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Nancagua":
        plt.plot([7199.2,	7246.2,	7314.1,	7345.5,	7408.2,	7512.7,	7523.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Palmilla":
        plt.plot([6429.1,	6519.3,	6632.1,	6662.2,	6692.2,	6707.3,	6722.3])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Peralillo":
        plt.plot([7267.0,	7309.3,	7368.3,	7419.0,	7435.9,	7461.2,	7537.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Placilla":
        plt.plot([7725.9,	7933.2,	7998.7,	8151.5,	8249.7,	8282.4,	8304.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pumanque":
        plt.plot([6343.8,	6485.4,	6683.7,	6796.9,	6796.9,	6796.9,	6796.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Santa Cruz":
        plt.plot([5840.0,	6003.0,	6080.9,	6149.0,	6200.1,	6260.9,	6307.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna =="Talca":
        plt.plot([8145.8,	8272.1,	8376.0,	8451.2,	8542.4,	8621.9,	8684.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Constitución":
        plt.plot([8866.3,	9005.3,	9104.6,	9241.7,	9376.7,	9533.6,	9674.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Curepto":
        plt.plot([6418.4,	6482.1,	6598.8,	6704.9,	6800.3,	6832.2,	6842.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Empedrado":
        plt.plot([7536.9,	7608.2,	7774.6,	7798.4,	7845.9,	7964.8,	8155.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Maule":
        plt.plot([7918.3,	8035.0,	8125.0,	8223.3,	8303.3,	8353.3,	8415.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pelarco":
        plt.plot([8664.5,	8884.7,	9016.8,	9071.9,	9115.9,	9126.9,	9115.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pencahue":
        plt.plot([8487.4,	8603.7,	8778.0,	8824.6,	8929.2,	8929.2,	8952.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Río Claro":
        plt.plot([9150.7,	9171.0,	9238.8,	9252.4,	9279.5,	9435.4,	9557.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Clemente ":
        plt.plot([8822.3,	9059.9,	9224.1,	9364.5,	9461.7,	9563.2,	9625.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Rafael ":
        plt.plot([10382.6	,10613.5	,10814.3	,11025.2	,11165.8	,11416.8	,11527.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cauquenes":
        plt.plot([5162.8,	5271.5,	5400.6,	5495.8,	5622.6,	5745.0,	5815.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Chanco":
        plt.plot([5176.3,	5369.2,	5497.8,	5551.4,	5658.6,	5680.0	,5690.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pelluhue":
        plt.plot([7031.6,	7192.3,	7451.8,	7587.7,	7909.0,	8020.3,	8168.6])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Curicó":
        plt.plot([11477.4	,11591.1	,11687.0	,11747.5	,11812.3	,11842.9,	11874.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Hualañé":
        plt.plot([7219.7,	7258.9,	7356.7,	7434.9,	7523.0,	7620.8,	7718.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Licantén":
        plt.plot([8542.0,	8613.5,	8627.8,	8728.0,	8799.5,	8956.9,	9042.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Molina":
        plt.plot([9397.6,	9520.1,	9622.5,	9712.9,	9789.2,	9911.6,	9939.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Rauco":
        plt.plot([11166.4,	11282.0,	11344.2,	11442.0,	11522.0,	11593.2,	11646.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Romeral":
        plt.plot([11311.1,	11502.8,	11583.2,	11614.1,	11682.1,	11756.3,	11805.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Sagrada Familia":
        plt.plot([7119.0,	7252.6,	7334.7,	7442.6,	7524.8,	7545.3,	7565.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Teno":
        plt.plot([9400.3,	9624.0,	9753.6,	9863.9,	9990.3,	10022.7,	10061.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Vichuquén":
        plt.plot([8194.5,	8308.6,	8354.3,	8331.4,	8399.9,	8468.4,	8491.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Linares":
        plt.plot([8355.3,	8514.6,	8622.5,	8739.2,	8845.1,	8924.2,	9019.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna ==  "Colbún":
        plt.plot([9244.4,	9461.6,	9638.8,	9780.6,	9980.1,	10090.8,	10170.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Longaví":
        plt.plot([9975.6,	10253.0,	10362.7,	10466.3,	10548.6,	10576.0,	10621.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Parral":
        plt.plot([8266.0,	8488.2,	8667.8,	8791.3,	8964.2,	9089.9,	9184.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Retiro":
        plt.plot([7038.1,	7156.8,	7394.0,	7531.7,	7683.5,	7835.4,	8006.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Javier":
        plt.plot([9453.8,	9597.4,	9668.2,	9743.0,	9807.7,	9850.2,	9890.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Villa Alegre ":
        plt.plot([7086.6,	7212.2,	7315.0,	7429.2,	7480.6,	7600.5,	7669.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Yerbas Buenas":
        plt.plot([8807.3,	9010.4,	9182.3,	9312.5,	9453.1,	9531.2,	9583.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Concepción":
        plt.plot([9495.9,	9620.2,	9698.4,	9779.0,	9843.3,	9908.4,	9973.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Coronel":
        plt.plot([11545.0,	11634.0,	11722.3,	11856.6,	11941.6,	12058.4,	12125.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Chiguayante":
        plt.plot([9833.3,	9981.4,	10068.0,	10155.7,	10209.5,	10266.5,	10317.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Florida":
        plt.plot([7913.2,	8031.4,	8175.0,	8360.8,	8495.9,	8597.2,	8639.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Hualqui":
        plt.plot([9992.0,	10114.1,	10186.6,	10251.5,	10301.1,	10369.8	,10388.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lota":
        plt.plot([12443.7,	12592.3,	12649.2,	12747.5,	12795.6,	12841.5,	12869.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Penco":
        plt.plot([10983.7,	11069.9,	11148.1,	11228.3,	11278.5,	 11344.6,	11410.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="San Pedro de la Paz":
        plt.plot([9092.2,	9199.8,	9264.9,	9360.8,	9454.0	,9537.0	,9589.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Santa Juana":
        plt.plot([9242.8,	9486.4,	9628.5,	9905.9,	10257.8,	10521.7,	10711.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Talcahuano":
        plt.plot([10219.5,	10350.2,	10431.7,	10507.4,	10561.1,	10630.0,	10671.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Tomé":
        plt.plot([8867.9,	8942.8,	9009.2,	9079.0,	9159.0,	9245.9,	9314.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Hualpén":
        plt.plot([10724.5,	10839.6,	10926.0,	11041.1,	11112.0	,11190.2,	11246.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
#################################################################33
    elif comuna == "Lebu":
        plt.plot([7428.0,	7597.8,	7786.0,	8018.5,	8177.1,	8357.9,	8490.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Arauco":
        plt.plot([11846.2,	11954.8,	12086.7,	12205.6,	12288.3,	12368.5,	12464.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cañete":
        plt.plot([9245.2,	9369.5	,9445.2,	9547.9,	9631.7,	9685.7,	9731.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Contulmo":
        plt.plot([7851.5,	7883.1,	7914.7,	7930.5	,7930.5	,8041.1	,8246.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Curanilahue":
        plt.plot([11088.2,	11235.7,	11395.0	,11501.2,	11637.0	,11701.9	,11752.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Los Álamos":
        plt.plot([9372.2, 9540.9,	9629.7,	9754.0,	9851.7,	10011.5,	10127.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Tirúa":
        plt.plot([9665.1,	9846.6,	9991.8,	10345.8	,10518.2	,10663.4	,10772.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Los Ángeles":
        plt.plot([10627.6,	10797.0	,10913.7,	11010.7	,11088.5,	11164.5,	11201.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Antuco":
        plt.plot([8012.1	,8128.2,	8197.9	,8267.5	,8383.7,	8430.1,	8523.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Cabrero":
        plt.plot([9035.0,	9171.7,	9275.8,	9340.9,	9393.0	,9428.8,	9458.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Laja":
        plt.plot([9730.7	,9977.8	,10086.7	,10208.2	,10292.0	,10388.3	,10480.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Mulchén":
        plt.plot([11671.7,	11803.7	,11910.1	,12042.1,	12135.6,	12245.1,	12299.9])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Nacimiento":
        plt.plot([9411.7,	9644.3,	9801.7,	9934.2,	10098.8	,10209.7,	10295.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Negrete":
        plt.plot([12522.8	,12618.7	,12628.2	,12705.0	,12791.3	,12935.1	,13031.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Quilaco":
        plt.plot([8782.0,	8901.7,	8949.5,	8973.4,	8997.4,	9069.2,	9117.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Quilleco":
        plt.plot([9788.7,	9838.5,	9918.3,	9928.2,	9978.1,	10037.9,	10237.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Rosendo":
        plt.plot([8003.3	,8031.0	,8114.1,	8141.8	,8224.9,	8363.3	,8501.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Santa Bárbara":
        plt.plot([9875.3,	9916.4,	9957.5,	10012.3	,10046.6	,10053.5	,10067.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Tucapel":
        plt.plot([6603.1,	6668.9,	6767.5,	6866.2,	6912.2,	6964.8,	7063.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Yumbel":
        plt.plot([8268.6,	8485.5,	8661.7,	8846.9,	8923.7,	9032.2,	9113.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Alto Biobío":
        plt.plot([13948.3	,14066.4	,14258.3	,14346.9	,14524.0	,14583.0,	14833.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
#################################################################33
    elif comuna == "Chillán":
        plt.plot([8987.3,	9080.5,	9154.0,	9226.0,	9285.4,	9347.3,	9390.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Bulnes":
        plt.plot([8802.6,	8886.6,	8948.6,	9063.6,	9099.0,	9156.5,	9209.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cobquecura":
        plt.plot([4284.4,	4379.1,	4492.9,	4530.8,	4549.8,	4625.6,	4644.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Coelemu":
        plt.plot([6233.3,	6292.7,	6334.2,	6369.8,	6399.5,	6417.3,	6464.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Coihueco":
        plt.plot([8063.4,	8211.5,	8334.8,	8398.2,	8486.3,	8567.4,	8623.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Chillán Viejo":
        plt.plot([7612.3,	7695.0,	7745.3,	7798.5,	7863.5,	7896.1,	7937.4])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="El Carmen ":
        plt.plot([5415.9	,5505.1	,5586.2	,5651.0	,5691.6	,5691.6	,5764.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Ninhue":
        plt.plot([7536.0,	7794.6,	7776.1,	7794.6,	7887.0,	7997.8,	8108.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Ñiquén":
        plt.plot([9259.1	,9336.9	,9457.9,	9587.6,	9622.2,	9648.1,	9725.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pemuco":
        plt.plot([7431.4,	7616.6,	7744.0,	7894.4,	8056.5,	8230.1,	8311.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pinto":
        plt.plot([5841.8,	5934.3,	6001.7,	6085.9,	6153.2,	6262.6,	6313.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Portezuelo":
        plt.plot([5668.0,	5931.2,	6012.1,	6093.1,	6234.8,	6356.3	,6417.0])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Quillón":
        plt.plot([7099.1	,7242.9	,7333.4	,7397.3	,7493.2	,7546.5,	7663.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Quirihue":
        plt.plot([6602.7,	6676.5,	6709.3,	6791.3,	6881.6	,6963.6	,6988.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Ránquil":
        plt.plot([7075.5	,7107.5	,7123.5	,7187.4	,7251.2	,7267.2	,7267.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Carlos":
        plt.plot([9288.6,	9464.6,	9610.3	,9750.8	,9848.5	,9949.9	,10003.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Fabián":
        plt.plot([6811.3,	6940.3,	7069.2,	7176.6,	7198.1,	7219.6	,7262.6])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "San Ignacio":
        plt.plot([6863.6,	6995.9,	7032.0,	7098.2,	7176.4,	7188.4,	7236.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "San Nicolás":
        plt.plot([9185.0,	9250.7,	9423.3,	9521.9	,9546.5	,9571.1	,9595.8])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Treguaco":
        plt.plot([8128.5	,8286.5	,8321.6	,8374.3	,8409.4	,8462.1,	8462.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Yungay":
        plt.plot([6350.8,	6458.4,	6555.2,	6646.6,	6673.5,	6678.9	,6727.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Temuco":
        plt.plot([9738.5	,9830.3	,9901.9	,9980.5	,10052.5	,10114.2	,10168.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Carahue":
        plt.plot([9499.3,	9632.7,	9793.6,	9966.3,	10056.5,	10123.2	,10174.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Cunco":
        plt.plot([8524.0,	8679.0,	8872.9	,9055.7	,9111.0	,9127.7	,9133.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Curarrehue":
        plt.plot([9907.7,	10215.3	,10535.8,	10663.9,	10881.8,	11022.8	,11253.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Freire":
        plt.plot([9203.8,	9404.2,	9537.8,	9655.7,	9820.8,	9868.0,	9911.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Galvarino":
        plt.plot([16836.9,	17058.5	,17296.0,	17470.1,	17731.3,	18024.2,	18372.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Gorbea":
        plt.plot([8370.7,	8483.0,	8628.2,	8766.8,	8931.9,	8964.9,	9077.1])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lautaro":
        plt.plot([10185.0,	10297.9,	10376.5,	10486.9,	10646.4,	10756.9,	10872.2])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna =="Loncoche":
        plt.plot([7983.3,	8108.7,	8274.4,	8456.3,	8569.5	,8690.7,	8787.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Melipeuco":
        plt.plot([7613.7,	7757.4,	7917.0,	7933.0,	8044.7,	8044.7,	8044.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Nueva Imperial":
        plt.plot([8896.6,	8994.3,	9065.3,	9154.2,	9195.6,	9314.0,	9352.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Padre las Casas":
        plt.plot([10675.9,	10790.4	,10920.7	,11019.4,	11085.1,	11159.4,	11213.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Perquenco":
        plt.plot([13941.6	,14024.6	,14176.9	,14301.5	,14412.3	,14481.5	,14550.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Pitrufquén":
        plt.plot([9376.9,	9583.8	,9714.1	,9890.4	,10005.4	,10108.8	,10174.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Pucón":
        plt.plot([8780.5,	9206.9,	9401.7,	9572.9,	9754.2, 9969.1	,10137.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Saavedra":
        plt.plot([11357.8	,11568.8	,11779.9	,11967.5	,12108.2	,12256.7	,12319.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Teodoro Schmid":
        plt.plot([7063.2,	7303.9,	7506.7,	7855.1,	8000.8,	8317.5,	8374.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Toltén":
        plt.plot([10263.6	,10512.2	,10800.6	,10989.6	,11158.6	,11317.8	,11447.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Vilcún":
        plt.plot([10365.3,	10514.9,10612.4,	10761.9,	10833.4,	10914.6,	11015.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Villarrica":
        plt.plot([8241.5,	8492.0,	8730.5,	8967.4,	9231.3,	9424.2,	9612.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Cholchol":
        plt.plot([8443.4,	8597.4,	8751.3,	8864.8,	8921.5,	9034.9,	9099.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()


    elif comuna == "Angol":
        plt.plot([10062.8,	10134.1,	10184.1	,10241.2,	10342.9	,10394.6,	10439.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Collipulli":
        plt.plot([11913.0	,12161.5	,12280.1	,12524.9	,12666.4	,12807.9	,12926.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Curacautín":
        plt.plot([6403.3,	6568.4,	6634.4,	6766.4,	6931.5,	7025.0,	7096.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Ercilla":
        plt.plot([14211.4,	14471.5,	14684.3,	14767.1	,15003.5,	15074.5,	15180.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lonquimay":
        plt.plot([6706.5,	6896.6,	7213.3,	7349.1,	7584.4,	7774.5,	7955.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Los Sauces":
        plt.plot([10695.8,	10935.2,	11241.2,	11467.3,	11693.5,	11813.2,	11946.3])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Lumaco":
        plt.plot([10636.8,	10726.4,	10766.2,	10806.0,	10865.7,	10885.6,	10965.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Purén":
        plt.plot([7819.2	,7893.0	,7901.2	,7942.2	,7958.6	,7975.1,	7983.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Renaico":
        plt.plot([15295.9,	15369.7	,15535.9,	15655.9	,15757.4,	15969.7	,15997.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Traiguén":
        plt.plot([9231.6	,9366.3	,9485.3	,9568.2	,9666.6	,9780.5,	9837.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Victoria":
        plt.plot([9352.4,	9428.5,	9479.2,	9546.9,	9611.8,	9671.0,	9702.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Valdivia":
        plt.plot([11014.6	,11185.5	,11306.5	,11442.3	,11553.7,	11654.4	,11725.1])
        plt.xlabel("últimas 7 días de incidencia")
        plt.show()
    elif comuna == "Corral":
        plt.plot([12337.1	,12428.9,	12502.3	,12612.4,	12685.9,	12777.7,	12869.5])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lanco":
        plt.plot([11930.7,	12196.9,	12446.2,	12627.5,	12791.8	,13001.4	,13154.3])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Los Lagos":
        plt.plot([15162.3,	15664.3	,15986.0	,16166.3	,16565.9	,16736.5	,16882.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Máfil":
        plt.plot([13790.8,	13980.2	,14196.8	,14535.1,	14778.7,	14887.0	,15062.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna =="Mariquina":
        plt.plot([13238.7,	13363.4,	13436.6,	13608.6,13673.1,	13789.2	,13862.4])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Paillaco":
        plt.plot([10698.1,	11015.5,	11179.0, 11380.9,	11539.6,	11731.9	,11861.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Panguipulli":
        plt.plot([11439.0,	11908.5,	12191.9,	12614.3,	12964.4,	13453.4,	13847.9])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "La Unión":
        plt.plot([11869.6,	12021.3,	12130.1,	12286.9,	12405.8,	12491.8,	12572.7])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Futrono":
        plt.plot([14389.6,	14835.2,	15143.2,	15411.8,	15837.8,	16230.9	,16683.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Lago Ranco":
        plt.plot([13039.3,	13700.0,	14030.3,	14584.1,	14972.8,	15575.2,	15993.0])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()
    elif comuna == "Río Bueno":
        plt.plot([9837.5,	9995.4,	10050.1,	10195.9,	10302.2,	10441.9,	10545.2])
        plt.xlabel("últimas 7 fechas de incidencia")
        plt.show()

    elif comuna == "Ancud":
        plt.plot([3466.1,	3764.9,	3904.4,	3984.1,	4043.8,	4163.3,	4163.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Calbuco":
        plt.plot([11009.8,	11122.2,	11209.6,	11259.6,	11284.6,	11403.2,	11453.2])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()       
    elif comuna == "Castro":
        plt.plot([10209.7,	10234.6,	10234.6,	10259.6,	10284.6,	10284.6,	10284.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Chaiten":
        plt.plot([9862.3,	10083.6,	10157.4,	10354.2,	10378.8,	10403.3,	10501.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Chonchi":
        plt.plot([11334.5,	11493.8,	11546.9,	11659.7,	11812.3,	11898.6,	11965.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()        
    elif comuna == "Cochamo":
        plt.plot([10943.4,	11006.6,	11030.3,	11125.2,	11220.0,	11283.2,	11346.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Curaco de Velez":
        plt.plot([12540.2,	12649.0,	12757.8,	12876.4,	12955.5,	13034.7,	13123.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Dalcahue":
        plt.plot([2815.4,	2815.4,	2851.0,	2851.0,	2886.7,	2886.7,	2922.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Fresia":
        plt.plot([12105.0,	12136.5,	12157.5,	12189.0,	12189.0,	12199.5,	12231.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Frutillar":
        plt.plot([12362.4,	12464.4,	12534.2,	12657.8,	12759.8,	12797.4,	12899.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Futaleufu":
        plt.plot([11533.9,	11573.2,	11635.0,	11719.1,	11780.9,	11853.8,	11932.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Hualaihue":
        plt.plot([15234.3,	15314.9,	15375.3,	15408.9,	15462.6,	15523.0,	15570.0])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Los Muermos":
        plt.plot([10630.9,	10760.6,	10835.6,	10925.6,	11036.3,	11128.5,	11209.8])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                     
    elif comuna =="Maullin":
        plt.plot([7225.0,	7225.0,	7225.0,	7279.7,	7334.4,	7334.4,	7334.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Osorno":
        plt.plot([10701.3,	10816.0,	10883.2,	10943.7,	11024.6,	11088.4,	11137.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Palena":
        plt.plot([9551.8,	9617.1,	9725.8,	9845.5,	9899.9,	9954.3,	9997.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Puerto Montt":
        plt.plot([8833.8,	8990.1,	9088.9,	9193.7,	9302.8,	9374.7,	9415.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Puerto Octay":
        plt.plot([11663.9,	11854.3,	11997.1,	12282.8,	12687.5,	13282.6,	13544.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Puerto Varas":
        plt.plot([11565.5,	11660.3,	11760.0,	11797.9,	11864.3,	11935.5,	11992.4])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Puqueldon":
        plt.plot([10087.4,	10180.7,	10291.0,	10452.2,	10604.9,	10698.2,	10876.4])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Purranque":
        plt.plot([7883.8,	8100.3,	8244.6,	8352.9,	8551.3,	8641.5,	8785.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Puyehue":
        plt.plot([8352.4,	8441.1,	8557.1,	8604.9,	8642.4,	8710.6,	8778.9])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Queilen":
        plt.plot([10395.1,	10554.5,	10577.3,	10622.8,	10668.3,	10702.5,	10736.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Quellon":
        plt.plot([10339.8,	10400.1,	10448.3,	10460.4,	10508.6	,10568.8,	10592.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Quemchi":
        plt.plot([11649.7,	11901.9,	12105.1,	12252.2,	12609.5,	12798.6,	13001.8])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Quinchao":
        plt.plot([16441.9,	16559.8,	16651.4,	16795.4,	16900.1,	17096.5,	17175.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna == "Río Negro":
        plt.plot([10755.2,	10859.5,	10935.3,	11067.9,	11191.1,	11314.3,	11418.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()                    
    elif comuna =="San Juan de la Costa":
        plt.plot([10642.1,	10764.9,	10845.6,	10925.4,	11016.0,	11092.8,	11155.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna ==  "San Pablo":
        plt.plot([6143.5,	6527.5,	6659.5,	6827.5,	6967.4,	7071.4,	7151.4])
        plt.xlabel("últimas 7 ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Aysen":
        plt.plot([7420.4,	7674.3,	7713.3,	7791.4,	7889.1,	7947.7,	8006.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Chile Chico":
        plt.plot([9059.7,	9265.6,	9437.2,	9574.5,	9711.7,	9780.4,	9952.0])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Cisnes":
        plt.plot([5590.2,	5997.3,	6160.1,	6377.2,	6540.0,	6675.7,	6675.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna =="Cochrane":
        plt.plot([8601.5,	8815.6,	9014.9,	9134.1,	9250.1,	9364.5,	9452.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna == "Coyhaique":
        plt.plot([11569.7,	11569.7,	11757.3,	11757.3,	11757.3,	11819.9,	12007.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna == "Guaitecas":
        plt.plot([4347.8,	4673.9,	4673.9,	4565.2,	4565.2,	4565.2,	4565.2])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Lago Verde":
        plt.plot([1512.9,	1512.9,	1512.9,	1512.9,	1512.9,	1512.9,	1512.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Ohiggins":
        plt.plot([6150.4,	6595.0,	7299.0,	7447.2,	7595.4,	7632.5,	7669.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()   
    elif comuna == "Río Ibanez":
        plt.plot([3321.7,	3496.5,	3671.3,	4720.3,	4720.3,	4720.3,	4720.3])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "Tortel":
        plt.plot([7776.5,	8041.2,	8223.9,	8358.1,	8477.4,	8579.9,	8664.7])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()  
    elif comuna == "Antartica":
        plt.plot([43065.7,	43065.7,	43065.7,	43065.7,	43065.7,	43065.7,	43065.7])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()                                                            
    elif comuna == "Cabo de Hornos":
        plt.plot([18406.5,	18406.5,	18406.5,	18356.0,	18406.5,	18406.5,	18406.5])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Laguna Blanca":
        plt.plot([9090.9,	9090.9,	9090.9,	9090.9,	9090.9,	9090.9,	9090.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Natales":
        plt.plot([22710.5,	22861.8,	22975.4,	23084.7,	23118.3	,23164.6,	23236.1])
        plt.xlabel("últimas 7 fechas")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Porvenir":
        plt.plot([16004.4,	16195.5,	16468.7,	16564.2,	16755.4,	16878.3,	16905.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Primavera":
        plt.plot([8789.6,	8789.6,	8789.6,	8789.6,	8789.6,	8789.6,	8789.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Punta Arenas":
        plt.plot([17160.4,	17268.8,	17336.5,	17394.9,	17425.2,	17473.8,	17506.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Río Verde":
        plt.plot([6161.1,	6161.1,	6161.1,	6161.1,	6161.1,	7582.9,	8056.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show() 
    elif comuna == "San Gregorio":
        plt.plot([10425.8,	10425.8,	10425.8,	10425.8,	10425.8,	10425.8,	10719.5])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()               
    elif comuna == "Timaukel":
        plt.plot([14893.6,	14893.6,	14893.6,	14893.6,	14893.6,	14893.6,	14893.6])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()
    elif comuna == "Torres del Paine":
        plt.plot([1860.9,	1860.9,	1860.9,	1860.9,	1860.9,	1860.9,	1860.9])
        plt.xlabel("últimas 7 fechas ")
        plt.ylabel("tasa de incidencia")
        plt.show()

elif opc==4:  #graficos por regiones ingresando el nombre o código de la región. opción 4 del menú principal:
    region=str(input("Ingrese el código o nombre de la región:\nINGRESO: "))
    
    if region=="15" :
            plt.plot([10728.3,	10886.9,	10999.6,	11151.5,	11248.7,	11357.3,	11448.2])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="01":
            plt.plot([12092.3,12207.5,12277.3,12356.7,12318.3,12477.4,12528.1])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="02":
            plt.plot([8699.5,8794.3,8865.9,8932.2,9000.9,9065.5,9118.5])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="03":
            plt.plot([7709.7,7887.9,7998.2,8131.3,8210.1,8355.0,8439.9])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="04":
            plt.plot([5879.8,6032.4,6147.9,6247.4,6329.5,6404.6,6466.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show() 
    elif region=="05":
            plt.plot([7661.4,7815.9,7929.7,8047.6,8139.8,8230.8,8305.5])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()       
    elif region=="13":
            plt.plot([9202.5,9365.4,9476.5,9583.3,9664.1,9736.0,9792.0])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="06":
            plt.plot([7628.0,7769.9,7869.0,7953.8,8020.7,8078.3,8127.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="07":
            plt.plot([8828.6,8974.5,9088.2,9180.9,9278.2,9357.7,9422.1])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="16":
            plt.plot([8173.0,8283.2,8366.7,8448.2,8513.5,8573.9,8624.2])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()   
    elif region=="08":
            plt.plot([10111.3,10241.2,10334.4,10437.1,10516,10596.8,10657.8])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="09":
            plt.plot([9723.4,9864.3,9986.2,10104.3,10215.4,10310.2,10388.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="14":
            plt.plot([11666.6,11910.0,12066.7,12258.7,12428.9,12604.9,12743.4])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="10":
            plt.plot([10642.1,10764.9,10845.6,10925.4,11016.0,11092.8,11155.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="11":
            plt.plot([7776.5,8041.2,8223.9,8358.1,8477.4,8579.9,8664.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="12":
            plt.plot([17747.6,17860.9,17942.2,18005.0,18042.0,18094.1,18133.3])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()        
    elif region=="Arica y Parinacota" :
            plt.plot([10728.3,	10886.9,	10999.6,	11151.5,	11248.7,	11357.3,	11448.2])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Tarapacá":
            plt.plot([12092.3,12207.5,12277.3,12356.7,12318.3,12477.4,12528.1])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Antofagasta":
            plt.plot([8699.5,8794.3,8865.9,8932.2,9000.9,9065.5,9118.5])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Atacama":
            plt.plot([7709.7,7887.9,7998.2,8131.3,8210.1,8355.0,8439.9])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Coquimbo":
            plt.plot([5879.8,6032.4,6147.9,6247.4,6329.5,6404.6,6466.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show() 
    elif region=="Valparaíso":
            plt.plot([7661.4,7815.9,7929.7,8047.6,8139.8,8230.8,8305.5])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()       
    elif region=="Metropolitana":
            plt.plot([9202.5,9365.4,9476.5,9583.3,9664.1,9736.0,9792.0])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Región del Libertador Gral. Bernardo Ohiggins":
            plt.plot([7628.0,7769.9,7869.0,7953.8,8020.7,8078.3,8127.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Maule":
            plt.plot([8828.6,8974.5,9088.2,9180.9,9278.2,9357.7,9422.1])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Ñuble":
            plt.plot([8173.0,8283.2,8366.7,8448.2,8513.5,8573.9,8624.2])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()   
    elif region=="Biobío":
            plt.plot([10111.3,10241.2,10334.4,10437.1,10516,10596.8,10657.8])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="La Araucanía":
            plt.plot([9723.4,9864.3,9986.2,10104.3,10215.4,10310.2,10388.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Los Ríos":
            plt.plot([11666.6,11910.0,12066.7,12258.7,12428.9,12604.9,12743.4])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Los Lagos":
            plt.plot([10642.1,10764.9,10845.6,10925.4,11016.0,11092.8,11155.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Región Aisén del Gral.Carlos Ibáñez del Campo":
            plt.plot([7776.5,8041.2,8223.9,8358.1,8477.4,8579.9,8664.7])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
    elif region=="Región de Magallanes":
            plt.plot([17747.6,17860.9,17942.2,18005.0,18042.0,18094.1,18133.3])
            plt.xlabel("últimas 7 fechas ")
            plt.ylabel("tasa de incidencia")
            plt.show()
