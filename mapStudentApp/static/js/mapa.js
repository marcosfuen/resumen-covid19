   var map = L.map( 'map', {
        center: [21.3808308, -77.9169388],
        /*center: [21.8, -79.5],*/
        minZoom: 2,
        zoom: 9
    });

     /*habilitar este codigo para cargar los mapas de internet*/
     
     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(map);

    var camaguey = L.layerGroup().addTo(map);
    
    /* fin habilitar este codigo para cargar los mapas de internet*/
   
    var estiloPopup = {'maxWidth': '300'}
 
	var iconoBase = L.Icon.extend({
		options: {
			iconSize:     [24, 39],
			iconAnchor:   [16, 87],
			popupAnchor:  [-3, -76]
		}
	});
 
	var iconoVerde = new iconoBase({iconUrl: '{% static 'images/marker-icon-green.png' %}'}),
        iconoRojo = new iconoBase({iconUrl: '{% static 'images/marker-icon-red.png' %}'}),
        iconoRNegro = new iconoBase({iconUrl: '{% static 'images/marker-icon-black.png' %}'}),
        iconoAzul = new iconoBase({iconUrl: '{% static 'images/marker-icon.png' %}'});
        iconoAmarillo = new iconoBase({iconUrl: '{% static 'images/marker-icon-yellow.png' %}'});
     
    {% for name, lastName, address__latitude, address__longitude in coordenadas %}
        la = "{{address__latitude}}".replace(' ', '.').replace(',', '.');
        lo = "{{address__longitude}}".replace(' ', '.').replace(',', '.');
        {% if address__latitude != None or address__longitude != None %}
        L.marker([la,lo], {icon: iconoAmarillo}).bindPopup("<h1>Cumplen con las medidas</h1><p>Ahorita no hay estan, save.</p>",estiloPopup).addTo(map);
       {% endif %}
    {% endfor %}
   
    
	L.marker([21.3808308,-77.9169388], {icon: iconoRojo}).bindPopup("<h1>Primer Infecctado</h2><p>Trabajador del hotel en cuanto se percato de los primeros sintomas corrio para el medico.</p>",estiloPopup).addTo(map);
    L.marker([21.27145920527429,-78.04412841796876], {icon: iconoRojo}).bindPopup("<h1>Segundo Infectado</h1><p>Este no le hizo caso a nadie y aqui esta el resultado.</p>.",estiloPopup).addTo(map);
    L.marker([21.035800796222002, -77.6788330078125], { icon: iconoRojo }).bindPopup("<h1>Segundo Infectado</h1><p>Este no le hizo caso a nadie y aqui esta el resultado.</p>.", estiloPopup).addTo(map);
    L.marker([20.88960751040438,-77.94525146484376], {icon: iconoVerde}).bindPopup("<h1>Primer Recuperado</h1><p>Se demuestra que los medicamentos cubanos los 24 que utilizan dan resultados alentadores.</p>",estiloPopup).addTo(map);
    L.marker([21.48374090716327,-78.45336914062501], {icon: iconoRojo}).bindPopup("<h1>Batey en cuarentena</h1><p>Aqui todos estan en cuarentena y tiene que pasar 14 dias sin ver el sol.</p>",estiloPopup).addTo(map);
    L.marker([21.34054846908118,-77.50305175781251], {icon: iconoAzul}).bindPopup("<h1>Cumplen con las medidas</h1><p>Ahorita no hay estan, save.</p>",estiloPopup).addTo(map);
    L.marker([21.0947505331402,-78.36547851562501], {icon: iconoAzul}).bindPopup("<h1>Cumplen con las medidas</h1><p>Ahorita no hay estan, save.</p>",estiloPopup).addTo(map);
    L.marker([21.1946553,-77.676086], {icon: iconoRNegro}).bindPopup("<h1>Primera muerte</h1><p>Se lamenta la primera muerte de la provincia.</p>",estiloPopup).addTo(map);
    L.marker([21.759499730719817,-77.98919677734376], {icon: iconoVerde}).bindPopup("<h1>Primer Recuperado</h1><p>Se demuestra que los medicamentos cubanos los 24 que utilizan dan resultados alentadores.</p>",estiloPopup).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [21.759499730719817, -77.98919677734376], [21.3808308, -77.9169388]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [20.88960751040438, -77.94525146484376]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [21.48374090716327, -78.45336914062501]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [21.34054846908118, -77.50305175781251]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [21.0947505331402, -78.36547851562501]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.3808308, -77.9169388], [21.1946553, -77.676086]], { color: 'orange', weight: 5 }).addTo(map);
    L.polyline([[21.1946553, -77.676086], [21.035800796222002, -77.6788330078125]], { color: 'orange', weight: 5 }).addTo(map);
    
    var popup = L.popup();

    function onMapClick(e) {
    popup
        .setLatLng(e.latlng) // Sets the geographical point where the popup will open.
        .setContent("Has hecho click en la coordenada:<br> " +  e.latlng.lat.toString() + "," +  e.latlng.lng.toString()) // Sets the HTML content of the popup.
        .openOn(map); // Adds the popup to the map and closes the previous one. 
    }
    

    map.on('click', onMapClick);
    function getColor(d) {
        return d == "Camagüey" ? '#800026' :
               d == "Florida"  ? '#BD0026' :
               d == "Carlos Manuel de Céspedes"  ? '#E31A1C' :
               d == "Minas"  ? '#FC4E2A' :
               d == "Guáimaro"   ? '#FD8D3C' :
               d == "Nuevitas"   ? '#FEB24C' :
               d == "Esmeralda"   ? '#FFFFFF' :
               d == "Sibanicú"   ? '#FFFF00' :
               d == "Sierra de Cubitas"   ? '#0000FF' :
               d == "Jimaguayú"   ? '#B2FFFF' :
               d == "Santa Cruz del Sur"   ? '#8C4966' :
               d == "Najasa"   ? '#FF6890' :
               d == "Vertientes"   ? '#0B4C5F' :
                          '#F3E2A9';
    }
    function colorPuntos(d) { 
        return d == "" ? '#FF0000' : 
        d == "" ? '#00FF00' : 
        d == "" ? '#0000FF' : 
        d == "" ? '#FF00FF' :
        d == "" ? '#FFFF00' :
            '#F392A9'; 
    };
    function estiloMapaCuba (feature) {
        return{
            radius: 7,
            fillColor: getColor(feature.properties.municipality), 
            color: 'white', 
            weight: 1,
            opacity : 1,
            fillOpacity : 0.8
        };
    };
    function estiloSelect() {
        var miSelect = document.getElementById("mapaMunicipios").value;
		var muni = L.geoJSON(municipios, {
							pointToLayer: function (feature, latlng) {
									return L.circleMarker(latlng, MarkerOptions);
								},
							filter: function(feature, layer) {								
								 if(miSelect != "TODOS")		
									return (feature.properties.municipality == miSelect );
                                else
                                    if(feature.properties.province == "Camagüey")
                                        return (feature.properties.municipality);
							},	
							style:style,
							onEachFeature: onEachFeature	
                    });
                    
        /*map.clearLayers;*/
        map.addLayer(muni);
        
    };	
    function style(feature) {
        return {
            fillColor: getColor(feature.properties.municipality),
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7
        };
    }
    function highlightFeature(e) {
        var layer = e.target;
        console.log(layer.feature.properties.municipality)
        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });
        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
    }
    function resetHighlight(e) {
        geojson.resetStyle(e.target);
    }
    function onEachFeature(feature, layer) {
        
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
        });
        if (feature.properties.province == "Camagüey") {
            layer.bindTooltip(
                feature.properties.municipality,
                {
                    permanent:true,
                    direction:'center',
                    className: 'countryLabel'
                }
        );
        if (feature.properties.municipality == "Camagüey" && feature.properties.municipality) {
            var popupContentCmg = '<img src="{% static 'images/camaguey.png' %}"/>' + "<h2>Datos Camagüey</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectados: " + {{ cantidadInfectadosCmg }} + "<p>";
            layer.bindPopup(popupContentCmg);
        };
        if (feature.properties.municipality == "Guáimaro" && feature.properties.municipality) {
            var popupContentGua = '<img src="{% static 'images/guaimaro.png' %}"/>' + "<h2>Datos Guáimaro</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosGua }} + "<p>";
            layer.bindPopup(popupContentGua);
        };
        if (feature.properties.municipality == "Florida" && feature.properties.municipality) {
            var popupContentFlor = '<img src="{% static 'images/florida.png' %}"/>' + "<h2>Datos Florida</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosFlo }} + "<p>";
            layer.bindPopup(popupContentFlor);
        };
        if (feature.properties.municipality == "Carlos Manuel de Céspedes" && feature.properties.municipality) {
            var popupContentCar = '<img src="{% static 'images/cespedes.png' %}"/>' + "<h2>Datos Céspedes</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosCmc }} + "<p>";
            layer.bindPopup(popupContentCar);
        };
        if (feature.properties.municipality == "Minas" && feature.properties.municipality) {
            var popupContentMin = '<img src="{% static 'images/minas.png' %}"/>' + "<h2>Datos Minas</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosMin }} + "<p>";
            layer.bindPopup(popupContentMin);
        };
        if (feature.properties.municipality == "Nuevitas" && feature.properties.municipality) {
            var popupContentNuev = '<img src="{% static 'images/nuevitas.png' %}"/>' + "<h2>Datos Nuevitas</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosNue }} + "<p>";
            layer.bindPopup(popupContentNuev);
        };
        if (feature.properties.municipality == "Esmeralda" && feature.properties.municipality) {
            var popupContentEsm = '<img src="{% static 'images/esmeralda.png' %}"/>' + "<h2>Datos Esmeralda</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosEsm }} + "<p>";
            layer.bindPopup(popupContentEsm);
        };
        if (feature.properties.municipality == "Sibanicú" && feature.properties.municipality) {
            var popupContentSib = '<img src="{% static 'images/sibanicu.png' %}"/>' + "<h2>Datos Sibanicú</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosSib }} + "<p>";
            layer.bindPopup(popupContentSib);
        };
        if (feature.properties.municipality == "Sierra de Cubitas" && feature.properties.municipality) {
            var popupContentSierr = '<img src="{% static 'images/SierraCubitas.png' %}"/>' + "<h2>Datos Cubitas</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosSeC }} + "<p>";
            layer.bindPopup(popupContentSierr);
        };
        if (feature.properties.municipality == "Jimaguayú" && feature.properties.municipality) {
            var popupContentJim = '<img src="{% static 'images/jimaguayu.png' %}"/>' + "<h2>Datos Jimaguayú</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosJma }} + "<p>";
            layer.bindPopup(popupContentJim);
        };
        if (feature.properties.municipality == "Santa Cruz del Sur" && feature.properties.municipality) {
            var popupContentSan = '<img src="{% static 'images/sanCruz.png' %}"/>' + "<h2>Datos Santa Cruz</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosScs }} + "<p>";
            layer.bindPopup(popupContentSan);
        };
        if (feature.properties.municipality == "Najasa" && feature.properties.municipality) {
            var popupContentNaj = '<img src="{% static 'images/najasa.png' %}"/>' + "<h2>Datos Najasa</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosNaj }} + "<p>";
            layer.bindPopup(popupContentNaj);
        };
        if (feature.properties.municipality == "Vertientes" && feature.properties.municipality) {
            var popupContentVert = '<img src="{% static 'images/vertientes.png' %}"/>' + "<h2>Datos Vertientes</h2>" + "<p>Municipio: " + feature.properties.municipality + "<p>" + "<p>Cantidad de Infectado: " + {{ cantidadInfectadosVer }} + "<p>";
            layer.bindPopup(popupContentVert);
        };

        }
        
    }
    var feature;
    function elegirDireccion(lat1, lng1, lat2, lng2, tipo_osm) {
            var loc1 = new L.LatLng(lat1, lng1);
            var loc2 = new L.LatLng(lat2, lng2);
            var bounds = new L.LatLngBounds(loc1, loc2);

            if (feature) {
                map.removeLayer(feature);
            }
            if (tipo_osm == "node") {
                feature = L.circle(loc1, 25, { color: 'green', fill: false }).addTo(map);
                map.fitBounds(bounds);
                map.setZoom(18);
            } else {
                var loc3 = new L.LatLng(lat1, lng2);
                var loc4 = new L.LatLng(lat2, lng1);

                feature = L.polyline([loc1, loc4, loc2, loc3, loc1], { color: 'red' }).addTo(map);
                map.fitBounds(bounds);
            }
    }
    function direccion_buscador() {
            var entrada = document.getElementById("direccion");

            $.getJSON('http://nominatim.openstreetmap.org/search?format=json&limit=5&q=' + entrada.value, function (data) {
                var items = [];

                $.each(data, function (key, val) {
                    bb = val.boundingbox;
                    items.push("<ul><a href='#' onclick='elegirDireccion(" + bb[0] + ", " + bb[2] + ", " + bb[1] + ", " + bb[3] + ", \"" + val.tipo_osm + "\");return false;'>" + val.display_name + '</a></ul>');
                });

                $('#resultado').empty();
                if (items.length != 0) {
                    $('<p>', { html: "Resultados de la b&uacute;queda:" }).appendTo('#resultado');
                    $('<ul/>', {
                        'class': 'my-new-list',
                        html: items.join('')
                    }).appendTo('#resultado');
                } else {
                    $('<p>', { html: "Ningun resultado encontrado." }).appendTo('#resultado');
                }
            });
        }
    /*
    geojson = L.geoJson(municipios, {
        style: estiloMapaCuba,
        onEachFeature: estiloSelect,
    }).addTo(map);
    */
    /*comentar este codigo cuanado se cargen los mapas de internet*/
    /*
    geojson = L.geoJson(provincias, {
        style: estiloMapaCuba,
        onEachFeature: estiloSelect,
    }).addTo(map);
    /*fin comentar este codigo cuanado se cargen los mapas de internet*/