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
        background: url("data:image/jpeg;base64,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")
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
