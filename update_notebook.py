import json

def update_notebook():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Manipulación y Estandarización de Textos (Strings)\n",
                "\n",
                "Tras limpiar los errores numéricos básicos, es vital asegurar que los datos de tipo texto (`object`) sean consistentes. Utilizaremos el accesor `.str` de Pandas para modificar cadenas de texto. Esto evita que categorías como 'Yes' y 'yes' sean tratadas como diferentes por un modelo. Ver el [Tutorial de Alura](https://www.aluracursos.com/blog/manipulacion-de-strings-en-pandas-lower-replace-startswith-y-contains)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- ESTANDARIZACIÓN DE STRINGS ---\")\n",
                "\n",
                "# 1. Convertir nombres de columnas problemáticas (si las hay)\n",
                "print(\"Nombres de columnas originales (primeros 5):\")\n",
                "print(df.columns[:5].tolist())\n",
                "\n",
                "# Reemplazar los puntos '.' que dejamos del json_normalize por guiones bajos '_'\n",
                "# usando .str.replace()\n",
                "df.columns = df.columns.str.replace('.', '_')\n",
                "print(\"\\nNuevos nombres de columnas (usando replace):\")\n",
                "print(df.columns[:5].tolist())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 2. Estandarizar valores categóricos a Minúsculas con .str.lower()\n",
                "# Esto asegura que evitar inconsistencias humanas.\n",
                "\n",
                "# Vamos a aplicarlo a la columna objetivo, 'Churn'.\n",
                "df['Churn'] = df['Churn'].str.lower()\n",
                "print(\"Valores en 'Churn' después de aplicar lower():\")\n",
                "print(df['Churn'].unique())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 3. Limpieza de descripciones usando .str.replace()\n",
                "\n",
                "print(\"Métodos de pago originales:\")\n",
                "print(df['account_PaymentMethod'].unique())\n",
                "\n",
                "# Algunos dicen '(automatic)', lo reemplazaremos por nada (lo eliminamos)\n",
                "# Usamos regex=True para manejar expresiones regulares; '\\(' escapa los paréntesis.\n",
                "df['account_PaymentMethod'] = df['account_PaymentMethod'].str.replace(' \\(automatic\\)', '', regex=True)\n",
                "\n",
                "print(\"\\nMétodos de pago limpios (sin '(automatic)'):\")\n",
                "print(df['account_PaymentMethod'].unique())"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 4. Búsquedas e identificaciones usando .str.startswith() y .str.contains()\n",
                "\n",
                "# STARTWITH: Identificar los contratos que comiencen por la cadena \"Month\"\n",
                "contratos_mensuales = df[df['account_Contract'].str.startswith('Month')]\n",
                "print(f\"Clientes con contrato que inicia en 'Month': {contratos_mensuales.shape[0]}\")\n",
                "\n",
                "# CONTAINS: Identificar aquellos servicios de internet que de alguna forma contengan \"Fiber\"\n",
                "clientes_fibra = df[df['internet_InternetService'].str.contains('Fiber', case=False, na=False)]\n",
                "print(f\"Clientes con internet de fibra (usando contiene): {clientes_fibra.shape[0]}\")"
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook()
