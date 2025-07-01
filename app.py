import streamlit as st
import sympy as sp

st.title("인수분해 계산기")

expr_input = st.text_input("다항식을 입력하세요 (예: x**2 + 2*x + 1):")

if expr_input:
    try:
        expr = sp.sympify(expr_input)
        factors = sp.factor(expr)
        st.write(f"인수분해 결과: {factors}")
    except Exception as e:
        st.error(f"오류 발생: {e}")
