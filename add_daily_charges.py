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
                "## 5. Ingeniería de Características (Feature Engineering): Nuevas Variables\n",
                "\n",
                "Para obtener una vista más detallada del comportamiento diario de facturación, calcularemos el gasto diario esperado por cada cliente basándonos en su factura mensual. Esto nos brindará una granularidad distinta al analizar la evasión."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Calculamos 'Cuentas_Diarias' dividiendo el cargo mensual ('account_Charges_Monthly') entre 30 días.\n",
                "# Usamos round() para mantener 2 decimales y que sea legible como moneda.\n",
                "df['Cuentas_Diarias'] = round(df['account_Charges_Monthly'] / 30, 2)\n",
                "\n",
                "print(\"Primeras filas mostrando los cargos mensuales y la nueva columna diaria:\")\n",
                "display(df[['account_Charges_Monthly', 'Cuentas_Diarias']].head())"
            ]
        }
    ]
    
    notebook["cells"].extend(new_cells)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=1)

if __name__ == "__main__":
    update_notebook()
