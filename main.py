import streamlit as st
import codecs
import streamlit.components.v1 as components
import pandas as pd
#from streamlit_lottie import st_lottie
import requests
#import matplotlib.pyplot as plt

#def st_webdev(calc_html,width=700,height=500):
  #calc_file = codecs.open(calc_html,'r')
  #page = calc_file.read()
  #components.html(page,width=width,height=height)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
data=pd.read_csv("data//clean_data.csv")
df=pd.read_csv("data//permissible_limits.csv")

st.set_page_config(layout="wide")

#def main():

rad=st.sidebar.radio("Menu",["Home","Analyst","Dashboard","Feeds"])
if rad == "Home":
    st.title("AQUA.ANALYST")
    st.markdown("""
      _ Water Smarter , What a Starter _
      ## INTRODUCTION
      ### As we are unaware of our groundwater quality and its importance , we are consuming the polluted water which is taking toll on our health , agriculture and every sector of our living. Aqua.Analyst is a platform to analyse the chemical details of groundwater
      ## ABOUT US
      """,True)
    st.video("data//WhatsApp Video 2021-04-03 at 16.14.16.mp4")
    st.header("Hydrological Models")
    a,b,c=st.beta_columns(3)
    a.image("data//Groundwater-Diagram-Gov-of-Newfoundland-Labrador-Canada-2016.jpg")
    b.image("data//R5e5ba91fbd353d083c43de60ff835aa6.jpg")
    c.image("data//R76a84086585340c2423f5a8adb145738.jpg")
    st.header("Research")
    a,b,c=st.beta_columns(3)
    a.image("data//HQ30D-Portable-pH-and-ConductivityTDS-Meter4-460x295.jpg")
    b.image("data//r_3994-natural-resources-wales-opens-new-water-testing-lab.jpg")
    c.image("data//OIP.jpg")
    st.header("Geo-Spacial Visuals")
    a,b,c=st.beta_columns(3)
    a.image("data//WhatsApp Image 2021-04-04 at 09.11.43.jpeg")
    b.image("data//WhatsApp Image 2021-04-04 at 09.11.52.jpeg")
    c.image("data//05153222-BB46-4A29-9B72-91136C4337EE.jpeg")


if rad== "Dashboard":
  rad1=st.sidebar.radio("Dashboard contents",["Agricultural Production","Agricultural Output","State Statistics"]) 
  if rad1 == "State Statistics":
   st.title("Visualisations")
   col1,col2=st.beta_columns((1,1))
   col1.subheader("BOD and Conductivity")
   col1.image("data//visualizations//bod_nd_conductivity_piechart.png")
   col2.subheader("Fecal Coliform and Nitrate")

   col2.image("data//visualizations//fecal_nd_nitrate_piechart.png")
   col3,col4=st.beta_columns(2)
   col3.subheader("BOD VS States")

   col3.image("data//visualizations//bod_vs_states.png")
   col4.subheader("Conductivity VS States")

   col4.image("data//visualizations//conductivity_vs_states.png")
   st.subheader(" State VS BOD, pH and Nitrate")
   
   st.image("data//visualizations//bod_ph_nirate_barchart.png")
   st.subheader("State VS fecal coliform, total coliform and Conductivity")

   st.image("data//visualizations//fecal_total_conductivity_barchart.png")
   col5,col6=st.beta_columns(2)
   col5.subheader("State VS Fecal coliform")

   col5.image("data//visualizations//fecal_vs_states.png")
   col6.subheader("State VS Nitrate")

   col6.image("data//visualizations//nitrate_vs_states.png")
   st.subheader("heat Map for co-relation")

   st.image("data//visualizations//heatmap.png")
   st.subheader("Line Plot of Chemical components")

   st.image("data//visualizations//linechart.png")
   col7,col8=st.beta_columns(2)
   col7.subheader("State VS Nitrate")

   col7.image("data//visualizations//nitrate_vs_states.png")
   col8.subheader("State VS Total Coliform")

   col8.image("data//visualizations//total_coliform_vs_states.png")
   st.subheader("Pair Plot for relationships")

   st.image("data//visualizations//pairplot.png")
   col9,col10=st.beta_columns(2)
   col9.subheader("State VS pH")

   col9.image("data//visualizations//pH_vs_states.png")
   col10.subheader("State VS Temperature")

   col10.image("data//visualizations//temp_vs_states.png")
   col11,col12=st.beta_columns(2)
   col11.subheader("Top 5 States With Highest BOD")

   col11.image("data//visualizations//top5_bod.png")
   col12.subheader("Top 5 States With Highest Total Coliform")

   col12.image("data//visualizations//top5_total_coliform.png")
   st.subheader("Total Coliform and pH of States")
   st.image("data//visualizations//total_coliform_nd_pH_piechart.png")
  if rad1 == "Agricultural Production":
    st.title("Visualisations")
    st.header("Land Area VS Production")
    c1,c2=st.beta_columns(2)
    st.header("Co-relation")
    c1.subheader("Line Chart")
    c1.image("data//area_vs_prod_linechart.png")
    c2.subheader("Scatter Plot")
    c2.image("data//area_vs_prod_scatterplot.png")
    c3,c4=st.beta_columns(2)
    c3.subheader("Heat Map")
    c3.image("data//heatmap.png")
    c4.subheader("pair plot")
    c4.image("data//pairplot.png")
    c5,c6=st.beta_columns(2)
    c5.subheader("Pie chart for Production and Production per area")
    c5.image("data//state_vs_prod_piechart.png")
    c6.subheader("Top ten States in Production")
    c6.image("data//top_10_prod_state_barchart.png")
  if rad1 == "Agricultural Output":
    st.title("Visualisations")
    st.header("Scatter Plots")
    c1,c2=st.beta_columns(2)
    c1.subheader("BOD VS Agricultural Output")

    c1.image("data//agri-output//bod_scatterplot.png")
    c2.subheader("Conductivity VS Agricultural Output")

    c2.image("data//agri-output//conductivity_scatterplot.png")
    c3,c4=st.beta_columns(2)
    c3.subheader("Fecal coliform VS Agricultural Output")

    c3.image("data//agri-output//fecal_coliform_scatterplot.png")
    c4.subheader("Nitrate VS Agricultural Output")

    c4.image("data//agri-output//nitrate_scatterplot.png")
    c5,c6=st.beta_columns(2)
    c5.subheader("pH VS Agricultural Output")

    c5.image("data//agri-output//ph_scatterplot.png")
    c6.subheader("Temperature VS Agricultural Output")

    c6.image("data//agri-output//temperature_scatterplot.png")
    st.subheader("Total Coliform VS Agricultural Output")
    st.image("data//agri-output//total_coliform_scatterplot.png")
if rad == "Analyst":
    #lottie_book = load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_8hddy41z.json')
    #st_lottie(lottie_book, speed=1, height=200, key="initial")
    st.title("Analyst")
    st.markdown(""" 1.8 billion people around the world lack access to safe water,
    therefore it is essential to spread water awareness :droplet: """)
    c1,c2= st.beta_columns(2)
    state=c1.selectbox("State",["","Madhya Pradesh","Lakshadweep","Odisha","Maharashtra"])
    if state=="Madhya Pradesh":
      lm=c2.selectbox("Landmark",["","GROUND WATER SAMPLING AT TWO POINTS IN INDUSTRIAL AREA MALANPUR","MEHATWAS, NAGDA","BHAGATPURI VILLAGE, NAGDA","DOSIGAON, RATLAM","CULVERT ON A.B. ROAD, MAKSI","Trenching Ground Nr Garden Dev Guradia","Trenching Ground Premises of Rishabh Masala","Trenching Ground Premises of Lakhani Foot Wear","TUBE WELL/ HAND PUMP AT INDUSTRIAL AREA, DEWAS","HAND PUMP NEAR PANCHAYAT BHAWAN, VILLAGE TINAWALI RAIRU","T.W./H.P near Manglia.Ind. Area","B.W.Water at.Kalindi Vihar Trenching ground","T.W.W. sec-III Pithampur Tube Wewll Water","T.W.W.at Village Tarpura sec-III Pithampur Tube Well Water"])
    elif state == "Lakshadweep":
      lm=c2.selectbox("Landmark",["WELL NEAR J.B SCHOOL","WELL NEAR OTTAVATHIL PALLI","WELL NEAR CHEKKILLAM HOUSE","WELL C/O KADAT PALLI","WELL NEAR BADER PALLI","WELL C/O PUTHIYA PALLI","WELL C/O ANDAM PALLI","WELL C/O CIRCUIT HOUSE","WELL C/O GOVT. PRESS","WELL C/O OLD POLICE BARRACKS","WELL NEAR HALIPAD","PUBLIC WELL OPPOSITE S.B.SCHOOL"])
    elif state == "Odisha":
      lm=c2.selectbox("Landmark",["JAGATPUR INDUSTRIAL AREA, CUTTACK","MADHUPATNA- KALYAN NAGAR AREA, CUTTACK","BIDANASHI - TULASIPUR AREA, CUTTACK","BADAMBARI AREA, CUTTACK","RANIHAT- MANGALABAGH AREA, CUTTACK","KHANDAGIRI AREA, BHUBANESWAR","CAPITAL HOSPITAL AREA, BHUBANESWAR","OLD TOWN- SAMANTARAAIPUR AREA, BHUBANESWAR","KALPNA - LAXMINAGAR AREA, BHUBANESWAR","MANCHESWAR INDUSTRIAL AREA, BHUBANESWAR","SECRETARIAT- GOVERNOR HOUSE- OLDBUS STAND AREA, BHUBANESWAR","NEAR SEA BEACH, PURI","NEAR JAGANNATH TEMPLE, PURI","HOSPITAL - BUSSTAND- MAUSHIMA TEMPLE AREA, PURI","NEAR RIVER KUSHABHADRA, PURI"])
    elif state == "Maharashtra":
      lm=c2.selectbox("Landmark",["Dug well at 5 -Star Industrial estate, Village-Kashimira Taluka- Mira- Bhayander District-Thane","Bore well at Village- Motapada Taluka- Dahanu District- Thane","Bore well Village-Gokhiware Taluka- Vasai District- Thane","Bore well at Gharatwadi, Village- Aliyali Taluka- Palghar District- Thane","Bore well at MWML site, Village-Karawla, Taloja Taluka- Panvel District- Raigad","Dug Well","Dug well at TPS-Durgapur Village-Durgapur , Taluka- Chandrapur, District- Chandrapur","Bore well Near Gram Panchayat office. Village-Changera, Taluka- Gondia, District- Gondia","Tube well at water treatment plant of.Achalpur M.C, near Post Office. Village-Paratwada, Taluka- Achalpur, District- Amravati","Bore well Opp. Gajanan MPCBaraj Temple at Anjangaon road. Village-Anjangaon, Taluka- Akot, District- Akola","Dug well at Plot No- 4, Street No. 49-C, at Nehru Bal Udyan Azad Maidan, owned by Yavatmal M.C. Village- Nehru Bal Udyan Azad Maidan, Taluka- Yavatmal, District- Yavatmal","Bore well water sample at savali, Tal. Miraj, Dist Sangli","Dugwell Water sample at Rasulwadi Tal. Miraj, Dist. Sangli","Bore Well","Dugwell at Ghane Kunth near Awashi, Owned by Shri. Rajendra Ambre vill Ghanekunth Tal. Khed, Dist. Ratnagiri","Hand Pump in the premises of Zilla Parishad Primary School. Village- Bhugaon, Taluka- Wardha, District- Wardha","Dug well owned by Shri Deshmukh. Village- Malegaon, Taluka- Baramati, District- Pune","Dug well owned by Shri Shivaji Baban Darekar Village- Sanaswadi, Taluka- Shirur, District- Pune","Bore well at Bale railway station premises owned by Shri. Digambar Joshi. Village- Dahegaon,Taluka- North Solapur, District- Solapur","Bore well near Chincholi. Village- Chincholi, Taluka- Mohol, District- Solapur","Bore well at Shete Vasti, near old Tuljapur road. Village- Tuljapur naka, Taluka- Solapur,District- Solapur","Dug well near Railway station, Cotton Market. Village- Wardha city, Taluka- Wardha,District- Wardha","Bore well Near Railway crossing at Dongri Buzurg. Village- Dongri-Buzurg, Taluka- Tumsar,District- Bandara","Dug well near Jilla Parishet Primary school, Visapur. Village- Visapur, Taluka- Ballarpur,District- Chandrapur","Dugwell water sample at Sakharoli Tal .Walwa, Dist Sangli","Dugwell no 1 at Brahamanwadi (C/O Shri Vaidya) Vill Anjanwell, Tal. Guhagar, Dist Ratangiri.","Dugwell no. 1 at Grampanchayat at Arkatewadi near Masjid, Khed, Ratangiri.","Dugwell no 2 at Arkatewadi, Khed, Ratnagiri","Durgwell no. 2 owned by Group Gram Panchayat at Brahmanwadi Vill Anjanwell, Tal. Guhagar, Dist. Ratnagiri."])

    if st.checkbox("Show Data"):
       st.subheader("Permissible limits for Potable Water")
       st.table(df)   
       st.subheader("Your Data")   
       data.loc[(data['LOCATIONS']==lm) & (data['STATE']==state)]
       st.subheader("States VS Temperature")
       st.bar_chart(data['Temperature_Mean'])
       st.subheader("States VS BOD")
       st.bar_chart(data['BOD_Mean'])
       st.subheader("States VS Conductivity")
       st.bar_chart(data['Conductivity_Mean'])
       st.subheader("States VS pH")
       st.bar_chart(data['pH_Mean'])
       st.subheader("States VS Nitrate")
       st.bar_chart(data['Nitrate_Mean'])
       st.subheader("States VS Fecal Coliform")
       st.bar_chart(data['Fecal_coliform_Mean'])
       st.subheader("States VS Total Coliform")
       st.bar_chart(data['Total_coliform_Mean'])
if rad == "Feeds":
       #lottie_book = load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_tjwsyfkj.json')
       #st_lottie(lottie_book, speed=1, height=200, key="initial")
       st.header('[World Bank Signs Agreement to Improve Groundwater Management](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=World+Bank+Signs+Agreement+to+Improve+Groundwater+Management+in+India&btnG=)')
       st.image('data//agri-output//the-world-bank-Insert.jpg')
       st.subheader('“In India groundwater is an important source for rural and urban domestic water supplies and its depletion is a cause of concern,” said Sameer Kumar Khare, Additional Secretary, Department of Economic Affairs, Ministry of Finance.  “The Atal Bhujal Yojana intends to strengthen the institutional framework for participatory groundwater management and encourage behavioral changes at the community level for sustainable groundwater resource management.  The use of cutting-edge technology, involving Artificial Intelligence and space technology will further help in better implementation of the program.”')
       st.header('[India’s Groundwater Crisis:](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=India%E2%80%99s+Groundwater+Crisis&btnG=)')
       st.image("data//agri-output//74038e4b9817459ba917b9d8a0209f82_6.jpg")
       st.subheader('India is the world’s highest user of groundwater. It consumes over a quarter of the global total – equivalent to 230 cubic kilometres per year. Groundwater from over 30 million access points supplies 85 per cent of drinking water in rural areas and 48 per cent of water requirements in urban areas. Most groundwater is used for irrigation, which accounts for 88 per cent of total groundwater usage. Groundwater is required for the daily needs of around 700 million Indians living in the country’s villages. An assessment of 6,607 groundwater units in 2011 found that 1,017 were “overexploited”, indicating the rate of groundwater extraction exceeded replenishment. Around one-third of all units in India were under stress. The World Bank predicts that by 2032, around 60 per cent of aquifers in the country will be in a critical state.')
       st.header('[Ground water Governance in South Asia:](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=ground+water+projects+by+Indian+Corporates&btnG=)')
       st.image("data//agri-output//oP3-8gKkIGmZxv6iFKSKgg_b.jpg")
       st.subheader("Gujarat, a rapidly industrializing state in western India, is notorious for groundwater over-exploitation. A perverse link between energy subsidies and groundwater overdraft has left the state with a bankrupt electricity utility and depleted aquifers, especially since the late 1980s. Moreover, this perverse relationship has meant that groundwater irrigators have essentially held Gujarat's non-farm rural economy to ransom. Efforts to regulate groundwater overdraft since the early 1970s have been unsuccessful, as have attempts to charge a rational electricity tariff to groundwater irrigators.")
       st.header('[Integrated concepts in water reuse: managing global water needs](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=Ground+water+contamination+in+going+projects+&btnG=)')
       st.image("data//agri-output//R6b0d6d42fc96ee535593f45a44ad2f4c.jpg")
       st.subheader("Communities across the world face water supply challenges due to increasing demand, drought, depletion and contamination of groundwater, and dependence on single sources of supply. Water reclamation, recycling, and reuse address these challenges by resolving water resource issues and creating new sources of high-quality water supplies. ")
