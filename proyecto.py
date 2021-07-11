import matplotlib.pyplot as plt

print("\nMENÚ DE CÓDIGO DE REGIONES:\n")
print("----------------------------------------------  -------------\nNOMBRE REGIÓN                                   CÓDIGO REGIÓN\nArica y Parinacota                                   15\nTarapacá                                             01\nAntofagasta                                          02\nAtacama                                              03\nCoquimbo                                             04\nValparaíso                                           05\nRegión del Libertador Gral.Bernardo O’Higgins        06\nRegión del Maule                                     07\nRegión del Biobío                                    08\nRegión de la Araucanía                               09\nRegión de los Ríos                                   14\nRegión de los Lagos                                  10\nRegión Aisén del Gral. Carlos Ibáñez del Campo       11\nRegión de Magallanes y de la Antártica Chilena       12\nRegión Metropolitana de Santiago                     13\n----------------------------------------------  -------------\n")
print("===================================================================================================================================")
print("menú de opciones:")
print("-presione 1 para mostrar códigos de  comuna filtrada por región")
print("-presione 2 para ingresar comuna por código o nombre y desplegar gráfica de la tasa de incidencia  de las ultimas 7 fechas")
print("-presione 3 para ingresar una region por código o nombre y desplegar una grafica  de la tasa de incidencia de los últimos 7 fechas")
print("-presione 4 par  desplegar un grafico a elección con la región con mayor y menor densidad de tasa de insidencia respectivamente")
print("-presione 5 para metrica de comparación")
print("===================================================================================================================================")
opc=input(">")
opc=int(opc)

#mostrar comunas filtradas por región:
if opc==1 :
 
 codigo=str(input("escriba código de región para filtrar comunas y sus códigos:"))

 if codigo =="15"  :
     
     
     arica={"Arica":"15101","Camarones":"15102",
            "Putre":"15201","General Lagos":"15202"}
     print("región de arica:")           
     print(arica)

 elif codigo =="01" :
     
    tarapaca={"Iquique":"01101","Alto Hospicio":"01107","Pozo Almonte": "01401",
              "Camiña":"01402","Colchane":"01403","Huara":"01404", "Pica":"01405",}

    print("región de Tarapacá:")
    print(tarapaca)

 elif codigo =="02":
    antofagasta={"Antofagasta":"02101","Mejillones":"02102","Sierra Gorda":"02103",
                 "Taltal":"02104", "Calama":"02201", "Ollagüe":"02202",
                 "San Pedro de Atacama":"02203", "Tocopilla":"02301", "María Elena":"02302"}
    print("región de Antofagasta:")
    print(antofagasta)

 elif codigo =="03":
    atacama={"Copiapó":"03101",  "Caldera":"03102", "Tierra Amarilla":"03103", "Chañaral":"03201",
            "Diego de Almagro":"03202", "Vallenar":"03301", "Alto del Carmen":"03302", "Freirina":"03303",
            "Huasco":"03304", }

    print("región de Atacama:")
    print(atacama)

 elif codigo == "04":
    coquimbo={"La Serena":"04101", "Coquimbo":"04102", "Andacollo":"04103", "La Higuera":"04104",
            "Paiguano":"04105", "Vicuña":"04106", "Illapel":"04201", "Canela":"04202", "Los Vilos":"04203",
            "Salamanca":"04204", "Ovalle":"04301", "Combarbalá":"04302", "Monte Patria":"04303",
            "Punitaqui":"04304", "Río Hurtado":"04305"}
    
    print("región de Coquimbo:")
    print(coquimbo)

 elif codigo =="05":
    valparaiso={"Valparaíso":"05101", "Casablanca":"05102", "Concón":"05103", "Juan Fernández":"05104",
                 "Puchuncaví":"05105", "Quintero":"05107", "Viña del Mar":"05109", "Isla de Pascua":"05201",
                 "Los Andes":"05301", "Calle Larga":"05302","Rinconada":"05303", "San Esteban":"05304",
                 "La Ligua":"05401", "Cabildo":"05402", "Papudo":"05403", "Petorca":"05404", "Zapallar":"05405", 
                 "Quillota":"05501","Calera":"05502", "Hijuelas":"05503", "La Cruz":"05504", "Nogales":"05506",
                 "San Antonio":"05601", "Algarrobo":"05602", "Cartagena"  :"05603", "El Quisco":  "05604",
                 "El Tabo"  :"05605", "Santo Domingo":  "05606", "San Felipe":  "05701", "Catemu":  "05702",
                 "Llaillay":  "05703", "Panquehue":  "05704","Putaendo":  "05705","Santa María":  "05706",
                 "Quilpué":  "05801", "Limache":  "05802","Olmué":  "05803", "Villa Alemana":"05804"}
   
    print("región de Valparaíso:")
    print(valparaiso)

 elif codigo=="06":
    libertador_gral_bernardo_ohiggins={"Rancagua":"06101", "Codegua":"06102", "Coinco":"06103", "Coltauco":"06104",
    "Doñihue":"06105", "Graneros":"06106", "Las Cabras":"06107", "Machalí":"06108", "Malloa":"06109", "Mostazal":"06110",
    "Olivar":"06111", "Peumo":"06112", "Pichidegua":"06113","Quinta de Tilcoco":"06114", "Rengo":"06115",
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

 
 elif codigo =="13":
    metropolitana_de_santiago={"Santiago":"13101", "Cerrillos":"13102", "Cerro Navia":"13103", "Conchalí":"13104", "El Bosque":"13105", "Estación Central":"13106", "Huechuraba":"13107", "Independencia":"13108", "La Cisterna":"13109", "La Florida":"13110", "La Granja":"13111", "La Pintana":"13112", "La Reina":"13113", "Las Condes":"13114", "Lo Barnechea":"13115", "Lo Espejo":"13116", "Lo Prado":"13117", "Macul":"13118", "Maipú":"13119", "Ñuñoa":"13120", "Pedro Aguirre Cerda":"13121", "Peñalolén":"13122", "Providencia":"13123", "Pudahuel":"13124", "Quilicura":"13125", "Quinta Normal":"13126", "Recoleta":"13127", "Renca":"13128", "San Joaquín":"13129", "San Miguel":"13130", "San Ramón":"13131", "Vitacura":"13132", "Puente Alto":"13201", "Pirque":"13202", "San José de Maipo":"13203", "Colina":"13301", "Lampa":"13302", "Tiltil":"13303", "San Bernardo":"13401", "Buin":"13402","Calera de Tango":"13403", "Paine":"13404", "Melipilla":"13501", "Alhué":"13502", "Curacaví":"13503", "María Pinto":"13504", "San Pedro":"13505", "Talagante":"13601", "El Monte":"13602", "Isla de Maipo":"13603", "Padre Hurtado":"13604", "Peñaflor":"13605"}
    print("región Metropolitana de Santiago:")
    print(metropolitana_de_santiago)
 
            


