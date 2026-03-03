import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_Data.json"
response = requests.get(url)
data = response.json()
df = pd.json_normalize(data)

df['account.Charges.Total'] = df['account.Charges.Total'].replace(' ', np.nan)
df['account.Charges.Total'] = pd.to_numeric(df['account.Charges.Total'])
df['account.Charges.Total'] = df['account.Charges.Total'].fillna(0)
df['Churn'] = df['Churn'].replace([' ', ''], np.nan)
df = df.dropna(subset=['Churn'])

df.columns = df.columns.str.replace('.', '_', regex=False)
df['Churn'] = df['Churn'].str.lower()
df['account_PaymentMethod'] = df['account_PaymentMethod'].str.replace(' \\(automatic\\)', '', regex=True)

df['Cuentas_Diarias'] = round(df['account_Charges_Monthly'] / 30, 2)

mapeo_binario = {'yes': 1, 'no': 0, 'Yes': 1, 'No': 0}
columnas_binarias = ['Churn', 'customer_Partner', 'customer_Dependents', 'phone_PhoneService', 'account_PaperlessBilling']
for col in columnas_binarias:
    if col in df.columns:
        df[col] = df[col].map(mapeo_binario).fillna(df[col])

traduccion_columnas = {
    'customerID': 'ID_Cliente', 'Churn': 'Evasion', 'customer_gender': 'Genero', 
    'customer_SeniorCitizen': 'Adulto_Mayor', 'customer_Partner': 'Tiene_Pareja', 
    'customer_Dependents': 'Tiene_Dependientes', 'customer_tenure': 'Meses_Permanencia', 
    'phone_PhoneService': 'Servicio_Telefonico', 'phone_MultipleLines': 'Multiples_Lineas', 
    'internet_InternetService': 'Servicio_Internet', 'internet_OnlineSecurity': 'Seguridad_Online', 
    'internet_OnlineBackup': 'Respaldo_Online', 'internet_DeviceProtection': 'Proteccion_Dispositivo', 
    'internet_TechSupport': 'Soporte_Tecnico', 'internet_StreamingTV': 'TV_Streaming', 
    'internet_StreamingMovies': 'Peliculas_Streaming', 'account_Contract': 'Tipo_Contrato', 
    'account_PaperlessBilling': 'Factura_Electronica', 'account_PaymentMethod': 'Metodo_Pago', 
    'account_Charges_Monthly': 'Cargo_Mensual', 'account_Charges_Total': 'Cargo_Total'
}
df = df.rename(columns=traduccion_columnas)

sns.set_theme(style="whitegrid")
colores = ["#2ecc71", "#e74c3c"]

# 1. Churn Distribution
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Análisis de Retención vs Evasión de Clientes", fontsize=16, fontweight='bold')
sns.countplot(data=df, x='Evasion', palette=colores, ax=axes[0])
axes[0].set_title("Cantidad de Clientes por Estado", fontsize=14)
axes[0].set_xlabel("Evasión (0 = No, 1 = Sí)", fontsize=12)
axes[0].set_ylabel("Número de Clientes", fontsize=12)
for p in axes[0].patches:
    axes[0].annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'bottom', fontsize=11)
evasion_counts = df['Evasion'].value_counts()
axes[1].pie(evasion_counts, labels=["Permanecen (0)", "Se dan de baja (1)"], autopct='%1.1f%%', startangle=90, colors=colores, explode=(0, 0.1), shadow=True)
axes[1].set_title("Proporción de Evasión", fontsize=14)
plt.tight_layout()
plt.savefig("d:\\pc\\Documents\\telecomx\\churn_distribution.png", dpi=300)
plt.close()

# 2. Categorical
columnas_cat = ['Tipo_Contrato', 'Servicio_Internet', 'Metodo_Pago', 'Adulto_Mayor']
nombres_titulos = ['Tipo de Contrato', 'Servicio de Internet', 'Método de Pago', 'Adulto Mayor (1=Sí)']
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Patrones de Evasión según Características del Servicio y Cliente", fontsize=18, fontweight='bold', y=1.02)
axes = axes.flatten()
for i, col in enumerate(columnas_cat):
    sns.countplot(data=df, x=col, hue='Evasion', palette=colores, ax=axes[i])
    axes[i].set_title(f"Evasión por {nombres_titulos[i]}", fontsize=14)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Número de Clientes")
    axes[i].legend(title="Evasión (1=Sí)")
    if col == 'Metodo_Pago':
        axes[i].tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig("d:\\pc\\Documents\\telecomx\\churn_categorical.png", dpi=300)
plt.close()

# 3. Numeric
columnas_num = ['Meses_Permanencia', 'Cargo_Mensual', 'Cargo_Total']
nombres_titulos_num = ['Meses en la Empresa (Tenure)', 'Cargo Mensual ($)', 'Cargos Totales Acumulados ($)']
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Distribución de Variables Numéricas vs Evasión", fontsize=16, fontweight='bold', y=1.05)
for i, col in enumerate(columnas_num):
    sns.kdeplot(data=df, x=col, hue='Evasion', fill=True, palette=colores, ax=axes[i], alpha=0.5)
    axes[i].set_title(nombres_titulos_num[i], fontsize=13)
    axes[i].set_xlabel("")
    axes[i].set_ylabel("Densidad (Proporción de clientes)")
plt.tight_layout()
plt.savefig("d:\\pc\\Documents\\telecomx\\churn_numeric_kde.png", dpi=300)
plt.close()

# 4. Total Services Ecosystem
servicios = ['Servicio_Telefonico', 'Multiples_Lineas', 'Servicio_Internet', 'Seguridad_Online', 'Respaldo_Online', 'Proteccion_Dispositivo', 'Soporte_Tecnico', 'TV_Streaming', 'Peliculas_Streaming']
df['Total_Servicios'] = 0
for col in servicios:
    if col in df.columns:
        if pd.api.types.is_numeric_dtype(df[col]):
            df['Total_Servicios'] += df[col]
        else:
            df['Total_Servicios'] += df[col].astype(str).str.contains('Yes|yes|Fiber|DSL', regex=True).astype(int)

plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='Total_Servicios', y='Evasion', color='#e74c3c')
plt.title("Tasa de Evasión Promedio según Cantidad Total de Servicios Contratados", fontsize=14)
plt.xlabel("Total de Servicios Adicionales Activos en el Hogar/Móvil", fontsize=12)
plt.ylabel("Tasa Promedio de Evasión (0 a 1)", fontsize=12)
tasa_global = df['Evasion'].mean()
plt.axhline(tasa_global, color='black', linestyle='--', label=f'Media Global ({round(tasa_global*100, 1)}%)')
plt.legend()
plt.tight_layout()
plt.savefig("d:\\pc\\Documents\\telecomx\\churn_ecosystem.png", dpi=300)
plt.close()

print("Imágenes generadas correctamente.")
