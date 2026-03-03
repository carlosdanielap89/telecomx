import json

def update_notebook_standardization():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Estandarización y Transformación de Datos\n",
                "\n",
                "Para preparar los datos para los modelos analíticos y hacerlos más interpretables, realizaremos dos tareas clave:\n",
                "1. **Binarización**: Convertir los valores de texto afirmativos/negativos ('yes', 'no', 'Yes', 'No') en variables numéricas binarias (1 y 0). Los algoritmos matemáticos procesan mejor números que texto.\n",
                "2. **Renombrar Columnas**: Traducir los nombres técnicos en inglés a español, lo cual facilitará la interpretación para los stakeholders (partes interesadas) no técnicos."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 1. Binarización de Variables Categóricas (Yes/No a 1/0)\n",
                "\n",
                "# Usamos un diccionario de mapeo\n",
                "mapeo_binario = {'yes': 1, 'no': 0, 'Yes': 1, 'No': 0}\n",
                "\n",
                "# Identificamos las columnas que contienen típicamente Yes/No\n",
                "columnas_binarias = [\n",
                "    'Churn', 'customer_Partner', 'customer_Dependents', \n",
                "    'phone_PhoneService', 'account_PaperlessBilling'\n",
                "]\n",
                "\n",
                "print(\"Transformando 'Yes' a 1 y 'No' a 0...\")\n",
                "# Aplicamos el mapeo a las columnas seleccionadas\n",
                "for col in columnas_binarias:\n",
                "    if col in df.columns:\n",
                "        # Usamos map() para reemplazar los valores según el diccionario\n",
                "        # Si existe algún valor distinto a 'yes'/'no' se convertirá en NaN, \n",
                "        # lo cual es útil para detectar inconsistencias ocultas.\n",
                "        df[col] = df[col].map(mapeo_binario).fillna(df[col])\n",
                "\n",
                "print(\"\\nValores únicos en 'Churn' después de binarizar:\")\n",
                "print(df['Churn'].unique())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 2. Renombrar Columnas al Español para Claridad\n",
                "\n",
                "traduccion_columnas = {\n",
                "    'customerID': 'ID_Cliente',\n",
                "    'Churn': 'Evasion',\n",
                "    'customer_gender': 'Genero',\n",
                "    'customer_SeniorCitizen': 'Adulto_Mayor',\n",
                "    'customer_Partner': 'Tiene_Pareja',\n",
                "    'customer_Dependents': 'Tiene_Dependientes',\n",
                "    'customer_tenure': 'Meses_Permanencia',\n",
                "    'phone_PhoneService': 'Servicio_Telefonico',\n",
                "    'phone_MultipleLines': 'Multiples_Lineas',\n",
                "    'internet_InternetService': 'Servicio_Internet',\n",
                "    'internet_OnlineSecurity': 'Seguridad_Online',\n",
                "    'internet_OnlineBackup': 'Respaldo_Online',\n",
                "    'internet_DeviceProtection': 'Proteccion_Dispositivo',\n",
                "    'internet_TechSupport': 'Soporte_Tecnico',\n",
                "    'internet_StreamingTV': 'TV_Streaming',\n",
                "    'internet_StreamingMovies': 'Peliculas_Streaming',\n",
                "    'account_Contract': 'Tipo_Contrato',\n",
                "    'account_PaperlessBilling': 'Factura_Electronica',\n",
                "    'account_PaymentMethod': 'Metodo_Pago',\n",
                "    'account_Charges_Monthly': 'Cargo_Mensual',\n",
                "    'account_Charges_Total': 'Cargo_Total'\n",
                "}\n",
                "\n",
                "# Aplicamos el renombramiento\n",
                "df = df.rename(columns=traduccion_columnas)\n",
                "\n",
                "print(\"Nuevos nombres de columnas (Español):\")\n",
                "print(df.columns.tolist())\n",
                "\n",
                "print(\"\\n--- MUESTRA FINAL DEL DATASET ESTANDARIZADO ---\")\n",
                "display(df.head())"
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook_standardization()
