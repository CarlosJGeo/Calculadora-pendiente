import math
import re
import matplotlib.pyplot as plt
import streamlit as st

def obtener_angulo(pendiente_str):
    try:
        match = re.match(r"(\d*\.?\d*)H/(\d*\.?\d*)V", pendiente_str.upper())
        if match:
            H = float(match.group(1))
            V = float(match.group(2))
            pendiente = V / H
            angulo_radianes = math.atan(pendiente)
            angulo_grados = math.degrees(angulo_radianes)
            return angulo_grados, H, V
        else:
            return "Formato incorrecto. Usa el formato 'xH/yV'.", None, None
    except ValueError:
        return "Error al procesar la pendiente.", None, None

def dibujar_pendiente(H, V, angulo_grados):
    fig, ax = plt.subplots()
    ax.plot([0, H], [0, 0], 'b-', label="H (Horizontal)")
    ax.plot([H, H], [0, V], 'r-', label="V (Vertical)")
    ax.plot([0, H], [0, V], 'g-', label="Pendiente")
    max_lim = max(H, V) * 1.2
    ax.set_xlim(0, max_lim)
    ax.set_ylim(0, max_lim)
    ax.text(H / 2, -max_lim * 0.05, f'H = {H}', ha='center')
    ax.text(H + max_lim * 0.05, V / 2, f'V = {V}', va='center')
    ax.text(H / 2, V / 2, f'{angulo_grados:.2f}°', fontsize=12, color='purple')
    ax.set_title(f"Gráfico de la pendiente (ángulo = {angulo_grados:.2f}°)")
    ax.set_xlabel('Componente Horizontal (H)')
    ax.set_ylabel('Componente Vertical (V)')
    ax.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box')
    return fig

st.title("Calculadora de Ángulo a partir de Pendiente")
pendiente_input = st.text_input("Introduce la pendiente (ej. 3H/2V)", value="3H/2V")
if pendiente_input:
    angulo, H, V = obtener_angulo(pendiente_input)
    if H is not None and V is not None:
        st.success(f"Ángulo calculado: {angulo:.2f}°")
        fig = dibujar_pendiente(H, V, angulo)
        st.pyplot(fig)
    else:
        st.error(angulo)
