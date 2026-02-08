import streamlit as st
import pandas as pd


st.set_page_config(page_title="Best food and groceries", page_icon="🛒")

def calcular_subtotal(nombre_producto, precio_producto, cantidad_producto):
    subtotal = float(precio_producto) * float(cantidad_producto)
    
    
    nueva_fila = {
        "producto": nombre_producto,
        "precio": precio_producto,
        "cantidad": cantidad_producto,
        "subtotal": subtotal 
    }
    
    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, pd.DataFrame([nueva_fila])],
        ignore_index=True
    )


if "table_data" not in st.session_state:
    st.session_state.table_data = pd.DataFrame(
        columns=["producto", "precio", "cantidad", "subtotal"]
    )
    
st.title("Best food and groceries 🛒")


with st.form("producto_form", clear_on_submit=True): 
    producto_nombre = st.text_input("Ingrese el nombre del producto")
    producto_precio = st.number_input("Ingrese el precio del producto", min_value=0.0, step=0.1)
    producto_cantidad = st.number_input("Ingrese la cantidad", min_value=1)

    subtotal_boton = st.form_submit_button("Añadir al carrito 🛒")

if subtotal_boton:
    if producto_nombre: # Validamos que el nombre no esté vacío
        calcular_subtotal(producto_nombre, producto_precio, producto_cantidad)
    else:
        st.error("Por favor, ingresa el nombre del producto.")


st.subheader("Tu Carrito")
st.dataframe(st.session_state.table_data, use_container_width=True)


if st.button("Finalizar Compra y Calcular Total"):
    if not st.session_state.table_data.empty:
        
        total = st.session_state.table_data["subtotal"].sum()
        
        st.divider()
        st.subheader(f"Total a pagar: ${total:,.2f}")
        st.balloons() 
    else:
        st.warning("El carrito está vacío.")
