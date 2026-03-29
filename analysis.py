import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='produit', title='Quantité vendue par produit')

figure.write_html('Ventes-par-produit.html')

données['chiffre'] = données['qte'] * données['prix']

figure2 = px.pie(données, values='chiffre', names='produit', title='Chiffre vendue par produit')

figure2.write_html('Chiffre-par-produit.html')

print('ventes-par-région.html généré avec succès !')
