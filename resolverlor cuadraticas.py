import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Resolvedor de Ecuaciones Cuadráticas')

# Celdas de entrada para los coeficientes con restricción a 2 decimales
a = round(st.number_input('Coeficiente a', value=1.0, step=0.01), 2)
b = round(st.number_input('Coeficiente b', value=0.0, step=0.01), 2)
c = round(st.number_input('Coeficiente c', value=0.0, step=0.01), 2)

# Resolver la ecuación cuadrática con procedimiento analítico detallado
discriminante = round(b**2 - 4*a*c, 2)

st.write(f'Discriminante calculado: ({b})² - 4({a})({c}) = {discriminante}')

if discriminante > 0:
    x1 = round((-b + np.sqrt(discriminante)) / (2*a), 2)
    x2 = round((-b - np.sqrt(discriminante)) / (2*a), 2)
    st.write(f'Raíces reales encontradas usando la fórmula general:')
    st.latex(rf"x_1 = \frac{{-{b} + \sqrt{{{discriminante}}}}}{{2 \cdot {a}}} = {x1}")
    st.latex(rf"x_2 = \frac{{-{b} - \sqrt{{{discriminante}}}}}{{2 \cdot {a}}} = {x2}")
elif discriminante == 0:
    x1 = round(-b / (2*a), 2)
    st.write(f'Raíz doble encontrada usando la fórmula general:')
    st.latex(f'x = \frac{{-{b}}}{{2 \cdot {a}}} = {x1}')
else:
    st.write('No hay raíces reales ya que el discriminante es negativo.')

# Definición de la función cuadrática
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

# Generación de valores para graficar
x = np.linspace(-10, 10, 400)
y = quadratic(x, a, b, c)

# Crear la gráfica
fig, ax = plt.subplots()
ax.plot(x, y, label=f'{a}x² + {b}x + {c}')
ax.axhline(0, color='gray', linewidth=0.8)
ax.axvline(0, color='gray', linewidth=0.8)
ax.grid(True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)

# Mostrar la fórmula con los valores actuales
st.write(f'**Ecuación:** ${a}x^2 + {b}x + {c}$')

# Mostrar la solución final
if discriminante > 0:
    st.write(f'**Solución para x:** $x_1 = {x1}$, $x_2 = {x2}$')
elif discriminante == 0:
    st.write(f'**Solución para x:** $x = {x1}$')
else:
    st.write(f'**Solución para x:** No hay soluciones reales')
