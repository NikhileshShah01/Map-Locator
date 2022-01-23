import streamlit as st
import streamlit.components.v1 as components 
import folium,requests
st.set_page_config(page_title='Nikhilesh Shah', page_icon=":earth_asia:")
st.title("Map Locator :world_map:")
city=st.text_input("ENTER THE NAME OF THE CITY")
st.markdown(
    """
    <style>
    .reportview-container 
    {
        background: url("https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fwww.dreamtemplate.com%2Fdreamcodes%2Fbg_images%2Fcolor%2Fc12.jpg&f=1&nofb=1")
        }
    </style>
    """,
    unsafe_allow_html=True
)
api="9b833c0ea6426b70902aa7a4b1da285c"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}"
response=requests.get(url)
x=response.json()
    
if(st.button("GET MAP")):
    try:
        lon=x["coord"]["lon"]
        lat=x["coord"]["lat"]
        map=folium.Map(location=[lat,lon])
        folium.Marker([lat,lon],popup=city.title()).add_to(map)
        map.save("map.html")
        HtmlFile = open("map.html", 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        components.html(source_code, height=400)
    except:
        st.warning("OOPS!! INVALID CITY TRY AGAIN ")
