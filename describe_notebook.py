import json

def update_notebook_describe():
    file_path = "d:\\pc\\Documents\\telecomx\\telecomx.ipynb"
    
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
        
    new_cells = [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 7. Análisis Descriptivo\n",
                "\n",
                "El análisis descriptivo nos ayuda a entender las distribuciones matemáticas de nuestros datos limpios y estandarizados. Utilizaremos el método `describe()` de Pandas, el cual calcula estadísticas de resumen como:\n",
                "\n",
                "- **Media (mean):** El promedio de los valores.\n",
                "- **Desviación Estándar (std):** Cuánto varían los datos respecto al promedio.\n",
                "- **Mínimo y Máximo (min, max):** Los valores extremos.\n",
                "- **Cuartiles (25%, 50%, 75%):** El 50% es la Mediana. Resulta útil para observar sesgos."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- ESTADÍSTICAS DESCRIPTIVAS (Variables Numéricas) ---\")\n",
                "\n",
                "# describe() por defecto solo toma las columnas numéricas (int64, float64).\n",
                "# Gracias a nuestro trabajo previo, variables como 'Cargo_Total' y 'Cuentas_Diarias'\n",
                "# ya aparecerán aquí correctamente calculadas.\n",
                "\n",
                "estadisticas = df.describe().round(2) # Redondeamos a 2 decimales para leerlo mejor\n",
                "display(estadisticas)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"--- ANÁLISIS DE LA VARIABLE OBJETIVO (Evasión) ---\")\n",
                "\n",
                "# Como convertimos la Evasión ('Churn') de Yes/No a 1/0, \n",
                "# ahora podemos calcular su MEDIA, lo que nos da la tasa exacta de abandono global.\n",
                "\n",
                "tasa_evasion = round(df['Evasion'].mean() * 100, 2)\n",
                "print(f\"La tasa global de evasión es del {tasa_evasion}%\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Qué observar en la tabla `describe()`:\n",
                "1. **`Adulto_Mayor` / `Evasion`**: Al ser variables binarias (0 y 1), su media indica la proporción (ej. si la media de `Evasion` es 0.26, significa que el ~26% de los clientes se fue).\n",
                "2. **`Meses_Permanencia`**: La divergencia entre la media y la mediana (el valor del 50%) te dirá si tienes más clientes antiguos o recientes.\n",
                "3. **`Cargo_Mensual` vs `Cuentas_Diarias`**: Podrás ver el promedio de lo que pagan tus clientes y cuáles son sus extremos y desviaciones."
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook_describe()
