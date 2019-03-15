import folium
import pandas

data = pandas.read_csv('Volcanoes.txt')     # load CSV into data frame
lat = list(data['LAT'])                     # make a Python list of latitudes from CSV file data
lon = list(data['LON'])                     # make a Python list of latitudes from CSV file data
elev = list(data['ELEV'])
name = list(data['NAME'])


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""


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


volcanoes = folium.FeatureGroup(name="volcanoes")
for lt, ln, el, nm in zip(lat, lon, elev, name):     # NB zip function for multiple lists (latitude and longitude)
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)  # strings interpolated into html string's %s parameters
    # folium.Marker(location=[lt, ln], popup ='<p><b><em>' + nm + ',</em></b></p> <p><b>' + str(el) + '</b> metres</p>', icon=folium.Icon(color='green')).add_to(volcanoes)  # list/array of coords
    folium.Marker(location=[lt, ln], popup = folium.Popup(iframe), icon=folium.Icon(color='green')).add_to(volcanoes)  # list/array of coords
volcanoes.add_to(map)


map.save('MapVolcanoesAdvancedPopup.html')
