import folium
map = folium.Map(location =[12.91,77.6],zoom_start = 6 ,tiles="Mapbox Bright")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[12.353819, 93.748103], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("map.html")
