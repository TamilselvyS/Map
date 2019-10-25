import folium
#location- co-ordinates(latitude and longitude of initial view)
map = folium.Map(location=[11.943346, 79.808207], zoom_start=7)

#create html map file
map.save("Map.html")    