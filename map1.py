import folium
map = folium.Map(location=[51,-4], zoom_start=7, tiles='Mapbox Bright')

# adding markers
map.add_child(folium.Marker([50.9,-3.9], popup="Hello, I'm a marker", icon=folium.Icon(color='green')))



# use feature group in adding markers
fg = folium.FeatureGroup(name="PJ Map")
fg.add_child(folium.Marker([50.8,-3.8], popup="Hello, I'm a marker in a feature group #1", icon=folium.Icon(color='green')))
fg.add_child(folium.Marker([50.7,-4.1], popup="Hello, I'm a marker in a feature group #2", icon=folium.Icon(color='green')))
map.add_child(fg)

for coordinates in [[50,-4],[50,-5]]:
    folium.Marker(location=coordinates, popup="Hello, I'm a marker in a feature group #1", icon=folium.Icon(color='green')).add_to(fg)


map.save('MapForListMarkers.html')
