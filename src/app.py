
# coding=utf-8
import streamlit as st
import yaml

import plotly.express as px
from streamlit import caching

import model_description as md
import fontes as ft
import team as tm
import simulation as sm
from models import Logo

def main():
    page = st.sidebar.selectbox("Menu", ["COVID19 no seu Município", "Metodologia", "Quem somos?"])


    if page == "Metodologia":
        if __name__ == "__main__":
            md.main()

    elif page == "COVID19 no seu Município":        
          if __name__ == "__main__":
            sm.main()    

    elif page == "Quem somos?":        
          if __name__ == "__main__":
            tm.main()               
            
 
if __name__ == "__main__":
    main()
    

