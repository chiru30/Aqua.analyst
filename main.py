import streamlit as st
import codecs
import streamlit.components.v1 as components
import pandas as pd

import numexpr as ne

def st_webdev(calc_html,width=700,height=500):
  calc_file = codecs.open(calc_html,'r')
  page = calc_file.read()
  components.html(page,width=width,height=height)


data=pd.read_csv("data//clean_data.csv")

st.set_page_config(layout="wide")

def main():

 rad=st.sidebar.radio("Menu",["Home","Analyst","Dashboard","Feeds"])
 if rad == "Home":
    st.image("data//1 (1).png", width=200)
    st.title("AQUA.ANALYST")
    st.header("Our aim is to bring the awareness among people for water conservation")
    st.subheader("What our project contains")

 if rad== "Dashboard":
  rad1=st.sidebar.radio("Dashboard contents",["Agricultural Production","Agricultural Output","State Statistics"]) 
  if rad1 == "State Statistics":
   st.title("Visualisations")
   st.markdown("Content ......................................")

   col1,col2=st.beta_columns((1,1))
   col1.image("data//visualizations//bod_nd_conductivity_piechart.png")
   col2.image("data//visualizations//fecal_nd_nitrate_piechart.png")
   col3,col4=st.beta_columns(2)
   col3.image("data//visualizations//bod_vs_states.png")
   col4.image("data//visualizations//conductivity_vs_states.png")
   st.image("data//visualizations//bod_ph_nirate_barchart.png")
   st.image("data//visualizations//fecal_total_conductivity_barchart.png")
   col5,col6=st.beta_columns(2)
   col5.image("data//visualizations//fecal_vs_states.png")
   col6.image("data//visualizations//nitrate_vs_states.png")
   st.image("data//visualizations//heatmap.png")
   st.image("data//visualizations//linechart.png")
   col7,col8=st.beta_columns(2)
   col7.image("data//visualizations//nitrate_vs_states.png")
   col8.image("data//visualizations//total_coliform_vs_states.png")
   st.image("data//visualizations//pairplot.png")
   col9,col10=st.beta_columns(2)
   col9.image("data//visualizations//pH_vs_states.png")
   col10.image("data//visualizations//temp_vs_states.png")
   col11,col12=st.beta_columns(2)
   col11.image("data//visualizations//top5_bod.png")
   col12.image("data//visualizations//top5_total_coliform.png")
   st.image("data//visualizations//total_coliform_nd_pH_piechart.png")
  if rad1 == "Agricultural Output":
    st.title("Visualisations")
    c1,c2=st.beta_columns(2)
    c1.image("data//area_vs_prod_linechart.png")
    c2.image("data//area_vs_prod_scatterplot.png")
    c3,c4=st.beta_columns(2)
    c3.image("data//heatmap.png")
    c4.image("data//pairplot.png")
    c5,c6=st.beta_columns(2)
    c5.image("data//state_vs_prod_piechart.png")
    c6.image("data//state_vs_production.png")
    st.image("data//top_10_prod_state_barchart.png")
  if rad1 == "Agricultural Production":
    st.title("Visualisations")
    c1,c2=st.beta_columns(2)
    c1.image("data//agri-output//bod_scatterplot.png")
    c2.image("data//agri-output//conductivity_scatterplot.png")
    c3,c4=st.beta_columns(2)
    c3.image("data//agri-output//fecal_coliform_scatterplot.png")
    c4.image("data//agri-output//nitrate_scatterplot.png")
    c5,c6=st.beta_columns(2)
    c5.image("data//agri-output//ph_scatterplot.png")
    c6.image("data//agri-output//temperature_scatterplot.png")
    st.image("data//agri-output//total_coliform_scatterplot.png")
 if rad == "Analyst":
    st.title("Analyst")
    st.markdown(""" 1.8 billion people around the world lack access to safe water,
    therefore it is essential to spread water awareness :droplet: """)
    c1,c2= st.beta_columns(2)
    state=c1.selectbox("State",["","Madhya Pradesh","Lakshadweep","Rajasthan","Tamil Nadu"])
    if state=="Madhya Pradesh":
      lm=c2.selectbox("Landmark",["","GROUND WATER SAMPLING AT TWO POINTS IN INDUSTRIAL AREA MALANPUR","MEHATWAS, NAGDA","BHAGATPURI VILLAGE, NAGDA","DOSIGAON, RATLAM","CULVERT ON A.B. ROAD, MAKSI","Trenching Ground Nr Garden Dev Guradia","Trenching Ground Premises of Rishabh Masala","Trenching Ground Premises of Lakhani Foot Wear","TUBE WELL/ HAND PUMP AT INDUSTRIAL AREA, DEWAS","HAND PUMP NEAR PANCHAYAT BHAWAN, VILLAGE TINAWALI RAIRU","T.W./H.P near Manglia.Ind. Area","B.W.Water at.Kalindi Vihar Trenching ground","T.W.W. sec-III Pithampur Tube Wewll Water","T.W.W.at Village Tarpura sec-III Pithampur Tube Well Water"])
    elif state == "Lakshadweep":
      lm=c2.selectbox("Landmark",["WELL NEAR J.B SCHOOL","WELL NEAR OTTAVATHIL PALLI","WELL NEAR CHEKKILLAM HOUSE","WELL C/O KADAT PALLI","WELL NEAR BADER PALLI","WELL C/O PUTHIYA PALLI"])
    elif state == "Rajasthan":
      lm=c2.selectbox("Landmark",["raj","as","than"])
    elif state == "Tamil Nadu":
      lm=c2.selectbox("Landmark",["a","b","c"])

    if st.checkbox("Show Data"):
       data.loc[(data['LOCATIONS']==lm) & (data['STATE']==state)]
 if rad == "Feeds":
       st_webdev('index.html')
       st_webdev('index2.html')
       st_webdev('index3.html')
       #if st.checkbox("To know Portability select me"):
        #a,b,c=st.beta_columns((1,1,1))
        #a.text_input("BOD_Min")
        #a.text_input("MMD")
        #b.text_input("BOD_Max")
        #c.text_input("BOD_Mean")
        #if st.button("Check"):
          #components.html("<html><body> <p><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3867559.4230803624!2d74.5308077009342!3d18.802007899954!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bcfc41e9c9cd6f9%3A0x1b2f22924be04fb6!2sMaharashtra!5e0!3m2!1sen!2sin!4v1617358832060!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe> </p></body></html>")
          #st_webdev('index.html')
       #p=data.index[(data['STATE']==state) & (data['LOCATIONS']==lm)].tolist()
       #p=(data.index[data['LOCATIONS'] == lm].tolist())
       #st.write(p)
       #from_val = p
       #data.iloc[:,12] 
       #st.write(p)
       #for index in data.iterrows():
        # if (index==p):
       #for key,value in data.iterrows():
          #if key==0:
            #if data.loc[(data['LOCATIONS']==lm) & (data['STATE']==state) & (data['BOD_Min']==0)]:
              #st.write("Permissible")
          #st.write(key,)   
          
       #data.at[data[0],'BOD_Min']
if __name__ == "__main__":
    main()
