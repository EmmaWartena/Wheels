!pip install plotly
import streamlit as st
import pandas as pd
import numoy as np

st.title("Wheel analysis Boeing 737 MAX 9")
st.write( 
  "Er zijn verschillende opties voor het bepalen van de voorraad van banden die nodig zijn voor het nieuwe jaar. Bij elke optie worden ook de voor- en nadelen besproken en op welke parameter de optie vooral is gebaseerd.")
st.header("Optie 1: Trent van bandenwissels doortrekken")

st.write(
 '''In de eerste optie is er gekeken naar het aantal bandenwissels van het afgelopen jaar en hier is een waarde uitgekomen. Deze waarde geeft aan hoeveel bandenwissels er plaatsvinden per week gemiddeld. 
         Er is hier dus niet meegenomen dat er de waardes misschien niet hetzelfde zijn als je een analyse wil van een speccifieke methode.''')

st.markdown('''
            Voordelen:
            - Wanneer het nummer van vluchten dit jaar gemiddeld genomen hetzelfde blijft vergeleken met vorrig jaar s dit een betrouwbare meting wanneer deze wordt uigevoerd over een langere periode;
            - Aangezien er vooral data bekend is van de zomerperiode (toen alle vliegtuigen aanwezig waren) pakt deze waarde hoogstwaarschijnlijk hoger uit dan de realiteit waardoor het niet 
            snel zal voorkomen dat we door de voorraad gaan en er vertragingen zouden onstaan omdat banden niet aanwezig zouden zijn en een levertijd hebben
            - Het is een snelle en eenvoudige analyse, die een grove schatting kan maken voor de benodigde hoeveelheid banden.

            Nadelen:
            - De analyse is niet betrouwbaar wanneer deze informatie moet bereken voor kleinere periodes, aangezien er geen factor wordt meegnoemen door invloeden van buitenaf. Denk hier bijvoorbeeld aan de 
            temperatuur op bestemming in de zomerperiodes, vluchten naar nieuwe bestemmingen, of andere factors die invloed kunnen hebben op de banden.
            - De analyse is ook minder betrouwbaar wanneer de flight planning er aankomend jaar anders uit zou zien als die van afgelopen jaar. Dit omdat de waarde een gemiddelde is, die is gebaseerd op het afgelopen jaar. 
            Dit maakt de waarde minder betrouwbaar op een volgend jaar met andere omstandigheden. '''
            )

# CSV Import
nw_1 = pd.read_csv('Wheel12.csv') 

nw_1.head()
